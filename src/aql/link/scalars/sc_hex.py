from .base import ScalarFunction
from ..registry import (
        register_function_call,
        FieldType,
        FuncType,
        SqlFunc
    ) 

@register_function_call(
        name="HEX",
        printable=SqlFunc(
            description="Returns hexadecimal value.",
            example="HEX(<field>)",
            func_type=FuncType.SCALAR,
            input_type=[FieldType.NUMBER],
            return_type=FieldType.TEXT
        )
    )
class HexFunction(ScalarFunction):

    def __init__(self):
        self.kind = "scalar"

    def evaluate(self, value):
        return hex(value)