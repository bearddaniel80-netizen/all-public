from dataclasses import is_dataclass, fields
from enum import Enum
from .base import PipelineStage

class NormalizeStage(PipelineStage):
    def process(self, data):
        return [self.normalize_row(row) for row in data]

    def normalize_row(self, row):
        if is_dataclass(row):
            out = {}
            for f in fields(row):
                if f.name.startswith("_"):
                    continue

                value = getattr(row, f.name)
                out[f.name] = self.normalize_value(value)
            return out

        if isinstance(row, dict):
            return {
                k: self.normalize_value(v)
                for k, v in row.items()
                if not k.startswith("_")
            }

        return row

    def normalize_value(self, v):
        if isinstance(v, Enum):
            return v.value
        return v