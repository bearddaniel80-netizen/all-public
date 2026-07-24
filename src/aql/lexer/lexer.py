from ..language.tokens import Token, TokenType
from ..context.analysis import AnalysisContext
from .registry import READER_REGISTRY
from . import readers

class Lexer:
    def __init__(self, ctx: AnalysisContext):
        self.text = ctx.text
        self.i = 0
        self.current = ctx.text[0] if ctx.text else None
        self.readers = [cls() for cls in READER_REGISTRY]
        self.ctx = ctx

    def peek(self, lexer):
        idx = lexer.i + 1
        return lexer.text[idx] if idx < len(lexer.text) else None

    def advance(self):
        self.i += 1
        self.current = self.text[self.i] if self.i < len(self.text) else None

    def skip_whitespace(self):
        while self.current and self.current.isspace():
            self.advance()

    def next_token(self):
        self.skip_whitespace()

        if not self.current:
            return Token(TokenType.EOF, "EOF")

        for reader in self.readers:
            if reader.can_read(self.current):
                return reader.read(self)
            
        self.ctx.artifacts["diagnostic"].warning("LL01", f"Unknown character: {self.current}", "Fix query")
        return

    def tokenize(self):
        tokens = []

        while True:
            tok = self.next_token()
            tokens.append(tok)
            if tok.type == TokenType.EOF:
                break
        
        self.ctx.artifacts["tokens"] = tokens
        # return tokens