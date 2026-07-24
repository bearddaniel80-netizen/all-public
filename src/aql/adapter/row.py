class RowAdapter:
    @staticmethod
    def get(obj, field):
        if isinstance(obj, dict):
            return obj.get(field)
        return getattr(obj, field, None)