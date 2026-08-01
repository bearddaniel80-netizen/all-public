from .base import BaseHandler
from ...language.ast.expressions.operators import NotOp
from ..registry import register_eval_handler, register_operator, Operator, SupportType

@register_operator(
    op = Operator(
        name="NOT",
        support_type=[SupportType.INT,SupportType.STR],
        template=[
            "WHERE NOT <field> <op> <value:int>",
            "WHERE NOT <field> <op> <value:str>",
            "WHERE NOT <field> LIKE <value:str>",
            "WHERE NOT <field> CONTAINS <value:str>",
            "WHERE NOT <field> STARTSWITH <value:str>",
            "WHERE NOT <field> ENDSWITH <value:str>",
            "WHERE <field> NOT BETWEEN <value:int> AND <value:int>",
            "WHERE <field> NOT IN [<value:int>]",
            "WHERE <field> NOT IN [<value:str>]"
        ]
    )
)
@register_eval_handler(priority=67)
class NotOpHandler(BaseHandler):
    def can_handle(self, node):
        return isinstance(node, NotOp)

    def process(self, node, ctx):
        return not ctx.eval(node.expr)