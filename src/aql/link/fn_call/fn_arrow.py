from ..registry import (
    CatagoryType,
    register_function_call, 
    SourceFunc,
    FuncType
)

from aql_link.managers.package_loader import load

@register_function_call(
        name="arrow",
        printable=SourceFunc(
            catagory_type=[CatagoryType.DATABASE],
            description="Stores data as a dataframe.",
            requirements=["pyarrow"],
            func_type=FuncType.ADAPTER,
            template="SELECT * FROM arrow(<file>)",
            enabled=False
        )
    )
class ArrowTableFunction:

    def execute(self, *args):
        raise NotImplementedError("coming soon")
        path = args[0]
        load("arrow")
        from aql_arrow.adaptor.arrow_source import ArrowSource

        source = ArrowSource.from_file(path)

        return source.to_dataset()