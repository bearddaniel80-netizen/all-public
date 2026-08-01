from ..registry import (
    CategoryType,
    register_function_call,
    SMEType,
    SourceFunc,
    FuncType
)

from aql_link.managers.package_loader import load

@register_function_call(
        name="maildir",
        printable=SourceFunc(
            catagory_type=[CategoryType.FLATFILE],
            description="Reads messages in dir.",
            sme_type=SMEType.SECURITY,
            func_type=FuncType.ADAPTER,
            template="SELECT * FROM maildir(<file>)",
            enabled=False
        )
    )
class MaildirTableFunction:

    def execute(self, *args):
        raise NotImplementedError("coming soon")
        path = args[0]
        load("maildir")
        from aql_maildir.adaptor.maildir_source import MaildirSource

        source = MaildirSource.from_dir(path)

        return source.to_dataset()