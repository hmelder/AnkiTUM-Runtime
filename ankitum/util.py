import os
import re
from typing import Tuple, List

import bleach
import click


valid_resource_file_extensions = ['.png', '.jpg', '.jpeg']


def parse_images(text: str, debug=False) -> Tuple[str, List[str]]:
    """
    Replaces all media clauses.

    Returns the replaced text, and a list of required file names
    """
    pattern = r"\[\[image: ([a-zA-Z0-9_.öäüÖÄÜß]+)\]\]"

    required_files = []

    def replace(match: re.Match):

        if debug:
            click.echo(f"detected image reference {match}")

        image_name = match.group(0)[9:-2]
        split = image_name.split(".")

        if len(split) != 2:
            click.echo(f"ERROR: Invalid file name {image_name}")
            exit(1)

        file_extension = split[1]

        if ("." + file_extension) not in valid_resource_file_extensions:
            click.echo(f"ERROR: File extension not supported: \"{image_name}\"")
            exit(1)

        required_files.append(image_name)
        return f"<img src=\"{image_name}\">"

    return re.sub(pattern, replace, text), required_files


def get_required_resources(required_files, resource_folder):
    req_set = set(required_files)

    resources = get_resources(resource_folder)
    res_file_names = list(map(lambda f: os.path.basename(f), resources))

    for fn in req_set:
        if fn not in res_file_names:
            click.echo(f"Warning: file \"{fn}\" not found")

    return resources


def get_resources(folder_path: str):
    """
    Gets all valid test_yamls from folder at relative path. Returns absolute paths of valid test_yamls
    """
    folder_path = os.path.abspath(folder_path)

    absolute_paths = []

    for f in os.listdir(folder_path):
        if not os.path.isfile(os.path.join(folder_path, f)):
            continue

        name, ext = os.path.splitext(f)

        if ext not in valid_resource_file_extensions:
            click.echo(f"File extension \"{ext}\" of file \"{name}\" not allowed!")
            continue

        absolute_paths.append(os.path.abspath(os.path.join(folder_path, f)))

    return absolute_paths


allowed_tags = ["b", "i", "u", "ul", "ol", "li", "code", "p", "h", "h1", "h2", "h3", "h4", "h5", "h6", "br", "sup", "sub"]
allowed_attributes = {"code": ["class"]}


def sanitize_html(text):
    """
    Remove any dangerous tags
    """
    return bleach.clean(text, tags=allowed_tags, attributes=allowed_attributes)
