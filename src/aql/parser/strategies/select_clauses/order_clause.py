from .base import SelectClause
from ..clause_registry import register_clause
from .parser.order import OrderByParser
from ....language.tokens import TokenType
from ....context.analysis import AnalysisContext

@register_clause(order=50)
class OrderByClauseHandler(SelectClause):

    def parse(self, ctx, query, analysis_ctx: AnalysisContext):

        if not ctx.match(TokenType.ORDER):
            return query

        ctx.expect(TokenType.BY)

        query.order_by = OrderByParser().parse(ctx, analysis_ctx)
        
        return query