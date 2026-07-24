from .base import Pattern
from dataclasses import dataclass

@dataclass
class Wildcard(Pattern):
    def __repr__(self):
        return "Wildcard(*)"

    def __eq__(self, other):
        return isinstance(other, Wildcard)

    def __hash__(self):
        return hash(Wildcard)

    def to_dict(self):
        return {
            "type": "Wildcard",
            "value": "*"
        }