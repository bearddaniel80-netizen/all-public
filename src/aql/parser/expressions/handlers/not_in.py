from .base import OperatorHandler
from ....language.tokens import TokenType
from ....language.ast.expressions.operators import NotOp

class NotInHandler(OperatorHandler):

    precedence = 5
    def can_handle(self, tok, ctx):
        return (
            tok.type == TokenType.NOT
            and ctx.peek_next()
            and ctx.peek_next().type == TokenType.IN
        )

    def parse(self, parser, ctx, left):
        ctx.consume()  # NOT
        ctx.consume()  # IN

        return NotOp(
            parser.parse_in(ctx, left)
        )