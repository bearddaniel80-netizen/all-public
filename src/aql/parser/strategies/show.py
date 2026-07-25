from .base import StatementStrategy
from ...language.tokens import TokenType
from ...language.ast.statements.show import Show
from ...link.registry import FUNCTION_CALL_REGISTRY
from ...link import fn_call
from ...context.analysis import AnalysisContext
from .select_clauses.parser._from import FromParser

class ShowStrategy(StatementStrategy):

    def can_handle(self, ctx):
        tok = ctx.peek()
        return tok and tok.type == TokenType.SHOW

    def parse(self, ctx, analysis_ctx: AnalysisContext):
        ctx.expect(TokenType.SHOW)
        target = ctx.peek()
        if target.value in FUNCTION_CALL_REGISTRY.keys():
            target = FromParser().parse(ctx, analysis_ctx)
        else:
            target = ctx.expect(TokenType.IDENT).value

        return Show(target)