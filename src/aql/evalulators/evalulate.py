from .dispatcher import Dispatcher
from .context import EvalContext

class Evaluator:
    def __init__(self):
        self.dispatcher = Dispatcher()

    def evaluate(self, node, obj):
        ctx = EvalContext(obj, self.dispatcher)
        return ctx.eval(node)