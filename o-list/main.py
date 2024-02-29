from cli.authors import app as authors_app
from fastapi import FastAPI
from typer import Typer


def create_fastapi_app() -> FastAPI:
    """Create a customized FastAPI instance"""
    app = FastAPI()
    return app


app = create_fastapi_app()

typer_app = Typer()
typer_app.add_typer(authors_app, name="authors")


if __name__ == "__main__":
    typer_app()
