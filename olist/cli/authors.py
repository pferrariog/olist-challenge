import csv

from rich.progress import Progress
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
        with Progress() as progress:
            task = progress.add_task("[green] Inserting authors...", total=sum(1 for row in file))
            for idx, name in enumerate(file):
                if idx == 0 or not name:
                    progress.update(task)
                    continue
                try:
                    repository.create(name[0])
                    progress.update(task)
                except Exception as e:
                    raise Exception(e.__str__)
