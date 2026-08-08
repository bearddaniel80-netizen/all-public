from .base import ScalarFunction
from ..registry import (
        register_function_call,
        FieldType,
        FuncType,
        SqlFunc
    ) 

@register_function_call(
        name="IS_UPPER",
        printable=SqlFunc(
            description="Checks all letters are upper case.",
            template=["SELECT IS_UPPER(<field:str>)"],
            func_type=FuncType.SCALAR,
            input_type=[FieldType.TEXT],
            return_type=FieldType.BOOL,
            needs_groupby=False
        )
    )
class IsUpperFunction(ScalarFunction):

    def __init__(self):
        self.kind = "scalar"

    def evaluate(self, value):
        return value.isupper()