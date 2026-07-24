from .base import OperatorHandler
from ....language.tokens import TokenType

class BetweenHandler(OperatorHandler):

    precedence = 10
    def can_handle(self, tok, ctx):
        return tok.type == TokenType.BETWEEN

    def parse(self, parser, ctx, left):
        ctx.consume()

        return parser.parse_between(ctx, left)