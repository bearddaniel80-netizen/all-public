
class DocComment:
    comment: str = ""

class ASTNode:
    doc: DocComment
    
    def to_dict(self):
        raise NotImplementedError