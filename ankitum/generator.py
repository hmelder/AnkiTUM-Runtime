import os.path
from typing import Any, Tuple, List
import click
import genanki
import html

from ankitum.card_models import basic_model, cloze_model
from ankitum.util import parse_images

required_files = []


def get_fields(card, model: genanki.Model) -> List[str]:
    fields = []
    global required_files

    for field in model.fields:
        name = field["name"]

        if name.lower() in card:
            card_field = card[name.lower()]

            if isinstance(card_field, str):
                card_field = html.escape(card_field)

                if name.lower() == "front" or name.lower() == "back":
                    card_field, required = parse_images(card_field)
                    required_files += required

                fields.append(card_field)
                continue

        click.echo(f"Field {name} not found in card {card}!")
        fields.append("")
        # exit(1)

    return fields


def parse_tags(card):
    tags = []

    if "tags" in card and isinstance(card["tags"], list):
        for tag in card["tags"]:
            if isinstance(tag, str):
                tags.append(html.escape(tag))
            else:
                return None

    return tags


def parse_basic(card) -> genanki.Note:
    if "chapter" not in card:
        card["chapter"] = ""

    tags = parse_tags(card)

    if tags is None:
        click.echo(f"Unable to parse tags of card: {card}")
        exit(1)

    fields = get_fields(card, basic_model)

    return genanki.Note(model=basic_model, fields=fields, tags=tags)


def parse_reverse(card) -> list[genanki.Note]:
    basic = parse_basic(card)

    reverse_fields = basic.fields.copy()

    front_index = -1
    back_index = -1

    # find indices of front and back fields
    for index, d in enumerate(basic_model.fields):
        if "front" == d["name"].lower():
            front_index = index
        elif "back" == d["name"].lower():
            back_index = index

    # swap
    front = reverse_fields[front_index]
    reverse_fields[front_index] = reverse_fields[back_index]
    reverse_fields[back_index] = front

    reverse = genanki.Note(model=basic_model, fields=reverse_fields, tags=basic.tags)
    return [basic, reverse]


def parse_cloze(card) -> genanki.Note:
    if "chapter" not in card:
        card["chapter"] = ""

    tags = []
    if "tags" in card:
        tags = parse_tags(card["tags"])
        if tags is None:
            click.echo(f"Tags of card {card} must be a string list!")
            exit(1)

    fields = get_fields(card, cloze_model)
    return genanki.Note(model=cloze_model, fields=fields, tags=tags)


def generate_notes(cards: list[Any], logo_name: str, debug=False) -> tuple[list[Any], list[Any]] | Any:
    total_flashcards = []
    global required_files
    required_files = []

    for card in cards:
        if "type" not in card or not isinstance(card["type"], str):
            click.echo(f"Invalid card type \"{card['type']}\"")

        type: str = card["type"]
        card["logo"] = logo_name

        if type.lower() == "basic" or type.lower() == "definition":
            flashcards = [parse_basic(card)]

        elif type.lower() == "reverse":
            flashcards = parse_reverse(card)

        elif type.lower() == "cloze":
            flashcards = [parse_cloze(card)]

        else:
            click.echo(f"Invalid type {type.lower()}")
            return exit(1)

        if flashcards is not None:
            if debug:
                click.echo(f"Created card with type {type}")

            # concat lists
            total_flashcards += flashcards
        else:
            click.echo("Error creating card")

    return total_flashcards, required_files


def create_deck(dstPath: str, deck_id: int, title: str, notes: list[genanki.Note], paths: list[str], debug=False):
    if debug:
        click.echo(f"Creating deck with id {deck_id} and name {title}")

    deck = genanki.Deck(deck_id=deck_id, name=title, description="Generated with ankiTUM")
    deck.notes = notes
    package = genanki.Package(deck)

    if debug:
        for p in paths:
            if os.path.isfile(p):
                click.echo(f"Adding image path \"{p}\"")
            else:
                click.echo(f"ERROR: missing image path \"{p}\"")
                exit(1)

    package.media_files = paths

    if debug:
        click.echo(f"Writing deck to path {dstPath}")

    package.write_to_file(dstPath)
    click.echo(f"Success")
