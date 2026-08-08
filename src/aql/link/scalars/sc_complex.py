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
            template=[
                "SELECT COMPLEX(<field:int>)",
            ],
            func_type=FuncType.SCALAR,
            input_type=[FieldType.INT, FieldType.FLOAT, FieldType.COMPLEX],
            return_type=FieldType.INT,
            needs_groupby=False
        )
    )
class ComplexFunction(ScalarFunction):

    def __init__(self):
        self.kind = "scalar"

    def evaluate(self, value):
        return complex(value)