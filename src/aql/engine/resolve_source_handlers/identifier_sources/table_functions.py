from ....schema.describe import DescribeStage
from ....schema.show import ShowStage
from ....schema.runner import Pipeline
from ..registry_identifier import register_source
from .base import IdentifierSource

@register_source(name="table_functions")
class FunctionSource(IdentifierSource):
    def describe(self, engine_context, inspector):
        from ....link.registry import PRINTABLE, SourceFunc
        from ....link import fn_call
        data = PRINTABLE
        pipeline = Pipeline([
            DescribeStage(engine_context, inspector, SourceFunc)
        ])
        return pipeline.run(data)
    
    def query(self):
        from ....link import fn_call
        from ....link.registry import PRINTABLE, FuncType
        return [ item for item in PRINTABLE if item["func_type"] == FuncType.ADAPTER]

    def show(self):
        from ....link import fn_call
        from ....link.registry import PRINTABLE, FuncType
        data = [ item for item in PRINTABLE if item["func_type"] == FuncType.ADAPTER]
        pipeline = Pipeline([
            ShowStage(data),
        ])

        return pipeline.run(data)