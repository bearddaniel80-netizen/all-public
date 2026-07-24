from .base import Stage
from ..query_exec_context import ExecutionContext

class SourceStage(Stage):

    def execute(self, context: ExecutionContext):

        if context.query.source is None:
            # One synthetic row
            context.rows = [{}]
            return context

        if context.query.source == "stdin":
            data, model_cls = context.engine_context.source_resolver.resolve(context.query.source,context.engine_context,context.analysis_ctx)
        else:
            name = context.query.source.name

            if name in context.ctes:
                context.rows = context.ctes[name]
                context.rows = self._add_id(context.rows)
                return context
            data = context.engine_context.source_resolver.resolve(context.query.source,context.engine_context,context.analysis_ctx)

        if data is None:
            raise ValueError(f"Unknown source: {context.query.source}")

        context.rows = data
        
        context.rows = self._add_id(context.rows)

        return context

    def _add_id(self, data):
        tmp = list(data)
        for i in range(0, len(tmp)):
            tmp[i]["ID"] = i + 1

        return tmp
