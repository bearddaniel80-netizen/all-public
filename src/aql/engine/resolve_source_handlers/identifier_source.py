from .base import BaseResolver
from ..registry_source import register_source as register
from ...language.ast.identifier import Identifier
from .registry_identifier import SOURCE_REGISTRY
from . import identifier_sources

@register(instance=Identifier)
class IdentifierSourceResolver:
    def __init__(self, data_sources):
        self.data_sources = data_sources

    def resolve(self, ast_node, engine_context, analysis_ctx, include_schema: bool = False):

        fn = SOURCE_REGISTRY[ast_node.name]

        if fn:
            fn_cls = fn()

            return fn_cls.query()
            
        # then physical sources
        factory = self.data_sources.get(ast_node.name)

        if factory is None:
            raise ValueError(f"Unknown source: {ast_node.name}")    

        # ✅ normal sources
        source = factory  # or factory.build()

        dataset = source.to_dataset()       # 👈 REQUIRED
        
        if include_schema == False:
            return dataset.as_rows()
        
        return dataset.as_rows(), dataset.schema()