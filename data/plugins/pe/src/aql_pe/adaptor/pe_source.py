import pefile
from aql_link.core.base import StdinSource
from aql_link.core.builder import build_model, infer_schema
from aql_link.core.dataset import Dataset

# SELECT *
# FROM pe('malware.exe')
# WHERE entropy > 7

class PESource:

    def __init__(self, rows):
        self._rows = rows

    @classmethod
    def from_file(cls, filename):

        pe = pefile.PE(filename)

        rows = []

        for section in pe.sections:
            rows.append({
                "name": section.Name.decode().strip(),
                "virtual_size": section.Misc_VirtualSize,
                "entropy": section.get_entropy(),
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
        return build_model("ParquetRow", schema)

    def schema(self):
        return infer_schema(self._rows[0])