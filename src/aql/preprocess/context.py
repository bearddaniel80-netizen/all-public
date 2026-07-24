from pathlib import Path
from dataclasses import dataclass, field

from .models import (
    Comments,
    Docs,
    Macro,
    Using
)

@dataclass
class PreprocessorContext:
    filename: Path
    source: str
    block_comment: list[str] = field(default_factory=list)
    
    in_doc_block: bool = False
    doc_collection: list[str] = field(default_factory=list)
    
    in_comment_block: bool = False
    comment_collection: list[str] = field(default_factory=list)

    comments: list[Comments] = field(default_factory=list)
    documentations: list[Docs] = field(default_factory=list)
    macros: list[Macro] = field(default_factory=list)
    usings: list[Using] = field(default_factory=list)