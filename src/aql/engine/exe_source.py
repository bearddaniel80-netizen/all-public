import sys
from aql_link.core.dataset import Dataset
from .executor import ExecutionEngine
from ..link.registry import FUNCTION_CALL_REGISTRY
from ..link import fn_call
from ..language.ast.function_call import TableFunctionCall
from ..language.ast.identifier import Identifier
from ..language.ast.statements.query import CommonTableExpression
from ..language.ast.expressions.literals import Literal

from .registry_source import SOURCE_REGISTRY
from . import resolve_source_handlers

class SourceResolver:
    def __init__(self, data_sources):
        self.data_sources = data_sources

    def resolve(self, ast_node, engine_context, analysis_ctx, include_schema: bool = False):
        # if(isinstance(ast_node, str)):
        #     return self.resolve_identifier(ast_node, engine_context, analysis_ctx, include_schema)
        # elif(isinstance(ast_node, Identifier)):
        #     return self.resolve_identifier(ast_node.name, engine_context, analysis_ctx, include_schema)
        # elif(isinstance(ast_node, TableFunctionCall)):
        #     return self.resolve_tbl_function(ast_node)
        # print(f"Node: {ast_node}")

        fn = SOURCE_REGISTRY[type(ast_node)]

        if not fn:
            raise Exception(f"{ast_node} not found.")

        fn_cls = fn(self.data_sources)
        return fn_cls.resolve(ast_node, engine_context, analysis_ctx, include_schema)
    
    def resolve_tbl_function(self, fn_type):
        raw = fn_type.arg[0]

        if isinstance(raw, Literal):
            raw = raw.value

        fn_cls = FUNCTION_CALL_REGISTRY.get(fn_type.name)

        if not fn_cls:
            raise Exception(f"Unknown table function: {fn_type.name}")

        source = fn_cls.execute(raw)

        return source.as_rows() #, dataset.schema()
            
    def resolve_identifier(self, source_name, engine_context, analysis_ctx, include_schema=False):

        # then physical sources
        factory = self.data_sources.get(source_name)

        if factory is None:
            raise ValueError(f"Unknown source: {source_name}")    

        # ✅ stdin case
        if source_name == "stdin":
            raw = sys.stdin.read()
            source = factory.from_raw(raw)

            dataset = source.to_dataset()   # 👈 normalize here
            return dataset.as_rows(), dataset.schema()

        # ✅ normal sources
        source = factory  # or factory.build()

        dataset = source.to_dataset()       # 👈 REQUIRED
        
        if include_schema == False:
            return dataset.as_rows()
        
        return dataset.as_rows(), dataset.schema()