from ..registry import (
    CategoryType,
    register_function_call,
    SourceFunc,
    FuncType
)

from aql_link.managers.package_loader import load

@register_function_call(
        name="aql_script",
        printable=SourceFunc(
            category_type=[CategoryType.FLATFILE],
            description="Reads aql script file.",
            func_type=FuncType.ADAPTER,
            enabled=False
        )
    )
class AqlScriptFunction:

    def execute(self, *args):
        raise NotImplementedError("coming soon")