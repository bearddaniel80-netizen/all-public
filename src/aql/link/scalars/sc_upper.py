from .base import ScalarFunction
from ..registry import (
        register_function_call,
        FieldType,
        FuncType,
        SqlFunc
    ) 

@register_function_call(
        name="UPPER",
        printable=SqlFunc(
            description="Make every letter upper case.",
            template=["SELECT UPPER(<field:str>)"],
            func_type=FuncType.SCALAR,
            input_type=[FieldType.TEXT],
            return_type=FieldType.TEXT,
            needs_groupby=False
        )
    )
class UpperFunction(ScalarFunction):

    def __init__(self):
        self.kind = "scalar"

    def evaluate(self, value):
        return value.upper()