from .base import Stage
from ..query_exec_context import ExecutionContext
from ....context.analysis import AnalysisContext

class CTEStage(Stage):

    def execute(self, context):

        query = context.query

        if not query.cte:
            return context

        for cte in query.cte:

            name = cte.name.value

            rows = self.execute_cte(
                cte.query,
                context
            )

            context.ctes[name] = rows

        return context


    def execute_cte(self, query, context):

        # create a child execution context
        child = ExecutionContext(
            query, 
            context.engine_context, 
            AnalysisContext(""), 
            context.pipeline
        )

        # execute the CTE query using the normal pipeline
        for stage in context.pipeline:
            child = stage.execute(child)

        return child.rows