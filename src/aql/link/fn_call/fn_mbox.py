from ..registry import (
    CatagoryType,
    register_function_call,
    SMEType,
    SourceFunc
)

from ...engine.package_loader import load

@register_function_call(
        name="mbox",
        printable=SourceFunc(
            catagory_type=[CatagoryType.FLATFILE],
            description="Reads message.",
            sme_type=SMEType.SECURITY
        )
    )
class MboxTableFunction:

    def execute(self, *args):
        path = args[0]
        load("mbox")
        from aql_mbox.adaptor.mbox_source import MboxSource

        source = MboxSource.from_file(path)

        return source.to_dataset()