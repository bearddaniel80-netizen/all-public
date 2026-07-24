READER_REGISTRY = []
def register_readers(cls):
    READER_REGISTRY.append(cls)
    return cls