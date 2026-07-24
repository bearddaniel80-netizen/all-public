from ..registry import (
    CatagoryType,
    register_function_call,
    SourceFunc
)
from ...engine.package_loader import load

@register_function_call(
        name="yaml",
        printable=SourceFunc(
            catagory_type=[CatagoryType.FLATFILE],
            description="Reads from file.",
            requirements=["pyyaml"]
        )
    )
class YamlTableFunction:

    def execute(self, *args):
        path = args[0]
        load("yaml")
        from aql_yaml.adaptor.yaml_source import YamlSource

        source = YamlSource.from_file(path)

        return source.to_dataset()