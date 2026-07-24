class OperatorHandler:

    def can_handle(self, tok, ctx):
        raise NotImplementedError

    def parse(self, parser, ctx, left):
        raise NotImplementedError