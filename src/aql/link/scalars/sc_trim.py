from .base import ScalarFunction
from ..registry import (
        register_function_call,
        FieldType,
        FuncType,
        SqlFunc
    ) 

@register_function_call(
        name="TRIM",
        printable=SqlFunc(
            description="Remove whitespace before and after.",
            example="TRIM(<field>)",
            func_type=FuncType.SCALAR,
            input_type=[FieldType.TEXT],
            return_type=FieldType.TEXT
        )
    )
class TrimFunction(ScalarFunction):

    def __init__(self):
        self.kind = "scalar"

    def evaluate(self, value):
        return value.strip()