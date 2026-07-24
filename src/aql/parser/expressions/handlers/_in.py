from .base import OperatorHandler
from ....language.tokens import TokenType

class InHandler(OperatorHandler):
    precedence = 20
    
    def can_handle(self, tok, ctx):
        return tok.type == TokenType.IN

    def parse(self, parser, ctx, left):
        ctx.consume()
        return parser.parse_in(ctx, left)