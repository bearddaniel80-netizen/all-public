from ..registry import (
    CatagoryType,
    register_function_call,
    SMEType,
    SourceFunc
)

from ...engine.package_loader import load

@register_function_call(
        name="maildir",
        printable=SourceFunc(
            catagory_type=[CatagoryType.FLATFILE],
            description="Reads messages in dir.",
            sme_type=SMEType.SECURITY
        )
    )
class MaildirTableFunction:

    def execute(self, *args):
        path = args[0]
        load("maildir")
        from aql_maildir.adaptor.maildir_source import MaildirSource

        source = MaildirSource.from_dir(path)

        return source.to_dataset()