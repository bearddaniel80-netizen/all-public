from .base import Pattern
from ..registry_classification import pattern
from ....model import QueryClassification
from .....language.tokens import TokenType

@pattern([
    TokenType.SELECT,
    TokenType.IDENT,
])
class SelectField(Pattern):
    def build(self, classifier: QueryClassification):
        classifier.fields.append(self.window[1].value)