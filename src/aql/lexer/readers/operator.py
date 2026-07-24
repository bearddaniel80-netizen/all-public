# aegis_prime.aql/lexer/readers/operator.py

from ...language.tokens import Token, TokenType
from .base import TokenReader
from ..registry import register_readers

@register_readers
class OperatorReader(TokenReader):

    OPERATORS = {
        "~=": TokenType.MATCH,
        "!=": TokenType.NEQ,
        "<=": TokenType.LTE,
        ">=": TokenType.GTE,
        "=": TokenType.EQ,
        "<": TokenType.LT,
        ">": TokenType.GT,
        "[": TokenType.LBRACK,
        "]": TokenType.RBRACK,
        ",": TokenType.COMMA,
        "(": TokenType.LPAREN,
        ")": TokenType.RPAREN,
        "+": TokenType.ADD_OP,
    }

    def can_read(self, ch: str) -> bool:
        return ch in {"!", "<", ">", "=", "~", "[", "]", ",", "(", ")", "+"}

    def read(self, lexer):
        ch = lexer.current
        nxt = self.peek(lexer)

        # 2-character operators
        if nxt:
            compound = ch + nxt
            if compound in self.OPERATORS:
                lexer.advance()
                lexer.advance()
                return Token(self.OPERATORS[compound], compound)

        lexer.advance()
        return Token(self.OPERATORS[ch], ch)

    def peek(self, lexer):
        idx = lexer.i + 1
        return lexer.text[idx] if idx < len(lexer.text) else None