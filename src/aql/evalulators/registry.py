from dataclasses import dataclass, field
from enum import StrEnum

class SupportType(StrEnum):
    INT = "integer"
    STR = "string"

@dataclass
class Operator:
    template: list[str] = field(
        default_factory=list
    )
    name: str = None
    support_type: list[SupportType] = field(
        default_factory=list
    )
    def to_dict(self):
        return {
            "name": self.name,
            "support_type": self.support_type,
            "template": self.template,
        }

OPERATOR_REGISTRY = {}

def register_operator(
        op: Operator() = None
    ):
    def decorator(cls):
        name = op.name
        OPERATOR_REGISTRY[name] = op
        return cls
    return decorator
    
EVAL_HANDLER_REGISTRY = []

def register_eval_handler(priority=100):
    def decorator(cls):
        EVAL_HANDLER_REGISTRY.append((priority, cls))
        return cls
    return decorator