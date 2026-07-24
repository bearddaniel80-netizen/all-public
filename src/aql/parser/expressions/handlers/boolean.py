from .base import OperatorHandler
from ....language.tokens import TokenType
from ....language.ast.expressions.operators import AndOp, OrOp

class AndHandler(OperatorHandler):
    precedence = 2

    def can_handle(self, tok, ctx):
        return tok.type == TokenType.AND

    def parse(self, parser, ctx, left):
        ctx.consume()

        prec = parser.PRECEDENCE["AND"]

        right = parser.parse(ctx, prec + 1)

        return AndOp(left, right)

class OrHandler(OperatorHandler):
    precedence = 1
    
    def can_handle(self, tok, ctx):
        return tok.type == TokenType.OR

    def parse(self, parser, ctx, left):
        ctx.consume()

        prec = parser.PRECEDENCE["OR"]

        right = parser.parse(ctx, prec + 1)

        return OrOp(left, right)