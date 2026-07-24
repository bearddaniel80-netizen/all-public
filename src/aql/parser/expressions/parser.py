from ...language.tokens import TokenType
from ...context.analysis import AnalysisContext
from ...language.ast.identifier import Identifier
from ...language.ast.expressions.literals import ListLiteral, Literal
from ...language.ast.expressions.operators import (
    BetweenOp, 
    InOp,
    NotOp,
)
from .handlers.between import BetweenHandler
from .handlers.binary import BinaryHandler
from .handlers.boolean import AndHandler, OrHandler
from .handlers._in import InHandler
from .handlers.not_regex import NotRegexMatchHandler
from .handlers.not_between import NotBetweenHandler
from .handlers.not_in import NotInHandler
from .handlers.regex import (
    RegexHandler,
    LikeHandler,
    ContainsHandler,
    StartsWithHandler,
    EndsWithHandler,
)

class ExpressionParser:
    def __init__(self, ctx: AnalysisContext, target: str):
        self.analysis_ctx = ctx
        self.target = target

        self.handlers = [
            NotBetweenHandler(),
            NotInHandler(),
            NotRegexMatchHandler(),
            BetweenHandler(),
            InHandler(),
            RegexHandler(),
            LikeHandler(ctx, target),
            ContainsHandler(),
            StartsWithHandler(),
            EndsWithHandler(),
            AndHandler(),
            OrHandler(),
            BinaryHandler(),
        ]
        self.PRECEDENCE = {
            "=": 10,
            "<": 10,
            ">": 10,
            "!=": 10,
            "<=": 10,
            ">=": 10,
            "BETWEEN": 10,
            "AND": 10,
            "~=": 20,
            "LIKE": 20,
            "CONTAINS": 20,
            "ENDSWITH": 20,
            "STARTSWITH": 20,
            "IN": 20,
            "NOT_LIKE": 5,
            "NOT_CONTAINS": 5,
            "NOT_ENDSWITH": 5,
            "NOT_STARTSWITH": 5,
            "NOT_IN": 5,
            "NOT_BETWEEN": 5,
            "NOT": 5,
            "OR": 1,
        }

    def parse(self, ctx, precedence=0):
        left = self.parse_primary(ctx)

        while True:
            tok = ctx.peek()

            if not tok:
                break

            handled = False

            for handler in self.handlers:
                if handler.can_handle(tok, ctx):
                    op_prec = handler.precedence

                    if op_prec < precedence:
                        break
                    left = handler.parse(self, ctx, left)
                    handled = True
                    break

            if not handled:
                break

        return left

    def parse_primary(self, ctx):
        tok = ctx.peek()

        if tok is None:
            self.analysis_ctx.artifacts["diagnostic"].warning(
                "PEP01",
                f"Expected expression in {self.target}.",
                "Provide an expression."
            )
            return None

        if tok.type == TokenType.NOT:
            ctx.consume()

            expr = self.parse(ctx, self.PRECEDENCE["NOT"])

            return NotOp(expr)

        tok = ctx.consume()


        if tok.type == TokenType.IDENT:
            return Identifier(tok.value)

        if tok.type == TokenType.NUMBER:
            return Literal(int(tok.value))

        if tok.type == TokenType.STRING:
            return Literal(tok.value)
        
        self.analysis_ctx.artifacts["diagnostic"].warning("PEP01", f"Unexpected token {tok} in {self.target}.", "Fix Token")
        ctx.consume()

    def parse_in(self, ctx, left):
        ctx.expect(TokenType.LBRACK)

        values = []
        while True:
            values.append(self.parse_primary(ctx))
            if not ctx.match(TokenType.COMMA):
                break

        ctx.expect(TokenType.RBRACK)

        return InOp(left, values)

    def parse_between(self, ctx, left):
        lower = self.parse_primary(ctx)

        ctx.expect(TokenType.AND)

        upper = self.parse_primary(ctx)

        return BetweenOp(left, lower, upper)
