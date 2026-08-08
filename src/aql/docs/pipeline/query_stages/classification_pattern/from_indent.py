from .base import Pattern
from ..registry_classification import pattern
from ....model import QueryClassification
from .....language.tokens import TokenType

@pattern([
    TokenType.FROM,
    TokenType.IDENT,
])
class FromIdent(Pattern):
    def build(self, classifier: QueryClassification):
        classifier.source = self.window[1].value