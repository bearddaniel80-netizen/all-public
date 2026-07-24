class PipelineStage:
    def __init__(self, context):
        self.context = context

    def process(self, data):
        raise NotImplementedError