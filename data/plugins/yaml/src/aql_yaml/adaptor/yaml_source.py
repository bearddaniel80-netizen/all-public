import yaml
from aql_link.core.base import StdinSource
from aql_link.core.builder import build_model, infer_schema
from aql_link.core.dataset import Dataset

class YamlSource(StdinSource):
    def __init__(self, raw: str):
        self.raw = raw
        self._data = yaml.safe_load(raw)

    def as_rows(self):
        if isinstance(self._data, list):
            return self._data
        return [self._data]

    @classmethod
    def from_file(cls, filename: str):
        with open(filename, "r") as f:
            data = f.read()

        return cls(data)
        
    @classmethod
    def from_raw(cls, raw):
        return cls(raw)


    def _flatten(self, d, parent="", sep="_"):
        out = {}
        for k, v in d.items():
            key = f"{parent}{sep}{k}" if parent else k
            if isinstance(v, dict):
                out.update(self._flatten(v, key, sep))
            else:
                out[key] = v
        return out

    def parse(self) -> list[dict]:

        if(isinstance(self.raw, str)):
            data = yaml.safe_load(self.raw)
        else:
            data = self.raw

        if isinstance(data, list):
            rows = data
        else:
            rows = [data]

        return [self._flatten(r) for r in rows]

    def to_dataset(self):
        rows = self.parse()  # list[dict] or dataclass
        return Dataset(rows, self.infer_model(rows))
    
    def infer_model(self, schema):
        schema = infer_schema(schema)
        return build_model("YamlRow", schema)

    def schema(self):
        rows = self.as_rows()
        sample = rows[0] if rows else {}
        return infer_schema(sample)