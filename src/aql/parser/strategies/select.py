from .base import StatementStrategy
from ...language.tokens import TokenType
from .clause_registry import CLAUSE_REGISTRY
from . import select_clauses
from ...context.analysis import AnalysisContext

class SelectStrategy(StatementStrategy):

    def __init__(self, query):
        self.query = query

    def can_handle(self, ctx):
        tok = ctx.peek()
        return tok and tok.type == TokenType.SELECT

    def parse(self, ctx, analysis_ctx: AnalysisContext):

        for clause in CLAUSE_REGISTRY:
            self.query = clause.parse(ctx, self.query, analysis_ctx)

        return self.query