from ..context import ParserContext
from ...context.analysis import AnalysisContext

class StatementStrategy:
    def can_handle(self, ctx: ParserContext) -> bool:
        raise NotImplementedError

    def parse(self, ctx: ParserContext, analysis_ctx: AnalysisContext):
        raise NotImplementedError