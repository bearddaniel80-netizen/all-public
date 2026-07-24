from .base import ASTNode
from dataclasses import dataclass


# example SELECT upper(...)
@dataclass
class FunctionCall(ASTNode):
    name: str
    arg: object
    alias: str

    def __repr__(self):
        return f"FunctionCall( name= {self.name} arg= {self.arg} alias= {self.alias})"

    def to_dict(self):
        return {
            "type": "function_call",
            "name": self.name,
            "args": self.args,
            "alias": self.alias,
        }

# example FROM json(...)
@dataclass
class TableFunctionCall(ASTNode):
    name: str
    arg: object
    alias: str

    def __repr__(self):
        return f"TableFunctionCall( name= {self.name} arg= {self.arg} alias= {self.alias})"

    def to_dict(self):
        return {
            "type": "table_function_call",
            "name": self.name,
            "arg": self.arg,
            "alias": self.alias,
        }

# example SELECT PARSE_KV(...)
@dataclass
class TransformCall(ASTNode):
    name: str
    arg: object
    alias: str

    def __repr__(self):
        return f"TransformCall( name= {self.name} arg= {self.arg} alias= {self.alias})"

    def to_dict(self):
        return {
            "type": "transform_call",
            "name": self.name,
            "arg": self.arg,
            "alias": self.alias,
        }