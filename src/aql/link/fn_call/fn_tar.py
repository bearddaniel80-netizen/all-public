from ..registry import (
    CatagoryType,
    register_function_call,
    SourceFunc
)

from ...engine.package_loader import load

@register_function_call(
        name="tar",
        printable=SourceFunc(
            catagory_type=[CatagoryType.FLATFILE, CatagoryType.ARCHIVE],
            description="Reads headers in archive file."
        )
    )
class TarTableFunction:

    def execute(self, *args):
        path = args[0]
        load("tar")
        from aql_tar.adaptor.tar_source import TarSource

        source = TarSource.from_file(path)

        return source.to_dataset()