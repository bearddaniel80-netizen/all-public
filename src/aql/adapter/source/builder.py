import re
import datetime
from enum import Enum
from dataclasses import dataclass, make_dataclass
from typing import Optional, Any


# =========================
# 1. TYPE SYSTEM
# =========================

class AQLType(Enum):
    STRING = "string"
    INT = "int"
    FLOAT = "float"
    BOOL = "bool"
    DATETIME = "datetime"
    NULL = "null"
    OBJECT = "object"
    ARRAY = "array"


PROMOTION_ORDER = [
    AQLType.NULL,
    AQLType.BOOL,
    AQLType.INT,
    AQLType.FLOAT,
    AQLType.DATETIME,
    AQLType.STRING,
]


def promote(t1: AQLType, t2: AQLType) -> AQLType:

    if t1 == t2:
        return t1

    if AQLType.STRING in (t1, t2):
        return AQLType.STRING

    return max(t1, t2, key=lambda t: PROMOTION_ORDER.index(t))


def detect_type(value) -> AQLType:
    if value is None:
        return AQLType.NULL
    if isinstance(value, bool):
        return AQLType.BOOL
    if isinstance(value, int):
        return AQLType.INT
    if isinstance(value, float):
        return AQLType.FLOAT
    if isinstance(value, dict):
        return AQLType.OBJECT
    if isinstance(value, list):
        return AQLType.ARRAY
    if isinstance(value, str):
        return detect_string_type(value)

    return AQLType.STRING


def detect_string_type(value: str) -> AQLType:
    v = value.strip()

    if re.fullmatch(r"-?\d+", v):
        return AQLType.INT

    if re.fullmatch(r"-?\d+\.\d+", v):
        return AQLType.FLOAT

    if v.lower() in {"true", "false"}:
        return AQLType.BOOL

    try:
        datetime.datetime.fromisoformat(v)
        return AQLType.DATETIME
    except Exception:
        return AQLType.STRING

# =========================
# 2. SCHEMA MODEL
# =========================

@dataclass
class SchemaNode:
    type: AQLType
    nullable: bool = True

    # NEW: evidence tracking
    count: int = 1

    fields: Optional[dict[str, "SchemaNode"]] = None
    element: Optional["SchemaNode"] = None

# =========================
# CONFIDENCE MODEL
# =========================
def compute_confidence(node: SchemaNode) -> float:
    return min(1.0, node.count / 10)  # simple smoothing example
    
def confidence(node: SchemaNode) -> float:
    if node.count == 0:
        return 0.0
    return 1.0  # or refined later with type entropy

def merge_nodes(n1: SchemaNode, n2: SchemaNode) -> SchemaNode:
    if n1.type != n2.type:
        return SchemaNode(
            type=promote(n1.type, n2.type),
            count=n1.count+n2.count
        )

    # OBJECT
    if n1.type == AQLType.OBJECT:
        merged = {}
        keys = set(n1.fields or {}) | set(n2.fields or {})
        for k in keys:
            if k in (n1.fields or {}) and k in (n2.fields or {}):
                merged[k] = merge_nodes(n1.fields[k], n2.fields[k])
            else:
                merged[k] = (n1.fields or {}).get(k) or (n2.fields or {}).get(k)
        return SchemaNode(type=AQLType.OBJECT, fields=merged,
            count=n1.count+n2.count)

    # ARRAY
    if n1.type == AQLType.ARRAY:
        return SchemaNode(
            type=AQLType.ARRAY,
            element=merge_nodes(n1.element, n2.element,
            count=n1.count+n2.count)
        )

    return SchemaNode(type=n1.type,
            count=n1.count+n2.count)


def infer_node(value) -> SchemaNode:
    t = detect_type(value)

    # OBJECT
    if t == AQLType.OBJECT:
        return SchemaNode(
            type=t,
            fields={k: infer_node(v) for k, v in value.items()}
        )

    # ARRAY
    if t == AQLType.ARRAY:
        if not value:
            return SchemaNode(type=t, element=SchemaNode(AQLType.STRING))

        element_node = infer_node(value[0])
        for v in value[1:]:
            element_node = merge_nodes(element_node, infer_node(v))

        return SchemaNode(type=t, element=element_node)

    return SchemaNode(type=t)


def infer_schema(rows: list[dict]) -> dict[str, SchemaNode]:
    schema: dict[str, SchemaNode] = {}

    for row in rows:
        for k, v in row.items():
            node = infer_node(v)

            if k not in schema:
                schema[k] = node
            else:
                schema[k] = merge_nodes(schema[k], node)

    return schema


# =========================
# 3. MODEL BUILDER
# =========================

AQL_TO_PYTHON = {
    AQLType.STRING: str,
    AQLType.INT: int,
    AQLType.FLOAT: float,
    AQLType.BOOL: bool,
    AQLType.DATETIME: str,  # or datetime.datetime
    AQLType.NULL: type(None),
}


def to_python_type(node: SchemaNode):
    if node.type == AQLType.OBJECT:
        return build_model("Nested", node.fields)

    if node.type == AQLType.ARRAY:
        return list[to_python_type(node.element)]

    base = AQL_TO_PYTHON.get(node.type, Any)

    if node.nullable:
        return Optional[base]

    return base


def build_model(name: str, schema: dict[str, SchemaNode]):
    fields = []

    for k, node in schema.items():
        py_type = to_python_type(node)
        fields.append((k, py_type, None))

    return make_dataclass(name, fields)