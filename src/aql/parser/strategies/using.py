from .base import StatementStrategy
from ...language.tokens import TokenType
from ...language.statements.using import UsingExpression

class UsingStrategy(StatementStrategy):
    def can_handle(self, ctx):
        tok = ctx.peek()
        return tok and tok.type == TokenType.USING

    def parse(self, ctx):

        if not ctx.match(TokenType.USING):
            return self.query

        return self.query
        