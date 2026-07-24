from .base import BaseHandler
from ...language.ast.expressions.operators import NotOp
from ..registry import register_eval_handler

@register_eval_handler(priority=67)
class NotOpHandler(BaseHandler):
    def can_handle(self, node):
        return isinstance(node, NotOp)

    def process(self, node, ctx):
        return not ctx.eval(node.expr)