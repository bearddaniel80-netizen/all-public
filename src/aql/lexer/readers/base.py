# aql_core/lexer/readers/base.py

from abc import ABC, abstractmethod
from ...language.tokens import Token


class TokenReader(ABC):
    @abstractmethod
    def can_read(self, ch: str) -> bool:
        pass

    @abstractmethod
    def read(self, lexer) -> Token:
        pass