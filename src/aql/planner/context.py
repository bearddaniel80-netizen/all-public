class PlanningContext:
    def __init__(self, has_stdin=False, ddl=None):
        self.has_stdin = has_stdin
        self.ddl = ddl