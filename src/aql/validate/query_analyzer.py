from ..language.ast.function_call import FunctionCall
from ..link import aggregates
from ..link import scalars
from ..link.registry import FUNCTION_CALL_REGISTRY

class QueryAnalyzer:
    @classmethod
    def has_group_by(cls):
        pass
    @classmethod
    def has_having(cls):
        pass
    @classmethod
    def aggregate_fields(cls):
        pass
    @classmethod
    def scalar_fields(cls):
        pass
    @classmethod
    def projected_fields(cls):
        pass
    @classmethod
    def group_fields(cls):
        pass
    @classmethod
    def aliases(cls):
        pass
    @classmethod
    def referenced_identifiers(cls):
        pass
    @classmethod
    def aggregate_functions(cls):
        pass
    @classmethod
    def scalar_functions(cls):
        pass
    @classmethod
    def table_functions(cls):
        pass
    @classmethod
    def has_star(cls):
        pass
    @classmethod
    def validate_projection(cls):
        pass
    
    @classmethod
    def contains_aggregate(cls, expr):

        if expr is None:
            return False

        if isinstance(expr, FunctionCall):

            fn_cls = FUNCTION_CALL_REGISTRY.get(expr.name)

            if (
                fn_cls and
                getattr(fn_cls, "kind", None) == "aggregate"
            ):
                return True

            return any(
                cls.contains_aggregate(arg)
                for arg in expr.args
            )

        for attr in ("left", "right", "expr", "args"):
            value = getattr(expr, attr, None)

            if isinstance(value, list):
                if any(cls.contains_aggregate(v) for v in value):
                    return True

            elif value is not None:
                if cls.contains_aggregate(value):
                    return True

        return False

    @classmethod
    def has_aggregate(cls, query):

        return any(
            cls.is_aggregate(field)
            for field in query.select
        )

    @classmethod
    def is_aggregate(cls, expr):

        if not isinstance(expr, FunctionCall):
            return False

        fn_cls = FUNCTION_CALL_REGISTRY.get(expr.name)

        if fn_cls is None:
            return False

        return fn_cls.kind == "aggregate"