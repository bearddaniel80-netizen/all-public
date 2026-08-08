from .template_stage import TemplateStage
from .strategies.aggregate_strategy import AggregateStrategy

class AggregateStage(TemplateStage):

    def __init__(self):
        super().__init__(AggregateStrategy())

