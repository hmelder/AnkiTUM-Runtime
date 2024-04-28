import html
import os
import traceback
from typing import Any

import click
import yaml
from genanki import Deck

from ankitum import generator
from ankitum.reverse_parser import generate_yaml
from ankitum.util import get_required_resources


@click.group()
def cli():
    pass


@cli.command("generate")
@click.argument("input_path", type=click.Path())
@click.option("--output", "-o", type=click.Path(), help="Output flashcards file")
@click.option("--resource-folder", "-r", type=click.Path(), help="Path to resource folder")
@click.option("--logo_path", "-l", type=click.Path(), help="Path to the logo")
@click.option("--debug", is_flag=True, help="Enable debug mode")
def generate(input_path, output, resource_folder=None, logo_path=None, debug=False):
    """
    Generate flashcards from a Yaml file.
    """

    if os.path.isfile(input_path):
        root_title = ""
        if input_path.lower().endswith(".yaml") or input_path.lower().endswith(".yml"):
            yaml_files = [input_path]

        else:
            yaml_files = []

    elif os.path.isdir(input_path):
        yaml_files = []
        root_title = os.path.basename(input_path)

        for file_path in os.listdir(input_path):
            if file_path.lower().endswith(".yaml") or file_path.lower().endswith(".yml"):
                yaml_files.append(os.path.join(input_path, file_path))

    else:
        click.echo("ERROR: Input file does not exist!")
        click.echo(os.path.abspath(input_path))
        exit(0)

    if len(yaml_files) == 0:
        click.echo("No yaml files found")
        exit(0)

    decks = []
    paths = set()

    for file in yaml_files:
        deck, path = create_deck(file, resource_folder, logo_path, root_title, debug)
        decks.append(deck)
        paths = paths.union(path)

    generator.create_package(decks, output, paths, debug)


def create_deck(input_file_path: str, resource_folder=None, logo_path=None, root_title: str = None, debug=False) -> \
tuple[Deck, list[str]]:
    with open(input_file_path, mode="r+", encoding="utf-8") as input_file:

        content = input_file.read()
        root = yaml.safe_load(content)

        if "title" not in root or not isinstance(root["title"], str):
            click.echo("ERROR: Missing deck title attribute")
            exit(1)

        if "cards" not in root or not isinstance(root["cards"], list):
            click.echo("ERROR: Missing cards attribute for " + str(root["title"]))
            exit(1)

        if "id" not in root:
            click.echo("ERROR: Missing id attribute for " + str(root["title"]))
            exit(1)

        deck_id = int(root["id"])

        title: str = html.escape(root["title"])

        if root_title:
            title = root_title + "::" + title

        cards: list[Any] = root["cards"]

        for card in cards:
            if isinstance(card, dict):
                card["title"] = title

        authors: list[str] = []

        if "authors" in root:
            if isinstance(root["authors"], str):
                authors.append(html.escape(root["authors"]))

            elif isinstance(root["authors"], list):
                for author in root["authors"]:
                    if isinstance(author, str):
                        authors.append(html.escape(author))

        if debug:
            click.echo(
                f"Parsed deck with title=\"{title}\" authors=\"{authors}\" and a list of {len(cards)} cards. Generated ID: {deck_id}")

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

        try:
            notes, required_files = generator.generate_notes(cards, logo_name, debug=debug)

            # calculate card ID
            for note in notes:
                note["id"] = hash(str(note["id"]) + str(deck_id))

        except Exception as e:
            click.echo("Could not generate Notes!")
            click.echo(traceback.format_exc(), err=True)

        if resource_folder is None:
            parent_dir = os.path.dirname(input_file_path)
            resource_folder = "./" + parent_dir + "/resources"

            if debug:
                click.echo(f"No resource folder specified. Searching: \"{resource_folder}\"")

        if len(required_files) > 0:
            if (not os.path.exists(resource_folder) or not os.path.isdir(resource_folder)):
                click.echo(f"ERROR: Default resource folder \"{resource_folder}\" does not exist! Please create it or "
                           f"specify a resource folder with -r")
                exit(1)


            paths = get_required_resources(required_files, resource_folder)

        else:
            paths = []

        return generator.create_deck(deck_id, title, notes, debug=debug), paths


@cli.command("reverse")
@click.argument("input_path", type=click.Path())
@click.option("--output", "-o", type=click.Path(exists=True, dir_okay=True, file_okay=False),
              help="Output flashcards file")
@click.option("--author", "-a", type=click.Path(), help="Author of the deck")
@click.option("--title", "-t", type=click.Path(), help="Title of the deck")
@click.option("--set-ids", "-i", is_flag=True, help="Generate IDs")
@click.option("--basic-type", help="Specify Note type for notes with front and back")
@click.option("--cloze-type", help="Specify Note type for notes with cloze")
def reverse_parse(input_path, output, author, title, set_ids, basic_type=None, cloze_type=None):
    generate_yaml(input_path, output, author, title, set_ids, basic_type, cloze_type)


if __name__ == '__main__':
    cli()
