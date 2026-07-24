from ..registry import (
    CatagoryType,
    register_function_call, 
    SourceFunc
)

from ...engine.package_loader import load

@register_function_call(
        name="arrow",
        printable=SourceFunc(
            catagory_type=[CatagoryType.DATABASE],
            description="Stores data as a dataframe.",
            requirements=["pyarrow"]
        )
    )
class ArrowTableFunction:

    def execute(self, *args):
        path = args[0]
        load("arrow")
        from aql_arrow.adaptor.arrow_source import ArrowSource

        source = ArrowSource.from_file(path)

        return source.to_dataset()