from ...planner.datacls.logical import LogicalPlan
from .base import BaseHandler
from ..registry import register_handler

@register_handler
class PlannerHandler(BaseHandler):
    def __init__(self, engine_context):
        self.engine_context = engine_context
        self.data_sources = engine_context.data_sources
        self.evaluator = engine_context.evaluator
        self.projector = engine_context.projector

    def can_handle(self, plan):
        return isinstance(plan, LogicalPlan)

    def handle(self, plan):
        data = self.engine_context.source_resolver.resolve(plan.source)
        # return project(data, plan.projections)