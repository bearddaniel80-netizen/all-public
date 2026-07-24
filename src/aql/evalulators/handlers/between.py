from .base import BaseHandler
from ...language.ast.expressions.operators import BetweenOp
from ..registry import register_eval_handler

@register_eval_handler(priority=66)
class BetweenOpHandler(BaseHandler):
    def can_handle(self, node):
        return isinstance(node, BetweenOp)

    def process(self, node, ctx):
        value = ctx.eval(node.expr)
        lower = ctx.eval(node.lower)
        upper = ctx.eval(node.upper)

        return lower <= value <= upper