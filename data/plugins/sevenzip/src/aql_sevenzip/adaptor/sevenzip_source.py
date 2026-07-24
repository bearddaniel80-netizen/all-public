import py7zr

from aql_link.core.base import StdinSource
from aql_link.core.builder import build_model, infer_schema
from aql_link.core.dataset import Dataset


class SevenZipSource:

    def __init__(self, rows):
        self._rows = rows

    @classmethod
    def from_file(cls, filename: str):

        rows = []

        with py7zr.SevenZipFile(
            filename,
            mode="r"
        ) as archive:

            for info in archive.list():

                rows.append({
                    "name": info.filename,
                    "compressed": info.compressed,
                    "uncompressed": info.uncompressed,
                    "is_directory": info.is_directory,
                    "creationtime": info.creationtime,
                    "crc32": info.crc32,
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
            "SevenZipRow",
            schema
        )

    def schema(self):
        return infer_schema(self._rows[0])