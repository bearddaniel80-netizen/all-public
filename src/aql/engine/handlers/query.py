from ...language.ast.statements.query import Query
from .base import BaseHandler
from .query_exec_context import ExecutionContext
from .query_handlers.cte_stage import CTEStage
from .query_handlers.source_stage import SourceStage
from .query_handlers.filter_stage import FilterStage
from .query_handlers.aggregate_stage import AggregateStage
from .query_handlers.projection_stage import ProjectStage
from .query_handlers.groupby_stage import GroupByStage
from .query_handlers.having_stage import HavingStage
from .query_handlers.orderby_stage import OrderByStage
from .query_handlers.limit_stage import LimitStage
from ...validate.query_analyzer import QueryAnalyzer
from ..registry import register_handler
from ...context.analysis import AnalysisContext

@register_handler
class QueryHandler(BaseHandler):
    def __init__(self, engine_context):
        self.engine_context = engine_context
        self.data_sources = engine_context.data_sources
        self.evaluator = engine_context.evaluator

    def can_handle(self, ast):
        return isinstance(ast, Query)

    def handle(self, analysis_ctx: AnalysisContext):

        query = analysis_ctx.artifacts["ast"]

        if QueryAnalyzer.has_aggregate(query):
            pipeline = [
                CTEStage(),
                SourceStage(),
                FilterStage(),
                GroupByStage(),
                AggregateStage(),
                HavingStage(),
                # ProjectStage(),
                OrderByStage(),
                LimitStage(),
            ]
        else:
            pipeline = [
                CTEStage(),
                SourceStage(),
                FilterStage(),
                GroupByStage(),
                HavingStage(),
                ProjectStage(),
                OrderByStage(),
                LimitStage(),
            ]

        context = ExecutionContext(
            query, 
            self.engine_context, 
            analysis_ctx, 
            pipeline
        )

        for stage in pipeline:
            context = stage.execute(context)

        return context.rows
