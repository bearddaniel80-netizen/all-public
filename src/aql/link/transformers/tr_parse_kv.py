import re
from .base import TransformFunction
from ..registry import (
        register_function_call,
        FieldType,
        FuncType,
        SqlFunc
    ) 

@register_function_call(
        name="PARSE_KV",
        printable=SqlFunc(
            description="Parse log fields into key/value pairs.",
            template=["SELECT PARSE_KV(<field>)"],
            extra_info="Pattern by default is \s then =",
            func_type=FuncType.TRANSFORM,
            input_type=[FieldType.TEXT],
            return_type=FieldType.ATTRIBUTE
        )
    )
class ParseKVFunction(TransformFunction):

    def __init__(self):
        self.kind = "transform"

    def evaluate(self, field: str, pattern: list = ['\s', '=']):
        line = field

        p = "|".join(pattern)

        parts = re.split(p, line)

        data = {}
        i = 0
        while i < len(parts) - 1:
            key = parts[i]
            value = parts[i + 1]
            data[key] = value
            i += 2

        return data