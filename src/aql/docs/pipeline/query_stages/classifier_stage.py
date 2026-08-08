from .base import StageBase
from ....context.analysis import AnalysisContext
from ....context.diagnostic import DiagnosticCollection
from ....evalulators.operator_list import build_dict
from ....lexer.lexer import Lexer
from ....link.registry import FUNCTION_CALL_REGISTRY
from ....link import aggregates, scalars
from ....language.tokens import TokenType
from ...model import QueryClassification
from .registry_classification import CLASSIICATION_REGISTRY
from . import classification_pattern
from enum import Enum

class ClauseType(str, Enum):
    AND = "AND"
    GROUP = "GROUP BY"
    HAVING = "HAVING"
    NOT = "NOT"
    ORDER = "ORDER BY"
    OR = "OR"

class ClassifierStage(StageBase):
    def create(self, ctx):
        classifier_collection = []
        analysis = AnalysisContext("")
        analysis.artifacts["diagnostic"] = DiagnosticCollection()

        for q in ctx.queries:
            analysis.text = q
            analysis.artifacts["tokens"] = []
            Lexer(analysis).tokenize()
            tokens = analysis.artifacts["tokens"]

            classifier: QueryClassification = QueryClassification(q)

            for fn in CLASSIICATION_REGISTRY:
                fn_cls = fn()
                if fn_cls.has_match(tokens):
                    fn_cls.build(classifier)

            for clause in ClauseType:
                if clause.value in q:
                    classifier.clauses.append(clause.value)

            for key in build_dict().keys():
                if key in q:
                    classifier.operation.append(key)

            for key in FUNCTION_CALL_REGISTRY.keys():
                if key.upper() in q:
                    classifier.feature = key
                    break
                
            classifier_collection.append(classifier)
            # print("Queryclassifier: ", classifier.to_dict())

        ctx.queries_classification = classifier_collection