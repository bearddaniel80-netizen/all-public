# aegis_prime.aql/lexer/readers/string.py

from ...language.tokens import Token, TokenType
from .base import TokenReader
from ..registry import register_readers

@register_readers
class StarReader(TokenReader):
    def can_read(self, char):
        return char == "*"

    def read(self, lexer):
        lexer.advance()
        return Token(TokenType.STAR, "*")