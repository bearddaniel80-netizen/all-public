from dataclasses import dataclass, field

@dataclass
class QueryClassification:
    query: str

    source: str | None = None

    feature: str | None = None

    operation: list[str] = field(default_factory=list)

    fields: list[str] = field(default_factory=list)

    values: list[object] = field(default_factory=list)

    clauses: list[str] = field(default_factory=list)

    is_cte: bool = False


    def to_dict(self):
        return {
            "query": self.query,
            "source": self.source,
            "feature": self.feature,
            "operation": self.operation,
            "fields": self.fields,
            "clauses": self.clauses,
            "is_cte": str(self.is_cte),
        }
        
@dataclass
class Examples:
    name: str
    file: str | None
    raw: str | None
    fields: dict[str, str]
    values: dict[str, list[object]]