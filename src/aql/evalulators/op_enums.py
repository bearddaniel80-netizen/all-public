from enum import Enum
import operator

class BinaryOpType(str, Enum):
    NEQ = "!="
    LTE = "<="
    GTE = ">="
    EQ = "="
    LT = "<"
    GT = ">"

    def func(self):
        return {
            BinaryOpType.NEQ: operator.ne,
            BinaryOpType.LTE: operator.le,
            BinaryOpType.GTE: operator.ge,
            BinaryOpType.EQ: operator.eq,
            BinaryOpType.LT: operator.lt,
            BinaryOpType.GT: operator.gt,
        }[self]


class LogicalOpType(str, Enum):
    AND = "AND"
    OR = "OR"