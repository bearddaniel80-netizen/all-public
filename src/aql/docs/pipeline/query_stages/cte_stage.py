from .base import StageBase

class CteStage(StageBase):
    def create(self, ctx):
        template = f"WITH generic_cte AS ( <placeholder> ) SELECT * FROM generic_cte"

        cte_queries = [ template.replace("<placeholder>", q) for q in ctx.queries ]

        ctx.add(cte_queries)
