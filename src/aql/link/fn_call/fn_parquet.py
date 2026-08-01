from ..registry import (
    CatagoryType,
    register_function_call, 
    SourceFunc,
    FuncType
)

from aql_link.managers.package_loader import load

@register_function_call(
        name="parquet",
        printable=SourceFunc(
            catagory_type=[CatagoryType.DATABASE],
            description="Stores data as a dataframe.",
            requirements=["pyarrow"],
            func_type=FuncType.ADAPTER,
            template="SELECT * FROM parquet(<file>)",
            enabled=False
        )
    )
class ParquetTableFunction:

    def execute(self, *args):
        raise NotImplementedError("coming soon")
        path = args[0]
        load("parquet")
        from aql_parquet.adaptor.parquet_source import ParquetSource

        source = ParquetSource.from_file(path)

        return source.to_dataset()