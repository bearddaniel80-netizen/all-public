from .context import PreprocessorContext
from .stages.fileloader import FileLoadingStage
from .stages.using import UsingStage
from .stages.macro import MacroStage
from .stages.comment_striper import CommentStripStage
from .stages.read_factory import ReadFactory

from pathlib import Path

class Preprocessor:

    def __init__(self, source_loader):
        self.stages = [
            FileLoadingStage(),
            ReadFactory(),
#            UsingStage(),
#            MacroStage(),            
#            CommentStripStage(),
        ]
        self.source_loader = source_loader

    def process(self, path):

        if Path(path).exists() == False:
            raise Exception(f"{path.name} not found.")

        if path.name in self.source_loader.collector.keys():
            return ctx

        ctx = PreprocessorContext(
            filename=path,
            source=path.read_text(encoding="utf-8")
        )

        for stage in self.stages:
            stage.process(ctx)

        self.source_loader.collector[path.name] = ctx

        for using in ctx.usings:
            child = self.process(Path.cwd() / using.target)
            ctx.source = child.source + ctx.source

        return ctx