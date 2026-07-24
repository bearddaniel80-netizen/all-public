from .base import SelectClause
from ..clause_registry import register_clause
from .parser._from import FromParser
from ....language.tokens import TokenType
from ....context.analysis import AnalysisContext

@register_clause(order=20)
class FromClauseHandler(SelectClause):

    def parse(self, ctx, query, analysis_ctx: AnalysisContext):
        tok = ctx.peek()
        
        if tok.type == TokenType.FROM:
            ctx.consume()
            query.source = FromParser().parse(ctx, analysis_ctx)

        return query