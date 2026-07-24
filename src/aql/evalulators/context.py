class EvalContext:
    def __init__(self, obj, dispatcher):
        self.obj = obj
        self.dispatcher = dispatcher

    def eval(self, node):
        return self.dispatcher.dispatch(node, self)

    