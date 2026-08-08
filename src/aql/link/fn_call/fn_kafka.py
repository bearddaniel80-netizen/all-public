from ..registry import (
    CategoryType,
    register_function_call,
    SMEType,
    SourceFunc,
    FuncType
)

from aql_link.managers.package_loader import load

@register_function_call(
        name="kafka",
        printable=SourceFunc(
            category_type=[CategoryType.NETWORK, CategoryType.STREAM],
            description="Reads kafka trafic.",
            func_type=FuncType.ADAPTER,
            enabled=False
        )
    )
class KafkaTableFunction:

    def execute(self, *args):
        raise NotImplementedError("coming soon")