from ..parser.parser import Parser
from ..language.ast.identifier import Identifier
from ..lexer.lexer import Lexer
from ..adapter.source.factory import StdinSourceFactory
from ..planner.planner import Planner
from ..planner.context import PlanningContext
from .exe_source import SourceResolver
import sys
from ..context.analysis import AnalysisContext
from ..context.diagnostic import DiagnosticCollection

class EngineContext:
    def __init__(self, data_sources, evaluator, projector, registry, inspector):
        self.data_sources = data_sources
        self.evaluator = evaluator
        self.projector = projector
        self.registry = registry
        self.inspector = inspector
        self.source_resolver = SourceResolver(data_sources)

class QueryEngine:
    def __init__(self, execution_engine):
        self.executor = execution_engine
        self._add_adapters()

    def run(self, query: str):
        self.analysis = AnalysisContext(query)
        self.analysis.artifacts["diagnostic"] = DiagnosticCollection()
        self.analysis.artifacts["ast"] = None
        self.analysis.artifacts["rows"] = None

        # print("Query: ", query)

        self._lex()

        # print("Tokens: ", self.analysis.artifacts["tokens"])

        self._parse()

        # print("AST: " , self.analysis.artifacts["ast"])

        self._execute()
        
#        plan = self._planner(ast, None)
#        result = self._execute(plan)
        return self.analysis.artifacts["rows"]

    # ---- adding adapters ----
    def _add_adapters(self):
        if not hasattr(self.executor, "data_sources"):
            self.executor.data_sources = {}

        self.executor.data_sources["stdin"] = StdinSourceFactory

    # ---- pipeline stages ----

    def _lex(self):
        Lexer(self.analysis).tokenize()

    def _parse(self):
       Parser(self.analysis).parse()

    def _planner(self, ast, ddl_input):
        context = PlanningContext(
            has_stdin=not sys.stdin.isatty(),
            ddl=ddl_input
        )

        return Planner(context).plan(ast)

    def _execute(self):
        self.executor.execute(self.analysis)