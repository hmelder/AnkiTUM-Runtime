/* convert - V1 AnkiTUM to V2 AnkiTUM converter
 * Copyright (C) 2023 Hugo Melder
 *
 * SPDX-License-Identifier: MIT
 */

package main

import (
	"math/rand"
	"os"
	"strings"

	"github.com/go-yaml/yaml"
)

type AnkiTUMV2 struct {
	Title  string `yaml:"title"`
	Author string `yaml:"author"`
	Cards  []Card `yaml:"cards"`
	ID     int    `yaml:"id"`
}
type Card struct {
	Type    string   `yaml:"type"`
	Format  string   `yaml:"format"`
	Front   string   `yaml:"front"`
	Back    string   `yaml:"back,omitempty"`
	Chapter string   `yaml:"chapter,omitempty"`
	Tags    []string `yaml:"tags,omitempty"`
}

func NewAnkiTUMV2(title string, author string, cards []Card) *AnkiTUMV2 {
	id := rand.Int()

	return &AnkiTUMV2{
		Title:  title,
		Author: author,
		Cards:  cards,
		ID:     id,
	}
}

func NewCard(front string, back string) Card {
	card := Card{
		Type:   "basic",
		Format: "md",
		Front:  front,
		Back:   back,
	}

	return card
}

func main() {
	var deckName string

	cardList := make([]Card, 0)

	if len(os.Args) < 2 {
		panic("No input file specified")
	}

	// Open file (first argument) and read into buffer
	data, err := os.ReadFile(os.Args[1])
	if err != nil {
		panic(err)
	}

	// Split file into lines
	lines := strings.Split(string(data), "\n")

	var lastCardName string
	var lastCardContent string

	count := 0

	// Don't judge this pls :)
	for _, line := range lines {
		// Check if line starts with '# '
		if strings.HasPrefix(line, "# ") && deckName == "" {
			deckName = strings.TrimPrefix(line, "# ")
		} else if strings.HasPrefix(line, "## ") {
			count += 1
			if lastCardName != "" {
				card := NewCard(lastCardName, lastCardContent)
				cardList = append(cardList, card)
				lastCardContent = ""
			}
			lastCardName = strings.TrimPrefix(line, "## ")
		} else if lastCardName != "" {
			lastCardContent += line + "\n"
		}
	}

	// Add last card
	if len(cardList) < count {
		cardList = append(cardList, NewCard(lastCardName, lastCardContent))
	}

	ankiTUMV2 := NewAnkiTUMV2(deckName, "AnkiTUM", cardList)

	data, err = yaml.Marshal(ankiTUMV2)
	if err != nil {
		panic(err)
	}

	print(string(data))
}
