from .build_template import BuildTemplate
from .strategies.negation_strategy import NegationStrategy

class BuildNegation(BuildTemplate):

    def __init__(self):
        super().__init__(NegationStrategy())

