from .context import ParserContext
from .strategies.common_table import CommonTableStrategy
from .strategies.select import SelectStrategy
from .strategies.show import ShowStrategy
from .strategies.describe import DescribeStrategy
from ..context.analysis import AnalysisContext
from ..language.ast.statements.query import Query

class Parser:
    def __init__(self, analysis_ctx: AnalysisContext):
        self.query = Query()
        self.ctx = ParserContext(analysis_ctx)
        self.analysis_ctx = analysis_ctx
        self.strategies = [
            CommonTableStrategy(self.query),
            SelectStrategy(self.query),
            ShowStrategy(),
            DescribeStrategy(),
        ]

    def parse(self):
        if not self.ctx.peek():
            self.analysis_ctx.artifacts["diagnostic"].fatal("PP01", f"Empty query", "Fix query")
            return

        while self.ctx.peek():

            handled = False

            for strategy in self.strategies:

                if strategy.can_handle(self.ctx):
                    value = strategy.parse(
                            self.ctx,
                            self.analysis_ctx,
                        )
                    
                    if isinstance(strategy, (DescribeStrategy, ShowStrategy)):
                        self.analysis_ctx.artifacts["ast"] = value
                        return
                    
                    handled = True
                    break

            if not handled:
                self.analysis_ctx.artifacts["diagnostic"].warning(
                    "PP02",
                    f"Unknown statement: {self.ctx.peek()}",
                    "Fix statement",
                )
                break
            
            self.analysis_ctx.artifacts["ast"] = self.query