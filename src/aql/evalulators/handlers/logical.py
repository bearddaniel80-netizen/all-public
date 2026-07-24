from .base import BaseHandler
from ...language.ast.expressions.operators import AndOp, OrOp
from ..registry import register_eval_handler

@register_eval_handler(priority=61)
class AndOpHandler(BaseHandler):
    def can_handle(self, node):
        return isinstance(node, AndOp)

    def process(self, node, ctx):
        left = ctx.eval(node.left)
        right = ctx.eval(node.right)
        return left and right

@register_eval_handler(priority=62)
class OrOpHandler(BaseHandler):
    def can_handle(self, node):
        return isinstance(node, OrOp)

    def process(self, node, ctx):
        left = ctx.eval(node.left)
        right = ctx.eval(node.right)
        return left or right