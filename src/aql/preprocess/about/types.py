from enum import StrEnum

class CommentType(StrEnum):
    BLOCK = "block"
    INLINE = "inline"

class AboutType(StrEnum):
    COMMENT = "comments"
    DOC = "docs"
    FLOW = "flow"
    INFO = "info"
    MACRO = "macros"
    SOURCE = "sources"
    USING = "usings"
