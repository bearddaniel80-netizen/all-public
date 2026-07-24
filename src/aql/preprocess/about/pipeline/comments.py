from ..types import AboutType
from ..registry import register_about
from .base import AboutBase

@register_about(AboutType.COMMENT)
class Comments(AboutBase):

    def process(self, source_loader):
        result = []
        for k, v in source_loader.collector.items():
            collection = [i.to_dict() for i in v.comments]
            item = {'source': k, 'comments': collection}
            result.append(item)
        return result
