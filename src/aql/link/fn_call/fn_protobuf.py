from ..registry import (
    CatagoryType,
    register_function_call,
    SourceFunc
)

from ...engine.package_loader import load

@register_function_call(
        name="protobuf",
        printable=SourceFunc(
            catagory_type=[CatagoryType.FLATFILE],
            description="Reads strongly typed JSON file.",
            requirements=["protobuf"]
        )
    )
class ProtobufTableFunction:

    def execute(self, *args):
        path = args[0]
        load("protobuf")
        from aql_prrotobuf.adaptor.protobuf_source import ProtobufSource

        source = ProtobufSource.from_file(path)

        return source.to_dataset()