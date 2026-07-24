from .base import SelectClause
from ..clause_registry import register_clause
from ....language.tokens import TokenType
from ....context.analysis import AnalysisContext

@register_clause(order=60)
class LimitClauseHandler(SelectClause):

    def parse(self, ctx, query, analysis_ctx: AnalysisContext):

        if not ctx.match(TokenType.LIMIT):
            return query

        query.limit = int(
            ctx.expect(TokenType.NUMBER).value
        )

        return query