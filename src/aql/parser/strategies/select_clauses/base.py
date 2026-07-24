from abc import ABC, abstractmethod
from ....context.analysis import AnalysisContext

class SelectClause(ABC):

    order = 0

    @abstractmethod
    def parse(self, ctx, query, analysis_ctx: AnalysisContext):
        pass