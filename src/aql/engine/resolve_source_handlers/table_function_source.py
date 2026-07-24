from .base import BaseResolver
from ..registry_source import register_source as register

from ...link.registry import FUNCTION_CALL_REGISTRY
from ...link import fn_call
from ...language.ast.function_call import TableFunctionCall
from ...language.ast.expressions.literals import Literal

@register(instance=TableFunctionCall)
class TableFunctionSourceResolver(BaseResolver):
    def __init__(self, data_sources):
        self.data_sources = data_sources
    def resolve(self, ast_node, engine_context, analysis_ctx, include_schema: bool = False):

        raw = ast_node.arg[0]

        if isinstance(raw, Literal):
            raw = raw.value

        fn_cls = FUNCTION_CALL_REGISTRY.get(ast_node.name)

        if not fn_cls:
            raise Exception(f"Unknown table function: {ast_node.name}")

        source = fn_cls.execute(raw)

        return source.as_rows() #, dataset.schema()
