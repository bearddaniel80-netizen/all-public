from .base import DocBase
from ...engine.resolve_source_handlers.identifier_sources.aggregates import AggregateSource

class BuildAggregates(DocBase):
    def build(self, ctx):
        lst = AggregateSource().query()

        ctx.aggregates = lst