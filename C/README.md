# C Anki Decks

Flashcard decks covering C programming — code understanding, standard library usage, and bug-spotting exercises.

## Format

```
Front (question or term)[TAB]Back (answer or definition)
```

---

## Planned Decks

| File | Description |
|------|-------------|
| `c_code_understanding.txt` | Reading and interpreting C code: types, pointers, memory, UB, expressions, compilation |
| `c_stdlib_usage.txt` | Standard library function usage examples across all major headers |
| `c_spot_the_bug.txt` | Snippets with bugs or wrong behavior to identify and explain |

---

# Topic Index

---

## 1. C Code Understanding

> Cards ask you to read, trace, or explain a code snippet — predict output, identify behavior, or describe what a construct does.

---

### Beginner

#### 1.1 Variables, Types & Expressions
- Primitive types: `char`, `short`, `int`, `long`, `float`, `double`, `unsigned` variants
- Integer promotion rules in expressions
- Signed vs unsigned overflow behavior
- Implicit type conversions and pitfalls (`int` + `unsigned int`)
- Size of types: `sizeof` operator, platform differences, `stdint.h` fixed-width types
- Constants: `#define` macros vs `const` variables
- Literals: integer suffixes (`u`, `l`, `ul`, `ll`), hex (`0x`), octal (`0`), binary (`0b`)
- Difference between `=` (assignment) and `==` (comparison) in conditions
- Short-circuit evaluation of `&&` and `||`
- Operator precedence gotchas: `*p++` vs `(*p)++`

#### 1.2 Pointers & Memory
- Pointer declaration syntax: `int *p`, `int* p`, `int * p` — all equivalent
- Pointer arithmetic: `p + 1` advances by `sizeof(*p)` bytes
- `NULL` pointer, dereferencing `NULL` → undefined behavior
- Pointer to pointer: `int **pp`
- `const` correctness: `const int *p` vs `int * const p` vs `const int * const p`
- Array decay: array name used as pointer to its first element
- Difference between `array[i]` and `*(array + i)`
- Stack vs heap allocation: automatic variables vs `malloc`/`free`
- Dangling pointer: using a pointer after `free` or after local variable goes out of scope
- Memory leak: allocated memory never freed
- `void *`: generic pointer, requires cast before dereferencing

#### 1.3 Control Flow & Functions
- `for`, `while`, `do-while` — when each is appropriate
- `break` and `continue` inside nested loops
- `switch` fall-through: intentional vs accidental, `[[fallthrough]]` annotation
- Function declaration vs definition vs prototype
- Pass by value: C always passes arguments by value; pass address to modify caller's variable
- Returning a pointer to a local variable → undefined behavior (dangling pointer)
- Recursive functions: call stack growth, stack overflow risk
- `static` local variables: initialized once, persist across calls
- Variadic functions: `...` parameter, `<stdarg.h>` macros

#### 1.4 Structs & Unions
- `struct` definition, member access with `.` and `->`
- Struct padding and alignment: `sizeof(struct)` may be larger than sum of members
- Designated initializers: `struct Point p = {.x = 1, .y = 2};`
- `union`: all members share same memory, only one active at a time
- `typedef struct` pattern and anonymous structs
- Bit fields: `unsigned int flag : 1;`
- Forward declaration of structs (opaque pointer pattern)

### Intermediate

#### 1.5 Pointers — Advanced Patterns
- Function pointers: declaration, assignment, calling syntax
- Array of function pointers (dispatch table / vtable simulation)
- Pointer to array: `int (*p)[5]` vs `int *p`
- `restrict` keyword: promise of no aliasing, enables compiler optimization
- `volatile` keyword: prevents compiler from caching memory-mapped or signal-modified values
- Pointer aliasing and strict aliasing rule (UB when casting unrelated pointer types)
- `memcpy` vs `memmove`: overlapping regions
- Flexible array member: last struct member as `int data[];`

#### 1.6 Undefined Behavior & Pitfalls
- Reading uninitialized variables
- Signed integer overflow (UB) vs unsigned wraparound (defined)
- Out-of-bounds array access
- Using `%d` with `unsigned int` or `size_t` → format mismatch UB
- Modifying a string literal: `char *s = "hello"; s[0] = 'H';` → UB
- Sequence points: `i++ + i++` is UB
- Comparing pointers to different objects with `<`/`>`
- `setjmp`/`longjmp` interaction with local variables

#### 1.7 Preprocessor & Compilation
- `#include` guards vs `#pragma once`
- Macro pitfalls: missing parentheses, double evaluation (`MAX(a++, b++)`)
- `#ifdef`, `#ifndef`, `#if defined(...)` for conditional compilation
- Predefined macros: `__FILE__`, `__LINE__`, `__func__`, `__DATE__`, `__TIME__`
- `static` at file scope: internal linkage (not visible outside translation unit)
- `extern` keyword: declaration without definition
- Compilation pipeline: preprocessing → compilation → assembly → linking
- `inline` functions vs function-like macros

### Pro

#### 1.8 Memory Model & Low-Level
- `_Atomic` and `<stdatomic.h>`: lock-free operations, memory order
- `_Alignas` / `_Alignof`: alignment control and query
- `_Generic` selection (C11 type-generic macros)
- `_Static_assert`: compile-time assertions
- Endianness: big-endian vs little-endian, detecting at runtime
- Type-punning via `union` (the only defined way in C)
- Calling conventions and ABI basics
- Position-independent code (PIC) and shared libraries

---

## 2. Standard Library Usage Examples

### 2.1 `<stdio.h>` — I/O

#### Functions
- `printf` / `fprintf` / `sprintf` / `snprintf` — formatted output
- `scanf` / `fscanf` / `sscanf` — formatted input
- `fopen` / `fclose` — file open/close, mode strings (`"r"`, `"w"`, `"a"`, `"rb"`, etc.)
- `fread` / `fwrite` — binary I/O
- `fgets` / `fputs` — line-oriented text I/O
- `fgetc` / `fputc` / `ungetc` — character I/O
- `fseek` / `ftell` / `rewind` — file position
- `feof` / `ferror` / `clearerr` — stream state
- `tmpfile` / `tmpnam` — temporary files
- `perror` — print error message from `errno`
- `remove` / `rename` — file management

#### Usage Patterns
- Safe string writing: always prefer `snprintf` over `sprintf`
- Reading a whole file into a buffer with `fread`
- Checking `fgets` return value for EOF detection
- Format specifiers: `%d`, `%u`, `%ld`, `%zu`, `%f`, `%lf`, `%s`, `%p`, `%x`
- Width and precision: `%10.2f`, `%-20s`, `%05d`

### 2.2 `<stdlib.h>` — Memory, Conversion, Process

#### Functions
- `malloc` / `calloc` / `realloc` / `free` — heap memory management
- `atoi` / `atol` / `atof` — string to number (no error detection)
- `strtol` / `strtoul` / `strtod` — string to number with error detection
- `abs` / `labs` / `llabs` — absolute value
- `div` / `ldiv` — integer division with quotient and remainder
- `rand` / `srand` — pseudo-random numbers
- `exit` / `_Exit` / `atexit` — program termination and cleanup hooks
- `abort` — abnormal termination
- `getenv` — environment variable lookup
- `system` — execute shell command (use with caution)
- `qsort` — general-purpose sort with comparator callback
- `bsearch` — binary search on sorted array
- `aligned_alloc` — allocation with specified alignment (C11)

#### Usage Patterns
- Checking `malloc` return value for `NULL` before use
- `calloc` to zero-initialize: `calloc(n, sizeof(int))`
- `realloc` pattern: assign to temporary pointer to detect failure
- `qsort` comparator signature: `int cmp(const void *a, const void *b)`
- Prefer `strtol` over `atoi` for robust integer parsing

### 2.3 `<string.h>` — String & Memory Operations

#### Functions
- `strlen` — string length (not counting `\0`)
- `strcpy` / `strncpy` — string copy (prefer `strncpy` or `strlcpy`)
- `strcat` / `strncat` — string concatenation
- `strcmp` / `strncmp` — string comparison
- `strchr` / `strrchr` — find character in string
- `strstr` — find substring
- `strtok` / `strtok_r` — tokenize string (modifies original!)
- `memset` — fill memory block with a byte value
- `memcpy` — copy non-overlapping memory blocks
- `memmove` — copy potentially overlapping memory blocks
- `memcmp` — compare memory blocks
- `memchr` — find byte in memory block
- `strdup` / `strndup` — duplicate string (POSIX; allocates with `malloc`)

#### Usage Patterns
- Null terminator: always ensure destination buffer has room for `\0`
- `strtok` is not reentrant — use `strtok_r` in multi-threaded or nested calls
- `memset` to zero a struct: `memset(&s, 0, sizeof(s))`
- Safer alternative: `strlcpy` / `strlcat` (BSD/POSIX) or `strncpy` + manual null-termination

### 2.4 `<math.h>` — Mathematical Functions

#### Functions
- `sqrt`, `cbrt` — square root, cube root
- `pow` — raise to a power
- `fabs` — absolute value for `double`
- `ceil`, `floor`, `round`, `trunc` — rounding
- `fmod` — floating-point remainder
- `exp`, `log`, `log2`, `log10` — exponential and logarithm
- `sin`, `cos`, `tan`, `asin`, `acos`, `atan`, `atan2` — trigonometry
- `isnan`, `isinf`, `isfinite` — floating-point classification macros
- `HUGE_VAL`, `NAN`, `INFINITY` — special values
- Link with `-lm` on most UNIX systems

### 2.5 `<ctype.h>` — Character Classification & Conversion

#### Functions
- `isalpha`, `isdigit`, `isalnum` — letter, digit, alphanumeric
- `isspace` — whitespace (space, tab, newline, etc.)
- `isupper`, `islower` — case check
- `toupper`, `tolower` — case conversion
- `isprint`, `ispunct`, `iscntrl` — printable, punctuation, control characters
- Input must be `unsigned char` cast or `EOF` to avoid UB with negative `char` values

### 2.6 `<time.h>` — Date & Time

#### Functions
- `time` — current calendar time as `time_t`
- `difftime` — difference between two `time_t` values in seconds
- `clock` — processor time used by program (`CLOCKS_PER_SEC`)
- `localtime` / `gmtime` — convert `time_t` to `struct tm`
- `mktime` — convert `struct tm` to `time_t`
- `strftime` — format `struct tm` as string
- `asctime` / `ctime` — deprecated formatted time strings

### 2.7 `<errno.h>` & `<assert.h>` — Error Handling & Debugging

#### Functions / Macros
- `errno` — thread-local error code set by failing library functions
- Common error codes: `EINVAL`, `ENOMEM`, `ENOENT`, `EACCES`, `ERANGE`, `EOVERFLOW`
- `strerror` (from `<string.h>`) — human-readable error message for `errno`
- `perror` (from `<stdio.h>`) — print `errno` message with custom prefix
- `assert(expr)` — abort with message if `expr` is false; disabled by `NDEBUG`
- `static_assert` / `_Static_assert` — compile-time assertion (C11)

### 2.8 `<stdint.h>` & `<inttypes.h>` — Portable Integer Types

#### Types
- `int8_t`, `uint8_t`, `int16_t`, `uint16_t`, `int32_t`, `uint32_t`, `int64_t`, `uint64_t`
- `intptr_t`, `uintptr_t` — integer large enough to hold a pointer
- `size_t`, `ptrdiff_t`, `ssize_t`
- `INT8_MIN`, `INT8_MAX`, `UINT32_MAX`, etc. — range constants
- `PRId32`, `PRIu64`, `PRIx64` — `printf`/`scanf` format macros from `<inttypes.h>`

### 2.9 `<signal.h>` — Signal Handling

#### Functions / Macros
- `signal` — register signal handler (`SIG_DFL`, `SIG_IGN`, or function pointer)
- `raise` — send signal to current process
- Common signals: `SIGINT`, `SIGTERM`, `SIGSEGV`, `SIGFPE`, `SIGABRT`, `SIGHUP`
- Async-signal-safe functions: only a small set of functions are safe to call inside handlers
- `sigaction` (POSIX) — more reliable signal registration than `signal`

### 2.10 `<setjmp.h>` — Non-local Jumps

#### Functions / Macros
- `setjmp` — save execution context (returns 0 on first call)
- `longjmp` — restore context saved by `setjmp` (never returns to `longjmp` call site)
- Use case: error recovery without unwinding the stack manually
- Pitfall: local variables modified after `setjmp` may have indeterminate values unless `volatile`

---

## 3. Spot the Bug — Errors & Wrong Behavior

Each card shows a short C snippet. The task is to identify what is wrong and explain the correct fix.

### 3.1 Memory Errors

- **Use after free**: calling `free(p)` then dereferencing `p`
- **Double free**: calling `free(p)` twice on the same pointer without nulling it
- **Uninitialized pointer dereference**: `int *p; *p = 5;` — `p` holds garbage
- **Stack buffer overflow**: writing past the end of a local array
- **Heap buffer overflow**: `malloc(n)` then writing `n+1` bytes
- **Memory leak**: `malloc` result never `free`d, e.g. early return before `free`
- **`realloc` failure not handled**: `p = realloc(p, n)` — if `realloc` returns `NULL`, original pointer is lost
- **Returning address of local variable**: `return &local_var;` — dangling pointer
- **Off-by-one in array**: loop runs `i <= n` instead of `i < n`
- **`sizeof` on a decayed pointer**: `sizeof(arr)` inside a function receiving `int *arr` gives pointer size, not array size

### 3.2 String & Format Bugs

- **`strcpy` buffer overflow**: destination too small for source string including `\0`
- **Missing null terminator**: `strncpy` pads with zeros only up to `n` — destination may not be null-terminated if source is exactly `n` chars
- **`gets` usage**: always unsafe — no bounds check; use `fgets` instead
- **Format string injection**: `printf(user_input)` — user controls the format; use `printf("%s", user_input)`
- **`scanf("%s", buf)`**: reads unbounded input; use `scanf("%255s", buf)`
- **Mismatched `printf` format**: `printf("%d", (long)x)` — should be `%ld`; `printf("%d", (unsigned)x)` — should be `%u`
- **`sprintf` overflow**: writing formatted output into a fixed buffer without size limit; use `snprintf`
- **`strtok` on a string literal**: `strtok("hello world", " ")` — modifies read-only memory (UB)
- **Comparing strings with `==`**: `if (s1 == s2)` compares pointer addresses, not content; use `strcmp`

### 3.3 Pointer & Type Bugs

- **Wrong pointer arithmetic units**: `char *p; p += sizeof(int);` — advances by 4 bytes, not 1; just do `p += 1`
- **Casting `int *` to `char *` and violating alignment**: reading a `short` from an unaligned `char` buffer via cast
- **`void *` arithmetic**: `void *p; p++;` — illegal in standard C (GCC extension only)
- **Incorrect `const` cast**: casting away `const` then modifying — UB if object was originally `const`
- **Pointer comparison across objects**: `ptr_a < ptr_b` when they point into different objects — undefined behavior
- **Null pointer dereference**: forgetting to check `malloc`/`fopen` return before use
- **Integer to pointer cast without `intptr_t`**: `int *p = (int *)42;` — may not round-trip on all platforms
- **`sizeof` applied to expression vs type confusion**: `sizeof(int *)` vs `sizeof(int)` mix-up

### 3.4 Integer & Arithmetic Bugs

- **Signed integer overflow**: `int x = INT_MAX; x++;` — undefined behavior (not guaranteed to wrap)
- **Unsigned wraparound misread as overflow**: `unsigned x = 0; x--;` gives `UINT_MAX`, not a crash
- **Truncation on assignment**: storing a `long` result into `int` silently truncates
- **Sign extension pitfall**: `char c = 0xFF; int i = c;` — may sign-extend to `-1` on platforms with signed `char`
- **Division by zero**: no check before `/` or `%` with a variable denominator
- **Shift by negative or ≥ width**: `x << 32` when `x` is 32-bit — undefined behavior
- **Left shift of negative value**: `int x = -1; x << 1;` — undefined behavior
- **Comparison of signed and unsigned**: `int n = -1; if (n < sizeof(arr))` — `-1` converted to huge unsigned value

### 3.5 Control Flow Bugs

- **Missing `break` in `switch`**: unintended fall-through executes next case body
- **Semicolon after `if`/`for`**: `if (cond);` — body is empty, following block always runs
- **Assignment in condition**: `if (x = 0)` instead of `if (x == 0)` — always false, modifies `x`
- **Infinite loop on `fgetc`**: storing result of `fgetc` in `char` instead of `int` — `EOF` (-1) truncated to `0xFF` never equals `EOF`
- **Loop variable shadowing**: declaring `int i` inside a nested block hides outer loop `i`
- **`continue` in `do-while`**: `continue` jumps to the condition check, not to the top — sometimes surprising

### 3.6 Preprocessor & Macro Bugs

- **Macro without parentheses**: `#define SQUARE(x) x*x` → `SQUARE(a+1)` expands to `a+1*a+1`
- **Double evaluation in macro**: `#define MAX(a,b) ((a)>(b)?(a):(b))` → `MAX(i++, j++)` increments twice
- **Missing include guard**: header included multiple times causes redefinition errors
- **Macro name collision with standard library**: `#define max(a,b)` clashes when `<sys/param.h>` also defines it
- **`#define` used as a type**: `#define BOOL int` then comparing with `true`/`false` — inconsistency with `<stdbool.h>`
- **Multiline macro without backslash continuation**: last line missing `\` causes syntax error

### 3.7 Resource & File Handling Bugs

- **File not closed on error path**: early `return` before `fclose` leaks file descriptor
- **Ignoring `fclose` return value**: `fclose` can fail (e.g. flushing buffered writes) — error silently lost
- **Using `tmpnam` without checking uniqueness race**: TOCTOU between name generation and file creation; use `tmpfile` or `mkstemp`
- **`fgets` return value ignored**: loop continues on EOF/error with stale buffer contents
- **Reading binary file in text mode**: `fopen("file", "r")` on Windows translates `\r\n` — use `"rb"` for binary
- **`system()` with unsanitized input**: command injection if user data is concatenated into the shell string

### 3.8 Concurrency & Signal Bugs

- **Non-atomic flag check**: `while (!done)` with `done` set in a signal handler — `done` must be `volatile sig_atomic_t`
- **Non-async-signal-safe function in handler**: calling `printf` or `malloc` inside a signal handler — undefined behavior
- **`setjmp` variable clobbering**: non-`volatile` local modified between `setjmp` and `longjmp` has indeterminate value
- **Shared global mutated without synchronization**: two threads writing the same global without a mutex or `_Atomic`

---

## Difficulty Levels

| Level | Description |
|-------|-------------|
| Beginner | Syntax, types, basic pointers, common stdlib functions |
| Intermediate | Pointer patterns, UB, preprocessor, deeper stdlib usage |
| Pro | Memory model, atomics, ABI, advanced idioms |
