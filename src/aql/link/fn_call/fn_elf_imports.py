from ..registry import (
    CategoryType,
    register_function_call,
    SMEType,
    SourceFunc,
    FuncType
)

from aql_link.managers.package_loader import load

@register_function_call(
        name="elf_imports",
        printable=SourceFunc(
            category_type=[CategoryType.EXECUTABLE, CategoryType.FLATFILE],
            description="Reads from elf file all dependencies.",
            requirements=["elftools"],
            sme_type=SMEType.LEGACY,
            func_type=FuncType.ADAPTER,
            enabled=False
        )
    )
class ElfImportsTableFunction:

    def execute(self, *args):
        raise NotImplementedError("coming soon")
        path = args[0]
        load("elf")
        from aql_elf.adaptor.elf_source import ELFImportsSource

        source = ELFImportsSource.from_file(path)

        return source.to_dataset()