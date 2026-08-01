from .base import AggregateFunction
from ..registry import (
        register_function_call,
        FieldType,
        FuncType,
        SqlFunc
    ) 

@register_function_call(
        name="COUNT",
        printable=SqlFunc(
            description="Count elements in a collection.",
            template=[
                "SELECT COUNT(<field>)",
                "HAVING COUNT(<field>) <op> <value:int>",
                "ORDER BY COUNT(<field>)"
            ],
            func_type=FuncType.AGGREGATE,
            input_type=[FieldType.INT],
            return_type=FieldType.INT,
            needs_groupby=True
        )
    )
class CountFunction(AggregateFunction):

    def __init__(self):
        self.kind = "aggregate"
        self.total = 0

    def step(self, value):
        self.total += 1

    def finalize(self):
        return self.total