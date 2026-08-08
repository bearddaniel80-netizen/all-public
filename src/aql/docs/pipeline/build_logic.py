from .build_template import BuildTemplate
from .strategies.logic_strategy import LogicStrategy

class BuildLogic(BuildTemplate):

    def __init__(self):
        super().__init__(LogicStrategy())