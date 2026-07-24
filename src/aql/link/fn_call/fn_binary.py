from ..registry import (
    CatagoryType,
    register_function_call,
    SMEType,
    SourceFunc
)

from ...engine.package_loader import load

@register_function_call(
        name="binary",
        printable=SourceFunc(
            catagory_type=[CatagoryType.EXECUTABLE, CatagoryType.STORAGE],
            description="Reads from storage format.",
            sme_type=SMEType.SECURITY
        )
    )
class BinaryTableFunction:

    def execute(self, *args):
        path = args[0]
        load("binary")
        from aql_bin.adaptor.binary_source import BinarySource

        source = BinarySource.from_file(path)

        return source.to_dataset()