from .base import PipelineStage

class ProjectStage(PipelineStage):
    def __init__(self, context, fields=None):
        super().__init__(context)
        self.fields = fields

    def process(self, data):
        if not self.fields:
            return data

        return [
            {k: row.get(k) for k in self.fields if k in row}
            for row in data
        ]