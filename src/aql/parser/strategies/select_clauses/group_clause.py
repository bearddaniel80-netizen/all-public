from .base import SelectClause
from ..clause_registry import register_clause
from .parser.projection import ProjectionParser
from ....language.tokens import TokenType
from ....context.analysis import AnalysisContext
from ....language.ast.expressions.group_by import GroupBy

@register_clause(order=40)
class GroupByClauseHandler(SelectClause):

    def parse(self, ctx, query, analysis_ctx: AnalysisContext):

        if not ctx.match(TokenType.GROUP):
            return query

        ctx.expect(TokenType.BY)

        query.group_by = GroupBy(
            ProjectionParser().parse(ctx, analysis_ctx, "group_by")
        )

        return query