from dataclasses import dataclass, field
from typing import Iterable, Any

from ...language.ast.statements.query import Query

@dataclass
class ExecutionContext:
    query: Query
    engine_context: Any
    analysis_ctx: Any
    pipeline: Any
    ctes = {}

    # Current stream of groups
    groups: Iterable[dict[str, Any]] = field(default_factory=list)

    # Current stream of rows
    rows: Iterable[dict[str, Any]] = field(default_factory=list)

    # Optional execution metadata
    metadata: dict[str, Any] = field(default_factory=dict)
