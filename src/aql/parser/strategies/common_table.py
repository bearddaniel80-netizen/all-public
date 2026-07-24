from .base import StatementStrategy
from ...language.tokens import TokenType
from ...language.ast.statements.query import CommonTableExpression, Query
from ...language.ast.statements.set_operator import ConstantRelation, SetOperation, SetOperatorType
from ...context.analysis import AnalysisContext
from .select import SelectStrategy

class CommonTableStrategy(StatementStrategy):
    def __init__(self, query):
        self.query = query

    def can_handle(self, ctx):
        tok = ctx.peek()
        return tok and tok.type == TokenType.WITH

    def parse(self, ctx, analysis_ctx: AnalysisContext):

        if not ctx.match(TokenType.WITH):
            return self.query

        return self._parser_orchestrator(ctx, analysis_ctx)

    def _parser_orchestrator(self, ctx, analysis_ctx):
        tok = ctx.peek()

        if tok.type == TokenType.RECURSIVE:
            ctx.consume()
            self._parse_recursive_cte(ctx, analysis_ctx)
        else:
            self._parse_cte(ctx, analysis_ctx)

        return self.query

    def _parse_head(self, ctx):

        name = ctx.expect(TokenType.IDENT)

        ctx.expect(TokenType.AS)

        ctx.expect(TokenType.LPAREN)

        return name

    def _parse_tail(self, ctx, analysis_ctx, cte, name, expression):
        
        ctx.expect(TokenType.RPAREN)

        analysis_ctx.ctes[name.value] = expression

        self.query.cte.append(cte)
        
        tok = ctx.peek()

        if tok.type == TokenType.COMMA:
            ctx.consume()
            return self._parser_orchestrator(ctx, analysis_ctx)

    def _parse_recursive_cte_operator(self, ctx):
        tok = ctx.peek()

        if tok.type == TokenType.UNION:
            ctx.consume()
            tok = ctx.peek()
            if tok.type == TokenType.ALL:
                ctx.consume()
                return SetOperatorType.UNION_ALL
            ctx.consume()
            return SetOperatorType.UNION
        elif tok.type == TokenType.INTERSECT:
            ctx.consume()
            return SetOperatorType.INTERSECT
        elif tok.type == TokenType.EXCEPT:
            ctx.consume()
            return SetOperatorType.EXCEPT
        
        ctx.consume()
        return SetOperatorType.UNION_ALL
        
    def _parse_recursive_cte(self, ctx, analysis_ctx):
        
        left = ConstantRelation()

        right = Query()

        name = self._parse_head(ctx)
        
        # left = SelectStrategy(left).parse(ctx, analysis_ctx)

        operator = self._parse_recursive_cte_operator(ctx)
        
        right = SelectStrategy(right).parse(ctx, analysis_ctx)

        cte = SetOperation(name, left, right, operator)

        self._parse_tail(ctx, analysis_ctx, cte, name, right)

    def _parse_cte(self, ctx, analysis_ctx: AnalysisContext):

        cte_query = Query()

        name = self._parse_head(ctx)

        expression = SelectStrategy(cte_query).parse(ctx, analysis_ctx)

        cte = CommonTableExpression(name, expression)

        self._parse_tail(ctx, analysis_ctx, cte, name, expression)
