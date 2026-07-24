from .registry import EVAL_HANDLER_REGISTRY
from . import handlers

class Dispatcher:
    def __init__(self):
        self.handler_chain = self._build_chain()

    def _build_chain(self):
        # sort by priority
        sorted_handlers = sorted(EVAL_HANDLER_REGISTRY, key=lambda x: x[0])

        instances = [cls() for _, cls in sorted_handlers]

        for i in range(len(instances) - 1):
            instances[i].next = instances[i + 1]

        return instances[0] if instances else None

    def dispatch(self, node, ctx):
        return self.handler_chain.handle(node, ctx)
