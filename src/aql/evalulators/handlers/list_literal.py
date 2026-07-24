from .base import BaseHandler
from ...language.ast.expressions.literals import ListLiteral
from ..registry import register_eval_handler

@register_eval_handler(priority=50)
class ListLiteralHandler(BaseHandler):
    def can_handle(self, node):
        return isinstance(node, ListLiteral)

    def process(self, node, ctx):
        return [ctx.eval(v) for v in node.values]