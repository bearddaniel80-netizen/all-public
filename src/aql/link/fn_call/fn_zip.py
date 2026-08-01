from ..registry import (
    CategoryType,
    register_function_call,
    SourceFunc,
    FuncType
)

from aql_link.managers.package_loader import load

@register_function_call(
        name="zip",
        printable=SourceFunc(
            catagory_type=[CategoryType.FLATFILE, CategoryType.ARCHIVE],
            description="Reads headers in archive file.",
            func_type=FuncType.ADAPTER,
            template="SELECT * FROM zip(<file>)",
            enabled=False
        )
    )
class ZipTableFunction:

    def execute(self, *args):
        raise NotImplementedError("coming soon")
        path = args[0]
        load("zip")
        from aql_zip.adaptor.zip_source import ZipSource

        source = ZipSource.from_file(path)

        return source.to_dataset()