from ..types import AboutType
from ..registry import register_about
from .base import AboutBase

@register_about(AboutType.INFO)
class Info(AboutBase):

    def process(self, source_loader):
        result = []
        for k, v in source_loader.collector.items():
            comments = len(v.comments)
            docs = len(v.documentations)
            macros = len(v.macros)
            usings = len(v.usings)
            item = {
                'source': k, 
                'comment_ct': comments,
                'documentations_ct': docs,
                'macros_ct': macros,
                'usings_ct': usings,
            }
            result.append(item)
        return result
