import tarfile

from aql_link.core.base import StdinSource
from aql_link.core.builder import build_model, infer_schema
from aql_link.core.dataset import Dataset

# aegis query "SELECT * FROM tar('data.tar')"
# aegis query "SELECT * FROM tar('data.tgz')"
# aegis query "SELECT * FROM tar('data.tar.bz2')"
# aegis query "SELECT * FROM tar('data.tar.gz')"
# aegis query "SELECT * FROM tar('data.tar.xz')"

class TarSource:

    def __init__(self, rows):
        self._rows = rows

    @classmethod
    def from_file(cls, filename: str):

        rows = []

        with tarfile.open(filename, "r:*") as tar:

            for member in tar.getmembers():

                rows.append({
                    "name": member.name,
                    "size": member.size,
                    "mode": member.mode,
                    "mtime": member.mtime,
                    "type": member.type,
                    "uid": member.uid,
                    "gid": member.gid,
                    "uname": member.uname,
                    "gname": member.gname,
                    "is_file": member.isfile(),
                    "is_dir": member.isdir(),
                    "is_symlink": member.issym(),
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
            "TarRow",
            schema
        )

    def schema(self):
        return infer_schema(self._rows[0])