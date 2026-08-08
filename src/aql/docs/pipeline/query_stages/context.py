from dataclasses import dataclass, field
from .template_resolver import TemplateResolver
from .combine_templates import CombineTemplates
from ...model import Examples, QueryClassification

@dataclass
class StageContext:
    source: object = None
    example: Examples = None
    template_resolver: TemplateResolver = TemplateResolver()
    combine_templates: CombineTemplates = CombineTemplates()

    queries: list[str] = field(default_factory=list)
    queries_classification: list = field(default_factory=list)
    
    operators: list = field(default_factory=list)
    aggregates: list = field(default_factory=list)
    scalars: list = field(default_factory=list)

    source_templates: list[str] = field(default_factory=list)

    def add(self, query):
        for q in query:
            self.queries.append(q)