import typer
from typing import Optional
from rich import print_json

from ..schema.inspector import SchemaInspector
from ..adapter.source.factory import StdinSourceFactory
from ..evalulators.evalulate import Evaluator
from ..engine.projector import Projector
from ..engine.query_engine import QueryEngine, EngineContext
from ..engine.executor import ExecutionEngine
# from aegis_prime.config.loader import load_config_context
# from aegis_prime.config.cli_merge import CLIOverrides
# from aegis_prime.config.resolver import ConfigResolver
# from aegis_prime.core.model_registry import MODEL_REGISTRY
# from aegis_prime import models

def normalize_query(query: str, data_sources: dict) -> str:
    if "FROM" not in query.upper() and data_sources["stdin"] is not None:
        return query.strip() + " FROM stdin"
    return query

# def build_cli_overrides(
#     q: str,
#     source: str = None,
#     format: str = None,
#     limit: int = None,
#     offset: int = None,
#     debug: bool = None,
#     profile: str = None,
# ):
#     return CLIOverrides(
#         source=source,
#         format=format,
#         limit=limit,
#         offset=offset,
#         debug=debug,
#         profile=profile,
#     )

def build_engine(data_sources, q) -> QueryEngine:

#    data_sources = {**MODEL_REGISTRY, **data_sources}
#    config = load_config_context("aegis.toml")
#    cli = build_cli_overrides(q)
    engine_context = EngineContext(
        data_sources=data_sources,
        evaluator=Evaluator(),
        projector=Projector(),
        registry=data_sources,
#        registry=MODEL_REGISTRY,
        inspector=SchemaInspector(),
    )

#    resolver = ConfigResolver(config, cli)
#    config_ctx = resolver.resolve()
    config_ctx = None
    execution_engine = ExecutionEngine(engine_context, config_ctx)
    return QueryEngine(execution_engine)

def query_results(q: str):
    data_sources = {}
    data_sources["stdin"] = StdinSourceFactory
    engine = build_engine(data_sources, q)

    q = normalize_query(q, data_sources)
    
    result = engine.run(q)
    
    result = list(result)

    print_json(data=result)