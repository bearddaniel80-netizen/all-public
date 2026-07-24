from ...context.analysis import AnalysisContext

class BaseHandler:
    def can_handle(self, ast) -> bool:
        raise NotImplementedError

    def handle(self, analysis_ctx: AnalysisContext):
        raise NotImplementedError