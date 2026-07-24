ABOUT_REGISTRY = {}
def register_about(instance):
    def decorator(cls):
        ABOUT_REGISTRY[instance] = cls
        return cls
    return decorator