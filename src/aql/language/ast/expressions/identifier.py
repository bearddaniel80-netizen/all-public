from ..base import ASTNode
from dataclasses import dataclass

@dataclass
class Field(ASTNode):
    name: str

    def __repr__(self):
        return f"Field( name= {self.name})"

    def to_dict(self):
        return {
            "type": "field",
            "name": self.name
        }