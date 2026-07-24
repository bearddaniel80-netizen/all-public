from .datacls.logical import LogicalPlan
from .datacls.field import Field

class Planner:
    def __init__(self, context):
        self.context = context  # runtime info (stdin, ddl, etc.)

    def plan(self, ast):
        self.source = self._resolve_source(ast)
        self.projections = self._resolve_projection(ast)
        self.filters = self._resolve_filters(ast)

        return LogicalPlan(self.source, self.projections, self.filters)

    def _resolve_source(self, ast):
        if ast.source:
            return ast.source

        if self.context.has_stdin:
            return "stdin"

        raise ValueError("Missing FROM clause and no stdin provided")

    def _resolve_projection(self, ast):
        if not ast.select:
            return [Field("*")]

        return [Field(f) for f in ast.select]

    def _resolve_filters(self, ast):
        return ast.where or []