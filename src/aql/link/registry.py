from dataclasses import dataclass, field
from enum import Enum

class CatagoryType(str, Enum):
    ARCHIVE = "archive"
    DATABASE = "database"
    EXECUTABLE = "executable"
    FLATFILE = "flatfile"
    NETWORK = "network"
    STORAGE = "storage"
    STREAM = "stream"

class SMEType(str, Enum):
    GENERAL = "general"
    LEGACY = "legacy"
    SECURITY = "security"

class FieldType(str, Enum):
    ANY = "any"
    ATTRIBUTE = "attribute"
    BOOL = "bool"
    FLOAT = "float"
    INT = "int"
    NUMBER = "int, float, or complex"
    TEXT = "str"

class FuncType(str, Enum):
    ADAPTER = "adapter"
    AGGREGATE = "aggregate"
    SCALAR = "scalar"
    TRANSFORM = "transform"

@dataclass
class BaseFunc:
    name: str = None,
    description: str = None,
    example: str = None,
    extra_info: str = None,
    requirements: list = None

    def to_dict(self):
        pass

@dataclass
class SqlFunc(BaseFunc):
    input_type: list[FieldType] = None,
    return_type: FieldType = None,
    func_type: FuncType = None

    def to_dict(self):
        return {
            "name": self.name,
            "description": self.description,
            "example": self.example,
            "extra_info": self.extra_info,
            "requirements": [ item for item in self.requirements] if self.requirements else None,
            "func_type": self.func_type,
            "input_type": [ item for item in self.input_type],
            "return_type": self.return_type
        }

@dataclass
class SourceFunc(BaseFunc):
    catagory_type: list[CatagoryType] = None,
    func_type: FuncType = FuncType.ADAPTER,
    sme_type: SMEType = SMEType.GENERAL

    def to_dict(self):
        return {
            "name": self.name,
            "description": self.description,
            "example": self.example,
            "extra_info": self.extra_info,
            "requirements": [ item for item in self.requirements] if self.requirements else None,
            "catagory_type": [ item for item in self.catagory_type],
            "func_type": self.func_type,
            "sme_type": self.sme_type
        }

FUNCTION_CALL_REGISTRY = {}
PRINTABLE = []

def register_function_call(
        name: str,
        printable: BaseFunc() = None
    ):
    def decorator(cls):
        instance = cls()
        FUNCTION_CALL_REGISTRY[name] = instance
        if printable:
            printable.name = name
            instance.requirements = printable.requirements
            PRINTABLE.append(printable.to_dict())
        else:
            PRINTABLE.append(BaseFunc(name=name).to_dict())
        return cls
    return decorator
