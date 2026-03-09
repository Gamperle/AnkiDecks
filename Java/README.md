# Java Anki Decks

Flashcard decks covering Java programming concepts from beginner to expert.  
All cards target **Java 17+** unless otherwise noted.

---

## Available Decks

### Beginner
| File | Description |
|------|-------------|
| `java_basics.txt` | Syntax, data types, operators, control flow, String basics |
| `java_oop.txt` | Classes, interfaces, inheritance, polymorphism, generics |
| `java_exceptions.txt` | Checked vs unchecked, try/catch/finally, custom exceptions, try-with-resources |
| `java_security_awareness.txt` | Least privilege, input validation, authentication vs authorization |

### Intermediate
| File | Description |
|------|-------------|
| `java_collections.txt` | List, Set, Map, Queue, Deque, iterators, Comparator |
| `java_functional.txt` | Lambdas, functional interfaces, Streams, Optional, method references |
| `java_datetime.txt` | java.time API — LocalDate/Time, ZonedDateTime, Instant, Duration, Period |
| `java_io_nio.txt` | java.io streams, java.nio.file Path/Files, NIO channels |
| `java_web_fundamentals.txt` | HTTP, HttpServlet, REST, Jackson, HttpClient (Java 11+) |
| `java_cryptography.txt` | Hashing, AES, JCA, bcrypt/PBKDF2, HMAC, Base64 |
| `java_web_security.txt` | OWASP Top 10, SQLi, XSS, CSRF, JWT, OAuth2, OIDC |

### Advanced
| File | Description |
|------|-------------|
| `java_concurrency.txt` | Threads, synchronization, locks, Executors, CompletableFuture |
| `java_jvm.txt` | JVM internals, GC algorithms, classloading, bytecode |
| `java_design_patterns.txt` | All 23 GoF patterns with JDK examples |
| `java_enterprise_patterns.txt` | DI/IoC, Repository, Service, DTO, Circuit Breaker, CQRS, Outbox |
| `java_web_frameworks.txt` | Spring MVC/Boot/Security/Data, WebFlux, gRPC, SSE |
| `java_cryptography_advanced.txt` | TLS, keystores, PKI, ECDH, PBKDF2, AES-GCM, secrets management |

### Expert
| File | Description |
|------|-------------|
| `java_virtual_threads.txt` | Project Loom — virtual threads, pinning, Scoped Values, Structured Concurrency |
| `java_generics_advanced.txt` | Type erasure, bridge methods, PECS, recursive bounds, heap pollution |
| `java_modules.txt` | JPMS directives, module types, --add-opens, Flow API, ServiceLoader |
| `java_metaprogramming.txt` | AbstractProcessor, dynamic proxies, CGLIB, GraalVM Native Image, MethodHandles |
| `java_reflection.txt` | Reflection API, annotation processing, meta-annotations, Method.invoke() |
| `java_security_hardening.txt` | Deserialization, XXE, SSRF, STRIDE, audit logging, post-quantum crypto |
| `java_panama.txt` | Foreign Function & Memory API — MemorySegment, Arena, Linker, jextract |
| `java_classfile_api.txt` | Class-File API (JEP 484) — ClassModel, CodeBuilder, ClassTransform |
| `java_lock_free.txt` | CAS, ABA problem, LongAdder, VarHandle memory ordering, Treiber stack |

### Extended Reference
| File | Description |
|------|-------------|
| `java_advanced_anki_expanded.txt` | **Superseded** — original expanded deck; content distributed into topical decks above. Kept for reference only. |

---

## Topic Plan by Tier

### Beginner
> Core language literacy. Goal: write and read basic Java programs confidently.

**Language Fundamentals** (`java_basics.txt`)
- [x] Primitive types: `byte`, `short`, `int`, `long`, `float`, `double`, `char`, `boolean`
- [x] Wrapper classes and autoboxing / unboxing
- [x] Operators: arithmetic, relational, logical, bitwise, ternary
- [x] Control flow: `if/else`, `switch`, `for`, `while`, `do-while`
- [x] `break`, `continue`, labeled statements
- [x] Arrays: declaration, initialization, multi-dimensional arrays
- [x] `String` basics: immutability, `String` pool, `==` vs `.equals()`, common methods
- [x] `StringBuilder` vs `String` concatenation
- [x] `var` (local variable type inference, Java 10+)
- [x] Text Blocks (Java 15+): multi-line string literals with `"""`, incidental whitespace stripping, `\` line-continuation escape
- [x] Switch expressions (Java 14+): arrow labels (`case X -> expr`), `yield`, exhaustiveness; difference from switch statements
- [x] `String` new methods (Java 11+): `isBlank()`, `strip()` / `stripLeading()` / `stripTrailing()` (Unicode-aware vs `trim()`), `lines()` returning a `Stream<String>`, `repeat(n)`
- [x] `String.indent(n)` (Java 12): adds/removes leading whitespace per line; `String.transform(Function)` (Java 12): applies a function to the string and returns the result
- [x] `String.formatted(args)` (Java 15): instance-method equivalent of `String.format()`; `String.stripIndent()` and `String.translateEscapes()` for text block support

**OOP Basics** (`java_oop.txt`)
- [x] Classes and objects; constructors and `this`
- [x] Access modifiers: `public`, `protected`, package-private, `private`
- [x] `static` fields and methods
- [x] `final` on variables, methods, and classes
- [x] Encapsulation and getters/setters
- [x] Enums: declaration, fields, methods

**Exceptions — Basics**
- [x] Checked vs unchecked exceptions
- [x] `try / catch / finally`
- [x] `throws` declarations
- [x] Common built-in exceptions (`NullPointerException`, `IllegalArgumentException`, etc.)

**Security Awareness (Beginner)**
- [x] Principle of least privilege
- [x] Never store plaintext passwords; use hashing
- [x] Don't log sensitive data (passwords, tokens, PII)
- [x] Validating and sanitizing user input
- [x] What is SQL injection and why string concatenation in queries is dangerous
- [x] What is XSS (Cross-Site Scripting) at a conceptual level

---

### Intermediate
> Idiomatic Java. Goal: use the standard library effectively and write clean, maintainable code.

**OOP — Depth** (`java_oop.txt`)
- [x] Inheritance and `super`
- [x] Abstract classes vs interfaces
- [x] Default and static interface methods (Java 8+)
- [x] Private interface methods (Java 9+): `private` and `private static` methods in interfaces to share code between default methods without exposing implementation
- [x] Sealed classes and `permits` (Java 17+)
- [x] Records (Java 16+): compact constructors, custom accessors, implementing interfaces, limitations
- [x] Pattern matching for `instanceof` (Java 16+): `if (obj instanceof String s)` — binding variable, scope rules
- [x] Pattern matching for `switch` (Java 21+, finalized): type patterns, guarded patterns (`case Foo f when f.x() > 0`), exhaustiveness checking with sealed types
- [x] Record Patterns (Java 21+): deconstruction in `instanceof` and `switch` — `case Point(int x, int y)`; nesting record patterns
- [x] Method overloading vs overriding
- [x] Polymorphism and dynamic dispatch
- [x] Generics: type parameters, bounded wildcards (`? extends`, `? super`), type erasure
- [x] Inner classes, static nested classes, anonymous classes, local classes
- [x] SOLID principles overview

**Collections Framework** (`java_collections.txt`)
- [x] `List`: `ArrayList`, `LinkedList`, `CopyOnWriteArrayList`
- [x] `Set`: `HashSet`, `LinkedHashSet`, `TreeSet`
- [x] `Map`: `HashMap`, `LinkedHashMap`, `TreeMap`, `EnumMap`
- [x] `Queue` and `Deque`: `ArrayDeque`, `PriorityQueue`
- [x] `Comparable` vs `Comparator`; `Collections.sort()`, `List.sort()`
- [x] Immutable collections: `List.of()`, `Map.of()`, `Set.of()` (Java 9+); `Map.ofEntries(Map.entry(k,v), ...)` for more than 10 entries
- [x] Unmodifiable copies: `List.copyOf()`, `Set.copyOf()`, `Map.copyOf()` (Java 10+); `Collectors.toUnmodifiableList/Set/Map()` (Java 10+)
- [x] `Map` new default methods (Java 8+): `getOrDefault()`, `putIfAbsent()`, `computeIfAbsent()`, `computeIfPresent()`, `compute()`, `merge()`, `forEach()`, `replaceAll()`
- [x] `Comparator` static factories (Java 8+): `Comparator.comparing()`, `.thenComparing()`, `.reversed()`, `.naturalOrder()`, `.reverseOrder()`, `.nullsFirst()`, `.nullsLast()`
- [x] Sequenced Collections (Java 21+): `SequencedCollection`, `SequencedSet`, `SequencedMap`; `getFirst()`, `getLast()`, `addFirst()`, `addLast()`, `reversed()`; which existing types implement them
- [x] Iteration: `Iterator`, `ListIterator`, for-each, `removeIf()`
- [x] Time-complexity trade-offs across implementations

**Functional Programming & Streams** (`java_advanced_anki_expanded.txt`)
- [x] Lambda expressions: syntax, effectively final, capturing scope
- [x] `var` in lambda parameters (Java 11+): `(var x, var y) -> x + y`; allows annotations on lambda parameters
- [x] `Predicate.not()` static method (Java 11+): `Predicate.not(String::isBlank)` as a clean negation of method references
- [x] Functional interfaces: `Predicate`, `Function`, `Consumer`, `Supplier`, `BiFunction`, `UnaryOperator`
- [x] Method references: static, bound instance, unbound instance, constructor
- [x] `Stream<T>` pipeline: source → intermediate ops → terminal op
- [x] Intermediate ops: `filter`, `map`, `flatMap`, `sorted`, `distinct`, `limit`, `skip`, `peek`
- [x] `Stream` Java 9+ additions: `takeWhile(Predicate)` (short-circuits on first non-match), `dropWhile(Predicate)`, `ofNullable(T)` (0 or 1 element), `iterate(seed, hasNext, next)` (finite iteration with a predicate)
- [x] Terminal ops: `collect`, `forEach`, `reduce`, `count`, `findFirst`, `anyMatch`, `toList()`
- [x] `Stream.toList()` (Java 16+): shorthand terminal op returning an **unmodifiable** list; contrast with `Collectors.toList()` which returns a mutable list
- [x] `Collectors`: `toList()`, `toSet()`, `toMap()`, `groupingBy()`, `partitioningBy()`, `joining()`
- [x] `Collectors.teeing(downstream1, downstream2, merger)` (Java 12+): collects into two downstream collectors simultaneously and merges results; e.g. compute min and max in a single pass
- [x] Primitive streams: `IntStream`, `LongStream`, `DoubleStream`
- [x] `Optional<T>`: `map`, `flatMap`, `orElse`, `orElseGet`, `ifPresent`
- [x] `Optional` Java 9+ additions: `or(Supplier<Optional>)` (alternative Optional if empty), `stream()` (0 or 1 element Stream), `ifPresentOrElse(action, emptyAction)`
- [x] `Optional.isEmpty()` (Java 11+): cleaner negation of `isPresent()`
- [x] Stream Gatherers (Java 24+, `Stream.gather(Gatherer)`): custom intermediate operations; built-in gatherers (`Gatherers.windowFixed()`, `windowSliding()`, `scan()`, `fold()`, `mapConcurrent()`); writing a custom `Gatherer` with integrator, combiner, finisher

**Exception Handling — Depth**
- [x] Custom exceptions; exception chaining (`initCause`, `getCause`)
- [x] Multi-catch (`catch (A | B e)`)
- [x] Try-with-resources and `AutoCloseable`
- [x] Helpful NullPointerExceptions (Java 14+, on by default Java 15+): JVM describes exactly which variable/field was null in the NPE message (e.g. `Cannot read field "name" because "person" is null`)
- [x] Exception best practices (avoid swallowing, prefer specific types)

**Date & Time API (`java.time`, Java 8+)**
- [x] Why `java.time`? Problems with `java.util.Date` / `Calendar`: mutability, poor API, thread-safety; `java.time` is immutable and fluent
- [x] `LocalDate`, `LocalTime`, `LocalDateTime`: date/time without timezone; creation via `of()`, `now()`, `parse()`
- [x] `ZonedDateTime` and `OffsetDateTime`: date-time with timezone (`ZoneId`) or fixed offset (`ZoneOffset`)
- [x] `Instant`: a point on the UTC timeline (epoch seconds + nanos); use for timestamps and persistence
- [x] `Duration`: amount of time in seconds/nanos (machine-based); `Period`: amount in years/months/days (human-based)
- [x] `DateTimeFormatter`: formatting and parsing; built-in formatters (`ISO_LOCAL_DATE`); custom patterns; thread-safe unlike `SimpleDateFormat`
- [x] `ZoneId` vs `ZoneOffset`: named timezone (e.g. `"Europe/Berlin"`, handles DST) vs fixed offset (e.g. `+02:00`)
- [x] Temporal arithmetic: `plusDays()`, `minusMonths()`, `with(TemporalAdjuster)`; `TemporalAdjusters` (e.g. `nextOrSame(DayOfWeek.MONDAY)`)
- [x] `ChronoUnit`: `DAYS.between(date1, date2)`, `HOURS.between()`, etc.
- [x] Converting legacy `Date`/`Calendar` to `java.time`: `date.toInstant()`, `Instant.atZone()`, `Date.from(instant)`
- [x] `Clock`: injectable clock for testable time-dependent code

**I/O & NIO**
- [x] `java.io`: `InputStream`, `OutputStream`, `Reader`, `Writer`, `BufferedReader`
- [x] `java.nio.file`: `Path`, `Files`, `Paths` utility methods
- [x] `Files.readAllLines()`, `Files.walk()`, `Files.copy()`
- [x] `Files.readString(Path)` / `Files.writeString(Path, CharSequence)` (Java 11+): convenient single-call file read/write with optional charset
- [x] `Files.mismatch(Path, Path)` (Java 12+): returns position of first differing byte between two files, or `-1L` if identical
- [x] Serialization: `Serializable`, `transient`, `serialVersionUID`

**Java Web — Fundamentals**
- [x] HTTP request/response cycle: methods (GET, POST, PUT, DELETE, PATCH), status codes
- [x] URL anatomy: scheme, host, port, path, query string, fragment
- [x] Servlets: `HttpServlet`, `doGet()`, `doPost()`, servlet lifecycle (`init`, `service`, `destroy`)
- [x] `HttpServletRequest` / `HttpServletResponse` API
- [x] Sessions: `HttpSession`, session ID, cookies vs URL rewriting
- [x] Filters and `FilterChain`
- [x] Listeners: `ServletContextListener`, `HttpSessionListener`
- [x] Jakarta EE overview: EJB, CDI, JPA, JAX-RS, JSF
- [x] RESTful API design: resources, statelessness, HATEOAS, HTTP verbs mapping
- [x] JSON processing: `Jackson` (`ObjectMapper`, `@JsonProperty`, `@JsonIgnore`), `Gson`
- [x] `HttpClient` (Java 11+): synchronous and asynchronous requests, `BodyHandlers`

**Cryptography & Hashing (Intermediate)**
- [x] Symmetric encryption: AES (block cipher, modes: CBC, GCM), key size
- [x] Asymmetric encryption: RSA, key pair generation, public/private key roles
- [x] Hashing: SHA-256, SHA-3; properties (one-way, deterministic, avalanche effect)
- [x] Password hashing: why MD5/SHA-1 are wrong; use bcrypt, Argon2, or PBKDF2
- [x] HMACs: keyed hashing for message authentication
- [x] `java.security.MessageDigest` for hashing
- [x] `javax.crypto.Cipher` for encryption/decryption
- [x] Key generation: `KeyGenerator`, `KeyPairGenerator`
- [x] Secure random: `SecureRandom` vs `Random`
- [x] Base64 encoding: `java.util.Base64` (not encryption — just encoding)

**Web Security (Intermediate)**
- [x] OWASP Top 10 overview (injection, broken auth, XSS, IDOR, misconfiguration, etc.)
- [x] SQL injection: how it works, prevention with `PreparedStatement` / parameterized queries
- [x] XSS (Cross-Site Scripting): reflected, stored, DOM-based; prevention via output encoding
- [x] CSRF (Cross-Site Request Forgery): how it works; prevention with CSRF tokens, `SameSite` cookies
- [x] Clickjacking: `X-Frame-Options`, `Content-Security-Policy: frame-ancestors`
- [x] Security headers: `Content-Security-Policy`, `X-Content-Type-Options`, `Strict-Transport-Security`
- [x] CORS (Cross-Origin Resource Sharing): preflight, `Access-Control-Allow-Origin`
- [x] Authentication vs authorization
- [x] JWT (JSON Web Token): structure (header.payload.signature), signing (HS256, RS256), validation pitfalls
- [x] OAuth2 flows: Authorization Code, Client Credentials, PKCE; roles (resource server, auth server, client)
- [x] OpenID Connect: ID token, `userinfo` endpoint, relationship to OAuth2
- [x] Session fixation and session hijacking prevention
- [x] Password storage in practice: salting, stretching, timing-safe comparison

---

### Advanced
> Expert practitioner. Goal: build correct, high-performance multi-threaded applications.

**Concurrency** (`java_concurrency.txt` + `java_advanced_anki_expanded.txt`)
- [x] Thread lifecycle; `Runnable` vs `Callable` vs `Thread`
- [x] `synchronized`: methods and blocks; intrinsic locks / monitors
- [x] `volatile`: visibility and ordering guarantees (not atomicity)
- [x] Java Memory Model: happens-before rules
- [x] Race conditions, deadlock, livelock, starvation
- [x] `ReentrantLock`, `ReadWriteLock`, `StampedLock`
- [x] `Condition` objects; `await()` / `signal()` / `signalAll()`
- [x] `AtomicInteger`, `AtomicReference`, `AtomicStampedReference`; CAS
- [x] `ThreadLocal`; proper cleanup in thread pools
- [x] `ExecutorService`, `ThreadPoolExecutor` configuration (core/max pool, queue, rejection policy)
- [x] `Executors` factory types: fixed, cached, single, scheduled, work-stealing
- [x] `Future` and `CompletableFuture`: `thenApply`, `thenCompose`, `thenCombine`, `allOf`, `exceptionally`
- [x] `CompletableFuture` Java 9+ additions: `orTimeout(duration)`, `completeOnTimeout(value, duration)`, `completeAsync(Supplier)`, `failedFuture(ex)`, `newIncompleteFuture()`
- [x] `BlockingQueue` implementations: `ArrayBlockingQueue`, `LinkedBlockingQueue`, `SynchronousQueue`
- [x] `CountDownLatch`, `CyclicBarrier`, `Phaser`, `Semaphore`, `Exchanger`
- [x] `ConcurrentHashMap`, `CopyOnWriteArrayList`, `ConcurrentLinkedQueue`
- [x] Fork/Join framework: `RecursiveTask`, `RecursiveAction`, work-stealing
- [x] Parallel streams: when to use and pitfalls
- [x] Scoped Values (Java 24+, finalized, JEP 487): immutable per-thread/per-fiber data sharing; `ScopedValue.where().run()`; difference from `ThreadLocal` (immutability, no inheritance issues, GC-friendly with virtual threads)
- [x] Structured Concurrency (Java 24+, 4th preview, JEP 499): `StructuredTaskScope`, `ShutdownOnFailure`, `ShutdownOnSuccess`; treating a group of concurrent tasks as a single unit of work; cancellation and error propagation

**JVM Internals** (`java_jvm.txt`)
- [x] JVM memory areas: Heap, Stack, Metaspace, PC Register, Native Method Stack
- [x] Young Generation (Eden + Survivor), Old Generation, object promotion
- [x] GC algorithms: Serial, Parallel, CMS, G1 (default), ZGC, Shenandoah
- [x] Generational ZGC (Java 21+, JEP 439): generational mode enabled with `-XX:+ZGenerational`; young and old generation in ZGC; why generational hypothesis improves throughput vs non-generational ZGC
- [x] GC tuning flags: `-Xms`, `-Xmx`, `-XX:NewRatio`, `-XX:+UseG1GC`, `-XX:+UseZGC`, `-XX:+ZGenerational`, pause time goals
- [x] ClassLoader hierarchy: Bootstrap → Platform → Application; delegation model
- [x] Class loading phases: loading, linking (verify/prepare/resolve), initialization
- [x] JIT compilation: C1, C2 compilers; tiered compilation; hot-spot detection
- [x] Bytecode: `javap -c`, common opcodes (`invokevirtual`, `invokedynamic`, `checkcast`)
- [x] Memory leaks: causes, detection with heap dumps, `jmap`, `jstack`, VisualVM
- [x] Java Flight Recorder (JFR, open-sourced Java 11+): low-overhead continuous profiling; `jcmd <pid> JFR.start`; events, recordings, JDK Mission Control (JMC) analysis
- [x] `StackWalker` API (Java 9+): lazy, efficient stack traversal; `StackWalker.getInstance(Option.RETAIN_CLASS_REFERENCE).walk(...)`; replaces `Thread.getStackTrace()` for performance-sensitive code
- [x] `ProcessHandle` API (Java 9+): `ProcessHandle.current()`, `.pid()`, `.info()`, `.children()`, `.onExit()` (returns `CompletableFuture`); inspect and manage OS processes
- [x] `RandomGenerator` interface (Java 17+): common abstraction over all random algorithms; `RandomGeneratorFactory` for discovery; new algorithms: `Xoshiro256PlusPlus`, `L64X128MixRandom` (LXM family), `SplittableRandom`; `RandomGenerator.of("L64X128MixRandom")`
- [x] `HexFormat` (Java 17+): `HexFormat.of()` for formatting/parsing hex strings; `toHexDigits()`, `parseHex()`; replaces manual byte-to-hex loops or `DatatypeConverter`

**Reflection & Annotations**
- [x] `Class<?>` API: `getDeclaredFields()`, `getDeclaredMethods()`, `getAnnotation()`
- [x] `Method.invoke()`, `Field.set()` with `setAccessible(true)`
- [x] Custom annotations: `@Retention`, `@Target`, `@Inherited`, `@Repeatable`
- [x] Annotation processing at compile time vs runtime

**GoF Design Patterns — Creational**
> Goal: control object creation to increase flexibility and reuse.
- [x] **Singleton** — one instance per JVM; thread-safe options: eager init, `synchronized` method, double-checked locking (`volatile`), enum singleton, `Holder` (initialization-on-demand)
- [x] **Factory Method** — defines an interface for creating an object but lets subclasses decide which class to instantiate; e.g. `NumberFormat.getInstance()`
- [x] **Abstract Factory** — provides an interface for creating families of related objects without specifying concrete classes; e.g. UI toolkit factories
- [x] **Builder** — separates construction of a complex object from its representation; fluent API style; e.g. `StringBuilder`, `Stream.Builder`, Lombok `@Builder`
- [x] **Prototype** — creates new objects by cloning existing ones; `Cloneable` / `clone()` pitfalls; copy constructors as a safer alternative

**GoF Design Patterns — Structural**
> Goal: compose objects and classes into larger structures.
- [x] **Adapter** — converts an interface into another expected by the client; class adapter (inheritance) vs object adapter (composition); e.g. `Arrays.asList()` wrapping an array
- [x] **Bridge** — decouples abstraction from implementation so they can vary independently; e.g. JDBC driver abstraction over vendor implementations
- [x] **Composite** — treats individual objects and compositions uniformly via a tree structure; e.g. `java.awt.Container` / `Component`
- [x] **Decorator** — attaches additional responsibilities dynamically without subclassing; e.g. `BufferedInputStream` wrapping `FileInputStream`, `Collections.synchronizedList()`
- [x] **Facade** — provides a simplified interface to a complex subsystem; e.g. `javax.faces.context.FacesContext`, `SLF4J` over logging backends
- [x] **Flyweight** — shares common state among many fine-grained objects to reduce memory; e.g. `Integer.valueOf()` cache (−128..127), `String` interning
- [x] **Proxy** — provides a surrogate to control access, add lazy loading, logging, or security; types: static, JDK dynamic proxy (`InvocationHandler`), CGLIB subclass proxy; e.g. Spring AOP, Hibernate lazy-loaded entities

**GoF Design Patterns — Behavioral**
> Goal: define how objects communicate and distribute responsibility.
- [x] **Chain of Responsibility** — passes a request along a chain of handlers until one handles it; e.g. Servlet `FilterChain`, Spring Security filter chain, logging levels
- [x] **Command** — encapsulates a request as an object; supports undo/redo, queuing; e.g. `Runnable`, `javax.swing.Action`
- [x] **Interpreter** — defines a grammar and an interpreter for a language; e.g. `java.util.regex.Pattern`, SpEL (Spring Expression Language)
- [x] **Iterator** — provides sequential access to elements without exposing the underlying structure; e.g. `java.util.Iterator`, enhanced for-loop, `Spliterator`
- [x] **Mediator** — centralizes complex communication between objects; e.g. `ExecutorService` mediating between producers and consumers, Spring `ApplicationEventPublisher`
- [x] **Memento** — captures and restores an object's internal state without violating encapsulation; e.g. `Serializable` snapshots, undo stacks
- [x] **Observer** — defines a one-to-many dependency so dependents are notified on state change; e.g. `java.util.Observer` (deprecated), `PropertyChangeListener`, Reactor `Flux` subscribers
- [x] **State** — allows an object to alter its behavior when its internal state changes; e.g. `Thread` lifecycle states, TCP connection states
- [x] **Strategy** — defines a family of algorithms, encapsulates each, makes them interchangeable; e.g. `Comparator`, `java.util.function.*`, `LayoutManager`
- [x] **Template Method** — defines the skeleton of an algorithm in a base class, deferring steps to subclasses; e.g. `AbstractList`, `HttpServlet.service()`
- [x] **Visitor** — lets you add operations to an object structure without modifying it; e.g. `FileVisitor` (`Files.walkFileTree()`), AST visitors in annotation processors

**Design Patterns in the JDK (Spot-the-Pattern)**
> Recognizing patterns in the standard library reinforces both the patterns and the API.
- [x] **Singleton** — `Runtime.getRuntime()`, `System.console()`, `Desktop.getDesktop()`
- [x] **Factory Method** — `Calendar.getInstance()`, `NumberFormat.getInstance()`, `Charset.forName()`, `Path.of()`
- [x] **Builder** — `StringBuilder` / `StringBuffer`, `Stream.Builder`, `ProcessBuilder`, `HttpRequest.newBuilder()`
- [x] **Prototype** — `Object.clone()`, `ArrayList(Collection)` copy constructor
- [x] **Adapter** — `Arrays.asList()`, `Collections.enumeration()`, `InputStreamReader` (byte → char)
- [x] **Decorator** — `BufferedReader(Reader)`, `DataOutputStream(OutputStream)`, `Collections.unmodifiableList()`, `Collections.synchronizedList()`
- [x] **Flyweight** — `Integer.valueOf()` / `Boolean.valueOf()` caches, `String.intern()`
- [x] **Proxy** — `java.lang.reflect.Proxy`, RMI stubs, Spring AOP proxies
- [x] **Composite** — `java.awt.Container`, `javax.faces.component.UIComponent`
- [x] **Iterator** — `java.util.Iterator`, `Spliterator`, `Scanner`
- [x] **Observer** — `java.util.EventListener`, `PropertyChangeSupport`, `Flow.Publisher/Subscriber` (Java 9+)
- [x] **Strategy** — `Comparator`, `java.util.function.*`, `ThreadPoolExecutor.RejectedExecutionHandler`
- [x] **Template Method** — `AbstractList`, `AbstractMap`, `HttpServlet`, `TimerTask`
- [x] **Command** — `Runnable`, `Callable`, `java.awt.event.ActionListener`
- [x] **Chain of Responsibility** — `ClassLoader` delegation, `javax.servlet.FilterChain`
- [x] **Visitor** — `java.nio.file.FileVisitor`, `javax.lang.model.element.ElementVisitor`
- [x] **Facade** — `java.net.URL` (hides socket/protocol complexity), `javax.xml.parsers.DocumentBuilderFactory`

**Enterprise & Architectural Patterns (Advanced)**
- [x] **Dependency Injection / IoC** — container injects dependencies rather than objects creating them; constructor injection vs field injection vs setter injection; Spring IoC container
- [x] **Repository** — abstracts data access behind a collection-like interface; `JpaRepository`, domain vs persistence model separation
- [x] **Service Layer** — encapsulates business logic; `@Service`, transaction boundaries
- [x] **DTO (Data Transfer Object)** — carries data between process layers without behavior; mapping with MapStruct or ModelMapper
- [x] **Value Object** — immutable object defined by its attributes, not identity; Java `record` as value object
- [x] **Domain Event** — captures something that happened in the domain; `ApplicationEvent` in Spring, event sourcing intro
- [x] **CQRS (Command Query Responsibility Segregation)** — separate read and write models
- [x] **Circuit Breaker** — stops cascading failures by short-circuiting calls to a failing service; Resilience4j, Spring Cloud Circuit Breaker
- [x] **Retry & Backoff** — retry transient failures with exponential backoff + jitter; Resilience4j `@Retry`
- [x] **Bulkhead** — isolate failures by partitioning thread pools or semaphores per downstream service
- [x] **Outbox Pattern** — reliably publish domain events via a database outbox table and a poller/CDC mechanism

**Java Web — Frameworks & APIs (Advanced)**
- [x] Spring MVC: `DispatcherServlet`, `@Controller`, `@RestController`, `@RequestMapping`, handler chain
- [x] Spring Boot: auto-configuration, `@SpringBootApplication`, embedded server (Tomcat/Netty)
- [x] Spring Security: `SecurityFilterChain`, authentication manager, `UserDetailsService`, password encoders
- [x] Spring Security: JWT filter integration, method-level security (`@PreAuthorize`)
- [x] Spring Data JPA: `JpaRepository`, query derivation, `@Query`, transactions (`@Transactional`)
- [x] JAX-RS (Jakarta REST): `@Path`, `@GET/@POST`, `@Produces/@Consumes`, `@PathParam`, `@QueryParam`
- [x] WebSockets in Java: `@ServerEndpoint` (JSR-356), Spring WebSocket / STOMP
- [x] Server-Sent Events (SSE) with Spring (`SseEmitter`) or JAX-RS
- [x] Reactive web: Project Reactor (`Mono`, `Flux`), Spring WebFlux, non-blocking I/O model
- [x] gRPC in Java: Protobuf, generated stubs, unary vs streaming RPCs
- [x] API versioning strategies: URI path, `Accept` header, query param
- [x] Rate limiting and throttling patterns in Java web services

**Advanced Cryptography & PKI (Advanced)**
- [x] TLS/SSL handshake: certificate exchange, cipher suite negotiation, session keys
- [x] Java SSL/TLS: `SSLContext`, `TrustManager`, `KeyManager`, `SSLSocket`
- [x] Keystore and truststore: `JKS`, `PKCS12`; `keytool` commands
- [x] Certificate chains, root CA vs intermediate CA, certificate validation
- [x] Digital signatures: `java.security.Signature`; sign with private key, verify with public key
- [x] JCA (Java Cryptography Architecture): provider model, `Security.addProvider()`
- [x] JCE (Java Cryptography Extension): `Cipher`, `Mac`, `KeyAgreement` (Diffie-Hellman, ECDH)
- [x] AES-GCM in practice: IV/nonce uniqueness, `GCMParameterSpec`, authenticated encryption
- [x] Key derivation: PBKDF2 (`SecretKeyFactory`), HKDF
- [x] Secrets management: avoiding hardcoded secrets; environment variables, Vault, AWS Secrets Manager

---

### Expert
> Deep mastery. Goal: diagnose low-level issues, design language-level abstractions, and tune the JVM.

**Advanced JVM & Performance**
- [x] GC log analysis; GC pause optimization; `G1` region sizing
- [x] Escape analysis and stack allocation; scalar replacement
- [x] Object layout: header word, mark word, klass pointer, padding (JOL tool)
- [x] False sharing; `@Contended` annotation
- [x] `VarHandle` (Java 9+): typed memory access with configurable ordering modes
- [x] JVMTI and Java agents: `premain`, `agentmain`, bytecode instrumentation with ASM/ByteBuddy
- [x] AOT Class Loading & Linking (Java 24+, JEP 483): training run generates a class-data cache (`-XX:AOTCache=app.aot`); replay run restores pre-parsed and pre-linked class data; difference from CDS (Class Data Sharing) archives; impact on startup time
- [x] AOT Method Profiling (Java 24+, JEP 490): persisting JIT profile data across runs via profile dump so the JIT can optimize sooner on next startup

**Foreign Function & Memory API — Project Panama (Java 22+, finalized)**
- [x] Why Panama? Replacing `sun.misc.Unsafe` and JNI with a safe, performant, pure-Java API
- [x] `MemorySegment`: typed, bounded off-heap memory region; `Arena` for lifecycle management (confined, shared, auto, global)
- [x] `MemoryLayout` and `ValueLayout`: describing C struct layouts; `PathElement` for member access
- [x] `SegmentAllocator`: allocating structs and arrays in native memory
- [x] `Linker`: downcall handles (`Linker.nativeLinker().downcallHandle()`) to call native C functions from Java
- [x] `MethodHandles` + `FunctionDescriptor` for describing native function signatures
- [x] Upcall stubs: passing a Java `MethodHandle` as a C function pointer to native code
- [x] `SymbolLookup`: finding symbols in native libraries; `SymbolLookup.loaderLookup()` vs `libraryLookup()`
- [x] `jextract` tool: auto-generating Java bindings from C headers
- [x] Safety model: confined access, thread ownership, scope lifetimes, preventing use-after-free

**Class-File API (Java 24+, finalized, JEP 484)**
- [x] Purpose: standard JDK API for reading, writing, and transforming `.class` files; replaces need for ASM in many cases
- [x] `ClassFile.of()` entry point; `ClassModel`, `MethodModel`, `CodeModel`
- [x] Building a class: `ClassFile.build(ClassDesc, classBuilder -> { ... })`
- [x] Reading and inspecting bytecode: iterating `CodeElement`s, matching instructions
- [x] Transforming classes: `ClassFile.transformClass()` with a `ClassTransform`; composing transforms
- [x] `ConstantPoolBuilder`, `CodeBuilder`: emitting bytecode instructions
- [x] Comparison to ASM: shared `ClassFile` version tracking, no visitor pattern complexity

**Lock-Free & Non-Blocking Programming**
- [x] CAS semantics and the ABA problem; `AtomicStampedReference`
- [x] `LongAdder` / `LongAccumulator` vs `AtomicLong` under high contention
- [x] Memory ordering: plain, opaque, acquire/release, volatile access via `VarHandle`

**Virtual Threads (Java 21+)**
- [x] Platform threads vs virtual threads; M:N scheduling via the JVM carrier thread
- [x] `Thread.ofVirtual().start()`, `Thread.ofVirtual().name("name").unstarted(r)`, and `Executors.newVirtualThreadPerTaskExecutor()`
- [x] Pinning: `synchronized` blocks and `Object.wait()` pin carrier threads; `-Djdk.tracePinnedThreads=full` to detect pinning
- [x] Avoid pooling virtual threads; thread-per-request model with virtual threads
- [x] `Thread.sleep()` and blocking I/O correctly yield the carrier with virtual threads
- [x] Scoped Values as the virtual-thread-friendly alternative to `ThreadLocal` (see Advanced)

**Advanced Generics**
- [x] Type erasure: implications at runtime; bridge methods
- [x] Bounded wildcards: PECS (Producer Extends, Consumer Super)
- [x] Recursive type bounds: `<T extends Comparable<T>>`
- [x] Raw types; heap pollution; `@SuppressWarnings("unchecked")`

**Module System (JPMS, Java 9+)**
- [x] `module-info.java`: `requires`, `exports`, `opens`, `uses`, `provides`
- [x] Unnamed module vs automatic module vs named module
- [x] Strong encapsulation and reflection access (`--add-opens`)
- [x] `Flow` API (Java 9+, `java.util.concurrent.Flow`): `Publisher`, `Subscriber`, `Subscription`, `Processor`; standard reactive-streams interfaces; bridge to Project Reactor / RxJava via `FlowAdapters`
- [x] `ServiceLoader` (JPMS integration): `provides ... with` in `module-info.java`; `ServiceLoader.load(Service.class)` for plugin architectures; `findFirst()` and `stream()` on `ServiceLoader`

**Metaprogramming**
- [x] Compile-time annotation processors: `AbstractProcessor`, `JavacPlugin`
- [x] Dynamic proxies: `InvocationHandler`, limitations vs CGLIB/ByteBuddy
- [x] Ahead-of-time compilation: GraalVM Native Image constraints

**Security Hardening & Threat Modeling (Expert)**
- [x] Java Security Manager (deprecated Java 17, removed Java 18): replacement strategies
- [x] Secure deserialization: why `ObjectInputStream` is dangerous; use `ObjectInputFilter` / avoid altogether
- [x] Java serialization gadget chains and related CVEs (Log4Shell context)
- [x] SSRF (Server-Side Request Forgery): causes and mitigation in Java HTTP clients
- [x] XXE (XML External Entity) injection: disabling external entity processing in `DocumentBuilderFactory`
- [x] Dependency vulnerability scanning: OWASP Dependency-Check, Snyk, GitHub Dependabot
- [x] Supply chain security: verifying artifact signatures, SBOM (Software Bill of Materials)
- [x] Threat modeling basics: STRIDE model, attack surface analysis
- [x] Penetration testing concepts relevant to Java apps: DAST tools (OWASP ZAP, Burp Suite)
- [x] Audit logging: what to log, structured logs, protecting log integrity
- [x] mTLS (mutual TLS): client certificate authentication, configuring in Java
- [x] FIPS 140-2/3 compliance: approved algorithms, using FIPS-certified providers in Java
- [x] Quantum-resistant / Post-Quantum Cryptography (Java 24+, JEP 496 & 497): ML-KEM (CRYSTALS-Kyber) for key encapsulation; ML-DSA (CRYSTALS-Dilithium) for digital signatures; `KeyPairGenerator.getInstance("ML-DSA")`, `KEM.getInstance("ML-KEM-768")`; hybrid classical+PQC approach; NIST PQC standardization context

---

## Format

```
Front (question or term)[TAB]Back (answer or definition)
```

Lines starting with `#` are comments and are ignored on Anki import.
