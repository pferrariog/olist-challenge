from api import author_router
from api import book_router
from cli.authors import app as authors_app
from fastapi import APIRouter
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from typer import Typer


def create_fastapi_app(title: str, description: str, routers: list[APIRouter]) -> FastAPI:
    """Create a customized FastAPI instance"""
    app = FastAPI(title=title, description=description)

    for router in routers:
        app.include_router(router)

    app.add_middleware(CORSMiddleware, allow_origins=["*"], allow_methods=["*"])

    return app


app = create_fastapi_app("O-List API", "Simple library app", [author_router, book_router])

typer_app = Typer()
typer_app.add_typer(authors_app, name="authors")


if __name__ == "__main__":
    typer_app()
