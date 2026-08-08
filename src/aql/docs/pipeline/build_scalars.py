from .base import DocBase
from ...engine.resolve_source_handlers.identifier_sources.scalars import ScalarSource

class BuildScalars(DocBase):
    def build(self, ctx):
        lst = ScalarSource().query()

        ctx.scalars = lst