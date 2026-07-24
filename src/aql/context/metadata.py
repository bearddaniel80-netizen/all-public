from dataclasses import dataclass, field

@dataclass
class Metadata:

    values: dict = field(default_factory=dict)

    def get(self, key, default=None):
        return self.values.get(key, default)

    def set(self, key, value):
        self.values[key] = value