from .base import AggregateFunction
from ..registry import (
        register_function_call,
        FieldType,
        FuncType,
        SqlFunc
    )
from ...engine.module_loader import load

@register_function_call(
        name="AVG",
        printable=SqlFunc(
            description="Find average or mean of a collection.",
            example="AVG(<field>)",
            func_type=FuncType.AGGREGATE,
            input_type=[FieldType.INT],
            return_type=FieldType.FLOAT
        )
    )
class AverageFunction(AggregateFunction):

    def __init__(self):
        self.kind = "aggregate"
        self.values = []

    def step(self, value):
        self.values.append(value)

    def finalize(self):
        load("numpy")
        import numpy as np
        return np.average(self.values)