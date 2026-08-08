import math
from .base import AggregateFunction
from ..registry import (
        register_function_call,
        FieldType,
        FuncType,
        SqlFunc
    ) 

@register_function_call(
        name="MIN",
        printable=SqlFunc(
            description="Find smallest value in a collection.",
            template=[
                "SELECT MIN(<field:int>)",
                "HAVING MIN(<field:int>) <op:int> <value:int>",
                "HAVING MIN(<field:int>) BETWEEN <value:int> AND <value:int>",
                "HAVING MIN(<field:int>) IN [<value:int>, <value:int>]",
                "ORDER BY MIN(<field:int>)"
            ],
            func_type=FuncType.AGGREGATE,
            input_type=[FieldType.INT],
            return_type=FieldType.INT,
            needs_groupby=True
        )
    )
class MinFunction(AggregateFunction):

    def __init__(self):
        self.kind = "aggregate"
        self._min = math.inf

    def step(self, value):
        if self._min > int(value):
            self._min = int(value)

    def finalize(self):
        return self._min