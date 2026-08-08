from .base import DocBase
from ..model import Examples

class BuildExamples(DocBase):
    def build(self, ctx):
        fields = {
            "<field:str>": "name",
            "<field:int>": "age"
        }
        examples = [
            {
                "name": "csv",
                "data": Examples(
                    name="csv",
                    file="data.csv",
                    raw="",
                    fields=fields,
                    values=[
                        {
                            "<value:str>": "Jim",
                            "<value:int>": 26
                        },
                        {
                            "<value:str>": "Bob",
                            "<value:int>": 46
                        },
                        {
                            "<value:str>": "Jim",
                            "<value:int>": 26
                        },
                        {
                            "<value:str>": "Bob",
                            "<value:int>": 46
                        },
                    ]
                )
            },
            {
                "name": "json",
                "data": Examples(
                    name="json",
                    file="data.json",
                    raw="",
                    fields=fields,
                    values=[
                        {
                            "<value:str>": "Jim",
                            "<value:int>": 26
                        },
                        {
                            "<value:str>": "Bob",
                            "<value:int>": 46
                        },
                        {
                            "<value:str>": "Jim",
                            "<value:int>": 26
                        },
                        {
                            "<value:str>": "Bob",
                            "<value:int>": 46
                        },
                    ]
                )
            },
            {
                "name": "log",
                "data": Examples(
                    name="log",
                    file="data.log",
                    raw="",
                    fields=fields,
                    values=[
                        {
                            "<value:str>": "Jim",
                            "<value:int>": 26
                        },
                        {
                            "<value:str>": "Bob",
                            "<value:int>": 46
                        },
                        {
                            "<value:str>": "Jim",
                            "<value:int>": 26
                        },
                        {
                            "<value:str>": "Bob",
                            "<value:int>": 46
                        },
                    ]
                )
            },
            {
                "name": "xml",
                "data":  Examples(
                    name="xml",
                    file="data.xml",
                    raw="",
                    fields=fields,
                    values=[
                        {
                            "<value:str>": "alice",
                            "<value:int>": 30
                        },
                        {
                            "<value:str>": "bob",
                            "<value:int>": 25
                        },
                        {
                            "<value:str>": "alice",
                            "<value:int>": 30
                        },
                        {
                            "<value:str>": "bob",
                            "<value:int>": 25
                        },
                    ]
                )
            },
            {
                "name": "yaml",
                "data":  Examples(
                    name="yaml",
                    file="data.yml",
                    raw="",
                    fields=fields,
                    values=[
                        {
                            "<value:str>": "alice",
                            "<value:int>": 30
                        },
                        {
                            "<value:str>": "bob",
                            "<value:int>": 25
                        },
                        {
                            "<value:str>": "alice",
                            "<value:int>": 30
                        },
                        {
                            "<value:str>": "bob",
                            "<value:int>": 25
                        },
                    ]
                )
            }
        ]

        ctx.examples = examples