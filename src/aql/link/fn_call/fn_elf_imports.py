from ..registry import (
    CatagoryType,
    register_function_call,
    SMEType,
    SourceFunc
)

from ...engine.package_loader import load

@register_function_call(
        name="elf_imports",
        printable=SourceFunc(
            catagory_type=[CatagoryType.EXECUTABLE, CatagoryType.FLATFILE],
            description="Reads from elf file all dependencies.",
            requirements=["elftools"],
            sme_type=SMEType.LEGACY
        )
    )
class ElfImportsTableFunction:

    def execute(self, *args):
        path = args[0]
        load("elf")
        from aql_elf.adaptor.elf_source import ELFImportsSource

        source = ELFImportsSource.from_file(path)

        return source.to_dataset()