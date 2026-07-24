from ..registry import (
    CatagoryType,
    register_function_call,
    SourceFunc
)
from ...engine.package_loader import load

@register_function_call(
        name="log",
        printable=SourceFunc(
            catagory_type=[CatagoryType.FLATFILE],
            description="Reads from file.",
            extra_info="aql deliminates lines into \s then ="
        )
    )
class LogTableFunction:

    def execute(self, *args):
        path = args[0]
        load("log")
        from aql_log.adaptor.log_source import LogStdinSource

        source = LogStdinSource.from_file(path)

        return source.to_dataset()