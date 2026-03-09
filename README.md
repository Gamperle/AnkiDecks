# AnkiDecks

A collection of Anki flashcard decks for learning and reviewing **Java**, **C++**, and **Android** development.

## Repository Structure

```
AnkiDecks/
├── Java/          # Flashcard decks for Java programming
├── Cpp/           # Flashcard decks for C++ programming
└── Android/       # Flashcard decks for Android development
```

## Topics Covered

| Folder    | Description |
|-----------|-------------|
| `Java/`   | Core Java concepts, OOP, collections, concurrency, JVM internals, and more |
| `Cpp/`    | C++ fundamentals, STL, memory management, templates, modern C++ features |
| `Android/`| Android SDK, Activities, Fragments, Jetpack components, Kotlin interop |

## Deck Format

Decks are stored as **tab-separated `.txt` files** that can be imported directly into Anki:

- Each line represents one flashcard.
- Format: `Front[TAB]Back`
- Lines beginning with `#` are comments and are ignored on import.

### Importing a Deck into Anki

1. Open Anki and select **File → Import…**
2. Choose the `.txt` file for the deck you want to import.
3. In the import dialog, set the field separator to **Tab**.
4. Select or create the target note type and deck.
5. Click **Import**.

## Contributing

1. Fork the repository.
2. Add or update cards in the relevant topic folder.
3. Follow the existing file format (tab-separated, UTF-8 encoding).
4. Open a pull request with a short description of the cards added or changed.

## License

This project is licensed under the [MIT License](LICENSE).
