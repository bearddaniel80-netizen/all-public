from .base import OperatorHandler
from ....language.tokens import TokenType
from ....language.ast.expressions.operators import BinaryOp

class BinaryHandler(OperatorHandler):
    precedence = 10

    OPS = {
        TokenType.EQ,
        TokenType.NEQ,
        TokenType.LT,
        TokenType.GT,
        TokenType.LTE,
        TokenType.GTE,
        TokenType.ADD_OP,
    }

    def can_handle(self, tok, ctx):
        return tok.type in self.OPS

    def parse(self, parser, ctx, left):
        op = ctx.consume().value

        prec = parser.PRECEDENCE[op]

        right = parser.parse(ctx, prec + 1)

        return BinaryOp(left, op, right)