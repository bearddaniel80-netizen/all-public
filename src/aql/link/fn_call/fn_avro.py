from ..registry import (
    CategoryType,
    register_function_call, 
    SourceFunc,
    FuncType
)

from aql_link.managers.package_loader import load

@register_function_call(
        name="avro",
        printable=SourceFunc(
            catagory_type=[CategoryType.DATABASE],
            description="Stores data as a dataframe.",
            requirements=["avro", "fastavro"],
            func_type=FuncType.ADAPTER,
            template="SELECT * FROM avro(<file>)",
            enabled=False
        )
    )
class AvroTableFunction:

    def execute(self, *args):
        raise NotImplementedError("coming soon")
        path = args[0]
        load("arrow")
        from aql_avro.adaptor.avro_source import AvroSource

        source = AvroSource.from_file(path)

        return source.to_dataset()