from .base import StageBase

class SourceStage(StageBase):
    def create(self, ctx):
        
        ctx.source_templates = [
            ctx.template_resolver.resolve(
                template,
                ctx.example,
            )
            for template in ctx.source["template"]
        ]

        ctx.add(ctx.source_templates)
