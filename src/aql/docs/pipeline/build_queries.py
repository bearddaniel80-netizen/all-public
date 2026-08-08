from .base import DocBase
from ..model import Examples
from .query_stages.context import StageContext
from .query_stages.source_stage import SourceStage
from .query_stages.operator_stage import OperatorStage
from .query_stages.aggregate_stage import AggregateStage
from .query_stages.scalar_stage import ScalarStage
from .query_stages.filter_stages.dedup_stage import DedupStage
from .query_stages.filter_stages.validate_stage import ValidateStage
from .query_stages.cte_stage import CteStage
from .query_stages.classifier_stage import ClassifierStage

class BuildQueries(DocBase):

    def _build_source_queries(self, source, example, ctx):

        stages = [
            SourceStage(),
            OperatorStage(),
            AggregateStage(),
            ScalarStage(),
            DedupStage(),
            ValidateStage(),
            CteStage(),
            ClassifierStage()
        ]
        
        stage_context = StageContext(
            example=example,
            source=source,
            operators=ctx.operators,
            aggregates=ctx.aggregates,
            scalars=ctx.scalars
        )

        for stage in stages:
            stage.create(stage_context)

        return stage_context.queries_classification # stage_context.queries

    def _find_example(self, name, ctx):
        
        if "_" in name:
            name = name.split("_")[0]
        
        for item in ctx.examples:
            if name in item["name"]:
                return item["data"]

    def build(self, ctx):

        queries = {}

        for name, source in ctx.sources.items():

            example = self._find_example(name, ctx)

            source_queries = self._build_source_queries(
                source,
                example,
                ctx,
            )

            queries[name] = source_queries

        ctx.queries_classification = queries