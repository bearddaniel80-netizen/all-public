import re
from .base import OperatorHandler
from ....context.analysis import AnalysisContext
from ....language.tokens import TokenType
from ....language.ast.expressions.literals import Literal
from ....language.ast.expressions.operators import RegexMatch

class RegexHandler(OperatorHandler):

    precedence = 20

    def can_handle(self, tok, ctx):
        return tok.type == TokenType.REGMATCH

    def parse(self, parser, ctx, left):
        op = ctx.consume()

        prec = parser.PRECEDENCE["~="]

        right = parser.parse(ctx, prec + 1)

        return RegexMatch(left, right)

class LikeHandler(OperatorHandler):

    precedence = 20
    def __init__(self, analysis_ctx: AnalysisContext, target):
        self.analysis_ctx = analysis_ctx
        self.target = target
    
    def can_handle(self, tok, ctx):
        return tok.type == TokenType.LIKE

    def parse(self, parser, ctx, left):
        ctx.consume()

        prec = parser.PRECEDENCE["LIKE"]

        right = parser.parse(ctx, prec + 1)

        if not isinstance(right, Literal):
            analysis_ctx.artifacts["diagnostic"].warning("PHR01", f"LIKE requires a string literal in {target}.", "Need a literal")
            right = Literal(right)

        pattern = re.escape(str(right.value))
        pattern = pattern.replace("%", ".*")
        pattern = pattern.replace("_", ".")

        regex = Literal(f"^{pattern}$")

        return RegexMatch(left, regex)

class StartsWithHandler(OperatorHandler):

    precedence = 20
    def can_handle(self, tok, ctx):
        return tok.type == TokenType.STARTSWITH

    def parse(self, parser, ctx, left):
        ctx.consume()

        prec = parser.PRECEDENCE["STARTSWITH"]

        right = parser.parse(ctx, prec + 1)

        regex = Literal(
            f"^{re.escape(str(right.value))}.*"
        )

        return RegexMatch(left, regex)

class EndsWithHandler(OperatorHandler):

    precedence = 20
    def can_handle(self, tok, ctx):
        return tok.type == TokenType.ENDSWITH

    def parse(self, parser, ctx, left):
        ctx.consume()

        prec = parser.PRECEDENCE["ENDSWITH"]

        right = parser.parse(ctx, prec + 1)

        regex = Literal(
            f".*{re.escape(str(right.value))}$"
        )

        return RegexMatch(left, regex)

class ContainsHandler(OperatorHandler):

    precedence = 20
    def can_handle(self, tok, ctx):
        return tok.type == TokenType.CONTAINS

    def parse(self, parser, ctx, left):
        ctx.consume()

        prec = parser.PRECEDENCE["CONTAINS"]

        right = parser.parse(ctx, prec + 1)

        regex = Literal(
            f".*{re.escape(str(right.value))}.*"
        )

        return RegexMatch(left, regex)