CLAUSE_REGISTRY = []

def register_clause(order: int):

    def decorator(cls):

        cls.order = order

        CLAUSE_REGISTRY.append(cls())

        CLAUSE_REGISTRY.sort(
            key=lambda c: c.order
        )

        return cls

    return decorator