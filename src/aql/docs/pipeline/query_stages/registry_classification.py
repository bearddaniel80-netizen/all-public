
CLASSIICATION_REGISTRY = []

def pattern(tokens):
    def decorator(cls):
        CLASSIICATION_REGISTRY.append(cls)
        cls.pattern = tokens
        return cls
    return decorator