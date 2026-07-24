import zipfile

from aql_link.core.base import StdinSource
from aql_link.core.builder import build_model, infer_schema
from aql_link.core.dataset import Dataset

# SELECT * FROM zip('backup.zip')

class ZipSource:

    def __init__(self, rows):
        self._rows = rows

    @classmethod
    def from_file(cls, filename):

        rows = []

        with zipfile.ZipFile(filename, "r") as z:

            for info in z.infolist():

                rows.append({
                    "name": info.filename,
                    "size": info.file_size,
                    "compressed_size": info.compress_size,
                    "modified": info.date_time,
                })

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
            "ZipRow",
            schema
        )

    def schema(self):
        return infer_schema(self._rows[0])