from ..registry import (
    CategoryType,
    register_function_call,
    SMEType,
    SourceFunc,
    FuncType
)

from aql_link.managers.package_loader import load

@register_function_call(
        name="elf",
        printable=SourceFunc(
            category_type=[CategoryType.EXECUTABLE, CategoryType.FLATFILE],
            description="Reads from file.",
            requirements=["elftools"],
            sme_type=SMEType.LEGACY,
            func_type=FuncType.ADAPTER,
            enabled=False
        )
    )
class ElfTableFunction:

    def execute(self, *args):
        raise NotImplementedError("coming soon")
        path = args[0]
        load("elf")
        from aql_elf.adaptor.elf_source import ELFSource

        source = ELFSource.from_file(path)

        return source.to_dataset()