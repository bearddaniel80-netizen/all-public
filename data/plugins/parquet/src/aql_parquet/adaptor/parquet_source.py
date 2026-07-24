import pyarrow.parquet as pq

from aql_link.core.base import StdinSource
from aql_link.core.builder import build_model, infer_schema
from aql_link.core.dataset import Dataset

class ParquetSource:

    def __init__(self, rows):
        self._rows = rows

    @classmethod
    def from_file(cls, filename: str):

        table = pq.read_table(filename)

        rows = table.to_pylist()

        return cls(rows)

    def as_rows(self):
        return self._rows

    def to_dataset(self):
        return Dataset(
            self._rows,
            self.infer_model(self._rows[0])
        )

    def infer_model(self, sample):
        schema = infer_schema(sample)
        return build_model("ParquetRow", schema)

    def schema(self):
        return infer_schema(self._rows[0])