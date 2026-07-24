from .base import BaseHandler
from ...language.ast.identifier import Identifier
from ...adapter.row import RowAdapter
from ..registry import register_eval_handler

@register_eval_handler(priority=20)
class IdentifierHandler(BaseHandler):
    def can_handle(self, node):
        return isinstance(node, Identifier)

    def process(self, node, ctx):
        return RowAdapter.get(ctx.obj, node.name)