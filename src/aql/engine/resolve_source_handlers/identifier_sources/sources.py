from ....schema.describe import DescribeStage
from ....schema.show import ShowStage
from ....schema.runner import Pipeline
from ..registry_identifier import register_source
from .base import IdentifierSource
from dataclasses import dataclass, field

@dataclass
class StdinSources:
    template: list[str] = field(
        default_factory=list
    )
    description: str = None
    name: str = None

    def to_dict(self):
        return {
            "name": self.name,
            "description": self.description,
            "template": self.template,
        }

@register_source(name="stdin_sources")
class Sources(IdentifierSource):
    def __init__(self):
        templates = [
            "cat <file> | DESCRIBE stdin",
            "echo <raw> | DESCRIBE stdin",
            "cat <file> | SHOW stdin",
            "echo <raw> | SHOW stdin",
            "cat <file> | SELECT *",
            "cat <file> | SELECT * FROM stdin",
            "echo <raw> | SELECT *",
            "echo <raw> | SELECT * FROM stdin",
            "cat <file> | SELECT <field:str>",
            "cat <file> | SELECT <field:str> FROM stdin",
            "echo <raw> | SELECT <field:str>",
            "echo <raw> | SELECT <field:str> FROM stdin",
            "cat <file> | SELECT <field:int>",
            "cat <file> | SELECT <field:int> FROM stdin",
            "echo <raw> | SELECT <field:int>",
            "echo <raw> | SELECT <field:int> FROM stdin"        
        ]
        self.data = []
        self.data.append(
            StdinSources(
                name="csv_stdin",
                description="Reads raw or file based data",
                template= templates
            )
        )
        self.data.append(
            StdinSources(
                name="json_stdin",
                description="Reads raw or file based data",
                template= templates
            )
        )
        self.data.append(
            StdinSources(
                name="log_stdin",
                description="Reads file based data",
                template=[
                    "cat <file> | SELECT *",
                    "cat <file> | SELECT * FROM stdin"
                ]
            )
        )
        self.data.append(
            StdinSources(
                name="xml_stdin",
                description="Reads raw or file based data",
                template=templates
            )
        )
        self.data.append(
            StdinSources(
                name="yaml_stdin",
                description="Reads raw or file based data",
                template=templates
            )
        )

    def describe(self, engine_context, inspector):
        data = [ item.to_dict() for item in self.data ]
        pipeline = Pipeline([
            DescribeStage(engine_context, inspector, StdinSources)
        ])
        return pipeline.run(data)
    
    def query(self):
        return [ item.to_dict() for item in self.data ]

    def show(self):
        data = [ item.to_dict() for item in self.data ]
        pipeline = Pipeline([
            ShowStage(data),
        ])
        return pipeline.run(data)