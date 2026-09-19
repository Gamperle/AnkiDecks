# C Code Riddles

Predict-the-output riddles that test knowledge of C's *unique/surprising* language properties — not general "what is X" recall, but "read this snippet, guess the output, then check why." Complements the definitional decks in `../` (e.g. `c_code_understanding.txt`, `c_spot_the_bug.txt`).

Because so much of C's surprise budget is spent on **undefined** and **implementation-defined** behavior, every card is explicit about which category applies — "this specific value" (defined), "this is what most compilers do, but the standard doesn't promise it" (implementation-defined/typical), or "genuinely anything could happen, including a different answer at a different optimization level" (UB).

## Format

```
What does this print? `code`[TAB]Output/behavior — explanation
```

Same tab-separated, `#`-comment-ignored format as the rest of the repo (see the root `CLAUDE.md`).

## Decks

| File | Focus |
|------|-------|
| `c_riddles_integers_overflow.txt` | Signed overflow (UB) vs unsigned wraparound (defined), signed/unsigned comparison traps, `sizeof`-driven underflow, integer promotion, out-of-range shifts, truncating division |
| `c_riddles_pointers_arrays.txt` | Array decay & `sizeof` traps, pointer arithmetic scaling, the `i[a]`/`a[i]` equivalence, row-major layout, dangling pointers, one-past-the-end rules, pointer comparison UB |
| `c_riddles_operators_precedence.txt` | `&` vs `==` precedence, the comma operator, ternary common-type promotion, sequence-point violations (contrasted with Java's defined order), classic macro double-evaluation and missing-parens bugs |
| `c_riddles_structs_unions_preprocessor.txt` | Struct padding/reordering, flexible array members, union type punning, bit-field portability, enum auto-increment, token pasting (`##`) and stringizing (`#`) |

Targets C99/C11 semantics unless a card says otherwise (e.g. C23 notes are called out inline where relevant).
