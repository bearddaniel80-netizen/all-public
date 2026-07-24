from ..base import PreprocessorStage
from ..models import Comments, Docs, CommentType

class CommentStripStage(PreprocessorStage):

    def process(self, ctx):
        ctx.source = self._remove_comments(ctx)

    def _remove_comments(self, ctx):
        lines: list[str] = []
        block_comment: list[str] = []
        in_block_comment: bool = False
        
        for line in ctx.source:
            x = line.strip()

            while x:
                if in_block_comment:
                    end = x.find("*/")
                    if end == -1:
                        x = ""
                        block_comment.append(line)
                    else:
                        z = " ".join(block_comment)
                        z = z.strip()
                        if "/**" in z:
                            y = Docs(source=z,_type=CommentType.BLOCK,target=None)
                            ctx.documentations.append(y)
                        else:
                            y = Comments(target=z)
                            ctx.comments.append(y)
                        block_comment = []
                        x = x[end + 2:]
                        in_block_comment = False
                else:
                    start = x.find("/*")
                    if start != -1:
                        end = x.find("*/", start + 2)
                        if end != -1:
                            # Remove inline block comment
                            y = Docs(source=x,_type=CommentType.INLINE,target=None)
                            x = x[:start] + x[end + 2:]
                            ctx.documentations.append(y)
                        else:
                            # Start of multi-line block comment
                            block_comment.append(x)
                            x = x[:start]
                            in_block_comment = True
                    else:
                        break

            x = x.strip()

            if not x:
                continue

            # Remove inline single-line comments
            comment_positions = [
                pos for pos in (
                    x.find("#"),
                    x.find("--"),
                    x.find("//"),
                )
                if pos != -1
            ]

            if comment_positions:
                y = x
                x = x[:min(comment_positions)].rstrip()
                c = Comments(
                    target=y
                )
                ctx.comments.append(c)

            if x:
                lines.append(x)
        return lines