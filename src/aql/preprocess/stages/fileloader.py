from ..base import PreprocessorStage

class FileLoadingStage(PreprocessorStage):

    def process(self, ctx):
        ctx.source = ctx.filename.read_text(encoding="utf-8").splitlines()