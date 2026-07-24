from .base import OperatorHandler
from ....language.tokens import TokenType
from ....language.ast.expressions.operators import NotOp

class NotBetweenHandler(OperatorHandler):

    precedence = 5
    def can_handle(self, tok, ctx):
        return (
            tok.type == TokenType.NOT
            and ctx.peek_next()
            and ctx.peek_next().type == TokenType.BETWEEN
        )

    def parse(self, parser, ctx, left):
        ctx.consume()
        ctx.consume()

        return NotOp(
            parser.parse_between(ctx, left)
        )