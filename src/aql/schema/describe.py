from dataclasses import is_dataclass, fields
from .base import PipelineStage

class DescribeStage(PipelineStage):
    def __init__(self, context, inspector, model_cls):
        super().__init__(context)
        self.inspector = inspector
        self.model_cls = model_cls

    def process(self, data):
        # data is ignored for describe
        return self.inspector.describe(self.model_cls)