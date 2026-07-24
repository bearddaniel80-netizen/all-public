from itertools import islice

from .base import Stage

class LimitStage(Stage):

    def execute(self, context):

        limit = context.query.limit

        if limit is None:
            return context

        context.rows = islice(
            context.rows,
            limit
        )

        return context