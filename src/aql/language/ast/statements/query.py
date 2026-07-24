from .base import Statement
from dataclasses import dataclass, field

@dataclass
class Query(Statement):
    cte: list = field(
        default_factory=list
    )
    select: list = field(
        default_factory=list
    )
    source: str = None
    where: object = None
    group_by: object = None
    having: object = None
    order_by: object = None
    limit: int | None = None

    def __repr__(self):
        parts = []

        if self.cte:
            parts.append(f"CTE {', '.join(str(f) for f in self.cte)}")

        parts.append(f"SELECT {', '.join(str(f) for f in self.select)}")

        if self.source:
            parts.append(f"FROM {self.source}")

        if self.where:
            parts.append(f"WHERE {self.where}")

        if self.group_by:
            parts.append(f"GROUP BY {self.group_by}")

        if self.order_by:
            parts.append(f"ORDER BY {self.order_by}")

        if self.having:
            parts.append(f"HAVING {self.having}")

        if self.limit is not None:
            parts.append(f"LIMIT {self.limit}")

        return " ".join(parts)

    def to_dict(self):
        return {
            "type": "query",
            "select": [f.to_dict() for f in self.select],
            "from": self.source.to_dict() if hasattr(self.source, "to_dict") else self.source,
            "where": self.where.to_dict() if self.where else None,
            "group_by": self.group_by.to_dict() if self.group_by else None,
            "order_by": self.order_by.to_dict() if self.order_by else None,
            "having": self.having.to_dict() if self.having else None,
            "limit": self.limit
        }

@dataclass
class CommonTableExpression:
    name: str
    query: Query
    materialized: bool = True # inline or materialized
    recursive: bool = False
    
    def __repr__(self):
        return f"CommonTableExpression( name= {self.name} query= {self.query} materialized= {self.materialized} )"
