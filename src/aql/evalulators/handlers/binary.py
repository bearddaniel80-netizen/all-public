from .base import BaseHandler
from ...language.ast.expressions.operators import BinaryOp
from ..registry import register_eval_handler
from ..op_enums import BinaryOpType

@register_eval_handler(priority=30)
class BinaryOpHandler(BaseHandler):
    def can_handle(self, node):
        return isinstance(node, BinaryOp)

    def process(self, node, ctx):
        left = ctx.eval(node.left)
        right = ctx.eval(node.right)

        op = BinaryOpType(node.operator)
        return op.func()(left, right)