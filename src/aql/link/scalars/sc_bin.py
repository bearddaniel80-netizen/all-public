from .base import ScalarFunction
from ..registry import (
        register_function_call,
        FieldType,
        FuncType,
        SqlFunc
    ) 

@register_function_call(
        name="BIN",
        printable=SqlFunc(
            description="Returns binary value.",
            template=["SELECT BIN(<field>)"],
            func_type=FuncType.SCALAR,
            input_type=[FieldType.INT, FieldType.FLOAT, FieldType.COMPLEX],
            return_type=FieldType.INT
        )
    )
class BinFunction(ScalarFunction):

    def __init__(self):
        self.kind = "scalar"

    def evaluate(self, value):
        return bin(value)