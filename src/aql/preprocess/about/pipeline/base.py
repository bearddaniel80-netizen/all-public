from abc import ABC, abstractmethod
from ..types import AboutType

class AboutBase(ABC):

    @abstractmethod
    def process(self, source_loader):
        pass
