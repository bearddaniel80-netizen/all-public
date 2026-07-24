from ..schema.inspector import SchemaInspector
from ..adapter.row import RowAdapter

class Projector:
    def __init__(self):
        self.inspector = SchemaInspector()

    def project(self, fields, row):

        if not fields:
            return self.inspector.serialize(row)

        first = fields[0]

        is_star = (
            first == "*" or
            getattr(first, "value", None) == "*" or
            getattr(first, "name", None) == "*"
        )

        if is_star:
            return self.inspector.serialize(row)

        result = {}

        for field in fields:
            raw = RowAdapter.get(row, field.name)
            result[field.name] = self.inspector.serialize(raw)

        return result