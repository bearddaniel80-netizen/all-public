from .template_stage import TemplateStage
from .strategies.scalar_strategy import ScalarStrategy

class ScalarStage(TemplateStage):

    def __init__(self):
        super().__init__(ScalarStrategy())

