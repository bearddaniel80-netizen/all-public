from .....language.tokens import TokenType
from .....language.ast.identifier import Identifier
from .....language.ast.function_call import TableFunctionCall
from ....expressions.parser import ExpressionParser
from .....context.analysis import AnalysisContext


class FromParser:

    def parse(self, ctx, analysis_ctx: AnalysisContext):

        ident = ctx.expect(TokenType.IDENT)

        #
        # csv(...)
        # json(...)
        # stdin(...)
        #
        if ctx.match(TokenType.LPAREN):

            args = []

            if ctx.peek().type != TokenType.RPAREN:

                while True:

                    args.append(
                        ExpressionParser(analysis_ctx, "source").parse(ctx)
                    )

                    if not ctx.match(TokenType.COMMA):
                        break

            ctx.expect(TokenType.RPAREN)

            alias = None

            if ctx.match(TokenType.AS):

                tok = ctx.consume()

                if tok.type not in (
                    TokenType.IDENT,
                    TokenType.STRING,
                ):
                    analysis_ctx.artifacts["diagnostic"].warning("PSCPF01", f"Expected alias name in source.", "Need a literal")

                    tok = ctx.consume()

                else:
                    alias = tok.value

            return TableFunctionCall(
                name=ident.value,
                arg=args,
                alias=alias,
            )

        #
        # table_name
        #
        return Identifier(ident.value)