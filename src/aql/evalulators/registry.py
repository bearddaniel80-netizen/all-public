EVAL_HANDLER_REGISTRY = []

def register_eval_handler(priority=100):
    def decorator(cls):
        EVAL_HANDLER_REGISTRY.append((priority, cls))
        return cls
    return decorator