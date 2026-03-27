import os

base_dir = r"c:\Users\MGamp\Documents\Anki\AnkiDecks\Java"
agg_dir = os.path.join(base_dir, "aggregated")
os.makedirs(agg_dir, exist_ok=True)

# Section rules per file: list of (marker_prefix_or_None, level)
# marker=None → default level from start of file
# When a line starts with a marker, the current level changes to its associated level
file_rules = {
    "java_basics.txt": [
        (None, "Beginner"),
        ("# === String & Type System ===", "Intermediate"),
        ("# === From java_advanced_anki_expanded ===", "Pro"),
    ],
    "java_oop.txt": [
        (None, "Beginner"),
        ("# === Modern OOP Features ===", "Intermediate"),
        ("# === Binding, Typing & Initialisation ===", "Pro"),
    ],
    "java_exceptions.txt": [
        (None, "Beginner"),
        ("# === Intermediate ===", "Intermediate"),
        ("# === From java_advanced_anki_expanded ===", "Intermediate"),
    ],
    "java_functional.txt": [
        (None, "Intermediate"),
    ],
    "java_collections.txt": [
        (None, "Beginner"),
        ("# === Internals & Modern API ===", "Intermediate"),
        ("# === From java_advanced_anki_expanded ===", "Intermediate"),
    ],
    "java_concurrency.txt": [
        (None, "Beginner"),
        ("# === Advanced Concurrency ===", "Pro"),
        ("# === From java_advanced_anki_expanded ===", "Intermediate"),
    ],
    "java_generics_advanced.txt": [
        (None, "Pro"),
        ("# === From java_advanced_anki_expanded ===", "Intermediate"),
    ],
    "java_io_nio.txt": [
        (None, "Intermediate"),
        ("# === NIO Channels", "Pro"),
        ("# === From java_advanced_anki_expanded ===", "Intermediate"),
    ],
    "java_reflection.txt": [
        (None, "Pro"),
    ],
    "java_jvm.txt": [
        (None, "Intermediate"),
        ("# === Expert JVM ===", "Pro"),
        ("# === From java_advanced_anki_expanded ===", "Intermediate"),
    ],
    "java_testing.txt": [
        (None, "Intermediate"),
    ],
    "java_design_patterns.txt": [
        (None, "Pro"),
    ],
    "java_modules.txt": [
        (None, "Pro"),
    ],
    "java_datetime.txt": [
        (None, "Intermediate"),
    ],
    "java_regex.txt": [
        (None, "Intermediate"),
    ],
    "java_build_tools.txt": [
        (None, "Intermediate"),
    ],
    "java_classfile_api.txt": [
        (None, "Pro"),
    ],
    "java_cryptography.txt": [
        (None, "Intermediate"),
    ],
    "java_cryptography_advanced.txt": [
        (None, "Pro"),
    ],
    "java_di.txt": [
        (None, "Intermediate"),
    ],
    "java_enterprise_patterns.txt": [
        (None, "Pro"),
    ],
    "java_i18n.txt": [
        (None, "Intermediate"),
    ],
    "java_jdbc.txt": [
        (None, "Intermediate"),
    ],
    "java_jmh.txt": [
        (None, "Pro"),
    ],
    "java_lock_free.txt": [
        (None, "Pro"),
    ],
    "java_logging.txt": [
        (None, "Intermediate"),
    ],
    "java_messaging.txt": [
        (None, "Intermediate"),
    ],
    "java_metaprogramming.txt": [
        (None, "Pro"),
    ],
    "java_networking.txt": [
        (None, "Intermediate"),
        ("# Netty", "Pro"),
    ],
    "java_observability.txt": [
        (None, "Intermediate"),
    ],
    "java_panama.txt": [
        (None, "Pro"),
    ],
    "java_security_awareness.txt": [
        (None, "Beginner"),
    ],
    "java_security_hardening.txt": [
        (None, "Pro"),
    ],
    "java_virtual_threads.txt": [
        (None, "Pro"),
    ],
    "java_web_frameworks.txt": [
        (None, "Pro"),
    ],
    "java_web_fundamentals.txt": [
        (None, "Intermediate"),
    ],
    "java_web_security.txt": [
        (None, "Intermediate"),
    ],
    "java_xml.txt": [
        (None, "Intermediate"),
    ],
}

# Per-question level overrides (match by startswith on the question front)
question_overrides = {
    # === java_oop.txt: Pro section overrides to Intermediate ===
    "What are the SOLID principles": "Intermediate",
    "What are private interface methods (Java 9+)": "Intermediate",
    "What are Record Patterns (Java 21+)": "Intermediate",

    # === java_concurrency.txt: From section overrides ===
    "What is CAS (Compare-And-Swap) and what is the ABA problem": "Pro",
    "What is double-checked locking (DCL)": "Pro",
    "What is the difference between `thenApply()` and `thenCompose()`": "Pro",

    # === java_jvm.txt: From section overrides to Pro ===
    "What is method inlining in the JIT compiler": "Pro",
    "What is HotSpot's tiered compilation": "Pro",
    "What is the difference between G1GC": "Pro",
    "What is a custom ClassLoader used for": "Pro",

    # === java_testing.txt: some basics should be Beginner ===
    "What annotation marks a JUnit 5 test method": "Beginner",
    "What are the three JUnit 5 modules": "Beginner",
    "What is the JUnit 5 equivalent of JUnit 4": "Beginner",
    "What does `@BeforeEach` do": "Beginner",
    "What does `@AfterEach` do": "Beginner",
    "What does `@AfterAll` do": "Beginner",
    "How do you disable a test": "Beginner",
    "What does `@DisplayName` do": "Beginner",
    "How does `@Nested` help": "Beginner",
    "What class provides assertions in JUnit 5": "Beginner",
    "How do you assert that a method throws": "Beginner",
    "What does `assertAll` do": "Beginner",
    "What is Mockito used for": "Beginner",
    "How do you create a mock in Mockito": "Beginner",
    "What is the AAA (Arrange-Act-Assert) pattern": "Beginner",
    "What is the difference between a unit test and an integration test": "Beginner",
    "What is a test fixture": "Beginner",
    "What is test isolation and why does it matter": "Beginner",

    # === java_build_tools.txt: some basics should be Beginner ===
    "What is Maven?": "Beginner",
    "What is Gradle?": "Beginner",
    "What is the Maven build lifecycle": "Beginner",
    "What does `mvn package` do": "Beginner",
    "What does `mvn install` do": "Beginner",
    "What does `mvn clean` do": "Beginner",
    "What are Maven coordinates": "Beginner",
    "What is the Gradle wrapper": "Beginner",
    "What is the Gradle build file": "Beginner",
    "What is the Maven local repository": "Beginner",

    # === java_logging.txt: some basics should be Beginner ===
    "What are the standard log levels": "Beginner",
    "What is the logging facade pattern": "Beginner",
    "Name the main Java logging frameworks": "Beginner",
    "How do you create an SLF4J logger": "Beginner",

    # === java_web_fundamentals.txt: HTTP basics should be Beginner ===
    "What are the main HTTP methods": "Beginner",
    "What are the key HTTP status code categories": "Beginner",
    "What are the components of a URL": "Beginner",

    # === java_messaging.txt: fundamentals should be Beginner ===
    "What is asynchronous messaging and why use it": "Beginner",
    "What is the difference between a message queue and a publish-subscribe topic": "Beginner",
    "What is at-most-once, at-least-once, and exactly-once delivery": "Beginner",

    # === java_networking.txt: basic concepts should be Beginner ===
    "What is a TCP socket in Java": "Beginner",
    "When is UDP preferred over TCP": "Beginner",

    # === java_observability.txt: pillar concepts ===
    "What are the three pillars of observability": "Beginner",
    "What is the difference between monitoring and observability": "Beginner",

    # === java_web_security.txt: OWASP concepts ===
    "What is the OWASP Top 10": "Beginner",

    # === java_cryptography.txt: concepts should be Beginner ===
    "What is the difference between hashing, encoding, and encryption": "Beginner",
    "What is symmetric vs asymmetric encryption": "Beginner",
    "What is a cryptographic hash function": "Beginner",
    "Why are MD5 and SHA-1 not suitable": "Beginner",

    # === java_di.txt: JSR-330 basics ===
    "What is JSR-330": "Beginner",
    "What does `@Inject` do": "Beginner",

    # === java_i18n.txt: basic concepts ===
    "What is i18n vs l10n": "Beginner",
    "What is a `Locale` in Java": "Beginner",

    # === java_jdbc.txt: basic concepts ===
    "What is JDBC?": "Beginner",
    "What are the four types of JDBC drivers": "Beginner",
    "What is the difference between `Statement`, `PreparedStatement`": "Beginner",
    "Why should you always use `PreparedStatement`": "Beginner",

    # === java_datetime.txt: basic concepts ===
    "Why was `java.time`": "Beginner",

    # === java_regex.txt: basics ===
    "What are the two main classes in `java.util.regex`": "Beginner",
    "How do you compile and use a regex": "Beginner",

    # === java_design_patterns.txt: common patterns should be Intermediate ===
    "What is the Singleton pattern": "Intermediate",
    "What is the Builder pattern": "Intermediate",
    "What is the Factory Method pattern": "Intermediate",
    "What is the Strategy pattern": "Intermediate",
    "What is the Observer pattern": "Intermediate",
    "What is the Adapter pattern": "Intermediate",
    "What is the Decorator pattern": "Intermediate",
    "What is the Template Method pattern": "Intermediate",

    # === java_xml.txt: basics ===
    "What are the four main Java XML processing APIs": "Beginner",
    "When should you use DOM vs SAX vs StAX": "Beginner",

    # === java_enterprise_patterns.txt: foundational concepts are Intermediate ===
    "What is Dependency Injection (DI) and Inversion of Control (IoC)": "Intermediate",
    "What is the Repository pattern": "Intermediate",
    "What is the Service Layer pattern": "Intermediate",
    "What is a DTO (Data Transfer Object)": "Intermediate",
    "What is a Value Object": "Intermediate",
}

beginner_qs = []
intermediate_qs = []
pro_qs = []

for filename, rules in file_rules.items():
    filepath = os.path.join(base_dir, filename)
    if not os.path.exists(filepath):
        print(f"Skipping {filename} - not found")
        continue

    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    lines = content.split('\n')

    # Determine default level
    current_level = "Intermediate"
    for marker, level in rules:
        if marker is None:
            current_level = level
            break

    new_lines = []

    for line in lines:
        stripped = line.strip()

        # Check if this line is a section marker that changes level
        for marker, level in rules:
            if marker is not None and stripped.startswith(marker):
                current_level = level
                break

        # Is this a question line? (contains tab, not a comment)
        if '\t' in line and not stripped.startswith('#'):
            # Determine level - check per-question overrides first
            level = current_level
            for override_start, override_level in question_overrides.items():
                if stripped.startswith(override_start):
                    level = override_level
                    break

            # Add labeled version to new file
            new_lines.append(f"[{level}] {line}")

            # Add to aggregated list
            if level == "Beginner":
                beginner_qs.append(line.strip())
            elif level == "Intermediate":
                intermediate_qs.append(line.strip())
            else:
                pro_qs.append(line.strip())
        else:
            new_lines.append(line)

    # Write labeled file back
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write('\n'.join(new_lines))

# Write aggregated files
for level_name, questions in [("beginner", beginner_qs), ("intermediate", intermediate_qs), ("pro", pro_qs)]:
    filepath = os.path.join(agg_dir, f"{level_name}.txt")
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(f"# Java {level_name.capitalize()} Questions\n")
        f.write("# Format: Front[TAB]Back\n\n")
        for q in questions:
            f.write(q + '\n')

print(f"Done!")
print(f"Beginner: {len(beginner_qs)}")
print(f"Intermediate: {len(intermediate_qs)}")
print(f"Pro: {len(pro_qs)}")
print(f"Total: {len(beginner_qs) + len(intermediate_qs) + len(pro_qs)}")
