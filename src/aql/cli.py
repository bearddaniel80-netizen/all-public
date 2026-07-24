import typer
from rich import print_json
from pathlib import Path

from .domain.query import query_results
from .preprocess.factory import Preprocessor
from .preprocess.about.types import AboutType
from .preprocess.about.registry import ABOUT_REGISTRY
from .preprocess.about import pipeline
from .preprocess.models import SourceLoader

app = typer.Typer(help="AQL query everything.")

@app.command()
def about(
    filename: str = typer.Argument(
        ...,
        help="AQL file name or path info",
    ),
    catagory: AboutType = typer.Option(
        AboutType.SOURCE,
        "--catagory",
        help="Output catagory"
    ),
):
    typer.echo(f"About: {filename}")
    path = Path.cwd() / filename
    source_loader = SourceLoader()
    preprocess_ctx = Preprocessor(source_loader).process(path)
    fn = ABOUT_REGISTRY[catagory]
    if not fn:
        raise Exception(f"About type {catagory} no found.")
    fn_cls = fn()
    result = fn_cls.process(source_loader)
    print_json(data=result)

@app.command()
def query(
    q: str = typer.Argument(
        ...,
        help="AQL query string",
    )
):
    typer.echo(f"Query: {q}")
    query_results(q)

@app.command()
def run(
    filename: str = typer.Argument(
        ...,
        help="AQL file name or path",
    )
):
    typer.echo(f"Run: {filename}")
    path = Path.cwd() / filename
    source_loader = SourceLoader()
    preprocess_ctx = Preprocessor(source_loader).process(path)

    data = " ".join(preprocess_ctx.source)
    query_results(data)