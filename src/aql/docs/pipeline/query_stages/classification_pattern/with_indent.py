from .base import Pattern
from ..registry_classification import pattern
from ....model import QueryClassification
from .....language.tokens import TokenType

@pattern([
    TokenType.WITH,
    TokenType.IDENT,
    TokenType.AS
])
class WithIndent(Pattern):
    def build(self, classifier: QueryClassification):
        classifier.is_cte = True
        classifier.fields.append(self.window[1].value)