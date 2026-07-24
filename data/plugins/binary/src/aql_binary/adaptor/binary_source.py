
from aql_link.core.base import StdinSource
from aql_link.core.builder import build_model, infer_schema
from aql_link.core.dataset import Dataset

# SELECT * FROM binary('program.bin') WHERE byte = 0x7F
# SELECT * FROM binary('sample.exe') WHERE grep(bytes, '4D5A')
# | Source     | Decoder         |
# | ---------- | --------------- |
# | binary()   | raw bytes       |
# | elf()      | ELF parser      |
# | pe()       | PE parser       |
# | pcap()     | packet parser   |
# | protobuf() | protobuf schema |
# | avro()     | avro decoder    |

class BinarySource:

    def __init__(self, rows):
        self._rows = rows


    @classmethod
    def from_file(cls, filename):

        with open(filename, "rb") as f:
            return cls(f.read())

    def as_rows(self):

        return [
            {
                "offset": i,
                "byte": b
            }
            for i, b in enumerate(self._data)
        ]

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