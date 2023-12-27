# Format


## File structure 
A deck is represented by a folder containing one or more yaml file and zero or more 
subfolders.

A yaml file represents a deck of flash cards according to the format described below.

A folder may either be a "resource" folder or a subdeck. 
Resource folders must be named "resources" and can only contain png, jpg and jpeg files.

## deck format

A deck yaml file can have the following attributes:

id (Required) - The id of the deck (integer). Should not be changed after initial creation
title (Required) - The title of the deck (only letters, numbers, spaces and underscores allowed)
authors (Optional) - The authors of the deck (a list of strings or a string, only letters and spaces allowed)
cards (Required) - One or more cards contained in the deck

A card is created with its type like this:

```yaml
# example card
type: basic
front: "Whats 1 + 1?"
back: "It's 2"
chapter: "Basic Arithmetic"
tags:
  - super_difficult
  - addition
```

Depending on the type there may be more optional or required attributes.

## Card types

### basic

Basic cards have a front and a back.

front (Required) - The front text of the card

back (Required) - The back text of the card

tags (Optional) - A list of tags (strings)

chapter (Optional) - The lecture or chapter that the card is based on

### reverse

Reverse Cards generate two basic cards: One of them has the front and back reversed.

front (Required) - The front text of the card

back (Required) - The back text of the card

tags (Optional) - A list of tags (strings)

chapter (Optional) - The lecture or chapter that the card is based on

### cloze

Cloze types do not have a back. They contain "clozes" which are words or phrases inside a sentence 
that are blacked out and get revealed when the user turns the card around.

front (Required) - The front text of the card

tags (Optional) - A list of tags (strings)

chapter (Optional) - The lecture or chapter that the card is based on


Clozes can be defined like in the anki standard cloze type: 

```
{{c1::text to be revealed}} {{c2::More text}}
```

## Images

Images can be added with an image clause:

```
[[image: image_name.png]]
```

The corresponding file by the name of "image_name.png" must be put into the "resources" folder.
JPG and JPEG file extensions are also supported.

Please note that cloze types can't have images for now.

## Examples

Here is an example deck:

```yaml
id: 123
title: Penguins
authors: Joe
cards:
  - type: basic
    front: Whats the worlds largest penguin?
    back: The Emperor Penguin
    chapter: Penguins 101
    
  - type: cloze
    front: The {{c1::Macaroni}} Penguin has the worlds most epic hairstyle
    chapter: Penguins 101
  
  # Card in Markdown
  - type: basic
    format: md
    front: Which penguin species is the fastet?
    back: |+
    # **Gentoo** Penguins are the fastest of all penguin species!
    1. Here a random list
    2. With
    3. No
    4. Content
      - But what is content?
```
