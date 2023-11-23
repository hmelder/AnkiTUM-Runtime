from typing import Any
import click
import genanki

from card_models import basic_model, cloze_model


def get_fields(card, model: genanki.Model) -> list[str]:
    fields = []

    for field in model.fields:
        name = field["name"]

        if name.lower() in card:
            card_field = card[name.lower()]

            if isinstance(card_field, str):
                fields.append(card_field)
                continue

        click.echo(f"Field {name} not found in card {card}!")
        fields.append("")
        # exit(1)

    return fields


def parse_tags(tags):
    tags = []
    if isinstance(tags, list):
        for tag in tags:
            if isinstance(tag, str):
                tags.append(tag)
            else:
                return None

    return tags


def parse_basic(card) -> genanki.Note:
    if "chapter" not in card:
        card["chapter"] = ""

    fields = get_fields(card, basic_model)
    return genanki.Note(model=basic_model, fields=fields)


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


def generate_notes(cards: list[Any], debug=False) -> list[genanki.Note]:
    total_flashcards = []

    for card in cards:
        if "type" not in card or not isinstance(card["type"], str):
            click.echo(f"Invalid card type \"{card['type']}\"")

        type: str = card["type"]

        card["tumlogo"] = "tum_logo.png"
        if type.lower() == "basic":
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

    return total_flashcards


def create_deck(dstPath: str, deck_id: int, title: str, notes: list[genanki.Note], debug=False):
    if debug:
        click.echo(f"Creating deck with id {deck_id} and name {title}")
    deck = genanki.Deck(deck_id=deck_id, name=title, description="Generated with ankiTUM")
    deck.notes = notes
    package = genanki.Package(deck)
    package.media_files = ["C:\\Users\\hendr\\PycharmProjects\\AnkiTUM-Runtime\\resources\\tum_logo.png"]
    package.write_to_file(dstPath)
