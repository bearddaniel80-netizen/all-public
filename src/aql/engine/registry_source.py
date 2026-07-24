SOURCE_REGISTRY = {}
def register_source(instance):
    def decorator(cls):
        SOURCE_REGISTRY[instance] = cls
        return cls
    return decorator