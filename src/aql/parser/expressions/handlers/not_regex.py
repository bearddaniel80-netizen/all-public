from .base import OperatorHandler
from ....language.tokens import TokenType
from ....language.ast.expressions.operators import NotOp

class NotRegexMatchHandler(OperatorHandler):

    precedence = 5
    def can_handle(self, tok, ctx):
        return (
            tok.type == TokenType.NOT
            and ctx.peek_next()
            and ctx.peek_next().type in [TokenType.CONTAINS, TokenType.ENDSWITH, TokenType.STARTSWITH, TokenType.LIKE]
        )

    def parse(self, parser, ctx, left):
        ctx.consume()  # NOT
        ctx.consume()  # CONTAINS, ENDSWITH, STARTSWITH, LIKE

        return NotOp(
            parser.parse(ctx, left)
        )