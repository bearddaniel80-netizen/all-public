from .base import BaseHandler
from ...language.ast.expressions.operators import BetweenOp
from ..registry import register_eval_handler, register_operator, Operator, SupportType

@register_operator(
    op = Operator(
        name="BETWEEN",
        support_type=[SupportType.INT],
        template=[
            "WHERE <field:int> BETWEEN <value:int> AND <value:int>",
        ]
    )
)
@register_eval_handler(priority=66)
class BetweenOpHandler(BaseHandler):
    def can_handle(self, node):
        return isinstance(node, BetweenOp)

    def process(self, node, ctx):
        value = ctx.eval(node.expr)
        lower = ctx.eval(node.lower)
        upper = ctx.eval(node.upper)

        return lower <= value <= upper