from .base import ScalarFunction
from ..registry import (
        register_function_call,
        FieldType,
        FuncType,
        SqlFunc
    ) 
@register_function_call(
        name="CAPITALIZE",
        printable=SqlFunc(
            description="Capitalize first letter in each word in a sentence.",
            example="CAPITALIZE(<field>)",
            func_type=FuncType.SCALAR,
            input_type=[FieldType.TEXT],
            return_type=FieldType.TEXT
        )
    )
class CapitalizeFunction(ScalarFunction):

    def __init__(self):
        self.kind = "scalar"

    def evaluate(self, value):
        return value.capitalize()