from ..registry import (
    CategoryType,
    register_function_call,
    SourceFunc,
    FuncType
)

from aql_link.managers.package_loader import load

@register_function_call(
        name="json",
        printable=SourceFunc(
            category_type=[CategoryType.FLATFILE],
            description="Reads from file.",
            enabled=True,
            func_type=FuncType.ADAPTER,
        )
    )
class JsonTableFunction:

    def execute(self, *args):
        path = args[0]

        load("json")
        from aql_json.adaptor.json_source import JsonFileSource

        source = JsonFileSource.from_file(path)

        return source.to_dataset()