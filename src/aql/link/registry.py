from dataclasses import dataclass, field
from enum import Enum

class CategoryType(str, Enum):
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
    STR = "str"
    COMPLEX = "complex"
    TEXT = "text"

class FuncType(str, Enum):
    ADAPTER = "adapter"
    AGGREGATE = "aggregate"
    SCALAR = "scalar"
    TRANSFORM = "transform"

@dataclass
class BaseFunc:
    name: str = None,
    description: str = None,
    template: list[str] = None,
    extra_info: str = None,
    requirements: list = None

    def to_dict(self):
        pass

@dataclass
class SqlFunc(BaseFunc):
    input_type: list[FieldType] = None,
    return_type: FieldType = None,
    func_type: FuncType = None,
    needs_groupby: bool = False

    def to_dict(self):
        return {
            "name": self.name,
            "description": self.description,
            "template": self.template,
            "extra_info": self.extra_info,
            "requirements": [ item for item in self.requirements] if self.requirements else None,
            "func_type": self.func_type,
            "input_type": [ item for item in self.input_type],
            "return_type": self.return_type,
            "needs_groupby_clause": str(self.needs_groupby),
        }

@dataclass
class SourceFunc(BaseFunc):
    category_type: list[CategoryType] = None,
    func_type: FuncType = FuncType.ADAPTER,
    sme_type: SMEType = SMEType.GENERAL,
    enabled: bool = False

    def to_dict(self):
        return {
            "name": self.name,
            "description": self.description,
            "template": [
                f"SELECT * FROM {self.name}('<file>')",
                f"SELECT <field:int> FROM {self.name}('<file>')",
                f"SELECT <field:str> FROM {self.name}('<file>')"
            ],
            "extra_info": self.extra_info,
            "requirements": [ item for item in self.requirements] if self.requirements else None,
            "category_type": [ item for item in self.category_type],
            "func_type": self.func_type,
            "sme_type": self.sme_type,
            "enabled": str(self.enabled)
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
