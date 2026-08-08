class ScalarStrategy:

    def items(self, ctx):
        return ctx.scalars

    def resolve(self, ctx, template, item, counters):
        return ctx.template_resolver.resolve(
            template=template,
            example=ctx.example,
            counters=counters
        )

    def combine(
        self,
        ctx,
        source_template,
        resolved,
        item,
    ):
        return ctx.combine_templates.function(
            source_template,
            resolved,
            item,
            ctx.example,
        )