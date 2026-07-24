from ..registry import (
    CatagoryType,
    register_function_call,
    SMEType,
    SourceFunc
)

from ...engine.package_loader import load

@register_function_call(
        name="email",
        printable=SourceFunc(
            catagory_type=[CatagoryType.FLATFILE],
            description="Reads from message headers.",
            sme_type=SMEType.SECURITY
        )
    )
class EmailTableFunction:

    def execute(self, *args):
        path = args[0]
        load("email")
        from aql_email.adaptor.email_source import EmailSource

        source = EmailSource.from_file(path)

        return source.to_dataset()