import os.path
import re

import yaml
import click

from ankitum.util import sanitize_html

cloze_regex = r"\{\{c(\d+):(.*?)\}\}"


def generate_yaml(file_path: str, output_path: str, author: str, title: str, set_ids: bool = False,
                  basic_type="basic", cloze_type="cloze"):

    if basic_type is None:
        basic_type = "html"

    if cloze_type is None:
        cloze_type = "html_cloze"

    # Initialize variables for parameters
    separator = None
    html_enabled = False
    guid_column = None
    notetype_column = None
    deck_column = None
    tags_column = None

    # Open the file and read parameters from the first few lines
    with open(file_path, "r", encoding="utf-8") as file:
        for line in file:
            if line.startswith("#separator:"):
                separator = line.strip().split(":")[1]
                if separator == "tab":
                    separator = "\t"

            elif line.startswith("#html:"):
                html_enabled = line.strip().split(":")[1].lower() == "true"
                if not html_enabled:
                    print("Html is not enabled")
                    exit(0)

            elif line.startswith("#guid column:"):
                guid_column = int(line.strip().split(":")[1])

            elif line.startswith("#notetype column:"):
                notetype_column = int(line.strip().split(":")[1])

            elif line.startswith("#deck column:"):
                deck_column = int(line.strip().split(":")[1])

            elif line.startswith("#tags column:"):
                tags_column = int(line.strip().split(":")[1])

        front_column = max((notetype_column, deck_column, guid_column)) + 1
        back_column = front_column + 1

    # Check if all necessary parameters are provided
    if None in (separator, guid_column, notetype_column, deck_column, tags_column):
        print("Missing required parameters. Please check the input file.")
        return

    # collect cards as a list of dicts
    decks = {}

    with open(file_path, "r", encoding="utf-8") as file:
        # Skip the lines with parameters
        for _ in range(6):
            next(file)

        current_line = ""

        while True:
            line = next(file, None)
            if line is None:
                if current_line is "":
                    break
                else:
                    data = current_line.strip().split(separator)
                    current_line = ""

            elif line[-2] == separator:  # last character is a newline, so we check the second to last char
                current_line += line
                data = current_line.strip().split(separator)
                current_line = ""

            else:
                current_line += line
                continue

            card = {}
            deck = ""

            for column, entry in enumerate(data):
                if column + 1 == guid_column and set_ids:
                    card["id"] = hash(entry) % 10000000
                elif column + 1 == notetype_column:
                    card["type"] = entry
                elif column + 1 == deck_column:
                    deck = entry
                elif column + 1 == front_column:
                    card["front"] = sanitize_html(entry)
                elif column + 1 == back_column:
                    card["back"] = sanitize_html(entry)

            if "front" not in card:
                click.secho("Warning: card does no have front field " + str(data), fg="yellow")

            elif "back" not in card:
                if re.match(cloze_regex, card["front"]):
                    # cloze type
                    card["type"] = cloze_type

                else:
                    click.secho("Warning: card does no have back field and does not seem to be a cloze " + str(data),
                                fg="yellow")
            else:
                # basic type
                card["type"] = basic_type

            if deck == "":
                click.secho("No deck specidied for card " + str(card), fg="red")
                continue
            elif deck in decks:
                decks[deck].append(card)
            else:
                decks[deck] = [card]

    for key, deck in decks.items():
        with open(os.path.join(output_path, (key + ".yaml")), "w") as file:
            output = {}
            output["title"] = title
            output["author"] = author
            output["cards"] = deck

            yaml.dump(output, file, default_flow_style=False, sort_keys=False)
