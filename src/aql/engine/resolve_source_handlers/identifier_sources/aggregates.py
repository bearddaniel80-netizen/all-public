from ....schema.describe import DescribeStage
from ....schema.show import ShowStage
from ....schema.runner import Pipeline
from ..registry_identifier import register_source
from .base import IdentifierSource

@register_source(name="aggregates")
class AggregateSource(IdentifierSource):
    def describe(self, engine_context, inspector):
        from ....link.registry import PRINTABLE, SqlFunc
        from ....link import aggregates
        data = PRINTABLE
        pipeline = Pipeline([
            DescribeStage(engine_context, inspector, SqlFunc)
        ])
        return pipeline.run(data)
    
    def query(self):
        from ....link import aggregates
        from ....link.registry import PRINTABLE, FuncType
        return [ item for item in PRINTABLE if item["func_type"] == FuncType.AGGREGATE]

    def show(self):
        from ....link import aggregates
        from ....link.registry import PRINTABLE, FuncType
        data = [ item for item in PRINTABLE if item["func_type"] == FuncType.AGGREGATE]
        pipeline = Pipeline([
            ShowStage(data),
        ])

        return pipeline.run(data)