from .base import ScalarFunction
from ..registry import (
        register_function_call,
        FieldType,
        FuncType,
        SqlFunc
    ) 

@register_function_call(
        name="OCT",
        printable=SqlFunc(
            description="Returns oct value.",
            example="OCT(<field>)",
            func_type=FuncType.SCALAR,
            input_type=[FieldType.NUMBER],
            return_type=FieldType.TEXT
        )
    )
class OctFunction(ScalarFunction):

    def __init__(self):
        self.kind = "scalar"

    def evaluate(self, value):
        return oct(value)