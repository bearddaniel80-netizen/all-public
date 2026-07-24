# aegis_prime.aql/lexer/readers/string.py

from ...language.tokens import Token, TokenType
from .base import TokenReader
from ..registry import register_readers

@register_readers
class StringReader(TokenReader):
    def can_read(self, ch: str) -> bool:
        return ch in ("'", '"')

    def read(self, lexer):
        quote = lexer.current
        lexer.advance()

        start = lexer.i

        while lexer.current and lexer.current != quote:
            lexer.advance()

        value = lexer.text[start:lexer.i]
        lexer.advance()

        return Token(TokenType.STRING, value)