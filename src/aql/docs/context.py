from dataclasses import dataclass, field
from .model import Examples, QueryClassification

@dataclass
class DocumentationContext:
    sources: dict = field(default_factory=dict)
    operators: list = field(default_factory=list)
    aggregates: list = field(default_factory=list)
    scalars: list = field(default_factory=list)
    examples: list[dict[str, Examples]] = field(default_factory=list)
    queries: dict[str, list[str]] = field(default_factory=dict)
    queries_classification: dict[str, list[object]] = field(default_factory=dict)