from ..registry import (
    CatagoryType,
    register_function_call, 
    SourceFunc
)

from ...engine.package_loader import load

@register_function_call(
        name="parquet",
        printable=SourceFunc(
            catagory_type=[CatagoryType.DATABASE],
            description="Stores data as a dataframe.",
            requirements=["pyarrow"]
        )
    )
class ParquetTableFunction:

    def execute(self, *args):
        path = args[0]
        load("parquet")
        from aql_parquet.adaptor.parquet_source import ParquetSource

        source = ParquetSource.from_file(path)

        return source.to_dataset()