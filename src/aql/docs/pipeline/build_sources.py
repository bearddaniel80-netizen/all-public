from .base import DocBase
from ...engine.resolve_source_handlers.identifier_sources.sources import Sources
from ...engine.resolve_source_handlers.identifier_sources.table_functions import FunctionSource

class BuildSources(DocBase):
    def build(self, ctx):
        lst = []
        sources = {}
        lst.extend(Sources().query())
        lst.extend(FunctionSource().query())

        for item in lst:
            name = item["name"]
            sources[name] = item

        ctx.sources = sources