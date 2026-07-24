from ..base import ASTNode
from ..expressions.identifier import Field
from dataclasses import dataclass

@dataclass
class MacroExpression(ASTNode):
    name: str
    expression: Field

    def __repr__(self):
        return f"MacroExpression( name= {self.name} expression= {self.expression})"

    def to_dict(self):
        return {
            "type": "macro",
            "name": self.name,
            "expression": self.expression.to_dict()
        }