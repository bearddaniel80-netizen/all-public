from dataclasses import fields, is_dataclass
from typing import get_origin, get_args, Union
from enum import Enum

class SchemaInspector:
    def format_type(self, t):
        origin = get_origin(t)

        # Handle Optional[T] (Union[T, None])
        if origin is Union:
            args = get_args(t)
            non_none = [a for a in args if a is not type(None)]
            if len(non_none) == 1:
                return f"{self.format_type(non_none[0])}?"
            return "union"

        # Handle list[T]
        if origin is list:
            args = get_args(t)
            inner = self.format_type(args[0]) if args else "Any"
            return f"list[{inner}]"

        # Handle Enum
        if isinstance(t, type) and issubclass(t, Enum):
            values = [e.value for e in t]
            return f"enum[{ '|'.join(map(str, values)) }]"

        # Fallback
        if hasattr(t, "__name__"):
            return t.__name__

        return str(t)

    def describe(self, model_cls):
        if not is_dataclass(model_cls):
            raise TypeError(f"{model_cls} is not a dataclass")

        result = []

        for f in fields(model_cls):
            if f.name.startswith("_"):
                continue

            result.append({
                "name": f.name,
                "type": self.format_type(f.type),
                "nullable": self._is_nullable(f.type),
            })

        return result

    def _is_nullable(self, t):
        origin = get_origin(t)
        if origin is Union:
            return type(None) in get_args(t)
        return False


    def serialize(self, value):

        if value is None:
            return None

        if isinstance(value, Enum):
            return value.value

        if is_dataclass(value):
            result = {}

            for f in fields(value):
                if f.name.startswith("_"):
                    continue

                result[f.name] = self.serialize(
                    getattr(value, f.name)
                )

            return result

        if isinstance(value, list):
            return [self.serialize(v) for v in value]

        if isinstance(value, dict):
            return {
                k: self.serialize(v)
                for k, v in value.items()
            }

        return value