from .base import SelectClause
from ..clause_registry import register_clause
from ....language.tokens import TokenType
from ...expressions.parser import ExpressionParser
from ....context.analysis import AnalysisContext

@register_clause(order=45)
class HavingClause(SelectClause):

    def parse(self, ctx, query, analysis_ctx: AnalysisContext):

        if not ctx.match(TokenType.HAVING):
            return query

        query.having = ExpressionParser(analysis_ctx, "having").parse(ctx)

        return query