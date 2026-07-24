from ..base import ASTNode
from dataclasses import dataclass

@dataclass
class GroupBy(ASTNode):
    fields: list

    def __repr__(self):
        return f"GroupBy( fields = {', '.join(self.fields)} )"

    def to_dict(self):
        return {
            "type": "GroupBy",
            "fields": ', '.join(self.fields)
        }