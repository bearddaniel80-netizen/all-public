# aegis_prime.aql/lexer/readers/identifier.py

from ...language.tokens import Token, TokenType
from ...language.keywords import KEYWORDS
from .base import TokenReader
from ..registry import register_readers

@register_readers
class IdentifierReader(TokenReader):
    def can_read(self, ch: str) -> bool:
        return ch.isalpha() or ch == "_"

    def read(self, lexer):
        start = lexer.i

        while lexer.current and (lexer.current.isalnum() or lexer.current == "_"):
            lexer.advance()

        raw = lexer.text[start:lexer.i]
        upper = raw.upper()

        token_type = KEYWORDS.get(upper, TokenType.IDENT)

        return Token(
            token_type,
            upper if token_type != TokenType.IDENT else raw
        )