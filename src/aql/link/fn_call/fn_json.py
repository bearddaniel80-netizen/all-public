from ..registry import (
    CatagoryType,
    register_function_call,
    SourceFunc,
    FuncType
)

from aql_link.managers.package_loader import load

@register_function_call(
        name="json",
        printable=SourceFunc(
            catagory_type=[CatagoryType.FLATFILE],
            description="Reads from file.",
            enabled=True,
            func_type=FuncType.ADAPTER,
            template="SELECT * FROM json(<file>)"
        )
    )
class JsonTableFunction:

    def execute(self, *args):
        path = args[0]

        load("json")
        from aql_json.adaptor.json_source import JsonFileSource

        source = JsonFileSource.from_file(path)

        return source.to_dataset()