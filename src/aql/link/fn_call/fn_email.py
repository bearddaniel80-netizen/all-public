from ..registry import (
    CategoryType,
    register_function_call,
    SMEType,
    SourceFunc,
    FuncType
)

from aql_link.managers.package_loader import load

@register_function_call(
        name="email",
        printable=SourceFunc(
            category_type=[CategoryType.FLATFILE],
            description="Reads from message headers.",
            sme_type=SMEType.SECURITY,
            func_type=FuncType.ADAPTER,
            enabled=False
        )
    )
class EmailTableFunction:

    def execute(self, *args):
        raise NotImplementedError("coming soon")
        path = args[0]
        load("email")
        from aql_email.adaptor.email_source import EmailSource

        source = EmailSource.from_file(path)

        return source.to_dataset()