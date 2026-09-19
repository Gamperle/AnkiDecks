# Java Code Riddles

Predict-the-output riddles that test knowledge of Java's *unique/surprising* language properties — not general "what is X" recall, but "read this snippet, guess the output, then check why." Complements the definitional decks in `../` (e.g. `java_basics.txt`, `java_oop.txt`).

## Format

```
What does this print? `code`[TAB]Output/behavior — explanation
```

Same tab-separated, `#`-comment-ignored format as the rest of the repo (see the root `CLAUDE.md`). Each card's front is a self-contained snippet; the back gives the exact output (or compile error / runtime exception) plus the language rule that explains it.

## Decks

| File | Focus |
|------|-------|
| `java_riddles_numbers_types.txt` | Integer overflow/wraparound, the `Integer` cache, autoboxing NPEs, char/mixed arithmetic, division/modulo/shift semantics, Java's *defined* evaluation order |
| `java_riddles_strings_objects.txt` | String pool & interning, `==` vs `.equals()`, the equals/hashCode contract, records vs plain classes, `instanceof`/`switch` pattern matching, text blocks |
| `java_riddles_control_flow_oop.txt` | `finally` vs `return`, try-with-resources suppressed exceptions, static dispatch vs field hiding, constructors calling overridable methods, overload resolution order, labeled loops |
| `java_riddles_collections_concurrency.txt` | `ConcurrentModificationException`, mutable map keys, immutable vs fixed-size vs unmodifiable-view collections, race conditions, `volatile` vs atomicity, lock reentrancy |

All cards target **Java 17+** (a couple of riddles note newer syntax, e.g. Java 21 pattern-matching `switch`, explicitly in the card text).
