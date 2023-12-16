import html
import os
from io import TextIOWrapper
from typing import Any

import click
import yaml

from ankitum.generator import generate_notes, create_deck
from ankitum.util import get_required_resources


@click.command()
@click.argument("input_file_path", type=click.Path())
@click.option("--output", "-o", type=click.Path(), help="Output flashcards file")
@click.option("--resource-folder", "-r", type=click.Path(), help="Path to resource folder")
@click.option("--logo_path", "-l", type=click.Path(), help="Path to the logo")
@click.option("--debug", is_flag=True, help="Enable debug mode")
def generate(input_file_path, output, resource_folder=None, logo_path=None, debug=False):
    """
        Generate flashcards from a Yaml file.
    """

    if not os.path.isfile(input_file_path):
        click.echo("ERROR: Input file does not exist!")
        exit(1)

    with open(input_file_path, mode="r+", encoding="utf-8") as input_file:
        content = input_file.read()
        root = yaml.load(content, Loader=yaml.FullLoader)

        if "id" not in root or not isinstance(root["id"], int) or int(root["id"]) < 0:
            click.echo("ERROR: Missing or malformed deck id attribute")
            exit(1)

        if "title" not in root or not isinstance(root["title"], str):
            click.echo("ERROR: Missing deck title attribute")
            exit(1)

        if "cards" not in root or not isinstance(root["cards"], list):
            click.echo("ERROR: Missing cards attribute")
            exit(1)

        deck_id = int(root["id"])
        title: str = html.escape(root["title"])
        cards: list[Any] = root["cards"]
        authors: list[str] = []

        if "authors" in root:
            if isinstance(root["authors"], str):
                authors.append(html.escape(root["authors"]))

            elif isinstance(root["authors"], list):
                for author in root["authors"]:
                    if isinstance(author, str):
                        authors.append(html.escape(author))

        if debug:
            click.echo(f"Parsed deck with title=\"{title}\" authors=\"{authors}\" and a list of {len(cards)} cards.")

        paths = []  # image paths
        if logo_path is not None:
            logo_path = os.path.abspath(logo_path)
            logo_name = os.path.basename(logo_path)

        else:
            logo_name = "tum_logo.png"
            os.path.abspath(logo_name)

        if debug:
            click.echo(f"Searching for logo at path: \"{logo_path}")

        paths.append(logo_path)

        notes, required_files = generate_notes(cards, logo_name, debug=debug)

        if resource_folder is None:
            parent_dir = os.path.dirname(input_file_path)
            resource_folder = "./" + parent_dir + "/resources"

            if debug:
                click.echo(f"No resource folder specified. Searching: \"{resource_folder}\"")

            if not os.path.exists(resource_folder) or not os.path.isdir(resource_folder):
                click.echo(f"ERROR: Default resource folder \"{resource_folder}\" does not exist! Please create it or "
                           f"specify a resource folder with -r")
                exit(1)

        paths = get_required_resources(required_files, resource_folder)

        create_deck(output, deck_id, title, notes, paths, debug=debug)


if __name__ == '__main__':
    generate()
