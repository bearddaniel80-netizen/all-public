from .identifier import Field
from ..base import ASTNode
from dataclasses import dataclass

@dataclass
class OrderBy:
    field: Field
    descending: bool = False

    def __repr__(self):
        return (
            f"OrderBy( field= {self.field} "
            f"desc= {self.descending})"
        )

    def to_dict(self):
        return {
            "type": "order_by",
            "field": self.field,
            "descending": self.descending,
        }