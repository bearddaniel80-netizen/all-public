from ..registry import (
    CatagoryType,
    register_function_call,
    SMEType,
    SourceFunc
)

from ...engine.package_loader import load

@register_function_call(
        name="elf",
        printable=SourceFunc(
            catagory_type=[CatagoryType.EXECUTABLE, CatagoryType.FLATFILE],
            description="Reads from file.",
            requirements=["elftools"],
            sme_type=SMEType.LEGACY
        )
    )
class ElfTableFunction:

    def execute(self, *args):
        path = args[0]
        load("elf")
        from aql_elf.adaptor.elf_source import ELFSource

        source = ELFSource.from_file(path)

        return source.to_dataset()