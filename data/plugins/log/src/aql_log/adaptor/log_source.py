import re
from aql_link.core.base import StdinSource
from aql_link.core.builder import build_model, infer_schema
from aql_link.core.dataset import Dataset

class LogStdinSource(StdinSource):
    def __init__(self, raw: str):
        self.raw = raw
        
    def as_rows(self):
        rows = []

        for line in self.raw.splitlines():
            # naive key=value parser
            matches = re.findall(r'(\w+)=([^\s]+)', line)
            row = {k: v for k, v in matches}

            if not row:
                row = {"message": line}

            rows.append(row)

        return rows

    @classmethod
    def from_file(cls, filename: str):
        with open(filename, "r") as f:
            data = f.read()

        return cls(data)

    @classmethod
    def from_raw(cls, raw):
        return cls(raw)

    def to_dataset(self):
        rows = self.parse()  # list[dict] or dataclass
        return Dataset(rows, self.infer_model(rows))

    def parse(self):
        return [
            {
                "line": line,
                "line_number": i
            }
            for i, line in enumerate(self.raw.splitlines(), 1)
            if line.strip()
        ]
        

    def infer_model(self, schema):
        schema = infer_schema(schema)
        return build_model("TextRow", schema)

    def schema(self):
        rows = self.as_rows()
        sample = rows[0] if rows else {}
        return infer_schema(sample)