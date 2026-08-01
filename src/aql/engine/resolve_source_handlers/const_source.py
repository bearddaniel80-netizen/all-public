from .base import BaseResolver
from ..registry_source import register_source as register
from ...language.ast.statements.set_operator import ConstantRelation

@register(instance=ConstantRelation)
class ConstantRelationSourceResolver(BaseResolver):
    def __init__(self, data_sources):
        self.data_sources = data_sources

    def resolve(self, ast_node, engine_context, analysis_ctx, include_schema: bool = False):
        return [{}] # empty 1x1
