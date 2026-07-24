import os
from email import policy
from email.parser import BytesParser

from aql_link.core.base import StdinSource
from aql_link.core.builder import build_model, infer_schema
from aql_link.core.dataset import Dataset

# SELECT from, subject FROM maildir('/var/mail/user')

class MaildirSource:

    def __init__(self, rows):
        self._rows = rows

    @classmethod
    def from_dir(cls, path: str):

        rows = []

        # Standard Maildir folders
        folders = ["cur", "new"]

        for folder in folders:

            folder_path = os.path.join(path, folder)

            if not os.path.exists(folder_path):
                continue

            for filename in os.listdir(folder_path):

                full_path = os.path.join(folder_path, filename)

                if not os.path.isfile(full_path):
                    continue

                try:

                    with open(full_path, "rb") as f:

                        msg = BytesParser(
                            policy=policy.default
                        ).parse(f)

                    rows.append({
                        "file": filename,
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
                        "file": filename,
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
            "MaildirRow",
            schema
        )

    def schema(self):
        return infer_schema(self._rows[0])