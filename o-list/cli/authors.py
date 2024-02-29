import csv

from typer import Typer

from ..core.database import get_db_connection
from ..models.repository.authors import AuthorRepository


app = Typer()


@app.command()
def import_authors(csv_file_path: str) -> None:
    """Import authors from csv file by CLI command"""
    repository = AuthorRepository(get_db_connection())

    with open(csv_file_path) as file:
        file = csv.reader(file)

        for idx, name in enumerate(file):
            if idx == 0 or not name:
                continue
            try:
                repository.create(name[0])
            except Exception:
                ...

    # TODO prettier print with rich
    # TODO add progress bar and success/fail numbers
