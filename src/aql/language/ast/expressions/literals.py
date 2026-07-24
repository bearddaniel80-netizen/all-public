from ..base import ASTNode
from dataclasses import dataclass

@dataclass
class ListLiteral(ASTNode):
    values: dict

    def __repr__(self):
        return f"ListLiteral( values= {', '.join(repr(v) for v in self.values)})"

    def to_dict(self):
        return {
            "type": "list",
            "values": [v.to_dict() for v in self.values]
        }

@dataclass
class Literal(ASTNode):
    value: str

    def __repr__(self):
        return f"Literal( value= {self.value})"

    def to_dict(self):
        return {
            "type": "literal",
            "value": self.value
        }

    def __eq__(self, other):
        return isinstance(other, Literal) and self.value == other.value

    def __hash__(self):
        return hash((Literal, self.value))