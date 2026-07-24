from .base import Stage

class OrderByStage(Stage):

    def execute(self, context):

        query = context.query

        if not query.order_by:
            return context

        context.rows = sorted(
            context.rows,
            key=self.build_key(query.order_by.field),
            reverse=query.order_by.descending
        )

        return context

    def build_key(self, field):
        def key(row):
            value = row.get(field)

            return (
                value is None,
                value
            )

        return key