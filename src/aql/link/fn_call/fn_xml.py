from ..registry import (
    CatagoryType,
    register_function_call,
    SourceFunc
)
from ...engine.package_loader import load

@register_function_call(
        name="xml",
        printable=SourceFunc(
            catagory_type=[CatagoryType.FLATFILE],
            description="Reads from file."
        )
    )
class XmlTableFunction:

    def execute(self, *args):
        path = args[0]
        load("xml")
        from aql_xml.adaptor.xml_source import XmlSource

        source = XmlSource.from_file(path)

        return source.to_dataset()