from abc import ABC, abstractmethod
from .context import PreprocessorContext

class PreprocessorStage(ABC):
    @abstractmethod
    def process(self, ctx: PreprocessorContext):
        pass

class ReadLinePipeline(ABC):
    @abstractmethod
    def can_handle(self, line: str):
        pass

    @abstractmethod
    def process(self, line: str, ctx: PreprocessorContext):
        pass