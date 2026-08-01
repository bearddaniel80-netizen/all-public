import re
from .base import BaseHandler
from ...language.ast.expressions.operators import RegexMatch
from ..registry import register_eval_handler, register_operator, Operator, SupportType

@register_operator(
    op = Operator(
        name="~=",
        support_type=[SupportType.INT,SupportType.STR],
        template=["WHERE <field> ~= <value>"]
    )
)
@register_eval_handler(priority=68)
class RegexMatchHandler(BaseHandler):
    def can_handle(self, node):
        return isinstance(node, RegexMatch)

    def process(self, node, ctx):
        left = ctx.eval(node.field)
        right = ctx.eval(node.pattern)
        
        if right.startswith("%"):
            right = right.replace("%","^")
        if right.endswith("%"):
            right = right.replace("%","$")
        right = right.replace("%", "*")

        return re.search(right, str(left)) is not None