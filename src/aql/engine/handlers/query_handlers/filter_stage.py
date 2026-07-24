from .base import Stage
from ....evalulators.evalulate import Evaluator

class FilterStage(Stage):

    def __init__(self):
        self.evaluator = Evaluator()

    def execute(self, context):

        query = context.query

        if not query.where:
            return context

        # self.validate(query)

        context.rows = (
            row
            for row in context.rows
            if self.evaluator.evaluate(
                query.where,
                row
            )
        )

        return context

    def validate(self, query):
        """ This will go in the validation pipeline """
        if contains_aggregate(
            query.where
        ):
            raise SyntaxError(
                "Aggregate functions are not allowed in WHERE"
            )