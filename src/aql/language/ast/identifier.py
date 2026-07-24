from .base import ASTNode
from dataclasses import dataclass

@dataclass
class Identifier(ASTNode):
    name: str
    alias: object = None

    def __repr__(self):
        return f"Identifier( name= {self.name} alias= {self.alias})"

    def to_dict(self):
        return {
            "type": "identifier",
            "name": self.name,
            "alias": self.alias,
        }

    def __eq__(self, other):
        return isinstance(other, Identifier) and self.name == other.name

    def __hash__(self):
        return hash((Identifier, self.name))