from .base import DocBase

class BuildTemplate(DocBase):

    def __init__(self, instance):
        self.instance = instance

    def build(self, ctx):
        for lst in self._items(ctx):
            self.instance.create_query(lst)

    def _items(self, ctx):
        return [
            ctx.operators,
            ctx.aggregates,
            ctx.scalars
        ]