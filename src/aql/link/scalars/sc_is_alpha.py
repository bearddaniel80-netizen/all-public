from .base import ScalarFunction
from ..registry import (
        register_function_call,
        FieldType,
        FuncType,
        SqlFunc
    ) 

@register_function_call(
        name="IS_ALPHA",
        printable=SqlFunc(
            description="Checks if field DOES NOT contain numbers, puncation, nor spaces.",
            example="IS_ALPHA(<field>)",
            func_type=FuncType.SCALAR,
            input_type=[FieldType.TEXT],
            return_type=FieldType.BOOL
        )
    )
class IsAlphaFunction(ScalarFunction):

    def __init__(self):
        self.kind = "scalar"

    def evaluate(self, value):
        return value.isalpha()