from ..registry import (
    CatagoryType,
    register_function_call, 
    SourceFunc
)
from ...engine.package_loader import load

@register_function_call(
        name="csv",
        printable=SourceFunc(
            catagory_type=[CatagoryType.FLATFILE],
            description="Reads from file."
        )
    )
class CsvTableFunction:

    def execute(self, *args):
        path = args[0]

        load("csv")

        from aql_csv.adaptor.csv_source import CsvSource

        source = CsvSource.from_file(path)

        return source.to_dataset()