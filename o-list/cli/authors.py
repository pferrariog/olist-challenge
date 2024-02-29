import csv

from typer import Typer

from ..services.authors import Service


app = Typer()


@app.command()
def import_authors(csv_file_path: str) -> None:
    """Import authors from csv file by CLI command"""
    service = Service(...)

    with open(csv_file_path) as file:
        file = csv.reader(file)

        for idx, name in enumerate(file):
            if idx == 0 or not name:
                continue
            try:
                service.create(name[0])
            except Exception:
                ...
