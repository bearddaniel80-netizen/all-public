from ..registry import (
    CatagoryType,
    register_function_call,
    SourceFunc
)

from ...engine.package_loader import load

@register_function_call(
        name="sqlite",
        printable=SourceFunc(
            catagory_type=[CatagoryType.FLATFILE, CatagoryType.DATABASE],
            description="Runs a query on the file."
        )
    )
class SqliteTableFunction:

    def execute(self, *args):
        db = args[0].value
        query = args[1].value
        load("sqlite")
        from aql_sqlite.adaptor.sqlite_source import SQLiteSource

        source = SQLiteSource.from_query(
            db,
            query
        )

        return source.to_dataset()