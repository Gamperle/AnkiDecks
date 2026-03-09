# CLAUDE.md — Copilot/Claude Instructions

This file provides context and conventions for AI assistants (GitHub Copilot, Claude, etc.) working on this repository.

---

## Project Overview

**AnkiDecks** is a collection of plain-text Anki flashcard decks for studying **Java**, **C++**, and **Android** development. Decks are tab-separated `.txt` files importable directly into the Anki desktop app.

---

## Repository Structure

```
AnkiDecks/
├── Java/        # Core Java, OOP, Collections, Concurrency, JVM
├── Cpp/         # C++ fundamentals, STL, memory, modern C++
├── Android/     # Android SDK, Jetpack, Kotlin, UI
├── README.md
├── LICENSE
└── CLAUDE.md    ← this file
```

---

## Card Format

Every `.txt` deck file follows this format:

```
# Comment lines start with # and are ignored by Anki on import
Front text[TAB]Back text
```

- **Separator**: a single literal tab character (`\t`) between front and back.
- **Encoding**: UTF-8.
- **One card per line.**
- Backticks (`` ` ``) are used in card text to denote inline code.
- No HTML tags unless intentional formatting is needed.

### Example

```
What is the difference between `==` and `.equals()` in Java?	`==` compares object references; `.equals()` compares content/values.
```

---

## Conventions for Adding or Editing Cards

1. **Card fronts** should be concise questions or "what is X?" prompts.
2. **Card backs** should be thorough and educational — include not just the direct answer but also relevant context, caveats, common pitfalls, and brief examples where helpful. A learner should be able to fully understand the concept from the back alone.
3. Group related cards together; use a `# Section` comment header when a file covers multiple sub-topics.
4. Keep backs **factually accurate** for the language/version being targeted.
   - Java cards target **Java 17+** unless a file header specifies otherwise.
   - C++ cards target **C++17/C++20** unless noted.
   - Android cards reflect **Jetpack / modern Android** practices.
5. Avoid duplicating cards that are already present in the file.
6. Maintain alphabetical or logical grouping within a section when possible.

---

## File-by-File Scope

### Java/
| File | Scope |
|------|-------|
| `java_basics.txt` | Primitives, operators, control flow, String basics |
| `java_oop.txt` | Classes, interfaces, inheritance, polymorphism, generics |
| `java_collections.txt` | List, Set, Map, Queue, Deque, iterators, Comparator |
| `java_concurrency.txt` | Threads, synchronization, locks, Executors, CompletableFuture |
| `java_jvm.txt` | JVM internals, GC algorithms, classloading, bytecode |
| `java_advanced_anki_expanded.txt` | Advanced / expanded coverage across all Java topics |

### Cpp/
| File | Scope |
|------|-------|
| `cpp_basics.txt` | Syntax, types, control flow, functions |
| `cpp_oop.txt` | Classes, inheritance, virtual dispatch, RTTI |
| `cpp_memory.txt` | Pointers, references, RAII, smart pointers |
| `cpp_stl.txt` | Containers, iterators, algorithms, `<functional>` |
| `cpp_modern.txt` | C++11/14/17/20 features: lambdas, move semantics, concepts |

### Android/
| File | Scope |
|------|-------|
| `android_fundamentals.txt` | Activities, Intents, Manifest, lifecycle |
| `android_ui.txt` | Views, layouts, RecyclerView, Material components |
| `android_jetpack.txt` | ViewModel, LiveData, Room, Navigation, WorkManager |
| `android_kotlin.txt` | Kotlin idioms, coroutines, Flow, extension functions |
| `android_architecture.txt` | MVVM, Clean Architecture, Dependency Injection (Hilt) |

---

## Common Tasks

### Adding new cards to an existing deck
1. Open the relevant `.txt` file.
2. Place the new card(s) after a logical section comment or at the end of the file.
3. Use the exact tab-separated format: `Front\tBack`.

### Creating a new deck file
1. Name the file using the pattern `<topic>_<subtopic>.txt` (snake_case, lowercase).
2. Start the file with a comment header:
   ```
   # <Topic> — <Subtopic>
   # Format: Front[TAB]Back
   ```
3. Add the file to the relevant subfolder's `README.md` table.

### Checking for duplicates
Search within a file for an existing front before adding a card:
```
grep -i "keyword" Java/java_basics.txt
```

---

## What NOT to Do

- Do **not** use commas or pipes as separators — Anki expects tabs.
- Do **not** add trailing whitespace after the back text.
- Do **not** include HTML line breaks (`<br>`) unless the card genuinely needs multi-line formatting.
- Do **not** create separate summary or changelog markdown files after edits unless explicitly requested.
