from __future__ import annotations
from pathlib import Path
from dataclasses import dataclass, field
from .about.types import CommentType

@dataclass
class ImportNode:
    path: Path

    parent: ImportNode | None = None
    children: list[ImportNode] = field(default_factory=list)

    prev: ImportNode | None = None
    next: ImportNode | None = None

@dataclass
class ImportGraph:
    root: ImportNode
    nodes: dict[Path, ImportNode] = field(default_factory=dict)

@dataclass
class SourceLoader:
    collector: dict = field(default_factory=dict)
    tree: ImportGraph | None = None

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
