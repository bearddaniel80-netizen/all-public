from .base import BaseResolver
from ..registry_source import register_source as register

import sys

@register(instance=str)
class StringSourceResolver(BaseResolver):
    def __init__(self, data_sources):
        self.data_sources = data_sources

    def resolve(self, ast_node, engine_context, analysis_ctx, include_schema: bool = False):

        # then physical sources
        factory = self.data_sources.get(ast_node)

        if factory is None:
            raise ValueError(f"Unknown source: {ast_node}")    

        # ✅ stdin case
        if ast_node == "stdin":
            raw = sys.stdin.read()
            source = factory.from_raw(raw)

            dataset = source.to_dataset()   # 👈 normalize here
            return dataset.as_rows(), dataset.schema()
