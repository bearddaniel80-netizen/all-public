import re
from ..base import StageBase

class ValidateStage(StageBase):
    def __init__(self):
        self.UNRESOLVED = re.compile(r"<(?:field|op):[^>]+>")

    def _is_valid_query(self, query: str) -> bool:
        return self.UNRESOLVED.search(query) is None

    def create(self, ctx):
        queries = list(filter(self._is_valid_query, ctx.queries))

        ctx.queries = queries
