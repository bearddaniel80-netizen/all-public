from .base import BaseHandler
from ..registry import register_handler
from ...language.ast.statements.show import Show
from ...language.ast.statements.describe import Describe
from ...adapter.source.base import StdinSource
from ...link.registry import FUNCTION_CALL_REGISTRY, PRINTABLE
from ...language.ast.function_call import TableFunctionCall
from ...language.ast.expressions.literals import Literal

from ...adapter.row import RowAdapter
from ...schema.runner import Pipeline
from ...schema.normalizer import NormalizeStage
from ...schema.project import ProjectStage
from ...schema.show import ShowStage
from ...schema.describe import DescribeStage
from ...schema.inspector import SchemaInspector
from ...context.analysis import AnalysisContext

@register_handler
class ShowHandler(BaseHandler):
    def __init__(self, engine_context):
        self.data_sources = engine_context.data_sources
        self.source_resolver = engine_context.source_resolver
        self.engine_context = engine_context
        self.inspector = SchemaInspector()

    def can_handle(self, ast):
        return isinstance(ast, (Show, Describe))

    def handle(self, analysis_ctx: AnalysisContext):
        ast = analysis_ctx.artifacts["ast"]

        if(isinstance(ast.target, TableFunctionCall)):
            return self.handle_fn_call(ast)

        if ast.target == "aggregates":
            return self.show_aggregates()
        elif ast.target == "functions":
            return self.show_fn_call()
        elif ast.target == "scalars":
            return self.show_scalars()
        elif ast.target == "sources":
            return self.show_sources()

        if ast.target not in self.data_sources:
            analysis_ctx.artifacts["diagnostic"].fatal("EHS01", f"Unknown target: {ast.target}", "Fix source")
            return

        data, model_cls = self.source_resolver.resolve(ast.target, self.engine_context, analysis_ctx, True)

        # 🔥 DESCRIBE path
        if isinstance(ast, Describe):
            if isinstance(model_cls, StdinSource):
                return model_cls.schema()
            pipeline = Pipeline([
                DescribeStage(self.engine_context, self.inspector, model_cls)
            ])
            return pipeline.run(data)

        # 🔥 SHOW path (rows)
        pipeline = Pipeline([
            NormalizeStage(data),
            ProjectStage(self.engine_context, RowAdapter.get(ast, "fields")),
            ShowStage(data),
        ])

        return pipeline.run(data)

    def show_aggregates(self):
        from ...link import aggregates
        return PRINTABLE

    def show_fn_call(self):
        from ...link import fn_call
        return PRINTABLE

    def show_scalars(self):
        from ...link import scalars
        return PRINTABLE

    def show_sources(self):
        return list(self.data_sources.keys())

    def handle_fn_call(self, ast):
        from ...link import fn_call
        
        fn_name = ast.target.name

        fn = FUNCTION_CALL_REGISTRY.get(fn_name)

        raw = ast.target.arg[0]

        if isinstance(raw, Literal):
            raw = raw.value

        source = fn.execute(raw)

        if(isinstance(ast, Show)):
            return source.as_rows()
        
        pipeline = Pipeline([
            DescribeStage(self.engine_context, self.inspector, source.schema())
        ])
        return pipeline.run(source)