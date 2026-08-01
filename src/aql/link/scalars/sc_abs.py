from .base import ScalarFunction
from ..registry import (
        register_function_call,
        FieldType,
        FuncType,
        SqlFunc
    ) 

@register_function_call(
        name="ABS",
        printable=SqlFunc(
            description="Returns distance from 0.",
            template=["SELECT ABS(<field>)"],
            extra_info="Integers return Integer; Float return floating integer; Complex return complex",
            func_type=FuncType.SCALAR,
            input_type=[FieldType.INT, FieldType.FLOAT, FieldType.COMPLEX],
            return_type=FieldType.INT
        )
    )
class AbsFunction(ScalarFunction):

    def __init__(self):
        self.kind = "scalar"

    def evaluate(self, value):
        return abs(value)