from .base import Pattern
from dataclasses import dataclass

@dataclass
class Literal(Pattern):
    value: object

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