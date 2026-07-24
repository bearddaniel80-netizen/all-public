from .base import Stage
from collections import defaultdict

class GroupByStage(Stage):
    def execute(self, context):

        if not context.query.group_by:
            return context

        groups = defaultdict(list)

        for row in context.rows:

            key = tuple(
                row[field.name]
                for field in context.query.group_by.fields
            )

            groups[key].append(row)

        context.groups = groups

        return context