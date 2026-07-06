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
- Literals: integer suffixes (`u`, `l`, `ul`, `ll`), hex (`0x`), octal (`0`), binary (`0b`), floating suffixes (`f`, `l`)
- Character literals vs string literals: `'a'` (int/char) vs `"a"` (`char[2]`)
- Difference between `=` (assignment) and `==` (comparison) in conditions
- Short-circuit evaluation of `&&` and `||`
- Comma operator vs comma as argument separator
- Ternary operator `?:` — type of the result, common misuse
- Operator precedence gotchas: `*p++` vs `(*p)++`, `a & b == c` (bitwise AND binds looser than `==`)
- Bitwise operators: `&`, `|`, `^`, `~`, `<<`, `>>` — common bit-flag idioms (set/clear/toggle/test a bit)
- `sizeof` is evaluated at compile time (except VLAs) and its operand is not executed

#### 1.2 Pointers & Memory
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

#### 1.3 Arrays & Strings
- Array declaration, initialization, and default zero-fill for partially initialized arrays
- Multidimensional arrays: `int m[3][4]` — row-major memory layout
- Array of pointers vs pointer to array: `char *argv[]` vs `char (*p)[N]`
- C strings are `\0`-terminated `char` arrays — there is no built-in "length" tracked at runtime
- String literals are stored in read-only memory and may be shared/pooled by the compiler
- `char buf[N]` vs `char *buf = "literal"` — the former is mutable and owns storage, the latter is not
- Passing arrays to functions: they decay to pointers, losing size information
- `sizeof` on a true array (in the defining scope) vs on a decayed pointer parameter
- Command-line arguments: `int main(int argc, char *argv[])`, `argv[argc] == NULL`
- Multi-dimensional array indexing pitfalls: `arr[i][j]` vs `arr[j][i]` cache/layout implications
- Wide characters and strings: `wchar_t`, `L"..."`, `<wchar.h>` basics

#### 1.4 Control Flow & Functions
- `for`, `while`, `do-while` — when each is appropriate
- `break` and `continue` inside nested loops
- `switch` fall-through: intentional vs accidental, `[[fallthrough]]` annotation
- Function declaration vs definition vs prototype
- Pass by value: C always passes arguments by value; pass address to modify caller's variable
- Returning a pointer to a local variable → undefined behavior (dangling pointer)
- Recursive functions: call stack growth, stack overflow risk
- `static` local variables: initialized once, persist across calls
- Variadic functions: `...` parameter, `<stdarg.h>` macros (`va_list`, `va_start`, `va_arg`, `va_end`)
- Default argument promotion for variadics: `float` → `double`, small integer types → `int`
- Function-like macros vs true functions: evaluation semantics differ
- `goto` and labels: legitimate uses (single-point cleanup, breaking nested loops) vs spaghetti code

#### 1.5 Structs & Unions
- `struct` definition, member access with `.` and `->`
- Struct padding and alignment: `sizeof(struct)` may be larger than sum of members
- Reordering members to reduce padding (structure packing optimization)
- Designated initializers: `struct Point p = {.x = 1, .y = 2};`
- `union`: all members share same memory, only one active at a time
- `typedef struct` pattern and anonymous structs/unions
- Bit fields: `unsigned int flag : 1;` — implementation-defined layout, portability caveats
- Forward declaration of structs (opaque pointer pattern) for encapsulation
- Self-referential structs (linked lists, trees) via pointer members
- Nested structs and arrays of structs, initialization syntax

### Intermediate

#### 1.6 Pointers — Advanced Patterns
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

#### 1.7 Undefined Behavior & Pitfalls
- Reading uninitialized variables
- Signed integer overflow (UB) vs unsigned wraparound (defined, modular arithmetic)
- Out-of-bounds array access (read and write)
- Using `%d` with `unsigned int` or `size_t` → format mismatch UB
- Modifying a string literal: `char *s = "hello"; s[0] = 'H';` → UB
- Sequence points: `i++ + i++` and `a[i] = i++` are UB (indeterminate order/multiple modification)
- Comparing pointers to different objects with `<`/`>` (UB unless same array/one-past-end)
- `setjmp`/`longjmp` interaction with local variables not marked `volatile`
- Strict aliasing violations via type-punned pointers
- Null pointer arithmetic and null pointer comparison edge cases
- Calling a function through an incompatible function pointer type
- Returning from a non-`void` function without a `return` statement (UB if the value is used)
- Multiple unsequenced side effects on the same object in one expression

#### 1.8 Preprocessor & Compilation
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
- Conditional compilation for platform/feature detection (`#if defined(_WIN32)`, feature-test macros)

#### 1.9 Multi-File Programs, Linkage & Build
- Header files vs source files: declarations vs definitions
- Internal linkage (`static`) vs external linkage (default for functions/globals) vs no linkage (locals)
- One Definition Rule equivalent in C: a function/object may be defined once across all translation units
- Separate compilation: compiling `.c` files independently into `.o`/`.obj`, then linking
- Makefiles / build systems: targets, dependencies, incremental builds (conceptual, not syntax-heavy)
- Static libraries (`.a`/`.lib`) vs shared/dynamic libraries (`.so`/`.dll`) — link time vs load/run time resolution
- Symbol visibility and name mangling differences vs C++ (`extern "C"` linkage for interop)
- Circular header dependencies and forward declarations to break them
- Version compatibility: ABI stability when changing struct layouts in a shared library

#### 1.10 Security-Relevant Code Patterns (Reading & Recognition)
- Recognizing an unbounded copy into a fixed-size buffer from a code snippet (`strcpy`, `gets`, manual loop without bound)
- Spotting user-controlled length values used directly in `malloc`/array indexing without validation
- Identifying a format string that originates from user input rather than a literal
- Recognizing trust boundaries in code: where does external input (argv, stdin, network, env vars) first get used unchecked?
- Identifying integer values used as sizes/lengths that could overflow before an allocation
- Spotting missing bounds checks in loops that copy or index into arrays with attacker-influenced indices
- Recognizing privilege-sensitive calls (`setuid`, `system`, `exec*`, `popen`) and what happens if their return value or preconditions are ignored
- Identifying where a `free`d pointer might still be reachable through another alias (use-after-free)
- Distinguishing a benign array copy from one that is a manual reimplementation of `strcpy`/`memcpy` without the same care
- Reading disassembly/pseudo-code mentally: mapping a stack buffer overflow snippet to "this can overwrite the return address"

### Pro

#### 1.11 Memory Model & Low-Level
- `_Atomic` and `<stdatomic.h>`: lock-free operations, memory order (`memory_order_relaxed`, `_acquire`, `_release`, `_seq_cst`)
- `_Alignas` / `_Alignof`: alignment control and query
- `_Generic` selection (C11 type-generic macros)
- `_Static_assert`: compile-time assertions
- Endianness: big-endian vs little-endian, detecting at runtime
- Type-punning via `union` (the only defined way in C) vs via pointer cast (UB) vs via `memcpy` (defined, portable)
- Calling conventions and ABI basics (register vs stack argument passing, caller/callee-saved registers)
- Position-independent code (PIC) and shared libraries
- Memory-mapped I/O and `volatile` for hardware registers
- Compiler barriers vs memory fences vs `volatile` — what each actually guarantees (and doesn't)
- Lock-free data structures: ABA problem, compare-and-swap (`atomic_compare_exchange`)
- Virtual memory basics: pages, the heap/stack/BSS/data/text segments, `mmap`-backed allocations

#### 1.12 Security-Relevant Code Patterns — Advanced / Exploit Mitigations
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
- `tmpfile` / `tmpnam` — temporary files (see security notes in 2.13)
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
- Never passing user-controlled data as the format argument (see 2.13 / 3.2 security notes)

### 2.2 `<stdlib.h>` — Memory, Conversion, Process

#### Functions
- `malloc` / `calloc` / `realloc` / `free` — heap memory management
- `atoi` / `atol` / `atof` — string to number (no error detection)
- `strtol` / `strtoul` / `strtod` / `strtoll` / `strtoull` — string to number with error detection
- `abs` / `labs` / `llabs` — absolute value
- `div` / `ldiv` / `lldiv` — integer division with quotient and remainder
- `rand` / `srand` — pseudo-random numbers (not cryptographically secure — see 2.13)
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
- `strcpy` / `strncpy` — string copy (prefer `strncpy` carefully, or safer alternatives — see 2.13)
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
- `memcmp` — compare memory blocks (byte-wise, not suitable for constant-time secret comparison — see 2.13)
- `memchr` — find byte in memory block
- `strdup` / `strndup` — duplicate string (POSIX; allocates with `malloc`, must be `free`d)
- `strerror` / `strerror_r` — human-readable error message for an `errno` value

#### Usage Patterns
- Null terminator: always ensure destination buffer has room for `\0`
- `strtok` is not reentrant and mutates its input — use `strtok_r` in multi-threaded or nested-parsing code
- `memset` to zero a struct: `memset(&s, 0, sizeof(s))`
- Safer alternatives: `strlcpy` / `strlcat` (BSD/POSIX, not standard C) or `strncpy` + manual null-termination
- Computing buffer sizes with `sizeof` on the actual array (not a decayed pointer) to avoid off-by-one truncation
- Comparing memory regions of secret data (passwords, MACs, tokens) with `memcmp` leaks timing information — needs a constant-time compare (see 2.13)

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

### 2.8 `<stdint.h>` & `<inttypes.h>` — Portable Integer Types

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

### 2.9 `<signal.h>` — Signal Handling

#### Functions / Macros
- `signal` — register signal handler (`SIG_DFL`, `SIG_IGN`, or function pointer)
- `raise` — send signal to current process
- Common signals: `SIGINT`, `SIGTERM`, `SIGSEGV`, `SIGFPE`, `SIGABRT`, `SIGHUP`, `SIGKILL` (not catchable), `SIGCHLD`
- Async-signal-safe functions: only a small POSIX-defined set is safe to call inside handlers
- `sigaction` (POSIX) — more reliable, portable signal registration than `signal` (control over masking/re-entry/`SA_RESTART`)
- `sigprocmask` / `sigemptyset` / `sigaddset` — signal mask manipulation

### 2.10 `<setjmp.h>` — Non-local Jumps

#### Functions / Macros
- `setjmp` — save execution context (returns 0 on first call)
- `longjmp` — restore context saved by `setjmp` (never returns to the `longjmp` call site)
- Use case: error recovery without unwinding the stack manually
- Pitfall: local variables modified after `setjmp` may have indeterminate values unless `volatile`

### 2.11 `<stdbool.h>`, `<limits.h>` & `<float.h>` — Booleans & Type Limits

#### Contents
- `<stdbool.h>`: `bool`, `true`, `false` macros (built-in keywords `_Bool`/`true`/`false` since C23)
- `<limits.h>`: `CHAR_BIT`, `INT_MIN`/`INT_MAX`, `LONG_MAX`, `UINT_MAX`, `CHAR_MIN`/`CHAR_MAX` (signedness of plain `char` is implementation-defined)
- `<float.h>`: `FLT_EPSILON`, `DBL_EPSILON`, `FLT_MAX`, `DBL_MIN`, `FLT_RADIX` — floating-point representation limits

#### Usage Patterns
- Using `INT_MAX`/`UINT_MAX` etc. to write portable overflow checks instead of hardcoding magic numbers
- Using `*_EPSILON` for tolerance-based floating point comparisons

### 2.12 `<unistd.h>` & POSIX Process/Permission APIs

#### Functions
- `fork` — create a child process (copy-on-write address space duplication)
- `exec*` family (`execl`, `execv`, `execve`, `execvp`, ...) — replace process image
- `wait` / `waitpid` — reap child process exit status
- `pipe` / `dup` / `dup2` — inter-process communication and fd redirection
- `getuid` / `geteuid` / `getgid` / `getegid` — real vs effective user/group IDs
- `setuid` / `seteuid` / `setgid` / `setegid` — changing privilege (see security notes in 2.13)
- `access` — check file permissions (subject to TOCTOU races — see 3.7/3.9)
- `chmod` / `chown` — change file permissions/ownership
- `read` / `write` / `close` / `lseek` — low-level unbuffered I/O
- `getpid` / `getppid` — process identification

#### Usage Patterns
- Understanding real UID vs effective UID vs saved UID when reasoning about setuid programs
- `fork` + `exec` pattern for launching subprocesses safely instead of `system()`
- Always checking return values of privilege-related and file-related syscalls — silent failure here is a classic security bug source

### 2.13 Secure Coding — Safer Standard Library Alternatives

#### Guidance
- `gets` was removed from the C standard entirely — always use `fgets` with an explicit buffer size instead
- Prefer `snprintf` over `sprintf`/`strcpy`/`strcat` for anything involving a fixed-size buffer and untrusted or variable-length input
- `strlcpy`/`strlcat` (BSD/POSIX, not in all libcs) guarantee null-termination and take the full buffer size, unlike `strncpy`/`strncat`
- `strncpy` does **not** guarantee null-termination if the source is `>= n` bytes — always manually terminate: `buf[n-1] = '\0';`
- `memset_s` (C11 Annex K, optional) / `explicit_bzero` (BSD) / `SecureZeroMemory` (Windows) — zero sensitive memory (passwords, keys) in a way the compiler won't optimize away, unlike a plain `memset` right before `free`
- Constant-time comparison for secrets: a naive `memcmp`/`strcmp` on a MAC or password hash leaks timing information; use a dedicated constant-time compare function
- `rand()`/`srand()` are not cryptographically secure — use a CSPRNG (`arc4random`, `/dev/urandom`, or a platform crypto API) for anything security-sensitive (tokens, nonces, keys)
- `system()` and `popen()` invoke a shell — never pass unsanitized/untrusted data into the command string; prefer `fork`+`exec*` with an argument array, which avoids shell interpretation entirely
- `tmpnam`/`tmpfile` race conditions: prefer `mkstemp` (POSIX), which atomically creates and opens a uniquely-named file
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
- **Shift by negative or ≥ width**: `x << 32` when `x` is 32-bit — undefined behavior
- **Left shift of negative value**: `int x = -1; x << 1;` — undefined behavior
- **Comparison of signed and unsigned**: `int n = -1; if (n < sizeof(arr))` — `-1` converted to a huge unsigned value
- **Integer overflow in size calculation**: `malloc(count * size)` where `count * size` overflows `size_t`, yielding a too-small allocation

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
- **Data race on non-atomic counter**: `counter++` from multiple threads without a mutex/atomic — read-modify-write is not atomic
- **Deadlock from inconsistent lock ordering**: thread A locks `mutex1` then `mutex2`, thread B locks `mutex2` then `mutex1`

### 3.9 Security Vulnerabilities & Exploitation Patterns

- **Classic stack smashing**: a fixed-size local buffer overflowed by unbounded `strcpy`/`gets`/manual copy, overwriting the saved return address to redirect control flow
- **Off-by-one overwriting a stack canary or adjacent local**: a one-byte overflow (e.g. `buf[len] = '\0'` when `len == sizeof(buf)`) that corrupts an adjacent variable or the canary without a full smash
- **Heap overflow corrupting allocator metadata or an adjacent object**: writing past a `malloc`'d chunk can corrupt heap bookkeeping or a neighboring object's data, leading to control-flow hijack later
- **Use-after-free exploited for control-flow hijack**: freed memory is reallocated and attacker-controlled, then the stale pointer's virtual call/function pointer is invoked
- **Double-free exploited for heap grooming**: a repeated `free` corrupts free-list structures, enabling an attacker to get `malloc` to return a chosen address
- **Format string vulnerability for arbitrary read/write**: `printf(user_input)` with `%x`/`%s` leaks stack memory, and `%n` can write to an attacker-chosen address
- **Integer overflow leading to undersized allocation**: `malloc(count * size)` overflow followed by writing `count` elements — the classic pattern behind many historical CVEs
- **TOCTOU (time-of-check to time-of-use) race**: `access()` followed later by `open()` on the same path — the file can be swapped (e.g. via a symlink) between the two calls
- **Privilege escalation via unsafe `setuid` usage**: a setuid-root program that fails to drop privileges before running attacker-influenced code (e.g. `system()`), or checks permissions with the real UID but acts with the effective UID
- **Environment variable trust**: a setuid program that trusts `PATH`, `IFS`, or `LD_PRELOAD`/`LD_LIBRARY_PATH` from the invoking environment, enabling code injection
- **Command injection via `system()`/`popen()`**: untrusted data concatenated into a shell command string, allowing metacharacters (`;`, `|`, `` ` ``, `$()`) to run arbitrary commands
- **Path traversal via unsanitized filename**: user-supplied path containing `../` used directly in `fopen`, escaping an intended directory sandbox
- **Insecure temporary file creation**: predictable `tmpnam` names racing with a symlink attack, vs the atomic create-and-open guarantee of `mkstemp`
- **Signed/unsigned confusion enabling a bounds-check bypass**: a length check `if (len < MAX)` where `len` is signed and attacker-supplied as negative, bypassing the intended upper-bound check
- **Timing side-channel from non-constant-time secret comparison**: using `memcmp`/`strcmp` to check a password or MAC allows an attacker to infer correct bytes one at a time from response timing

---

## Difficulty Levels

| Level | Description |
|-------|-------------|
| Beginner | Syntax, types, basic pointers/arrays, common stdlib functions |
| Intermediate | Pointer patterns, UB, preprocessor, linkage/build, deeper stdlib usage, recognizing vulnerable code patterns |
| Pro | Memory model, atomics, ABI, exploit mitigations (ASLR/canaries/NX/CFI), advanced idioms |
