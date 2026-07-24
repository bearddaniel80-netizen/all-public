from ..query_exec_context import ExecutionContext

class Stage:
    def execute(self, context: ExecutionContext):
        raise NotImplementedError