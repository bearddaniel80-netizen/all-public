from ..types import AboutType
from ..registry import register_about
from .base import AboutBase

@register_about(AboutType.SOURCE)
class Source(AboutBase):

    def process(self, source_loader):
        result = []
        for k, v in source_loader.collector.items():
            collection = v.source
            item = {'source': k, 'contents': " ".join(collection)}
            result.append(item)
        return result
