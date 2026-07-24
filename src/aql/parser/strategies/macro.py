from .base import StatementStrategy
from ...language.tokens import TokenType
from ...context.analysis import AnalysisContext
from .select_clauses.parser.projection import ProjectionParser
from .select_clauses.parser._from import FromParser

class MacroStrategy(StatementStrategy):
    def __init__(self, query):
        self.query = query

    def can_handle(self, ctx):
        tok = ctx.peek()
        return tok and tok.type == TokenType.DECLARE

    def parse(self, ctx, analysis_ctx: AnalysisContext):

        if not ctx.match(TokenType.DECLARE):
            return self.query

        ident = ctx.expect(TokenType.IDENT)

        ctx.expect(TokenType.AS)

        expression = ProjectionParser().parse(ctx, analysis_ctx, "declare")

        if not expression:
            expression = FromParser().parse(ctx, analysis_ctx)

        return self.query
        