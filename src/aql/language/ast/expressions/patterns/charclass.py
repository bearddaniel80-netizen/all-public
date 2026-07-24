from .base import Pattern
from dataclasses import dataclass, field

@dataclass
class CharClass(Pattern):
    chars: set(str)

    def __repr__(self):
        # sort for stable/debug-friendly output
        chars_display = "".join(sorted(self.chars))
        return f"CharClass( chars= {chars_display})"

    def __eq__(self, other):
        return isinstance(other, CharClass) and self.chars == other.chars

    def __hash__(self):
        return hash((CharClass, frozenset(self.chars)))

    def to_dict(self):
        return {
            "type": "CharClass",
            "chars": sorted(self.chars)
        }
