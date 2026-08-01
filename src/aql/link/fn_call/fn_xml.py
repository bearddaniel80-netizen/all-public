from ..registry import (
    CatagoryType,
    register_function_call,
    SourceFunc,
    FuncType
)

from aql_link.managers.package_loader import load

@register_function_call(
        name="xml",
        printable=SourceFunc(
            catagory_type=[CatagoryType.FLATFILE],
            description="Reads from file.",
            enabled=True,
            func_type=FuncType.ADAPTER,
            template="SELECT * FROM xml(<file>)"
        )
    )
class XmlTableFunction:

    def execute(self, *args):
        path = args[0]
        load("xml")
        from aql_xml.adaptor.xml_source import XmlSource

        source = XmlSource.from_file(path)

        return source.to_dataset()