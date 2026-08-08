from .base import Pattern
from ..registry_classification import pattern
from ....model import QueryClassification
from .....language.tokens import TokenType

@pattern([
    TokenType.SELECT,
    TokenType.STAR,
])
class SelectStar(Pattern):
    def build(self, classifier: QueryClassification):
        classifier.fields.append(TokenType.STAR)