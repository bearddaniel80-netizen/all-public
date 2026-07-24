from .....language.tokens import TokenType
from .....language.ast.identifier import Identifier
from .....language.ast.function_call import FunctionCall
from ....expressions.parser import ExpressionParser
from .....context.analysis import AnalysisContext

class ProjectionParser:

    def parse(self, ctx, analysis_ctx: AnalysisContext, target):

        fields = []

        while True:

            fields.append(
                self.parse_item(ctx, analysis_ctx, target)
            )

            if not ctx.match(TokenType.COMMA):
                break

        return fields

    def parse_item(self, ctx, analysis_ctx, target):

        tok = ctx.peek()

        #
        # *
        #
        if tok.type == TokenType.STAR:

            ctx.consume()

            expr = Identifier("*")

        #
        # COUNT(...)
        # SUM(...)
        # UPPER(...)
        #
        elif (
            tok.type == TokenType.IDENT
            and ctx.peek_next()
            and ctx.peek_next().type == TokenType.LPAREN
        ):
            expr = self.parse_function(ctx, analysis_ctx, target)

        #
        # identifier
        #
        else:

            ident = ctx.expect(TokenType.IDENT)

            expr = Identifier(ident.value)

        return self.parse_alias(ctx, expr, analysis_ctx, target)

    def parse_function(self, ctx, analysis_ctx: AnalysisContext, target):

        ident = ctx.expect(TokenType.IDENT)

        ctx.expect(TokenType.LPAREN)

        args = []

        if ctx.peek().type != TokenType.RPAREN:

            while True:

                #
                # COUNT(*)
                #
                if ctx.peek().type == TokenType.STAR:

                    ctx.consume()

                    args.append(
                        Identifier("*")
                    )

                else:

                    args.append(
                        ExpressionParser(analysis_ctx, target).parse(ctx)
                    )

                if not ctx.match(TokenType.COMMA):
                    break

        ctx.expect(TokenType.RPAREN)

        return FunctionCall(
            ident.value.upper(),
            args,
            None
        )

    def parse_alias(self, ctx, expr, analysis_ctx: AnalysisContext, target):

        if not ctx.match(TokenType.AS):
            return expr

        tok = ctx.consume()

        if tok.type not in (
            TokenType.IDENT,
            TokenType.STRING,
        ):
            analysis_ctx.artifacts["diagnostic"].warning("PSCPP01", f"Expected alias name in {target}.", "Need a literal")

            tok = ctx.consume()

        else:

            expr.alias = tok.value

        return expr