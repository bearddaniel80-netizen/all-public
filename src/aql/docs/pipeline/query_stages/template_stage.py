from .base import StageBase

class TemplateStage(StageBase):

    def __init__(self, instance):
        self.instance = instance

    def create(self, ctx):
        queries = []
        counters = {}

        for item in self.instance.items(ctx):

            for template in item["template"]:

                resolved = self.instance.resolve(
                    ctx,
                    template,
                    item,
                    counters
                )

                for source_template in ctx.source_templates:

                    query = self.instance.combine(
                        ctx,
                        source_template,
                        resolved,
                        item,
                    )

                    if isinstance(query, str):
                        queries.append(query)
                    else:
                        queries.extend(query)

        ctx.add(queries)
