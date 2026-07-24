from .base import PipelineStage

class ShowStage(PipelineStage):
    def process(self, data):
        return data  # CLI can render later