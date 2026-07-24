from dataclasses import make_dataclass
from typing import Any

class StdinSource:
    def parse(self, raw: str) -> list[dict]:
        raise NotImplementedError

    def infer_model(self, schema: dict[str, type]):
        raise NotImplementedError

    def to_dataset(self, raw: str):
        raise NotImplementedError