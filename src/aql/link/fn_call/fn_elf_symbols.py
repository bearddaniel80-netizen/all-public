from ..registry import (
    CatagoryType,
    register_function_call,
    SMEType,
    SourceFunc,
    FuncType
)

from aql_link.managers.package_loader import load

@register_function_call(
        name="elf_symbols",
        printable=SourceFunc(
            catagory_type=[CatagoryType.EXECUTABLE, CatagoryType.FLATFILE],
            description="Reads from file, internal functions.",
            requirements=["elftools"],
            sme_type=SMEType.LEGACY,
            func_type=FuncType.ADAPTER,
            template="SELECT * FROM elf_symbols(<file>)",
            enabled=False
        )
    )
class ElfSymbolsTableFunction:

    def execute(self, *args):
        raise NotImplementedError("coming soon")
        path = args[0]
        load("elf")
        from aql_elf.adaptor.elf_source import ELFSymbolSource

        source = ELFSymbolsSource.from_file(path)

        return source.to_dataset()