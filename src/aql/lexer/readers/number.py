# aegis_prime.aql/lexer/readers/number.py

from ...language.tokens import Token, TokenType
from .base import TokenReader
from ..registry import register_readers

@register_readers
class NumberReader(TokenReader):
    def can_read(self, ch: str) -> bool:
        return ch.isdigit()

    def read(self, lexer):
        start = lexer.i

        while lexer.current and lexer.current.isdigit():
            lexer.advance()

        return Token(TokenType.NUMBER, lexer.text[start:lexer.i])