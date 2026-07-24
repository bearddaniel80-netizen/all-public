from ...ast.identifier import Identifier
from .base import Statement
from dataclasses import dataclass

@dataclass
class Describe(Statement):
    target: Identifier

    def __repr__(self):
        return f"Describe( target= {self.target})"

    def to_dict(self):
        return {
            "type": "Describe",
            "target": self.target.to_dict()
        }
