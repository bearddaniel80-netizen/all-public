from .base import AggregateFunction
from ..registry import (
        register_function_call,
        FieldType,
        FuncType,
        SqlFunc
    ) 

@register_function_call(
        name="SUM",
        printable=SqlFunc(
            description="Add all values in a collection.",
            template=[
                "SELECT SUM(<field>)",
                "HAVING SUM(<field>) <op> <value:int>",
                "ORDER BY SUM(<field>)"
            ],
            func_type=FuncType.AGGREGATE,
            input_type=[FieldType.INT],
            return_type=FieldType.INT,
            needs_groupby=True
        )
    )
class SumFunction(AggregateFunction):

    def __init__(self):
        self.kind = "aggregate"
        self.total = 0

    def step(self, value):
        self.total += int(value)

    def finalize(self):
        return self.total