from ..base import PreprocessorStage, ReadLinePipeline
from ..context import PreprocessorContext
from ..models import Comments, Docs, CommentType, Macro, Using
from ...lexer.lexer import Lexer
from ...context.analysis import AnalysisContext

class UsingPipeline(ReadLinePipeline):
    def can_handle(self, line):
        line = line.strip()
        return line.startswith("USING")

    def process(self, line: str, ctx: PreprocessorContext):
        line = line.strip()
        analysis = AnalysisContext(line)
        Lexer(analysis).tokenize()
        target = analysis.artifacts["tokens"][1].value
        x = Using(
            target=target
        )
        ctx.usings.append(x)

class MacroPipeline(ReadLinePipeline):
    def can_handle(self, line):
        line = line.strip()
        return line.startswith("DECLARE")

    def process(self, line: str, ctx: PreprocessorContext):
        line = line.strip()
        line = line.replace("DECLARE", "").replace("AS", "=")
        line = line.strip()
        cmd = line.split("=")
        x = Macro(
            name=cmd[0].strip(),
            target=cmd[1].strip()
        )

        ctx.macros.append(x)

class CommentsBlockPipeline(ReadLinePipeline):
    def __init__(self,ctx):
        self.ctx = ctx

    def can_handle(self, line):
        x = line.strip()
        return x.find("/*") > -1 and not self.ctx.in_doc_block

    def process(self, line: str, ctx: PreprocessorContext):
        line = line.strip()
        ctx.block_comment.append(line)
        ctx.in_comment_block = True

class CommentsInlinePipeline(ReadLinePipeline):
    def can_handle(self, line):
        x = line.strip()
        self.comment_positions = [
            pos for pos in (
                x.find("#"),
                x.find("--"),
                x.find("//"),
            )
            if pos != -1
        ]
        return self.comment_positions

    def process(self, line: str, ctx: PreprocessorContext):
        line = line.strip()
        ctx.comments.append(Comments(target=line, _type=CommentType.INLINE))

class DocBlockPipeline(ReadLinePipeline):
    def __init__(self,ctx):
        self.ctx = ctx

    def can_handle(self, line):
        x = line.strip()
        return x.find("/**") > -1 and not self.ctx.in_comment_block

    def process(self, line: str, ctx: PreprocessorContext):
        line = line.strip()
        ctx.block_comment.append(line)
        ctx.in_doc_block = True

class DocInlinePipeline(ReadLinePipeline):
    def can_handle(self, line):
        x = line.strip()
        return x.find("///") > -1

    def process(self, line: str, ctx: PreprocessorContext):
        line = line.strip()
        ctx.documentations.append(Docs(source=None, target=line, _type=CommentType.INLINE))

class BlockBodyPipeline(ReadLinePipeline):
    def __init__(self,ctx):
        self.ctx = ctx

    def can_handle(self, line):
        return self.ctx.in_comment_block or self.ctx.in_doc_block

    def process(self, line: str, ctx: PreprocessorContext):
        line = line.strip()
        ctx.block_comment.append(line)

class BlockClosingPipeline(ReadLinePipeline):
    def can_handle(self, line):
        x = line.strip()
        return x.find("*/") > -1

    def process(self, line: str, ctx: PreprocessorContext):
        line = line.strip()
        ctx.block_comment.append(line)
        comment = " ".join(ctx.block_comment)
        _type = CommentType.BLOCK
        if ctx.in_comment_block == True:
            ctx.in_comment_block = False
            ctx.comments.append(Comments(target=comment, _type=_type))
        else:
            ctx.in_doc_block = False
            ctx.documentations.append(Docs(source=None, target=comment, _type=_type))
        ctx.block_comment = []

class ReadFactory(PreprocessorStage):
    def process(self, ctx):
        pipeline = [
            UsingPipeline(),
            MacroPipeline(),
            DocBlockPipeline(ctx),
            DocInlinePipeline(),
            CommentsBlockPipeline(ctx),
            CommentsInlinePipeline(),
            BlockBodyPipeline(ctx),
            BlockClosingPipeline()
        ]
        is_handled: bool = False
        keep = []
        for line in ctx.source:
            for stage in pipeline:
                if stage.can_handle(line):
                    stage.process(line, ctx)
                    if isinstance(stage, (CommentsInlinePipeline, DocInlinePipeline)) and not ctx.in_comment_block and not ctx.in_doc_block:
                        line = line.strip()
                        x = line
                        comment_positions = [
                            pos for pos in (
                                x.find("#"),
                                x.find("--"),
                                x.find("//"),
                            )
                            if pos != -1
                        ]
                        if comment_positions and min(comment_positions) > 0:
                            x = line[:comment_positions[0]]
                            keep.append(x)
                    is_handled = True

            if is_handled == False:
                keep.append(line)
            is_handled = False

        ctx.source = keep


                    
