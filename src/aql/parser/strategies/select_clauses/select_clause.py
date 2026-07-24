from .base import SelectClause
from ..clause_registry import register_clause
from .parser.projection import ProjectionParser
from ....language.tokens import TokenType
from ....context.analysis import AnalysisContext

@register_clause(order=10)
class SelectClauseHandler(SelectClause):

    def parse(self, ctx, query, analysis_ctx: AnalysisContext):

        ctx.expect(TokenType.SELECT)

        query.select = ProjectionParser().parse(ctx, analysis_ctx, "select")

        return query