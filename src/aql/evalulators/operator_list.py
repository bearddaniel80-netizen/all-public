from . import handlers
from .registry import OPERATOR_REGISTRY, Operator, SupportType
from .op_enums import BinaryOpType

def _added_regex(value, operator_registry):
    operator = Operator(
        name=f"{value}",
        support_type=[SupportType.STR],
        template=[
            f"WHERE <field:str> {value} '<value:str>'"
        ]
    )
    operator_registry[value] = operator

def build_dict():
    operator_registry = OPERATOR_REGISTRY
    for member in BinaryOpType:
        if member.value == "=" or member.value == "!=":
            operator = Operator(
                name=f"{member.value}",
                support_type=[SupportType.INT, SupportType.STR],
                template=[
                    f"WHERE <field:int> <op:int> <value:int>",
                    f"WHERE <field:str> <op:str> '<value:str>'"
                ]
            )
        else:
            operator = Operator(
                name=f"{member.value}",
                support_type=[SupportType.INT],
                template=[
                    f"WHERE <field:int> <op:int> <value:int>"
                ]
            )
        operator_registry[member.value] = operator

    _added_regex("LIKE", operator_registry)
    _added_regex("CONTAINS", operator_registry)
    _added_regex("STARTSWITH", operator_registry)
    _added_regex("ENDSWITH", operator_registry)
    return operator_registry