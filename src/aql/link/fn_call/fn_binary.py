from ..registry import (
    CategoryType,
    register_function_call,
    SMEType,
    SourceFunc,
    FuncType
)

from aql_link.managers.package_loader import load

@register_function_call(
        name="binary",
        printable=SourceFunc(
            catagory_type=[CategoryType.EXECUTABLE, CategoryType.STORAGE],
            description="Reads from storage format.",
            sme_type=SMEType.SECURITY,
            func_type=FuncType.ADAPTER,
            template="SELECT * FROM bin(<file>)",
            enabled=False
        )
    )
class BinaryTableFunction:

    def execute(self, *args):
        raise NotImplementedError("coming soon")
        path = args[0]
        load("binary")
        from aql_bin.adaptor.binary_source import BinarySource

        source = BinarySource.from_file(path)

        return source.to_dataset()