import os.path
import traceback
from typing import Any, List
import click
import genanki
import html
import mistune
from genanki import Deck

from ankitum.card_models import basic_model, cloze_model, latex_plus
from ankitum.markdown_renderer import MdRenderer
from ankitum.util import parse_images, sanitize_html

md_parser = mistune.Markdown(renderer=MdRenderer())
required_files = []


class AnkiNote(genanki.Note):
    def __init__(self, *args, guid=None, **kwargs):
        super().__init__(*args, **kwargs)
        self._guid = guid

    @property
    def guid(self):
        if self._guid:
            return self._guid

        else:
            # hash the first field (usually the front field)
            return genanki.guid_for(self.fields[0])


def get_fields(card, model: genanki.Model, parse_md=False, allow_html=False) -> List[str]:
    fields = []
    global required_files

    for field in model.fields:
        name = field["name"]

        if name.lower() in card:
            card_field = card[name.lower()]

            if isinstance(card_field, str):
                # The user has the option to use a type which sets the "parseMarkdown" flag,
                # or set the "format" field to "md" to enable markdown parsing.
                if parse_md:
                    card_field, _ = md_parser.parse(card_field)

                else:
                    if allow_html:
                        # allow basic html
                        card_field = sanitize_html(card_field)
                    else:
                        card_field = html.escape(card_field)

                if name.lower() == "front" or name.lower() == "back":
                    card_field, required = parse_images(card_field)
                    required_files += required

                fields.append(card_field)
                continue

        click.echo(f"Warning: Field {name} not found in card {card}!")
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


def parse_basic(card, parse_md=False, allow_html=False) -> genanki.Note:
    if "chapter" not in card:
        card["chapter"] = ""

    guid = None
    if "id" in card:
        guid = str(card["id"])

    tags = parse_tags(card)

    if tags is None:
        click.echo(f"ERROR: Unable to parse tags of card: {card}")
        exit(1)

    fields = get_fields(card, basic_model, parse_md, allow_html)

    return AnkiNote(model=basic_model, fields=fields, tags=tags, guid=guid)


def parse_latex_plus(card) -> genanki.Note:
    if "chapter" not in card:
        card["chapter"] = ""

    guid = None
    if "id" in card and isinstance(card["id"], int):
        guid = card["id"]

    fields = get_fields(card, basic_model, allow_html=True)
    tags = parse_tags(card)

    if tags is None:
        click.echo(f"ERROR: Unable to parse tags of card: {card}")
        exit(1)

    return AnkiNote(model=latex_plus, fields=fields, tags=tags, guid=guid)


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

    reverse = AnkiNote(model=basic_model, fields=reverse_fields, tags=basic.tags)
    return [basic, reverse]


def parse_cloze(card, allow_html=False) -> genanki.Note:
    if "chapter" not in card:
        card["chapter"] = ""

    tags = []
    if "tags" in card:
        tags = parse_tags(card["tags"])
        if tags is None:
            click.echo(f"ERROR: Tags of card {card} must be a string list!")
            exit(1)

    fields = get_fields(card, cloze_model, allow_html)
    return AnkiNote(model=cloze_model, fields=fields, tags=tags)


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

        elif type.lower() == "md_basic" or type.lower() == "markdown":
            flashcards = [parse_basic(card, parse_md=True)]

        elif type.lower() == "reverse":
            flashcards = parse_reverse(card)

        elif type.lower() == "cloze":
            flashcards = [parse_cloze(card)]

        elif type.lower() == "html":
            flashcards = [parse_basic(card, allow_html=True)]

        elif type.lower() == "latex_plus":
            flashcards = [parse_latex_plus(card)]

        elif type.lower() == "html_cloze":
            flashcards = [parse_cloze(card, allow_html=True)]

        else:
            click.echo(f"ERROR: Invalid type {type.lower()}")
            return exit(1)

        if flashcards is not None:
            # concat lists
            total_flashcards += flashcards

        else:
            click.echo("Error creating card")

    if debug:
        click.echo(f"Created {len(total_flashcards)} cards")

    return total_flashcards, required_files


def create_package(decks: list[Deck], dst_path: str, paths: list[str], debug=False):
    package = genanki.Package(decks)

    if debug:
        for p in paths:
            if os.path.isfile(p):
                click.echo(f"Adding image path \"{p}\"")

            else:
                click.echo(f"ERROR: missing image path \"{p}\"")
                exit(1)

    package.media_files = paths

    click.echo(f"Writing deck to path {dst_path}")

    try:
        package.write_to_file(dst_path)

    except Exception as e:
        click.echo("Could not write to file!")
        click.echo(traceback.format_exc(), err=True)
        exit(1)

    click.echo(f"Finished!")


def create_deck(deck_id: int, title: str, notes: list[genanki.Note], debug=False):
    if debug:
        click.echo(f"Creating deck with id {deck_id} and name {title}")

    deck = genanki.Deck(deck_id=deck_id, name=title, description="Generated with AnkiTUM")
    deck.notes = notes

    return deck
