class Filter:
    def __init__(self):
        self.source = []

    def from_source(self, source: []):
        self.source = source
        return self

    def largest(self):

        scores = [self._score(q) for q in self.source]
        largest = max(scores)

        self.source = [
            q
            for q, score in zip(self.source, scores)
            if score == largest
        ]

        return self


    def _score(self, query) -> int:
        return (
            len(query["operation"])
            + len(query["clauses"])
        )

    def where(self, field: str, value: str):
        self.source = [ q for q in self.source if value in q[field]]
        return self

    def print_source(self):
        print([q["query"] for q in self.source])
        print("Filtered: ", len(self.source))