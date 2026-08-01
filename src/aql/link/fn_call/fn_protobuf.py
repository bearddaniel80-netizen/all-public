from ..registry import (
    CategoryType,
    register_function_call,
    SourceFunc,
    FuncType
)

from aql_link.managers.package_loader import load

@register_function_call(
        name="protobuf",
        printable=SourceFunc(
            catagory_type=[CategoryType.FLATFILE],
            description="Reads strongly typed JSON file.",
            requirements=["protobuf"],
            func_type=FuncType.ADAPTER,
            template="SELECT * FROM protobuf(<file>)",
            enabled=False
        )
    )
class ProtobufTableFunction:

    def execute(self, *args):
        raise NotImplementedError("coming soon")
        path = args[0]
        load("protobuf")
        from aql_prrotobuf.adaptor.protobuf_source import ProtobufSource

        source = ProtobufSource.from_file(path)

        return source.to_dataset()