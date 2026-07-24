from .base import SelectClause
from ..clause_registry import register_clause
from ...expressions.parser import ExpressionParser
from ....language.tokens import TokenType
from ....context.analysis import AnalysisContext

@register_clause(order=30)
class WhereClauseHandler(SelectClause):

    def parse(self, ctx, query, analysis_ctx: AnalysisContext):

        if ctx.match(TokenType.WHERE):

            query.where = ExpressionParser(analysis_ctx, "where").parse(ctx)

        return query