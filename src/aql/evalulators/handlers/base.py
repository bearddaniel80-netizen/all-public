from ..context import EvalContext

class BaseHandler:
    def __init__(self, next_handler=None):
        self.next = next_handler

    def handle(self, node, ctx: EvalContext):
        if self.can_handle(node):
            return self.process(node, ctx)

        if self.next:
            return self.next.handle(node, ctx)

        raise ValueError(f"No handler for node: {node}")

    def can_handle(self, node):
        raise NotImplementedError

    def process(self, node, ctx: EvalContext):
        raise NotImplementedError