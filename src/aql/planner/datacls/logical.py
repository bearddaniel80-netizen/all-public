class LogicalPlan:
    def __init__(self, source, projections, filters):
        self.source = source              # "stdin", "file.json", "cluster"
        self.projections = projections    # ["name", "age"]
        self.filters = filters            # [Expr, Expr]