from ..registry import (
    CatagoryType,
    register_function_call,
    SourceFunc,
    FuncType
)

from aql_link.managers.package_loader import load

@register_function_call(
        name="log",
        printable=SourceFunc(
            catagory_type=[CatagoryType.FLATFILE],
            description="Reads from file.",
            extra_info="aql deliminates lines into \s then =",
            enabled=True,
            func_type=FuncType.ADAPTER,
            template="SELECT * FROM log(<file>)"
        )
    )
class LogTableFunction:

    def execute(self, *args):
        path = args[0]
        load("log")
        from aql_log.adaptor.log_source import LogStdinSource

        source = LogStdinSource.from_file(path)

        return source.to_dataset()