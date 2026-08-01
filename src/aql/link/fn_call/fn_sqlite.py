from ..registry import (
    CategoryType,
    register_function_call,
    SourceFunc,
    FuncType
)

from aql_link.managers.package_loader import load

@register_function_call(
        name="sqlite",
        printable=SourceFunc(
            catagory_type=[CategoryType.FLATFILE, CategoryType.DATABASE],
            description="Runs a query on the file.",
            func_type=FuncType.ADAPTER,
            template="SELECT * FROM sqlite(<file>)",
            enabled=False
        )
    )
class SqliteTableFunction:

    def execute(self, *args):
        raise NotImplementedError("coming soon")
        db = args[0].value
        query = args[1].value
        load("sqlite")
        from aql_sqlite.adaptor.sqlite_source import SQLiteSource

        source = SQLiteSource.from_query(
            db,
            query
        )

        return source.to_dataset()