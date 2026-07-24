import sqlite3

from aql_link.core.base import StdinSource
from aql_link.core.builder import build_model, infer_schema
from aql_link.core.dataset import Dataset


class SQLiteSource:

    def __init__(self, rows):
        self._rows = rows

    @classmethod
    def from_query(cls, filename: str, query: str):

        conn = sqlite3.connect(filename)

        conn.row_factory = sqlite3.Row

        cursor = conn.execute(query)

        rows = [
            dict(row)
            for row in cursor.fetchall()
        ]

        conn.close()

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

        return build_model(
            "SQLiteRow",
            schema
        )

    def schema(self):
        return infer_schema(self._rows[0])