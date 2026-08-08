from ..registry import (
    CategoryType,
    register_function_call,
    SMEType,
    SourceFunc,
    FuncType
)

from aql_link.managers.package_loader import load

@register_function_call(
        name="pe",
        printable=SourceFunc(
            category_type=[CategoryType.FLATFILE],
            description="Reads maleware anomolies.",
            requirements=["pefile"],
            sme_type=SMEType.SECURITY,
            func_type=FuncType.ADAPTER,
            enabled=False
        )
    )
class PeTableFunction:

    def execute(self, *args):
        raise NotImplementedError("coming soon")
        path = args[0]
        load("pe")
        from aql_pe.adaptor.pe_source import PESource

        source = PESource.from_file(path)

        return source.to_dataset()