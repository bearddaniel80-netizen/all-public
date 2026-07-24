from ..types import AboutType
from ..registry import register_about
from .base import AboutBase

@register_about(AboutType.USING)
class Usings(AboutBase):

    def process(self, source_loader):
        result = []
        for k, v in source_loader.collector.items():
            collection = [i.to_dict() for i in v.usings]
            item = {'source': k, 'usings': collection}
            result.append(item)
        return result
