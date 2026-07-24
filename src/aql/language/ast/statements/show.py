from ...ast.identifier import Identifier
from .base import Statement
from dataclasses import dataclass

@dataclass
class Show(Statement):
    target: Identifier

    def __repr__(self):
        return f"Show( target= {self.target})"

    def to_dict(self):
        return {
            "type": "show",
            "target": self.target.to_dict()
        }
