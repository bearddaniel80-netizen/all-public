from dataclasses import dataclass, field
from .about.types import CommentType

@dataclass
class SourceLoader:
    collector: dict = field(
        default_factory=dict
    )
    flow: dict = field(
        default_factory=dict
    )

@dataclass
class Comments:
    _type: CommentType
    target: str

    def to_dict(self):
        return {
            'type': self._type,
            'target': self.target
        }

@dataclass
class Docs:
    source: str
    _type: CommentType
    target: str

    def to_dict(self):
        return {
            'source': self.source,
            'type': self._type,
            'target': self.target
        }
@dataclass
class Macro:
    name: str
    target: str

    def to_dict(self):
        return {
            'name': self.name,
            'target': self.target
        }

@dataclass
class Using:
    target: str

    def to_dict(self):
        return {
            'target': self.target
        }
