from ..base import PreprocessorStage
from ..models import Using

class UsingStage(PreprocessorStage):

    def process(self, ctx):
        usings = list(filter(self._starts_with, ctx.source))
        if not usings:
            return
        self._parcer(ctx, usings)
        ctx.source = [ item for item in ctx.source if item not in usings]

    def _starts_with(self, value):
        return value.startswith("USING")

    def _parcer(self, ctx, usings):

        for using in usings:
            using = using.replace("USING", "").replace("\"", "")
            cmd = using.strip()
            x = Using(
                target=cmd.strip()
            )
            ctx.usings.append(x)