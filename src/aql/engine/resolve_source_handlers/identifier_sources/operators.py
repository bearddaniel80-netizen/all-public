from ....schema.describe import DescribeStage
from ....schema.show import ShowStage
from ....schema.runner import Pipeline
from ..registry_identifier import register_source
from .base import IdentifierSource

@register_source(name="operators")
class OperatorSource(IdentifierSource):
    def describe(self, engine_context, inspector):
        from ....evalulators.registry import Operator
        from ....evalulators.operator_list import build_dict
        data = [ v.to_dict() for k, v in build_dict().items() ]
        pipeline = Pipeline([
            DescribeStage(engine_context, inspector, Operator)
        ])
        return pipeline.run(data)
    
    def query(self):
        from ....evalulators.operator_list import build_dict
        data = [ v.to_dict() for k, v in build_dict().items() ]
        return data

    def show(self):
        from ....evalulators.operator_list import build_dict
        data = [ v.to_dict() for k, v in build_dict().items() ]
        pipeline = Pipeline([
            ShowStage(data),
        ])

        return pipeline.run(data)