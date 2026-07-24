from .....language.tokens import TokenType
from .....language.ast.expressions.order_by import OrderBy
from .projection import ProjectionParser
from .....context.analysis import AnalysisContext

class OrderByParser:

    def parse(self, ctx, analysis_ctx: AnalysisContext):

        fields = []

        while True:

            expr = ProjectionParser().parse_item(ctx, analysis_ctx, "order_by")

            descending = False

            if ctx.match(TokenType.DESC):
                descending = True

            elif ctx.match(TokenType.ASC):
                descending = False

            fields.append(
                OrderBy(
                    expr,
                    descending
                )
            )

            if not ctx.match(TokenType.COMMA):
                break

        return fields