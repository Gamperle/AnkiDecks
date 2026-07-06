# C Anki Decks

Flashcard decks covering C programming — code understanding, standard library usage, and bug-spotting exercises, with dedicated security-focused coverage woven through all three.

## Format

```
Front (question or term)[TAB]Back (answer or definition)
```

---

## Planned Decks

| File | Description |
|------|-------------|
| `c_code_understanding.txt` | Reading and interpreting C code: types, pointers, memory, UB, expressions, compilation, and security-relevant code patterns |
| `c_stdlib_usage.txt` | Standard library function usage examples across all major headers, including secure-coding alternatives to unsafe functions |
| `c_spot_the_bug.txt` | Snippets with bugs or wrong behavior to identify and explain, including exploitable security vulnerabilities |
| `c_systems_embedded.txt` | Beyond the language: threading depth, embedded/bare-metal conventions, Linux/POSIX systems programming, toolchain, and secure-coding standards |

---

# Topic Index

---

## 1. C Code Understanding

> Cards ask you to read, trace, or explain a code snippet — predict output, identify behavior, or describe what a construct does.

---

### Beginner

#### 1.1 Variables, Types & Expressions
- Primitive types: `char`, `short`, `int`, `long`, `long long`, `float`, `double`, `long double`, `unsigned` variants
- Integer promotion rules in expressions ("usual arithmetic conversions")
- Signed vs unsigned overflow behavior
- Implicit type conversions and pitfalls (`int` + `unsigned int`)
- Size of types: `sizeof` operator, platform differences, `stdint.h` fixed-width types
- Constants: `#define` macros vs `const` variables vs `enum` constants
- `typedef`: creating type aliases, readability vs hiding pointer types
- Literals: integer suffixes (`u`, `l`, `ul`, `ll`), hex (`0x`), octal (`0`), binary (`0b`), floating suffixes (`f`, `l`)
- Character literals vs string literals: `'a'` (int/char) vs `"a"` (`char[2]`)
- Compound literals: `(int[]){1, 2, 3}`, `(struct Point){.x=1}` — anonymous objects with automatic storage
- lvalues vs rvalues: what can appear on the left of `=`
- Difference between `=` (assignment) and `==` (comparison) in conditions
- Short-circuit evaluation of `&&` and `||`
- Comma operator vs comma as argument separator
- Ternary operator `?:` — type of the result, common misuse
- Operator precedence gotchas: `*p++` vs `(*p)++`, `a & b == c` (bitwise AND binds looser than `==`)
- Bitwise operators: `&`, `|`, `^`, `~`, `<<`, `>>` — common bit-flag idioms (set/clear/toggle/test a bit)
- `sizeof` is evaluated at compile time (except VLAs) and its operand is not executed

#### 1.2 Storage Classes, Scope & Lifetime
- Storage-class specifiers: `auto`, `register`, `static`, `extern`, `_Thread_local`
- Block scope vs file scope vs function-prototype scope
- Storage duration: automatic, static, thread, and allocated
- `static` local variable: single instance, initialized once, retains value across calls
- `static` at file scope vs `extern`: internal vs external linkage
- Uninitialized static/global variables are zero-initialized; uninitialized automatic variables are not
- Lifetime vs scope: a `static` local is in scope only in its block but lives for the whole program
- `register` is largely a no-op hint today; you cannot take the address of a `register` variable

#### 1.3 Pointers & Memory
- Pointer declaration syntax: `int *p`, `int* p`, `int * p` — all equivalent
- Pointer arithmetic: `p + 1` advances by `sizeof(*p)` bytes
- `NULL` pointer, dereferencing `NULL` → undefined behavior
- Pointer to pointer: `int **pp`
- `const` correctness: `const int *p` vs `int * const p` vs `const int * const p`
- Array decay: array name used as pointer to its first element
- Difference between `array[i]` and `*(array + i)` and `i[array]` (legal but obscure)
- Stack vs heap allocation: automatic variables vs `malloc`/`free`
- Dangling pointer: using a pointer after `free` or after local variable goes out of scope
- Memory leak: allocated memory never freed
- `void *`: generic pointer, requires cast before dereferencing (implicit in C, required in C++)
- Null-pointer-vs-uninitialized-pointer distinction: an uninitialized pointer is not guaranteed to be `NULL`
- Pointer equality and identity vs the objects they point to

#### 1.4 Arrays & Strings
- Array declaration, initialization, and default zero-fill for partially initialized arrays
- Designated array initializers: `int a[10] = {[0]=1, [9]=5};`
- Multidimensional arrays: `int m[3][4]` — row-major memory layout
- Array of pointers vs pointer to array: `char *argv[]` vs `char (*p)[N]`
- Variable-length arrays (VLAs): `int a[n]` with runtime `n` — stack cost and portability caveats (optional since C11)
- C strings are `\0`-terminated `char` arrays — there is no built-in "length" tracked at runtime
- String literals are stored in read-only memory and may be shared/pooled by the compiler
- `char buf[N]` vs `char *buf = "literal"` — the former is mutable and owns storage, the latter is not
- Passing arrays to functions: they decay to pointers, losing size information
- `sizeof` on a true array (in the defining scope) vs on a decayed pointer parameter
- Command-line arguments: `int main(int argc, char *argv[])`, `argv[argc] == NULL`
- Multi-dimensional array indexing pitfalls: `arr[i][j]` vs `arr[j][i]` cache/layout implications
- Wide characters and strings: `wchar_t`, `L"..."`, `<wchar.h>` basics; UTF-8 stored in plain `char[]`

#### 1.5 Control Flow & Functions
- `for`, `while`, `do-while` — when each is appropriate
- `break` and `continue` inside nested loops
- `switch` fall-through: intentional vs accidental, `[[fallthrough]]` annotation
- Function declaration vs definition vs prototype
- Empty parameter list `f()` (unspecified args, legacy) vs `f(void)` (explicitly no args)
- Pass by value: C always passes arguments by value; pass address to modify caller's variable
- Returning a pointer to a local variable → undefined behavior (dangling pointer)
- Recursive functions: call stack growth, stack overflow risk
- `static` local variables: initialized once, persist across calls
- Variadic functions: `...` parameter, `<stdarg.h>` macros (`va_list`, `va_start`, `va_arg`, `va_end`)
- Default argument promotion for variadics: `float` → `double`, small integer types → `int`
- Function-like macros vs true functions: evaluation semantics differ
- `goto` and labels: legitimate uses (single-point cleanup, breaking nested loops) vs spaghetti code
- `_Noreturn` / `noreturn` functions (e.g. wrappers around `exit`/`abort`)

#### 1.6 Structs, Unions & Enums
- `struct` definition, member access with `.` and `->`
- Struct padding and alignment: `sizeof(struct)` may be larger than sum of members
- Reordering members to reduce padding (structure packing optimization)
- Designated initializers: `struct Point p = {.x = 1, .y = 2};`
- `union`: all members share same memory, only one active at a time
- `typedef struct` pattern and anonymous structs/unions
- `enum`: named integer constants, implicit incrementing values, explicit assignment, underlying type
- Using `enum` for state machines and flag sets; scoping caveats (enum constants live in the enclosing scope)
- Bit fields: `unsigned int flag : 1;` — implementation-defined layout, portability caveats
- Forward declaration of structs (opaque pointer pattern) for encapsulation
- Self-referential structs (linked lists, trees) via pointer members
- Nested structs and arrays of structs, initialization syntax
- `offsetof` (from `<stddef.h>`) to compute a member's byte offset

### Intermediate

#### 1.7 Pointers — Advanced Patterns
- Function pointers: declaration, assignment, calling syntax
- Array of function pointers (dispatch table / vtable simulation)
- Pointer to array: `int (*p)[5]` vs `int *p`
- `restrict` keyword: promise of no aliasing, enables compiler optimization
- `volatile` keyword: prevents compiler from caching memory-mapped or signal-modified values
- Pointer aliasing and strict aliasing rule (UB when casting unrelated pointer types)
- `memcpy` vs `memmove`: overlapping regions
- Flexible array member: last struct member as `int data[];`
- Opaque handles and PIMPL-style encapsulation in C libraries
- Double pointers for output parameters: `int foo(int **out)`
- Pointer-to-`const`-pointer patterns in read-only iteration APIs
- Callback-based APIs: passing a `void *user_data` alongside a function pointer

#### 1.8 Undefined, Unspecified & Implementation-Defined Behavior
- The three distinct categories: UB (anything can happen), unspecified (a valid but unpredictable choice), implementation-defined (documented per-compiler)
- Reading uninitialized variables (UB)
- Signed integer overflow (UB) vs unsigned wraparound (defined, modular arithmetic)
- Out-of-bounds array access (read and write)
- Using `%d` with `unsigned int` or `size_t` → format mismatch UB
- Modifying a string literal: `char *s = "hello"; s[0] = 'H';` → UB
- Sequence points: `i++ + i++` and `a[i] = i++` are UB (indeterminate order/multiple modification)
- Unspecified evaluation order of function arguments: `f(g(), h())`
- Comparing pointers to different objects with `<`/`>` (UB unless same array/one-past-end)
- `setjmp`/`longjmp` interaction with local variables not marked `volatile`
- Strict aliasing violations via type-punned pointers
- Null pointer arithmetic and null pointer comparison edge cases
- Calling a function through an incompatible function pointer type
- Returning from a non-`void` function without a `return` statement (UB if the value is used)
- Multiple unsequenced side effects on the same object in one expression
- Implementation-defined: signedness of plain `char`, right-shift of negative values, integer representation

#### 1.9 Preprocessor & Compilation
- `#include` guards vs `#pragma once`
- Macro pitfalls: missing parentheses, double evaluation (`MAX(a++, b++)`)
- `#ifdef`, `#ifndef`, `#if defined(...)` for conditional compilation
- Predefined macros: `__FILE__`, `__LINE__`, `__func__`, `__DATE__`, `__TIME__`, `__STDC_VERSION__`
- `static` at file scope: internal linkage (not visible outside translation unit)
- `extern` keyword: declaration without definition
- Compilation pipeline: preprocessing → compilation → assembly → linking
- `inline` functions vs function-like macros
- Token pasting (`##`) and stringizing (`#`) in macros
- Variadic macros: `#define LOG(fmt, ...) printf(fmt, __VA_ARGS__)`
- `#error` and `#pragma` directives
- Conditional compilation for platform/feature detection (`#if defined(_WIN32)`, feature-test macros)

#### 1.10 Multi-File Programs, Linkage & Build
- Header files vs source files: declarations vs definitions
- Internal linkage (`static`) vs external linkage (default for functions/globals) vs no linkage (locals)
- One Definition Rule equivalent in C: a function/object may be defined once across all translation units
- `extern` variable declarations in headers with a single definition in one `.c` file
- Tentative definitions and common symbols
- Separate compilation: compiling `.c` files independently into `.o`/`.obj`, then linking
- Makefiles / build systems: targets, dependencies, incremental builds (conceptual, not syntax-heavy)
- Static libraries (`.a`/`.lib`) vs shared/dynamic libraries (`.so`/`.dll`) — link time vs load/run time resolution
- Symbol visibility and name mangling differences vs C++ (`extern "C"` linkage for interop)
- Circular header dependencies and forward declarations to break them
- Version compatibility: ABI stability when changing struct layouts in a shared library

#### 1.11 Error-Handling Idioms
- Return-code conventions: `0`/negative-on-error, `-1` + `errno`, or a dedicated status enum
- The `errno` pattern: set to 0 before a call, check after failure only
- Single-exit cleanup with `goto cleanup;` to free resources on every error path
- Output-parameter + boolean-success pattern: `bool parse(const char *s, int *out)`
- Distinguishing "valid result that looks like an error" from real errors (`strtol` returning 0 vs failure)
- Propagating errors up a call stack without exceptions (C has none)
- Resource-acquisition ordering so cleanup can unwind in reverse

#### 1.12 Security-Relevant Code Patterns (Reading & Recognition)
- Recognizing an unbounded copy into a fixed-size buffer from a code snippet (`strcpy`, `gets`, manual loop without bound)
- Spotting user-controlled length values used directly in `malloc`/array indexing without validation
- Identifying a format string that originates from user input rather than a literal
- Recognizing trust boundaries in code: where does external input (argv, stdin, files, network, env vars) first get used unchecked?
- Identifying integer values used as sizes/lengths that could overflow before an allocation
- Spotting missing bounds checks in loops that copy or index into arrays with attacker-influenced indices
- Recognizing a signed length compared with `<` against a max but later used as an unsigned size
- Recognizing privilege-sensitive calls (`setuid`, `system`, `exec*`, `popen`) and what happens if their return value or preconditions are ignored
- Identifying where a `free`d pointer might still be reachable through another alias (use-after-free)
- Spotting a buffer that is read/sent back to a caller without being fully initialized (information disclosure)
- Distinguishing a benign array copy from one that is a manual reimplementation of `strcpy`/`memcpy` without the same care
- Reading disassembly/pseudo-code mentally: mapping a stack buffer overflow snippet to "this can overwrite the return address"

### Pro

#### 1.13 Memory Model & Low-Level
- `_Atomic` and `<stdatomic.h>`: lock-free operations, memory order (`memory_order_relaxed`, `_acquire`, `_release`, `_seq_cst`)
- `_Alignas` / `_Alignof`: alignment control and query
- `_Generic` selection (C11 type-generic macros)
- `_Static_assert`: compile-time assertions
- Endianness: big-endian vs little-endian, detecting at runtime
- IEEE 754 floating-point representation: sign/exponent/mantissa, subnormals, signed zero, why `0.1` isn't exact
- Floating-point special values and their propagation: `NaN != NaN`, `Inf` arithmetic, rounding modes
- Type-punning via `union` (the only defined way in C) vs via pointer cast (UB) vs via `memcpy` (defined, portable)
- Calling conventions and ABI basics (register vs stack argument passing, caller/callee-saved registers)
- Position-independent code (PIC) and shared libraries
- Memory-mapped I/O and `volatile` for hardware registers
- Compiler barriers vs memory fences vs `volatile` — what each actually guarantees (and doesn't)
- Lock-free data structures: ABA problem, compare-and-swap (`atomic_compare_exchange`)
- Virtual memory basics: pages, the heap/stack/BSS/data/text segments, `mmap`-backed allocations

#### 1.14 Security-Relevant Code Patterns — Advanced / Exploit Mitigations
- Stack layout during a function call: return address, saved frame pointer, local buffers, and why buffer overflows can overwrite the return address
- Stack canaries (`-fstack-protector`): how they detect (not prevent) a stack buffer overflow, and what they don't catch (heap overflows, overwriting adjacent locals before the canary)
- Address Space Layout Randomization (ASLR): why it makes return-to-libc/ROP harder, and how information leaks defeat it
- Data Execution Prevention / W^X (`NX` bit): why classic shellcode-on-the-stack no longer executes, motivating return-oriented programming (ROP)
- `PIE` (position-independent executables) and `RELRO` (`GOT` read-only) as exploit-hardening compiler/linker flags
- Fortify source (`_FORTIFY_SOURCE`, `__builtin___memcpy_chk` etc.): compile-time buffer-size checks inserted automatically for known-size destinations
- Control-Flow Integrity (CFI) concepts: restricting indirect call/jump targets to a valid set
- AddressSanitizer / UndefinedBehaviorSanitizer / Valgrind: how instrumentation detects heap/stack overflows, use-after-free, and UB at runtime during testing
- Safe integer arithmetic helpers (`__builtin_add_overflow` and friends) to detect overflow before it causes a downstream memory bug
- Why "defense in depth" matters: any single mitigation (canary, ASLR, NX) can be bypassed; combined they raise exploitation cost significantly

---

## 2. Standard Library Usage Examples

### 2.1 `<stdio.h>` — I/O

#### Functions
- `printf` / `fprintf` / `sprintf` / `snprintf` — formatted output
- `scanf` / `fscanf` / `sscanf` — formatted input
- `fopen` / `fclose` / `freopen` — file open/close/reopen, mode strings (`"r"`, `"w"`, `"a"`, `"rb"`, `"r+"`, etc.)
- `fread` / `fwrite` — binary I/O
- `fgets` / `fputs` — line-oriented text I/O
- `fgetc` / `fputc` / `ungetc` — character I/O
- `fseek` / `ftell` / `rewind` / `fgetpos` / `fsetpos` — file position
- `feof` / `ferror` / `clearerr` — stream state
- `tmpfile` / `tmpnam` — temporary files (see security notes in 2.16)
- `perror` — print error message from `errno`
- `remove` / `rename` — file management
- `setvbuf` / `setbuf` — controlling stream buffering mode
- `fflush` — force-write buffered output (and its non-portable use on input streams)
- `getline` (POSIX) — dynamically-allocated, bounds-safe line reading

#### Usage Patterns
- Safe string writing: always prefer `snprintf` over `sprintf`
- Reading a whole file into a buffer with `fread`, checking the returned element count
- Checking `fgets` return value (`NULL` on EOF/error) before touching the buffer
- Format specifiers: `%d`, `%u`, `%ld`, `%zu`, `%f`, `%lf`, `%s`, `%p`, `%x`, `%%`
- Width and precision: `%10.2f`, `%-20s`, `%05d`
- Buffering modes: fully buffered (files) vs line buffered (terminal stdout) vs unbuffered (stderr)
- Checking `printf`'s return value (number of characters written, or negative on error)
- Never passing user-controlled data as the format argument (see 2.16 / 3.2 security notes)

### 2.2 `<stdlib.h>` — Memory, Conversion, Process

#### Functions
- `malloc` / `calloc` / `realloc` / `free` — heap memory management
- `atoi` / `atol` / `atof` — string to number (no error detection)
- `strtol` / `strtoul` / `strtod` / `strtoll` / `strtoull` — string to number with error detection
- `abs` / `labs` / `llabs` — absolute value
- `div` / `ldiv` / `lldiv` — integer division with quotient and remainder
- `rand` / `srand` — pseudo-random numbers (not cryptographically secure — see 2.16)
- `exit` / `_Exit` / `atexit` / `quick_exit` — program termination and cleanup hooks
- `abort` — abnormal termination, typically raises `SIGABRT`
- `getenv` / `setenv` / `putenv` / `unsetenv` (POSIX) — environment variable access
- `system` — execute shell command (use with extreme caution — see 3.7/3.9 security notes)
- `qsort` — general-purpose sort with comparator callback
- `bsearch` — binary search on sorted array
- `aligned_alloc` — allocation with specified alignment (C11)
- `mblen` / `mbtowc` / `wctomb` — multibyte/wide character conversions

#### Usage Patterns
- Checking `malloc`/`calloc`/`realloc` return value for `NULL` before use
- `calloc` to zero-initialize: `calloc(n, sizeof(int))` — and why it internally guards against `n * sizeof(int)` overflow, unlike a manual `malloc(n * sizeof(int))`
- `realloc` pattern: assign to a temporary pointer to detect failure without leaking the original block
- `qsort` comparator signature: `int cmp(const void *a, const void *b)`, correct casting of `void *` parameters
- Prefer `strtol`/`strtoul` over `atoi`/`atol` for robust integer parsing with error/overflow detection (`errno == ERANGE`, checking `endptr`)
- Never trust `atoi` on untrusted input — it silently returns 0 on failure with no way to distinguish "0" from "invalid"
- Freeing memory exactly once, and setting the pointer to `NULL` after `free` to make double-free/use-after-free easier to catch

### 2.3 `<string.h>` — String & Memory Operations

#### Functions
- `strlen` — string length (not counting `\0`)
- `strcpy` / `strncpy` — string copy (prefer `strncpy` carefully, or safer alternatives — see 2.16)
- `strcat` / `strncat` — string concatenation
- `strcmp` / `strncmp` — string comparison
- `strchr` / `strrchr` — find character in string
- `strstr` — find substring
- `strpbrk` — find first occurrence of any character from a set
- `strspn` / `strcspn` — length of initial segment matching/not matching a character set
- `strtok` / `strtok_r` — tokenize string (modifies original!)
- `memset` — fill memory block with a byte value
- `memcpy` — copy non-overlapping memory blocks
- `memmove` — copy potentially overlapping memory blocks
- `memcmp` — compare memory blocks (byte-wise, not suitable for constant-time secret comparison — see 2.16)
- `memchr` — find byte in memory block
- `strdup` / `strndup` — duplicate string (POSIX; allocates with `malloc`, must be `free`d)
- `strerror` / `strerror_r` — human-readable error message for an `errno` value

#### Usage Patterns
- Null terminator: always ensure destination buffer has room for `\0`
- `strtok` is not reentrant and mutates its input — use `strtok_r` in multi-threaded or nested-parsing code
- `memset` to zero a struct: `memset(&s, 0, sizeof(s))`
- Safer alternatives: `strlcpy` / `strlcat` (BSD/POSIX, not standard C) or `strncpy` + manual null-termination
- Computing buffer sizes with `sizeof` on the actual array (not a decayed pointer) to avoid off-by-one truncation
- Comparing memory regions of secret data (passwords, MACs, tokens) with `memcmp` leaks timing information — needs a constant-time compare (see 2.16)

### 2.4 `<math.h>` — Mathematical Functions

#### Functions
- `sqrt`, `cbrt` — square root, cube root
- `pow` — raise to a power
- `fabs` — absolute value for `double`
- `ceil`, `floor`, `round`, `trunc`, `nearbyint`, `rint` — rounding variants
- `fmod`, `remainder` — floating-point remainder
- `exp`, `log`, `log2`, `log10`, `expm1`, `log1p` — exponential and logarithm
- `sin`, `cos`, `tan`, `asin`, `acos`, `atan`, `atan2` — trigonometry
- `sinh`, `cosh`, `tanh` — hyperbolic functions
- `isnan`, `isinf`, `isfinite`, `isnormal`, `signbit` — floating-point classification macros
- `HUGE_VAL`, `NAN`, `INFINITY` — special values
- `fma` — fused multiply-add (single rounding, better precision)
- Link with `-lm` on most UNIX systems

#### Usage Patterns
- Checking `errno`/`isnan`/`isinf` after math calls that can fail (domain errors, overflow)
- Floating-point comparison pitfalls: never use `==` directly; compare within an epsilon
- Precision loss from repeated `float` operations vs using `double`

### 2.5 `<ctype.h>` — Character Classification & Conversion

#### Functions
- `isalpha`, `isdigit`, `isalnum` — letter, digit, alphanumeric
- `isspace` — whitespace (space, tab, newline, etc.)
- `isupper`, `islower` — case check
- `toupper`, `tolower` — case conversion
- `isprint`, `ispunct`, `iscntrl` — printable, punctuation, control characters
- `isxdigit` — hexadecimal digit check
- `isgraph` — printable and not a space

#### Usage Patterns
- Input must be cast to `unsigned char` (or be `EOF`) before passing to `is*`/`to*` functions to avoid UB with negative `char` values on platforms where `char` is signed
- Locale sensitivity: these functions' behavior can change under `setlocale`

### 2.6 `<time.h>` — Date & Time

#### Functions
- `time` — current calendar time as `time_t`
- `difftime` — difference between two `time_t` values in seconds
- `clock` — processor time used by program (`CLOCKS_PER_SEC`)
- `localtime` / `localtime_r` / `gmtime` / `gmtime_r` — convert `time_t` to `struct tm` (reentrant variants)
- `mktime` — convert `struct tm` to `time_t`
- `strftime` — format `struct tm` as string
- `asctime` / `ctime` — deprecated, non-reentrant formatted time strings (buffer-overflow-prone with crafted `struct tm`)
- `timespec_get` (C11) — higher-resolution time

#### Usage Patterns
- Prefer reentrant `_r` variants (`localtime_r`, `gmtime_r`) in multi-threaded code — the non-`_r` versions return a pointer to shared static storage
- Never trust `asctime`/`ctime` with attacker-influenced `struct tm` fields — historically a source of buffer overflows

### 2.7 `<errno.h>` & `<assert.h>` — Error Handling & Debugging

#### Functions / Macros
- `errno` — thread-local error code set by failing library functions (only meaningful immediately after a failing call)
- Common error codes: `EINVAL`, `ENOMEM`, `ENOENT`, `EACCES`, `ERANGE`, `EOVERFLOW`, `EEXIST`, `EAGAIN`
- `strerror` (from `<string.h>`) — human-readable error message for `errno`
- `perror` (from `<stdio.h>`) — print `errno` message with custom prefix
- `assert(expr)` — abort with message if `expr` is false; disabled entirely when `NDEBUG` is defined
- `static_assert` / `_Static_assert` — compile-time assertion (C11), no runtime cost

#### Usage Patterns
- Never rely on `assert` for security checks or input validation in release builds — `NDEBUG` strips it silently
- Always check `errno` only after confirming the call actually failed (many functions don't reset `errno` to 0 on success)

### 2.8 `<stddef.h>` — Common Definitions

#### Contents
- `size_t` — unsigned type for sizes and `sizeof` results
- `ptrdiff_t` — signed type for the difference of two pointers
- `NULL` — null pointer constant
- `offsetof(type, member)` — byte offset of a struct member
- `max_align_t` — type with the largest fundamental alignment
- `wchar_t` — wide character type

#### Usage Patterns
- Using `size_t` consistently for lengths/indices to avoid signed/unsigned comparison bugs
- `offsetof` for serialization, container-of idioms, and hardware register maps

### 2.9 `<stdint.h>` & `<inttypes.h>` — Portable Integer Types

#### Types
- `int8_t`, `uint8_t`, `int16_t`, `uint16_t`, `int32_t`, `uint32_t`, `int64_t`, `uint64_t`
- `intptr_t`, `uintptr_t` — integer large enough to hold a pointer
- `size_t`, `ptrdiff_t`, `ssize_t` (POSIX)
- `int_least*_t`, `int_fast*_t` — minimum-width and fastest-width integer types
- `INT8_MIN`, `INT8_MAX`, `UINT32_MAX`, `SIZE_MAX`, etc. — range constants
- `PRId32`, `PRIu64`, `PRIx64`, `SCNd32` — `printf`/`scanf` format macros from `<inttypes.h>`

#### Usage Patterns
- Using `SIZE_MAX` to detect potential overflow before a size computation (`if (n > SIZE_MAX / sizeof(*p)) ...`)
- Preferring fixed-width types for on-disk/network formats where exact size and representation matter

### 2.10 `<stdarg.h>` — Variadic Arguments

#### Macros
- `va_list` — holds the state for iterating variadic arguments
- `va_start(ap, last)` — initialize before reading; `last` is the final named parameter
- `va_arg(ap, type)` — retrieve the next argument as `type`
- `va_copy(dst, src)` — clone a `va_list` (needed to traverse twice)
- `va_end(ap)` — clean up

#### Usage Patterns
- Passing a `va_list` through to `vprintf`/`vsnprintf`/`vfprintf` when writing logging wrappers
- There is no portable way to know the argument count/types — you need a count parameter or a format string sentinel
- Default argument promotions apply, so `va_arg(ap, char)` is wrong — read `int`; read `double`, never `float`

### 2.11 `<signal.h>` — Signal Handling

#### Functions / Macros
- `signal` — register signal handler (`SIG_DFL`, `SIG_IGN`, or function pointer)
- `raise` — send signal to current process
- Common signals: `SIGINT`, `SIGTERM`, `SIGSEGV`, `SIGFPE`, `SIGABRT`, `SIGHUP`, `SIGKILL` (not catchable), `SIGCHLD`
- `sig_atomic_t` — the only type safe to modify in a handler; combine with `volatile`
- Async-signal-safe functions: only a small POSIX-defined set is safe to call inside handlers
- `sigaction` (POSIX) — more reliable, portable signal registration than `signal` (control over masking/re-entry/`SA_RESTART`)
- `sigprocmask` / `sigemptyset` / `sigaddset` — signal mask manipulation

### 2.12 `<setjmp.h>` — Non-local Jumps

#### Functions / Macros
- `setjmp` — save execution context (returns 0 on first call)
- `longjmp` — restore context saved by `setjmp` (never returns to the `longjmp` call site)
- Use case: error recovery without unwinding the stack manually
- Pitfall: local variables modified after `setjmp` may have indeterminate values unless `volatile`

### 2.13 `<stdbool.h>`, `<limits.h>` & `<float.h>` — Booleans & Type Limits

#### Contents
- `<stdbool.h>`: `bool`, `true`, `false` macros (built-in keywords `_Bool`/`true`/`false` since C23)
- `<limits.h>`: `CHAR_BIT`, `INT_MIN`/`INT_MAX`, `LONG_MAX`, `UINT_MAX`, `CHAR_MIN`/`CHAR_MAX` (signedness of plain `char` is implementation-defined)
- `<float.h>`: `FLT_EPSILON`, `DBL_EPSILON`, `FLT_MAX`, `DBL_MIN`, `FLT_RADIX` — floating-point representation limits

#### Usage Patterns
- Using `INT_MAX`/`UINT_MAX` etc. to write portable overflow checks instead of hardcoding magic numbers
- Using `*_EPSILON` for tolerance-based floating point comparisons

### 2.14 Concurrency: `<threads.h>` (C11) & `<pthread.h>` (POSIX)

#### Functions / Types
- C11 `<threads.h>`: `thrd_create`, `thrd_join`, `mtx_t`/`mtx_lock`/`mtx_unlock`, `cnd_t` condition variables, `thread_local`, `call_once`
- POSIX `<pthread.h>`: `pthread_create`, `pthread_join`, `pthread_mutex_t`, `pthread_cond_t`, `pthread_once`, `pthread_rwlock_t`
- `<stdatomic.h>`: `atomic_int`, `atomic_load`/`atomic_store`, `atomic_fetch_add`, memory-order arguments

#### Usage Patterns
- Protecting shared mutable state with a mutex; keeping critical sections small
- Condition variables always used with a predicate loop (`while (!ready) cond_wait(...)`) to handle spurious wakeups
- Preferring `_Atomic`/atomics for simple counters/flags instead of a full mutex
- Consistent lock-ordering to avoid deadlock; avoiding calling unknown callbacks while holding a lock

### 2.15 Specialized & Platform Headers

#### Standard
- `<complex.h>`: `double complex`, `creal`/`cimag`, `cabs`, `I` imaginary unit
- `<fenv.h>`: floating-point exception flags (`FE_DIVBYZERO`, `FE_OVERFLOW`) and rounding-mode control (`fesetround`)
- `<locale.h>`: `setlocale`, `localeconv` — locale-dependent formatting/classification
- `<uchar.h>`: `char16_t`, `char32_t` and UTF conversion functions
- `<wchar.h>` / `<wctype.h>`: wide-string and wide-character classification counterparts

#### POSIX file, process & dynamic loading
- `<unistd.h>`: `fork`, `exec*`, `read`/`write`/`close`/`lseek`, `pipe`, `dup`/`dup2`, `getuid`/`geteuid`, `setuid`/`seteuid`, `access`
- `<fcntl.h>`: `open` with flags (`O_RDONLY`, `O_CREAT`, `O_EXCL`, `O_APPEND`), `O_CLOEXEC`
- `<sys/stat.h>`: `stat`/`fstat`/`lstat`, file mode bits, `mkdir`, `umask`
- `<sys/socket.h>`, `<netinet/in.h>`, `<arpa/inet.h>`: `socket`, `bind`, `listen`, `accept`, `connect`, `send`/`recv`, `htons`/`ntohl`
- `<dlfcn.h>`: `dlopen`, `dlsym`, `dlclose` for runtime dynamic loading
- `wait`/`waitpid` to reap children; real vs effective vs saved UID when reasoning about setuid programs

#### Usage Patterns
- `open(..., O_CREAT | O_EXCL)` for race-free exclusive file creation
- `fork` + `exec*` (with an argv array) instead of `system()` to avoid shell interpretation
- Byte-order conversion (`htons`/`ntohl`) on every integer sent over a socket
- Always checking return values of privilege-related and file-related syscalls — silent failure here is a classic security bug source

### 2.16 Secure Coding — Safer Standard Library Alternatives

#### Guidance
- `gets` was removed from the C standard entirely — always use `fgets` with an explicit buffer size instead
- Prefer `snprintf` over `sprintf`/`strcpy`/`strcat` for anything involving a fixed-size buffer and untrusted or variable-length input
- `strlcpy`/`strlcat` (BSD/POSIX, not in all libcs) guarantee null-termination and take the full buffer size, unlike `strncpy`/`strncat`
- `strncpy` does **not** guarantee null-termination if the source is `>= n` bytes — always manually terminate: `buf[n-1] = '\0';`
- Optional C11 Annex K bounds-checked functions (`strcpy_s`, `sprintf_s`, `memcpy_s`) — availability is spotty; know they exist but don't assume they're present
- `memset_s` (C11 Annex K, optional) / `explicit_bzero` (BSD) / `SecureZeroMemory` (Windows) — zero sensitive memory (passwords, keys) in a way the compiler won't optimize away, unlike a plain `memset` right before `free`
- Constant-time comparison for secrets: a naive `memcmp`/`strcmp` on a MAC or password hash leaks timing information; use a dedicated constant-time compare function
- `rand()`/`srand()` are not cryptographically secure — use a CSPRNG (`arc4random`, `getrandom`, `/dev/urandom`, or a platform crypto API) for anything security-sensitive (tokens, nonces, keys)
- `system()` and `popen()` invoke a shell — never pass unsanitized/untrusted data into the command string; prefer `fork`+`exec*` with an argument array, which avoids shell interpretation entirely
- `tmpnam`/`tmpfile` race conditions: prefer `mkstemp` (POSIX), which atomically creates and opens a uniquely-named file
- Validating and canonicalizing file paths (`realpath`) before use to defeat `../` traversal
- Checking every return value from `malloc`, allocation-adjacent size arithmetic, and privilege-changing calls (`setuid` et al.) — treating these as "can't fail" is a recurring root cause of real-world CVEs
- Using compiler hardening flags as a companion to safe-function usage: `-D_FORTIFY_SOURCE=2`, `-fstack-protector-strong`, `-Wformat -Wformat-security`, `-Wall -Wextra`

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
- **`realloc` failure not handled**: `p = realloc(p, n)` — if `realloc` returns `NULL`, original pointer is lost (and leaked)
- **Returning address of local variable**: `return &local_var;` — dangling pointer
- **Off-by-one in array**: loop runs `i <= n` instead of `i < n`
- **`sizeof` on a decayed pointer**: `sizeof(arr)` inside a function receiving `int *arr` gives pointer size, not array size
- **Freeing memory not obtained from `malloc`**: `free`ing a pointer into the middle of a block, a stack address, or a string literal
- **Mismatched allocator/deallocator**: freeing memory obtained via a custom allocator with plain `free` (or vice versa)

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
- **Off-by-one buffer sizing**: allocating `strlen(s)` bytes instead of `strlen(s) + 1` for the terminator

### 3.3 Pointer & Type Bugs

- **Wrong pointer arithmetic units**: `char *p; p += sizeof(int);` — advances by 4 bytes, not 1; just do `p += 1`
- **Casting `int *` to `char *` and violating alignment**: reading a `short` from an unaligned `char` buffer via cast
- **`void *` arithmetic**: `void *p; p++;` — illegal in standard C (GCC extension only)
- **Incorrect `const` cast**: casting away `const` then modifying — UB if object was originally `const`
- **Pointer comparison across objects**: `ptr_a < ptr_b` when they point into different objects — undefined behavior
- **Null pointer dereference**: forgetting to check `malloc`/`fopen` return before use
- **Integer to pointer cast without `intptr_t`**: `int *p = (int *)42;` — may not round-trip on all platforms
- **`sizeof` applied to expression vs type confusion**: `sizeof(int *)` vs `sizeof(int)` mix-up
- **Function pointer type mismatch**: calling through a cast to an incompatible signature — UB even if it "happens to work"

### 3.4 Integer & Arithmetic Bugs

- **Signed integer overflow**: `int x = INT_MAX; x++;` — undefined behavior (not guaranteed to wrap)
- **Unsigned wraparound misread as overflow**: `unsigned x = 0; x--;` gives `UINT_MAX`, not a crash
- **Truncation on assignment**: storing a `long` result into `int` silently truncates
- **Sign extension pitfall**: `char c = 0xFF; int i = c;` — may sign-extend to `-1` on platforms with signed `char`
- **Division by zero**: no check before `/` or `%` with a variable denominator
- **`INT_MIN / -1` and `INT_MIN % -1`**: overflow — undefined behavior even though it looks harmless
- **Shift by negative or ≥ width**: `x << 32` when `x` is 32-bit — undefined behavior
- **Left shift of negative value**: `int x = -1; x << 1;` — undefined behavior
- **Comparison of signed and unsigned**: `int n = -1; if (n < sizeof(arr))` — `-1` converted to a huge unsigned value
- **Integer overflow in size calculation**: `malloc(count * size)` where `count * size` overflows `size_t`, yielding a too-small allocation

### 3.5 Floating-Point Bugs

- **Exact equality comparison**: `if (x == 0.1)` — `0.1` isn't representable; compare within an epsilon
- **Accumulated rounding error**: summing many small `float`s loses precision; use `double` or Kahan summation
- **`NaN` comparisons**: `if (x == x)` is false when `x` is `NaN`; use `isnan`
- **Integer division assigned to float**: `float f = 1 / 2;` yields `0.0`, not `0.5` — one operand must be floating point
- **Silent `double` → `float` narrowing** losing precision on assignment
- **Comparing results across optimization levels**: excess intermediate precision (x87 / FMA contraction) changing results

### 3.6 Control Flow Bugs

- **Missing `break` in `switch`**: unintended fall-through executes next case body
- **Semicolon after `if`/`for`**: `if (cond);` — body is empty, following block always runs
- **Assignment in condition**: `if (x = 0)` instead of `if (x == 0)` — always false, modifies `x`
- **Infinite loop on `fgetc`**: storing result of `fgetc` in `char` instead of `int` — `EOF` (-1) truncated to `0xFF` never equals `EOF`
- **Loop variable shadowing**: declaring `int i` inside a nested block hides outer loop `i`
- **`continue` in `do-while`**: `continue` jumps to the condition check, not to the top — sometimes surprising
- **Dangling `else`**: `else` binds to the nearest unmatched `if`, not the one indentation suggests

### 3.7 Operator & Precedence Bugs

- **Bitwise vs comparison precedence**: `if (flags & MASK == 0)` parses as `flags & (MASK == 0)`
- **Assignment vs equality in a wider expression**: `x = a == b;` assigns a boolean, likely unintended
- **Ternary precedence**: `int y = cond ? a : b + 1;` binds as `cond ? a : (b + 1)`
- **Shift precedence**: `x + 1 << 2` is `(x + 1) << 2`? No — `<<` is lower than `+`, so it is `(x + 1) << 2`; verify before relying on it
- **Increment/dereference order**: `*p++` increments the pointer, not the pointee; use `(*p)++` for the latter
- **Logical vs bitwise operator swap**: using `&`/`|` where `&&`/`||` was intended (loses short-circuit, changes result)

### 3.8 Preprocessor & Macro Bugs

- **Macro without parentheses**: `#define SQUARE(x) x*x` → `SQUARE(a+1)` expands to `a+1*a+1`
- **Double evaluation in macro**: `#define MAX(a,b) ((a)>(b)?(a):(b))` → `MAX(i++, j++)` increments twice
- **Missing include guard**: header included multiple times causes redefinition errors
- **Macro name collision with standard library**: `#define max(a,b)` clashes when `<sys/param.h>` also defines it
- **`#define` used as a type**: `#define BOOL int` then comparing with `true`/`false` — inconsistency with `<stdbool.h>`
- **Multiline macro without backslash continuation**: last line missing `\` causes syntax error
- **Semicolon in a macro body**: `#define INIT() a=0;` breaks when used in `if (x) INIT(); else ...`; use a `do { ... } while (0)` wrapper

### 3.9 Resource & File Handling Bugs

- **File not closed on error path**: early `return` before `fclose` leaks file descriptor
- **Ignoring `fclose` return value**: `fclose` can fail (e.g. flushing buffered writes) — error silently lost
- **Using `tmpnam` without checking uniqueness race**: TOCTOU between name generation and file creation; use `tmpfile` or `mkstemp`
- **`fgets` return value ignored**: loop continues on EOF/error with stale buffer contents
- **Reading binary file in text mode**: `fopen("file", "r")` on Windows translates `\r\n` — use `"rb"` for binary
- **`system()` with unsanitized input**: command injection if user data is concatenated into the shell string
- **Leaking a file descriptor across `exec`**: not setting `O_CLOEXEC`/`FD_CLOEXEC` on descriptors a child shouldn't inherit

### 3.10 Concurrency & Signal Bugs

- **Non-atomic flag check**: `while (!done)` with `done` set in a signal handler — `done` must be `volatile sig_atomic_t`
- **Non-async-signal-safe function in handler**: calling `printf` or `malloc` inside a signal handler — undefined behavior
- **`setjmp` variable clobbering**: non-`volatile` local modified between `setjmp` and `longjmp` has indeterminate value
- **Shared global mutated without synchronization**: two threads writing the same global without a mutex or `_Atomic`
- **Data race on non-atomic counter**: `counter++` from multiple threads without a mutex/atomic — read-modify-write is not atomic
- **Deadlock from inconsistent lock ordering**: thread A locks `mutex1` then `mutex2`, thread B locks `mutex2` then `mutex1`
- **Condition-variable wait without a predicate loop**: using `if` instead of `while` misses spurious wakeups and lost signals

### 3.11 Security Vulnerabilities & Exploitation Patterns

- **Classic stack smashing**: a fixed-size local buffer overflowed by unbounded `strcpy`/`gets`/manual copy, overwriting the saved return address to redirect control flow
- **Off-by-one overwriting a stack canary or adjacent local**: a one-byte overflow (e.g. `buf[len] = '\0'` when `len == sizeof(buf)`) that corrupts an adjacent variable or the canary without a full smash
- **Heap overflow corrupting allocator metadata or an adjacent object**: writing past a `malloc`'d chunk can corrupt heap bookkeeping or a neighboring object's data, leading to control-flow hijack later
- **Use-after-free exploited for control-flow hijack**: freed memory is reallocated and attacker-controlled, then the stale pointer's virtual call/function pointer is invoked
- **Double-free exploited for heap grooming**: a repeated `free` corrupts free-list structures, enabling an attacker to get `malloc` to return a chosen address
- **Format string vulnerability for arbitrary read/write**: `printf(user_input)` with `%x`/`%s` leaks stack memory, and `%n` can write to an attacker-chosen address
- **Integer overflow leading to undersized allocation**: `malloc(count * size)` overflow followed by writing `count` elements — the classic pattern behind many historical CVEs
- **Buffer over-read / information disclosure (Heartbleed-style)**: trusting a caller-supplied length larger than the actual data, so the reply includes adjacent memory contents
- **Uninitialized memory disclosure**: returning/sending a struct with padding bytes or an only-partially-filled buffer, leaking stale stack/heap data to an attacker
- **Out-of-bounds read from an untrusted index**: using an attacker-supplied index/offset to read an array without bounds-checking, leaking memory
- **Missing length validation in protocol/binary parsing**: trusting a length field from the wire and copying that many bytes into a fixed buffer
- **TOCTOU (time-of-check to time-of-use) race**: `access()` followed later by `open()` on the same path — the file can be swapped (e.g. via a symlink) between the two calls
- **Privilege escalation via unsafe `setuid` usage**: a setuid-root program that fails to drop privileges before running attacker-influenced code (e.g. `system()`), or checks permissions with the real UID but acts with the effective UID
- **Ignoring the return value of `setuid`/`setgid`**: privileges silently not dropped, so later "unprivileged" code still runs as root
- **Environment variable trust**: a setuid program that trusts `PATH`, `IFS`, or `LD_PRELOAD`/`LD_LIBRARY_PATH` from the invoking environment, enabling code injection
- **Command injection via `system()`/`popen()`**: untrusted data concatenated into a shell command string, allowing metacharacters (`;`, `|`, `` ` ``, `$()`) to run arbitrary commands
- **Path traversal via unsanitized filename**: user-supplied path containing `../` used directly in `fopen`, escaping an intended directory sandbox
- **Null-byte injection**: a `\0` embedded in an attacker-controlled string truncating a path/name at a different point than the validation logic expected
- **Insecure temporary file creation**: predictable `tmpnam` names racing with a symlink attack, vs the atomic create-and-open guarantee of `mkstemp`
- **Signed/unsigned confusion enabling a bounds-check bypass**: a length check `if (len < MAX)` where `len` is signed and attacker-supplied as negative, bypassing the intended upper-bound check; the negative value then becomes a huge `size_t` in `memcpy`
- **Predictable randomness for security tokens**: using `rand()`/`srand(time(NULL))` to generate session IDs, keys, or nonces instead of a CSPRNG
- **Secrets left in memory / hardcoded credentials**: keys/passwords not wiped with `explicit_bzero` before `free`, or credentials compiled into the binary
- **Timing side-channel from non-constant-time secret comparison**: using `memcmp`/`strcmp` to check a password or MAC allows an attacker to infer correct bytes one at a time from response timing

---

## 4. Systems, Embedded & Toolchain — Understanding C in Full

> Beyond the core language: how C is actually used on real threads, real hardware, and real operating systems, plus the tooling and standards that surround production C.

### 4.1 Language Standards & Evolution
- C89/C90 (ANSI C), C99, C11, C17, C23 — knowing which features belong to which revision
- C99 additions: `//` comments, `inline`, VLAs, designated initializers, `<stdint.h>`, `<stdbool.h>`, compound literals, `restrict`, mixed declarations and code, `long long`
- C11 additions: `_Static_assert`, `_Generic`, atomics, `<threads.h>`, anonymous structs/unions, `_Alignas`/`_Alignof`, `_Noreturn`, optional bounds-checked (Annex K), `gets` removed
- C17: bug-fix/clarification release — no new language features
- C23 additions: `nullptr`, `constexpr`, `typeof`, `#embed`, `bool`/`true`/`false`/`static_assert` as keywords, binary literals, digit separators, `[[attributes]]`, checked integer arithmetic
- Freestanding vs hosted implementation: what the standard guarantees with no OS (only a subset of headers)
- Selecting a standard: `-std=c11`/`-std=c17`/`-std=c23`, `__STDC_VERSION__`, strict ISO (`-pedantic`) vs GNU extensions (`-std=gnu11`)

### 4.2 Concurrency & the C Memory Model (Deeper)
- The formal relationships: sequenced-before, happens-before, synchronizes-with
- Data race = undefined behavior; how mutexes/atomics establish an ordering that removes the race
- Memory orders in depth: `relaxed`, `acquire`, `release`, `acq_rel`, `seq_cst` — what each permits the compiler/CPU to reorder
- False sharing: two threads hammering different variables on the same cache line; fixing with padding/alignment
- Thread-local storage: `_Thread_local` / `__thread`
- Lazy one-time init: `call_once` / `pthread_once`; double-checked locking done correctly with atomics
- Mutex vs spinlock vs read-write lock — when each is appropriate
- Lock-free vs wait-free; the ABA problem, compare-and-swap loops, hazard pointers
- Condition variables with a predicate loop; barriers; producer-consumer patterns

### 4.3 Embedded & Bare-Metal Conventions
- Freestanding environment: no `malloc`/`stdio`, custom startup (`_start`/reset handler), no OS
- Memory-mapped I/O: `volatile`-qualified pointers to peripheral registers, why the optimizer must not cache them
- Register bit manipulation: read-modify-write of hardware registers, set/clear/toggle masks
- Interrupt service routines (ISRs): keep them short, share state via `volatile sig_atomic_t`-style flags, reentrancy concerns
- Fixed-point arithmetic and Q-notation when there is no FPU
- Static / pool / arena allocation instead of the heap to avoid fragmentation and non-determinism
- Linker scripts and memory sections: `.text`/`.data`/`.bss`/`.rodata`, custom sections, `__attribute__((section(...)))`
- Placing constants in flash/ROM with `const`; vector tables and startup code
- Struct packing for wire/register layout: `__attribute__((packed))` / `#pragma pack`, alignment trade-offs
- Weak symbols and overridable default (interrupt) handlers
- Endianness handling in protocols and serialization
- Circular/ring buffers for lock-free-ish producer-consumer without dynamic memory
- Watchdog timers, deterministic timing, and avoiding UB the optimizer can weaponize

### 4.4 Real-Time Operating Systems (RTOS)
- What an RTOS is vs bare-metal vs a general-purpose OS; hard vs soft vs firm real-time; determinism over throughput
- Tasks/threads and the scheduler: preemptive priority-based, round-robin/time-sliced, cooperative
- Task states: running, ready, blocked, suspended — and what transitions between them
- The tick interrupt (`SysTick`), context switching, and tickless idle for low power
- Synchronization primitives: mutexes, binary vs counting semaphores, event flags/groups, message queues, mailboxes
- Priority inversion and its fixes: priority inheritance and priority-ceiling protocols
- Deadlock and starvation in a real-time context
- ISR-to-task communication: deferred interrupt handling and the "…FromISR" API variants (never block in an ISR)
- Per-task stacks, stack-overflow detection, and heap schemes (static vs pooled allocation)
- Software timers, periodic tasks, `vTaskDelay`/`vTaskDelayUntil`-style precise periodic scheduling
- Latency concepts: interrupt latency, scheduling latency, jitter, and worst-case execution time (WCET)
- Schedulability theory: rate-monotonic scheduling (RMS) and earliest-deadline-first (EDF)
- Memory protection: MPU-backed task isolation, memory pools, avoiding fragmentation
- Common RTOSes: FreeRTOS, Zephyr, ThreadX/Azure RTOS, RT-Thread, µC/OS, VxWorks, RTEMS
- Real-time Linux: `PREEMPT_RT`, `SCHED_FIFO`/`SCHED_RR`, `mlockall` to avoid page-fault jitter, CPU isolation/affinity
- FreeRTOS specifics: `xTaskCreate`, `vTaskDelay`, `xQueueSend`/`xQueueReceive`, `xSemaphoreTake`/`Give`, `taskENTER_CRITICAL`/`taskEXIT_CRITICAL`, `configTICK_RATE_HZ`

### 4.5 Linux / POSIX Systems Programming
- System calls vs libc wrappers; the raw `syscall()` interface and how `errno` is set
- The file-descriptor model ("everything is a file"), `dup`/`dup2`, `O_CLOEXEC` and fd inheritance
- `mmap`/`munmap`/`mprotect`: file mappings, anonymous memory, shared vs private mappings
- I/O multiplexing: `select`, `poll`, `epoll` (level- vs edge-triggered), non-blocking I/O
- Process control: `fork`/`exec`/`wait`, zombies and orphans, process groups and sessions
- Signals in depth: `sigaction`, signal masks, `signalfd`, `SA_RESTART` and interrupted syscalls
- IPC: pipes, FIFOs, System V vs POSIX shared memory/semaphores/message queues, Unix domain sockets
- Network sockets: TCP/UDP, `getaddrinfo`, blocking vs non-blocking connect/accept
- Time: `clock_gettime`, monotonic vs realtime clocks, `timerfd`, `nanosleep`
- CLI and environment: `getopt`/`getopt_long`, environment variables, `argv` handling
- Daemonization, `syslog`, reading `/proc` and `/sys`
- ELF and dynamic linking: `LD_PRELOAD`, `RPATH`/`RUNPATH`, symbol interposition, `dlopen`
- glibc vs musl differences; feature-test macros (`_GNU_SOURCE`, `_POSIX_C_SOURCE`, `_DEFAULT_SOURCE`)

### 4.6 Toolchain, Debugging, Testing & Analysis
- Compilers: gcc vs clang; optimization levels `-O0`–`-O3`/`-Os`/`-Ofast`, `-g`, warnings `-Wall -Wextra -Werror`
- Inspecting output: `-E` (preprocessed), `-S` (assembly); `objdump`, `nm`, `readelf`, `strings`, `ldd`
- Debuggers: gdb/lldb — breakpoints, watchpoints, backtraces, inspecting core dumps
- Dynamic analysis: Valgrind (memcheck), AddressSanitizer, UndefinedBehaviorSanitizer, ThreadSanitizer, MemorySanitizer, LeakSanitizer
- Static analysis: `clang-tidy`, `cppcheck`, `scan-build`, Coverity
- Fuzzing: libFuzzer, AFL++ for surfacing memory-safety bugs on untrusted input
- Unit-testing frameworks: Unity, CMocka, Check, Criterion; assertion-based tests
- Profiling: `perf`, `gprof`, cachegrind for hot-path and cache analysis
- Build & packaging: Make, CMake, Meson, autotools, `pkg-config`, cross-compilation toolchains

### 4.7 Compiler Extensions & Inline Assembly
- GCC/Clang `__attribute__`: `packed`, `aligned`, `noreturn`, `deprecated`, `always_inline`, `constructor`/`destructor`, `format(printf,...)`, `cleanup`, `warn_unused_result`
- MSVC counterparts: `__declspec`, `#pragma` intrinsics
- Builtins: `__builtin_expect` (branch hints), `__builtin_unreachable`, `__builtin_overflow`, `__builtin_types_compatible_p`, `__builtin_offsetof`
- SIMD intrinsics (`<immintrin.h>`) and GCC vector extensions
- Inline assembly: `asm`/`__asm__` basic and extended syntax — operands, constraints, clobber lists
- Useful pragmas: `#pragma once`, `#pragma GCC diagnostic push/ignored`, `#pragma pack`
- Statement expressions (`({ ... })`) and other common GNU C extensions

### 4.8 Custom Memory Management
- Arena/region allocators: bump-pointer allocation with a single bulk free
- Object pools / free lists for fast fixed-size allocation and deallocation
- Slab allocation concepts (kernel-style)
- `alloca` (stack allocation) and why it is dangerous (no failure signal, overflow risk)
- Aligned allocation for SIMD/DMA; over-allocation-and-align trick, `aligned_alloc`, `posix_memalign`
- `malloc` internals: chunks, bins, per-thread arenas (glibc), fragmentation causes
- Replacing the allocator: jemalloc/tcmalloc, `LD_PRELOAD`-based interposition, allocator hooks
- Ownership and lifetime conventions in C APIs (who frees what); reference counting

### 4.9 Secure Coding Standards & Hardening (Security)
- CERT C Secure Coding Standard rule families (INT integer, STR string, MEM memory, FIO file I/O, ERR error handling)
- MISRA-C for safety-critical/embedded: no dynamic memory, no recursion, restricted UB, single-exit rules
- CWE-to-C mapping: CWE-119/787/125 (buffer read/write out of bounds), CWE-416 (use-after-free), CWE-190 (integer overflow), CWE-78 (command injection), CWE-134 (format string), CWE-476 (null deref)
- Threat modeling a C program: identifying trust boundaries, attack surface, and an input-validation strategy
- Hardening flags recap: `-fstack-protector-strong`, `-D_FORTIFY_SOURCE=2/3`, `-fPIE -pie`, `-Wl,-z,relro,-z,now`, running `-fsanitize=address,undefined` in CI
- Hardware-assisted CFI: shadow stacks (Intel CET), pointer authentication (ARM PAC), branch-target identification
- Runtime least privilege: `seccomp` syscall filtering, Linux capabilities, privilege dropping, sandboxing
- Safer-by-construction patterns: bounds-carrying slices/"fat pointers", `-fbounds-safety`, avoiding raw pointer+length pairs

---

## Difficulty Levels

| Level | Description |
|-------|-------------|
| Beginner | Syntax, types, storage classes, basic pointers/arrays, common stdlib functions |
| Intermediate | Pointer patterns, UB categories, preprocessor, linkage/build, error-handling idioms, deeper stdlib usage, recognizing vulnerable code patterns |
| Pro | Memory model, atomics, IEEE 754, ABI, exploit mitigations (ASLR/canaries/NX/CFI), advanced idioms |
| Systems/Embedded | Concurrency model depth, bare-metal & MMIO conventions, Linux/POSIX syscalls, toolchain & sanitizers, CERT/MISRA secure-coding standards |
