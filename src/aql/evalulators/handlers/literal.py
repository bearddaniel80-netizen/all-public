from .base import BaseHandler
from ...language.ast.expressions.literals import Literal
from ..registry import register_eval_handler

@register_eval_handler(priority=10)
class LiteralHandler(BaseHandler):
    def can_handle(self, node):
        return isinstance(node, Literal)

    def process(self, node, ctx):
        return node.value