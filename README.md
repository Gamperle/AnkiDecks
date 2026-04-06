# AnkiDecks

A collection of Anki flashcard decks for learning and reviewing **Java**, **C++**, **Android**, **Security**, **Git**, and **Linux** topics.

## Repository Structure

```
AnkiDecks/
├── Java/          # Flashcard decks for Java programming
├── Cpp/           # Flashcard decks for C++ programming
├── Android/       # Flashcard decks for Android development
├── Security/      # Flashcard decks for cybersecurity fundamentals
├── Git/           # Flashcard decks for Git & version control
└── Linux/         # Flashcard decks for Linux fundamentals & administration
```

## Topics Covered

| Folder | Description |
|---|---|
| `Java/` | Core Java, OOP, collections, concurrency, JVM internals, networking, cryptography, web frameworks, and more (35+ decks) |
| `Cpp/` | C++ fundamentals, STL, memory management, OOP, modern C++ features |
| `Android/` | Android app development, AOSP internals, Android Automotive OS (AAOS), AAOS security — beginner through pro (12 decks) |
| `Security/` | Cybersecurity fundamentals — beginner, intermediate, and pro levels |
| `Git/` | Git & version control — basics, workflows, internals, security, and Git at scale |
| `Linux/` | Linux fundamentals, shell scripting, system administration, kernel internals, eBPF, and performance tuning |

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
