from ..types import AboutType
from ..registry import register_about
from .base import AboutBase

@register_about(AboutType.DOC)
class Documentations(AboutBase):

    def process(self, source_loader):
        result = []
        for k, v in source_loader.collector.items():
            collection = [i.to_dict() for i in v.documentations]
            item = {'source': k, 'documentations': collection}
            result.append(item)
        return result
