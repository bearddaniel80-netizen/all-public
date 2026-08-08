from .template_stage import TemplateStage
from .strategies.operator_strategy import OperatorStrategy

class OperatorStage(TemplateStage):

    def __init__(self):
        super().__init__(OperatorStrategy())