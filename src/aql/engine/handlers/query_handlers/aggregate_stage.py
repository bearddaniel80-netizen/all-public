from .base import Stage
from ....language.ast.function_call import FunctionCall
from ....link import aggregates
from ....link.registry import FUNCTION_CALL_REGISTRY

class AggregateStage(Stage):

    def execute(self, context):

        query = context.query

        aggregates = [
            field
            for field in query.select
            if self.is_aggregate(field)
        ]

        if not aggregates:
            return context

        non_aggregates = [
            f for f in query.select
            if not self.is_aggregate(f)
        ]

        """ This will go in the validation pipeline """
        if aggregates and non_aggregates and not context.groups:
            raise SyntaxError(
                "Mixing aggregate and non-aggregate fields requires GROUP BY"
            )

        if context.groups:

            output = []

            for group_key, rows in context.groups.items():

                result = {}

                # Emit GROUP BY columns
                for field, value in zip(query.group_by.fields, group_key):
                    result[field.alias or field.name] = value

                # Emit aggregates
                for field in aggregates:

                    fn_cls = FUNCTION_CALL_REGISTRY[field.name]

                    arg = field.arg[0]

                    if getattr(arg, "name", None) == "*":
                        for _ in rows:
                            fn_cls.step(1)
                    else:
                        for row in rows:
                            value = row.get(arg.name)
                            if value is not None:
                                fn_cls.step(value)

                    result[field.alias or field.name] = fn_cls.finalize()

                output.append(result)

            context.rows = output

        return context

    def is_aggregate(self, field):

        if not isinstance(field, FunctionCall):
            return False

        fn_cls = FUNCTION_CALL_REGISTRY.get(field.name)

        if fn_cls is None:
            return False

        return fn_cls.kind == "aggregate"