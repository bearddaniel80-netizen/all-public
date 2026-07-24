import mailbox

from aql_link.core.base import StdinSource
from aql_link.core.builder import build_model, infer_schema
from aql_link.core.dataset import Dataset

# SELECT from, subject FROM mbox('archive.mbox')

class MboxSource:

    def __init__(self, rows):
        self._rows = rows

    @classmethod
    def from_file(cls, filename: str):

        rows = []

        mbox = mailbox.mbox(filename)

        for i, msg in enumerate(mbox):

            try:

                rows.append({
                    "index": i,
                    "from": msg.get("From"),
                    "to": msg.get("To"),
                    "subject": msg.get("Subject"),
                    "date": msg.get("Date"),
                    "message_id": msg.get("Message-ID"),
                    "received": msg.get_all("Received", []),
                    "spf": msg.get("Received-SPF"),
                    "dkim": msg.get("DKIM-Signature"),
                    "reply_to": msg.get("Reply-To"),
                })

            except Exception as e:

                rows.append({
                    "index": i,
                    "error": str(e),
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
            "MboxRow",
            schema
        )

    def schema(self):
        return infer_schema(self._rows[0])