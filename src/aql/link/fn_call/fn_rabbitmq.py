from ..registry import (
    CategoryType,
    register_function_call,
    SMEType,
    SourceFunc,
    FuncType
)

from aql_link.managers.package_loader import load

@register_function_call(
        name="rabbitmq",
        printable=SourceFunc(
            category_type=[CategoryType.NETWORK, CategoryType.STREAM],
            description="Reads rabbitmq trafic.",
            func_type=FuncType.ADAPTER,
            enabled=False
        )
    )
class RabbitMQTableFunction:

    def execute(self, *args):
        raise NotImplementedError("coming soon")