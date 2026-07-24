from ....ast.base import ASTNode

class Pattern(ASTNode):
    def to_dict(self):
        raise NotImplementedError