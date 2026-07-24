from ..context.analysis import AnalysisContext

class ParserContext:
    def __init__(self, ctx: AnalysisContext):
        self.tokens = ctx.artifacts["tokens"]
        self.pos = 0
        self.analysis_ctx = ctx

    def check(self, token_type):
        return self.peek().type == token_type
        
    def peek(self):
        if self.pos < len(self.tokens):
            return self.tokens[self.pos]
        return None
    
    def peek_next(self):
        if self.pos + 1 >= len(self.tokens):
            return None
        return self.tokens[self.pos + 1]

    def consume(self):
        tok = self.peek()
        self.pos += 1
        return tok

    def match(self, token_type):
        tok = self.peek()
        if tok and tok.type == token_type:
            return self.consume()
        return None

    def expect(self, token_type):
        tok = self.consume()
        if not tok or tok.type != token_type:
            self.analysis_ctx.artifacts["diagnostic"].warning("PC01", f"Expected {token_type}, got {tok}", "Fix token")
            tok = self.consume()
        return tok