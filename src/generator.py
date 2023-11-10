from typing import Any
import click
import genanki


basic_model = genanki.BASIC_MODEL


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
        exit(1)

    return fields


def parse_basic(card):
    fields = get_fields(card, basic_model)
    return genanki.Note(model=basic_model, fields=fields, guid=9438948)


def parse_reverse(card):
    pass


def parse_cloze(card):
    pass


def generate_notes(cards: list[Any], debug=False) -> list[genanki.Note]:

    flashcards = []

    for card in cards:
        if "type" not in card or not isinstance(card["type"], str):
            click.echo(f"Invalid card type \"{card['type']}\"")

        type: str = card["type"]

        if type.lower() == "basic":
            flashcard = parse_basic(card)

        elif type.lower() == "reverse":
            flashcard = parse_reverse(card)

        elif type.lower() == "cloze":
            flashcard = parse_cloze(card)

        else:
            click.echo(f"Invalid type {type.lower()}")
            exit(1)

        if flashcard is not None:
            if debug:
                click.echo(f"Created card with type {type}")

            flashcards.append(flashcard)

    return flashcards


def create_deck(dstPath: str, deck_id: int, title: str, notes: list[genanki.Note], debug=False):

    if debug:
        click.echo(f"Creating deck with id {deck_id} and name {title}")
    deck = genanki.Deck(deck_id=deck_id, name=title, description="Generated with ankiTUM")
    deck.notes = notes
    genanki.Package(deck).write_to_file(dstPath)
