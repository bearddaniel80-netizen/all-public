from .base import AggregateFunction
from ..registry import (
        register_function_call,
        FieldType,
        FuncType,
        SqlFunc
    ) 

@register_function_call(
        name="MAX",
        printable=SqlFunc(
            description="Find largest value in a collection.",
            example="MAX(<field>)",
            func_type=FuncType.AGGREGATE,
            input_type=[FieldType.INT],
            return_type=FieldType.INT
        )
    )
class MaxFunction(AggregateFunction):

    def __init__(self):
        self.kind = "aggregate"
        self._max = 0

    def step(self, value):
        if self._max < int(value):
            self._max = int(value)

    def finalize(self):
        return self._max