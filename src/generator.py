from typing import Any
import click
import genanki


def parse_basic(card):
    pass


def parse_reverse(card):
    pass


def parse_cloze(card):
    pass


def generate_flashcards(title: str, authors: list[str], cards: list[Any]):
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

