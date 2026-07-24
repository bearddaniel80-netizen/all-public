from .base import Stage
from ..query_exec_context import ExecutionContext
from ....context.analysis import AnalysisContext

class CTEExecutor:

    def __init__(self, context):
        self.context = context

    def execute(self):

        for cte in self.context.query.cte:

            if cte.recursive:
                rows = self._execute_recursive(cte)
            else:
                rows = self._execute_normal(cte)

            self.context.ctes[cte.name.value] = rows

    def _execute_normal(self, cte):

        child = self._child_context(cte.query)

        self._run_pipeline(child)

        return child.rows

    def _execute_recursive(self, cte):

        anchor = cte.left
        recursive = cte.right

        #
        # Execute anchor
        #
        result = list(self._execute_query(anchor))

        #
        # Current iteration
        #
        delta = result

        while delta:

            #
            # Make previous iteration visible
            #
            self.context.ctes[cte.name.value] = delta

            #
            # Execute recursive member
            #
            new_rows = list(self._execute_query(recursive))

            #
            # UNION
            #
            new_rows = self._remove_duplicates(
                result,
                new_rows,
            )

            if not new_rows:
                break

            result.extend(new_rows)

            delta = new_rows

        return result
    
    def _remove_duplicates(self, result, new_rows):

        seen = {
            tuple(sorted(row.items()))
            for row in result
        }

        output = []

        for row in new_rows:

            key = tuple(sorted(row.items()))

            if key not in seen:
                seen.add(key)
                output.append(row)

        return output

    def _execute_query(self, query):

        child = self._child_context(query)

        self._run_pipeline(child)

        return child.rows

    def _child_context(self, query):

        # create a child execution context
        child = ExecutionContext(
            query, 
            self.context.engine_context, 
            AnalysisContext(""), 
            self.context.pipeline
        )

        #
        # Share already materialized CTEs
        #
        child.ctes = dict(self.context.ctes)

        return child

    def _run_pipeline(self, child):

        # execute the CTE query using the normal pipeline
        for stage in self.context.pipeline:
            child = stage.execute(child)

class CTEStage(Stage):

    def execute(self, context):

        executor = CTEExecutor(context)

        executor.execute()

        return context