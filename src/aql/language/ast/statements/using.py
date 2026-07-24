from ..base import ASTNode
from dataclasses import dataclass

@dataclass
class UsingExpression(ASTNode):
    filename: ASTNode

    def __repr__(self):
        return f"UsingExpression( filename= {self.filename})"

    def to_dict(self):
        return {
            "type": "using",
            "filename": self.filename.to_dict()
        }