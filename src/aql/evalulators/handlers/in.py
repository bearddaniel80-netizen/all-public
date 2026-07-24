from .base import BaseHandler
from ...language.ast.expressions.operators import InOp
from ..registry import register_eval_handler

@register_eval_handler(priority=60)
class InOpHandler(BaseHandler):
    def can_handle(self, node):
        return isinstance(node, InOp)

    def process(self, node, ctx):
        left = ctx.eval(node.left)
        values = [ctx.eval(v) for v in node.right]

        if isinstance(left, list):
            return any(v in values for v in left)

        return left in values