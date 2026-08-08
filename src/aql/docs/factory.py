from .context import DocumentationContext
from .pipeline.build_examples import BuildExamples
from .pipeline.build_aggregates import BuildAggregates
from .pipeline.build_scalars import BuildScalars
from .pipeline.build_operators import BuildOperator
from .pipeline.build_queries import BuildQueries
from .pipeline.build_sources import BuildSources
from .pipeline.build_negation import BuildNegation
from .pipeline.build_logic import BuildLogic

class DocumentationFactory:
    def create(self):
        ctx = DocumentationContext()
        pipeline = [
            BuildSources(),
            BuildScalars(),
            BuildAggregates(),
            BuildOperator(),
            BuildNegation(),
            BuildLogic(),
            BuildExamples(),
            BuildQueries()
        ]
        for item in pipeline:
            item.build(ctx)

        return ctx