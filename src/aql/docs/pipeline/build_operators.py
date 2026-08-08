from .base import DocBase
from ...engine.resolve_source_handlers.identifier_sources.operators import OperatorSource

class BuildOperator(DocBase):
    def build(self, ctx):
        ctx.operators = OperatorSource().query()