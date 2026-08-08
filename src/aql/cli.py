import typer
from rich import print_json
from pathlib import Path

from .domain.query import query_results
from .preprocess.factory import Preprocessor
from .preprocess.about.types import AboutType
from .preprocess.about.registry import ABOUT_REGISTRY
from .preprocess.about import pipeline
from .preprocess.models import SourceLoader, ImportGraph

app = typer.Typer(help="AQL query everything.")

@app.command()
def about(
    filename: str = typer.Argument(
        ...,
        help="AQL file name or path info",
    ),
    category: AboutType = typer.Option(
        AboutType.SOURCE,
        "--category",
        help="Output category"
    ),
):
    # typer.echo(f"About: {filename}")
    path = Path.cwd() / filename
    source_loader = SourceLoader()
    import_graph = ImportGraph(root=ImportNode(path))
    preprocess_ctx = Preprocessor(source_loader).process(path)
    fn = ABOUT_REGISTRY[category]
    if not fn:
        raise Exception(f"About type {category} no found.")
    fn_cls = fn()
    result = fn_cls.process(source_loader)
    print_json(data=result)

@app.command()
def docs():
    typer.echo("Writing docs")
    from .docs.documentation_filter import Filter
    from .docs.factory import DocumentationFactory
    query_results = DocumentationFactory().create().queries_classification['csv']
    queries = [q.to_dict() for q in query_results]
    # Filter().from_source(queries).where("fields", "*").largest().print_source()
    Filter().from_source(queries).where("feature", "SUM").largest().print_source()
    # print_json(data=[q.to_dict() for q in query_results])

    print("Number of queries: ", len(query_results))

@app.command()
def query(
    q: str = typer.Argument(
        ...,
        help="AQL query string",
    )
):
    # typer.echo(f"Query: {q}")
    query_results(q)

@app.command()
def run(
    filename: str = typer.Argument(
        ...,
        help="AQL file name or path",
    )
):
    # typer.echo(f"Run: {filename}")
    path = Path.cwd() / filename
    source_loader = SourceLoader()
    preprocess_ctx = Preprocessor(source_loader).process(path)

    data = " ".join(preprocess_ctx.source)
    query_results(data)

@app.callback(invoke_without_command=True)
def main(ctx: typer.Context, script: Path | None = None):
    if script:
        run(script)