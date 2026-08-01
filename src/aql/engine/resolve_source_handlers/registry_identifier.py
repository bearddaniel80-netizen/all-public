SOURCE_REGISTRY = {}

def register_source(name):
    def decorator(cls):
        SOURCE_REGISTRY[name] = cls
        return cls
    return decorator