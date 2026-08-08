from ..registry import (
    CategoryType,
    register_function_call,
    SMEType,
    SourceFunc,
    FuncType
)

from aql_link.managers.package_loader import load

@register_function_call(
        name="mbox",
        printable=SourceFunc(
            category_type=[CategoryType.FLATFILE],
            description="Reads message.",
            sme_type=SMEType.SECURITY,
            func_type=FuncType.ADAPTER,
            enabled=False
        )
    )
class MboxTableFunction:

    def execute(self, *args):
        raise NotImplementedError("coming soon")
        path = args[0]
        load("mbox")
        from aql_mbox.adaptor.mbox_source import MboxSource

        source = MboxSource.from_file(path)

        return source.to_dataset()