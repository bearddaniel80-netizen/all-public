from .base import Pattern
from dataclasses import dataclass

@dataclass
class SingleChar(Pattern):
    def __repr__(self):
        return "SingleChar(?)"

    def __eq__(self, other):
        return isinstance(other, SingleChar)

    def __hash__(self):
        return hash(SingleChar)

    def to_dict(self):
        return {
            "type": "SingleChar",
            "value": "?"
        }

class EndsWith(Pattern):
    def __init__(self, suffix: str):
        self.suffix = suffix

    def __repr__(self):
        return f"EndsWith({self.suffix!r})"

    def __eq__(self, other):
        return isinstance(other, EndsWith) and self.suffix == other.suffix

    def __hash__(self):
        return hash((EndsWith, self.suffix))

    def to_dict(self):
        return {
            "type": "EndsWith",
            "value": self.suffix
        }
        