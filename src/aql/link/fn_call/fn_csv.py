from ..registry import (
    CategoryType,
    register_function_call, 
    SourceFunc,
    FuncType
)
from aql_link.managers.package_loader import load

@register_function_call(
        name="csv",
        printable=SourceFunc(
            catagory_type=[CategoryType.FLATFILE],
            description="Reads from file.",
            enabled=True,
            func_type=FuncType.ADAPTER,
            template="SELECT * FROM csv(<file>)"
        )
    )
class CsvTableFunction:

    def execute(self, *args):
        path = args[0]

        load("csv")

        from aql_csv.adaptor.csv_source import CsvSource

        source = CsvSource.from_file(path)

        return source.to_dataset()