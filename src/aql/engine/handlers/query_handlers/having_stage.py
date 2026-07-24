from .base import Stage
from ..query_exec_context import ExecutionContext

class HavingStage(Stage):

    def execute(self, context: ExecutionContext):

        if context.query.having:

            context.rows = (
                row
                for row in context.rows
                if context.engine_context.evaluator.evaluate(
                    context.query.having,
                    row
                )
            )

        return context
