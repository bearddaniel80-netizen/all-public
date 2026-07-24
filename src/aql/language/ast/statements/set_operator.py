from .base import Statement
from ..base import ASTNode
from enum import Enum
from dataclasses import dataclass, field

class SetOperatorType(str, Enum):
    UNION = "UNION"
    UNION_ALL = "UNION_ALL"
    INTERSECT = "INTERSECT"
    EXCEPT = "EXCEPT"

@dataclass
class ConstantRelation(ASTNode):
    rows: list = field(
        default_factory=list
    )

    def __repr__(self):
        return f"ConstantRelation( rows= {self.rows})"

    def to_dict(self):
        return {
            "type": "const_relation",
            "row": self.rows,
        }

@dataclass
class SetOperation(ASTNode):
    name: str
    left: ConstantRelation
    right: Statement
    operator: SetOperatorType
    recursive: bool = True

    def __repr__(self):
        return f"SetOperation( name= {self.name} left= {self.left} operator= {self.operator} right= {self.right})"

    def to_dict(self):
        return {
            "type": "set_op",
            "name": self.name,
            "operator": self.operator,
            "left": self.left.to_dict(),
            "right": self.right.to_dict(),
            "recursive": self.recursive
        }
