from ..base import PreprocessorStage
from dataclasses import dataclass, field
from ..models import Macro

class MacroStage(PreprocessorStage):

    def process(self, ctx):
        macros = list(filter(self._starts_with, ctx.source))
        if not macros:
            return
        self._parcer(ctx, macros)
        ctx.source = [ item for item in ctx.source if item not in macros]
        self._replace(ctx)

    def _starts_with(self, value):
        return value.startswith("DECLARE")

    def _parcer(self, ctx, macros):

        for macro in macros:
            macro = macro.replace("DECLARE", "").replace("AS", "=")
            macro = macro.strip()
            cmd = macro.split("=")
            x = Macro(
                name=cmd[0].strip(),
                target=cmd[1].strip()
            )

            ctx.macros.append(x)

    def _replace(self, ctx):
        for i in range(0, len(ctx.source)):
            for macro in ctx.macros:
                name = macro.name
                name_lst = name.split()
                if name in ctx.source[i]:
                    ctx.source[i] = ctx.source[i].replace(name, macro.target)
                elif self._sliding_window(name_lst, ctx.source[i]):
                    ctx.source[i] = ctx.source[i].replace(name, macro.target)

    def _sliding_window(self, targets, source):
        return any(
            source[i:i + len(targets)] == targets
            for i in range(len(source) - len(targets) + 1)
        )
