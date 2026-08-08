from .base import ScalarFunction
from ..registry import (
        register_function_call,
        FieldType,
        FuncType,
        SqlFunc
    ) 

@register_function_call(
        name="LOWER",
        printable=SqlFunc(
            description="Make every letter lower case.",
            template=["SELECT LOWER(<field:str>)"],
            func_type=FuncType.SCALAR,
            input_type=[FieldType.TEXT],
            return_type=FieldType.TEXT,
            needs_groupby=False
        )
    )
class LowerFunction(ScalarFunction):

    def __init__(self):
        self.kind = "scalar"

    def evaluate(self, value):
        return value.lower()