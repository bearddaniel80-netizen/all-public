from ..base import ASTNode
from .identifier import Field
from dataclasses import dataclass

@dataclass
class BinaryOp(ASTNode):
    left: ASTNode         # Expression
    operator: str         # '=', '<', '>'
    right: ASTNode        # Expression

    def __repr__(self):
        return f"BinaryOp( left= {self.left} operator= {self.operator} right= {self.right})"

    def to_dict(self):
        return {
            "type": "binary_op",
            "operator": self.operator,
            "left": self.left.to_dict(),
            "right": self.right.to_dict()
        }

@dataclass
class InOp(ASTNode):
    left: ASTNode          # Expression
    right: ASTNode        # Expression

    def __repr__(self):
        return f"InOp( left= {self.left} right={self.right})"

    def to_dict(self):
        return {
            "type": "in_op",
            "left": self.left.to_dict(),
            "right": self.right.to_dict()
        }

@dataclass
class RegexMatch(ASTNode):
    field: Field
    pattern: str

    def __repr__(self):
        return f"RegexMatch( field= {self.field} pattern= {self.pattern})"

    def to_dict(self):
        return {
            "type": "regex_match",
            "field": self.field.to_dict(),
            "pattern": self.pattern.to_dict()
        }


@dataclass
class NotOp(ASTNode):
    expr: ASTNode

    def __repr__(self):
        return f"NotOp( expr= {self.expr} )"

    def to_dict(self):
        return {
            "type": "not_op",
            "expr": self.expr.to_dict()
        }

@dataclass
class BetweenOp(ASTNode):
    expr: ASTNode
    lower: object
    upper: object

    def __repr__(self):
        return f"BetweenOp( expr={self.expr} lower={self.lower} upper={self.upper})"

    def to_dict(self):
        return {
            "type": "between_op",
            "expression": self.expr.to_dict(),
            "lower": self.lower,
            "upper": self.upper
        }

@dataclass
class AndOp(ASTNode):
    left: ASTNode
    right: ASTNode

    def evaluate(self, row):
        return (
            self.left.evaluate(row)
            and
            self.right.evaluate(row)
        )

    def __repr__(self):
        return f"AndOp( left={self.left} right={self.right})"

    def to_dict(self):
        return {
            "type": "and_op",
            "left": self.left.to_dict(),
            "right": self.right.to_dict()
        }

@dataclass
class OrOp(ASTNode):
    left: ASTNode
    right: ASTNode

    def evaluate(self, row):
        return (
            self.left.evaluate(row)
            or
            self.right.evaluate(row)
        )

    def __repr__(self):
        return f"OrOp( left={self.left} right={self.right})"

    def to_dict(self):
        return {
            "type": "or_op",
            "left": self.left.to_dict(),
            "right": self.right.to_dict()
        }