from ....evalulators.registry import SupportType
from ....engine.resolve_source_handlers.identifier_sources.operators import OperatorSource

class TemplateResolver:
    def __init__(self):
        self.operator_map: dict[str, list] = {
            "<op:int>": [],
            "<op:str>": [],
        }
        lst = OperatorSource().query()
        self._create_op_map(lst)

    def _create_op_map(self, lst):
        for item in lst:
            name = item["name"]
            
            if name.isalpha():
                continue

            for support in item["support_type"]:
                if "str" in support:
                    self.operator_map["<op:str>"].append(name)
                
                if "int" in support:
                    self.operator_map["<op:int>"].append(name)

    def resolve(self, template, example, counters=None):
        replacements = {
            "<file>": example.file,
            "<raw>": "<field:str>", # f"'{example.raw}'",

            "<field:str>":
                example.fields["<field:str>"],

            "<field:int>":
                example.fields["<field:int>"],
        }

        if counters is not None:
            template = self._resolve_operators(template, counters)

        template = self._resolve_values(
            template,
            example,
        )

        for token, value in replacements.items():
            template = template.replace(token, value)

        return template

        
    def _resolve_values(self, template, example):

        counters = {}

        import re
        
        PLACEHOLDER = re.compile(
            r"<value:(?P<type>\w+)>"
        )

        def replace_value(match):
            value_type = match.group("type")
            placeholder = match.group(0)

            index = counters.get(value_type, 0)

            value = example.values[index % len(example.values)]

            counters[value_type] = index + 1
            
            return str(value[placeholder])

        return PLACEHOLDER.sub(
            replace_value,
            template,
        )

    def _resolve_operators(self, template, counters):

        import re

        PLACEHOLDER = re.compile(
            r"<op:(?P<type>\w+)>"
        )

        def replace_operator(match):
            operator_type = match.group("type")

            placeholder = match.group(0)

            values = self.operator_map[placeholder]

            index = counters.get(operator_type, 0)

            value = values[index % len(values)]

            counters[operator_type] = index + 1

            return value

        return PLACEHOLDER.sub(
            replace_operator,
            template,
        )
