from ..registry import (
    CatagoryType,
    register_function_call,
    SourceFunc
)

from ...engine.package_loader import load

@register_function_call(
        name="7z",
        printable=SourceFunc(
            catagory_type=[CatagoryType.FLATFILE, CatagoryType.ARCHIVE],
            description="Reads headers in archive file.",
            requirements=["py7zr"]
        )
    )
class SevenZipTableFunction:

    def execute(self, *args):
        path = args[0]
        load("sevenzip")
        from aql_sevenzip.adaptor.sevenzip_source import SevenZipSource

        source = SevenZipSource.from_file(path)

        return source.to_dataset()