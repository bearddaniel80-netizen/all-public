from ..registry import (
    CatagoryType,
    register_function_call,
    SourceFunc
)

from ...engine.package_loader import load

@register_function_call(
        name="zip",
        printable=SourceFunc(
            catagory_type=[CatagoryType.FLATFILE, CatagoryType.ARCHIVE],
            description="Reads headers in archive file."
        )
    )
class ZipTableFunction:

    def execute(self, *args):
        path = args[0]
        load("zip")
        from aql_zip.adaptor.zip_source import ZipSource

        source = ZipSource.from_file(path)

        return source.to_dataset()