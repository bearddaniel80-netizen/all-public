from .base import ScalarFunction
from ..registry import (
        register_function_call,
        FieldType,
        FuncType,
        SqlFunc
    ) 

@register_function_call(
        name="COMPLEX",
        printable=SqlFunc(
            description="Returns complex value.",
            example="COMPLEX(<field>)",
            func_type=FuncType.SCALAR,
            input_type=[FieldType.NUMBER],
            return_type=FieldType.NUMBER
        )
    )
class ComplexFunction(ScalarFunction):

    def __init__(self):
        self.kind = "scalar"

    def evaluate(self, value):
        return complex(value)