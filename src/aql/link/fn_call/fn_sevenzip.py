from ..registry import (
    CategoryType,
    register_function_call,
    SourceFunc,
    FuncType
)

from aql_link.managers.package_loader import load

@register_function_call(
        name="7z",
        printable=SourceFunc(
            catagory_type=[CategoryType.FLATFILE, CategoryType.ARCHIVE],
            description="Reads headers in archive file.",
            requirements=["py7zr"],
            func_type=FuncType.ADAPTER,
            template="SELECT * FROM 7z(<file>)",
            enabled=False
        )
    )
class SevenZipTableFunction:

    def execute(self, *args):
        raise NotImplementedError("coming soon")
        path = args[0]
        load("sevenzip")
        from aql_sevenzip.adaptor.sevenzip_source import SevenZipSource

        source = SevenZipSource.from_file(path)

        return source.to_dataset()