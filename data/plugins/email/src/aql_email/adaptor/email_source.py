from email import policy
from email.parser import BytesParser

from aql_link.core.base import StdinSource
from aql_link.core.builder import build_model, infer_schema
from aql_link.core.dataset import Dataset

# SELECT from, subject FROM email('message.eml')

class EmailSource:

    def __init__(self, rows):
        self._rows = rows

    @classmethod
    def from_file(cls, filename):

        with open(filename, "rb") as f:

            msg = BytesParser(
                policy=policy.default
            ).parse(f)

        row = {
            "from": msg.get("From"),
            "to": msg.get("To"),
            "subject": msg.get("Subject"),
            "date": msg.get("Date"),
            "message_id": msg.get("Message-ID"),
            "received": msg.get_all("Received", []),
            "spf": msg.get("Received-SPF"),
            "dkim": msg.get("DKIM-Signature"),
        }

        return cls([row])

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
            "EmailRow",
            schema
        )

    def schema(self):
        return infer_schema(self._rows[0])