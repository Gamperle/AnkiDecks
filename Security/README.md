# Security Anki Decks — Topic Index

Comprehensive security topics for coding, web development, and embedded development, classified by difficulty level.

---

## Beginner

### General Security Fundamentals
- CIA Triad (Confidentiality, Integrity, Availability)
- Least Privilege Principle
- Defense in Depth
- Security vs. Obscurity
- Threat Modeling Basics (STRIDE)
- Common Vulnerability Scoring System (CVSS) overview
- Reading CVE entries

### Authentication & Authorization Basics
- Passwords — hashing, salting, storage best practices
- Multi-Factor Authentication (MFA) concepts
- Session management fundamentals (cookies, session IDs)
- Role-Based Access Control (RBAC) basics
- OAuth 2.0 / OpenID Connect overview

### TLS & Transport Security Basics
- What is TLS and why it replaced SSL
- TLS versions overview — SSL 3.0, TLS 1.0/1.1 (deprecated), TLS 1.2, TLS 1.3
- Symmetric vs. asymmetric encryption in TLS (high-level)
- What is a certificate and what does it prove
- Certificate Authorities (CAs) — what they do, trust anchors
- How HTTPS works — URL bar padlock, what it guarantees and what it doesn't
- Self-signed certificates vs. CA-signed certificates
- Let's Encrypt — free automated certificates
- Common TLS errors — expired cert, hostname mismatch, untrusted CA
- HTTP vs. HTTPS — what travels in plaintext

### Web Security Fundamentals
- Same-Origin Policy (SOP)
- HTTPS / TLS basics — why encryption matters
- HTTP security headers overview (HSTS, X-Content-Type-Options, X-Frame-Options)
- Cross-Site Scripting (XSS) — what it is, reflected vs. stored vs. DOM-based
- Cross-Site Request Forgery (CSRF) — what it is and token-based prevention
- SQL Injection — what it is, parameterized queries
- Input validation and output encoding principles
- Content Security Policy (CSP) basics
- Secure cookie attributes (HttpOnly, Secure, SameSite)

### Memory & Process Security Basics
- What is a buffer overflow — concept and why it's dangerous
- Stack vs. heap — basic memory layout of a process
- Why C/C++ are memory-unsafe vs. managed languages (Java, C#, Rust)
- What is a segmentation fault and what causes it
- Dangling pointers and use-after-free — concept
- Null pointer dereference — what happens and why it matters
- Memory leaks — what they are, impact on availability
- Why you should never store secrets in plaintext in memory longer than needed
- Address Space Layout Randomization (ASLR) — what it does at a high level
- Data Execution Prevention (DEP) / NX bit — concept
- Managed memory — how garbage collectors prevent memory bugs
- Safe string handling — why `strcpy` is dangerous, safer alternatives

### Secure Coding Basics
- Input validation — allowlists vs. denylists
- Avoiding hardcoded secrets and credentials
- Error handling — safe error messages vs. information leakage
- Dependency management — keeping libraries up to date
- OWASP Top 10 overview
- Static Application Security Testing (SAST) — concept and basic tools
- Code review for security — what to look for

### Unix / Linux Security Basics
- File permissions — owner, group, other; read, write, execute (`chmod`, `chown`)
- The root user — why running as root is dangerous
- `sudo` — what it does, `/etc/sudoers` basics
- Users and groups — `/etc/passwd`, `/etc/shadow`, `/etc/group`
- File permission special bits — setuid, setgid, sticky bit
- SSH basics — key-based vs. password authentication
- Firewall basics — `iptables` / `nftables` / `ufw` overview
- File integrity — what `/etc` files should not change
- Package manager security — signed packages, trusted repositories
- Log files — `/var/log/auth.log`, `/var/log/syslog`, why logging matters
- World-readable/writable files — why they're dangerous
- Cron jobs — permission model, security considerations

### Java Security Basics
- Java Security Manager — concept (deprecated in Java 17, removed in 21)
- The sandbox model — how the JVM restricts untrusted code
- Input validation in Java — `String` sanitization, avoiding injection
- Secure random numbers — `SecureRandom` vs. `Random`
- Serialization dangers — why `ObjectInputStream` is risky
- SQL injection prevention — `PreparedStatement` vs. string concatenation
- Dependency vulnerabilities — checking JARs with OWASP Dependency-Check
- Password storage — using bcrypt/scrypt/Argon2 via libraries (jBCrypt, Bouncy Castle)
- HTTPS in Java — `HttpsURLConnection`, trusting certificates
- Exception handling — not leaking stack traces to users
- Classpath and JAR loading — untrusted code risks
- Logging secrets — why `toString()` on sensitive objects is dangerous

### Android Security Basics
- Android permission model — install-time vs. runtime permissions, `AndroidManifest.xml`
- Principle of least privilege on Android — requesting only needed permissions
- App sandboxing — each app runs as its own Linux user, isolated `/data/data/<pkg>`
- Secure data storage — `SharedPreferences` vs. `EncryptedSharedPreferences`, avoiding external storage for secrets
- HTTPS enforcement — `android:usesCleartextTraffic="false"`, Network Security Config
- WebView security basics — JavaScript injection risks, `setAllowFileAccess(false)`
- Intent security — explicit vs. implicit intents, exported components
- Logging sensitive data — why `Log.d()` with secrets is dangerous in production
- APK signing — why apps must be signed, debug vs. release keys
- Google Play Protect — what it scans for
- Root detection awareness — what rooted devices mean for app security
- Secure coding with `ContentProvider` — don't expose sensitive data unintentionally

### Automotive Security Basics
- Vehicle network overview — CAN bus, LIN, FlexRay, Ethernet in vehicles
- Why vehicle security matters — safety-critical systems, remote attack surface
- CAN bus fundamentals — broadcast protocol, no authentication by default
- ECU (Electronic Control Unit) — what it is, how many are in a modern car
- OBD-II port — what it exposes, diagnostic access
- Over-the-air updates — why signing and verification matter for vehicles
- Vehicle connectivity — Bluetooth, Wi-Fi, cellular (telematics), attack surface expansion
- Key fob / keyless entry — how it works, relay attack concept
- Basic automotive standards — ISO 26262 (functional safety), introduction to ISO/SAE 21434
- V2X (Vehicle-to-Everything) communication — concept and why security matters
- Infotainment system isolation — why head units should be separated from safety-critical networks
- Physical access attacks — OBD-II dongles, USB ports, aftermarket devices

### Embedded Security Basics
- Physical security considerations
- Secure boot concept
- Firmware update basics — why signing matters
- Default credentials and why they're dangerous
- Serial/debug port exposure (UART, JTAG)
- Basic network segmentation for IoT devices

---

## Intermediate

### TLS & Transport Security (In Depth)
- TLS 1.2 handshake — full walkthrough (ClientHello, ServerHello, key exchange, Finished)
- TLS 1.3 handshake — 1-RTT and 0-RTT, removed features (static RSA, CBC cipher suites)
- Cipher suites — naming convention, components (key exchange, bulk cipher, MAC, PRF)
- TLS 1.2 recommended cipher suites (ECDHE + AES-GCM, CHACHA20-POLY1305)
- TLS 1.3 cipher suites (TLS_AES_128_GCM_SHA256, TLS_AES_256_GCM_SHA384, TLS_CHACHA20_POLY1305_SHA256)
- ALPN (Application-Layer Protocol Negotiation) — what it is, how it selects HTTP/2 vs HTTP/1.1
- SNI (Server Name Indication) — how virtual hosting works with TLS, privacy concerns
- HSTS (HTTP Strict Transport Security) — preload lists, max-age, includeSubDomains
- Certificate chains — leaf, intermediate, root; chain building and validation
- Certificate pinning — what it is, HPKP (deprecated), pin-sha256, mobile app pinning
- OCSP and CRL — certificate revocation checking, OCSP stapling
- Diffie-Hellman key exchange — DHE vs. ECDHE, forward secrecy
- Perfect Forward Secrecy (PFS) — why ephemeral keys matter
- mTLS (mutual TLS) — client certificates, use cases (service-to-service, zero trust)
- TLS termination — where to terminate (load balancer, reverse proxy, application)
- SSL/TLS testing tools — SSL Labs, testssl.sh, openssl s_client
- Common TLS misconfigurations — weak cipher suites, missing intermediate certs, protocol downgrade

### Cryptography
- Symmetric vs. asymmetric encryption
- AES — modes of operation (CBC, GCM, CTR)
- RSA — key generation, padding schemes (OAEP vs. PKCS#1 v1.5)
- Elliptic Curve Cryptography (ECC) overview
- Hash functions — SHA-256, SHA-3, collision resistance
- HMAC — message authentication codes
- Key Derivation Functions (PBKDF2, bcrypt, scrypt, Argon2)
- Digital signatures — how they work, verification
- Certificate chains and PKI fundamentals
- Random number generation — CSPRNG vs. PRNG

### Web Application Security (Advanced)
- OWASP Top 10 in depth — each vulnerability with exploitation and mitigation
- Server-Side Request Forgery (SSRF)
- XML External Entity (XXE) injection
- Insecure Direct Object References (IDOR)
- File upload vulnerabilities
- Path traversal / directory traversal
- HTTP request smuggling basics
- Clickjacking and frame-busting techniques
- Subresource Integrity (SRI)
- CORS — misconfigurations and security implications
- Open redirect vulnerabilities
- Mass assignment / parameter pollution
- Rate limiting and brute-force protection
- Security logging and monitoring — what to log, SIEM basics

### Authentication & Session Security (Advanced)
- JWT — structure, signing (HS256 vs. RS256), common vulnerabilities (alg:none, key confusion)
- Token storage strategies (localStorage vs. cookie vs. memory)
- Session fixation attacks
- Credential stuffing and password spraying
- Account enumeration prevention
- SSO and federated identity security
- SAML — basics and common attack vectors
- Passwordless authentication (WebAuthn / FIDO2)
- Refresh token rotation and revocation

### API Security
- REST API security best practices
- API authentication — API keys, OAuth 2.0 client credentials
- GraphQL security — introspection, query depth/complexity limits, batching attacks
- Rate limiting and throttling strategies
- Input validation for APIs — schema validation (JSON Schema, OpenAPI)
- CORS for APIs
- API versioning and deprecation security considerations
- gRPC security — TLS, authentication interceptors

### Network & Infrastructure Security
- Firewall rules and network segmentation
- DNS security — DNS spoofing, DNSSEC
- VPN fundamentals
- SSH key management and hardening
- Container security — image scanning, least privilege, seccomp profiles
- Kubernetes security basics — RBAC, network policies, pod security
- Cloud security fundamentals (IAM, security groups, encryption at rest)
- Infrastructure as Code security (Terraform, CloudFormation scanning)

### Memory & Process Security (In Depth)
- Process memory layout — text, data, BSS, heap, stack, kernel space
- Stack-based buffer overflow — how it works, overwriting return addresses
- Heap-based buffer overflow — heap metadata corruption, exploitation
- Stack canaries / stack guards — how they detect buffer overflows
- ASLR in depth — how randomization works, entropy, limitations
- DEP / W^X (Write XOR Execute) — marking memory pages non-executable
- Position-Independent Executables (PIE) — why ASLR needs PIE
- Format string vulnerabilities — `%n`, `%x`, reading/writing arbitrary memory
- Integer overflow and underflow — how they lead to buffer overflows
- Use-after-free exploitation — dangling pointers, heap spraying
- Double-free vulnerabilities — heap corruption attacks
- Type confusion attacks — casting errors leading to memory corruption
- Memory-safe languages — Rust ownership/borrow checker, Go bounds checking
- AddressSanitizer (ASan) and MemorySanitizer (MSan) — runtime detection tools
- Valgrind — memory error detection, how it works
- OS process isolation — virtual memory, page tables, user vs. kernel mode
- Inter-process communication (IPC) security — shared memory, pipes, message queues
- Memory-mapped files — security considerations, permissions
- Secrets in memory — zeroing buffers after use, `SecureString`, `mlock()`
- Core dumps — disabling or securing them to prevent secret leakage
- Compiler mitigations — `-fstack-protector`, `-D_FORTIFY_SOURCE`, RELRO

### Secure Development Lifecycle
- Dynamic Application Security Testing (DAST)
- Software Composition Analysis (SCA) — detecting vulnerable dependencies
- Secret scanning in CI/CD pipelines
- Security requirements and abuse cases
- Secure code review methodologies
- Penetration testing basics — methodology and scope
- Bug bounty programs — how they work
- Security champions program

### Unix / Linux Security (In Depth)
- PAM (Pluggable Authentication Modules) — how authentication stacks work
- SELinux — mandatory access control, contexts, policies, enforcing vs. permissive
- AppArmor — profile-based MAC, confining applications
- `chroot` jails — isolation basics, limitations, escaping chroot
- Namespace isolation — PID, network, mount, user namespaces (foundation of containers)
- cgroups — resource limits, preventing denial-of-service from rogue processes
- Capabilities — splitting root privileges (`CAP_NET_BIND_SERVICE`, `CAP_SYS_ADMIN`, etc.)
- `seccomp` and `seccomp-BPF` — syscall filtering
- File ACLs — `setfacl` / `getfacl`, fine-grained permissions beyond owner/group/other
- Auditd — Linux audit framework, writing audit rules, log analysis
- Hardening SSH — disabling root login, key-only auth, `AllowUsers`, fail2ban
- Kernel hardening — sysctl settings (`randomize_va_space`, `dmesg_restrict`, `ptrace_scope`)
- /proc and /sys security — information leakage, restricting access
- Umask — default permission masks, secure defaults
- Systemd service hardening — `ProtectSystem`, `NoNewPrivileges`, `PrivateTmp`, sandboxing units
- tmpfiles and world-writable /tmp — symlink attacks, sticky bit, private /tmp
- SUID binary auditing — finding and minimizing setuid programs

### Java Security (In Depth)
- Java Cryptography Architecture (JCA) — providers, `Cipher`, `MessageDigest`, `KeyPairGenerator`
- Java Cryptography Extension (JCE) — unlimited strength policy, provider ordering
- TLS in Java — `SSLContext`, `SSLSocketFactory`, configuring protocols and cipher suites
- Keystores and truststores — JKS, PKCS12, `keytool` commands, loading programmatically
- Certificate validation — `TrustManager`, custom validation, pinning in Java
- JSSE (Java Secure Socket Extension) — SNI, ALPN configuration, debugging with `-Djavax.net.debug=ssl`
- XML security — XXE prevention (`DocumentBuilderFactory` features), XML signature validation
- Deserialization attacks — gadget chains, `ObjectInputStream` exploits, look-ahead deserialization
- Serialization filters — JEP 290 (`ObjectInputFilter`), allowlisting classes
- Secure coding with `String` — immutability for sensitive data, `char[]` for passwords
- Access control — `AccessController` (legacy), module system (`java.base` encapsulation)
- Java module system security — strong encapsulation, `--add-opens` risks
- JDBC security — connection string injection, credential management
- Reflection and security — `setAccessible(true)`, module boundaries, `Unsafe`
- Bouncy Castle — advanced crypto provider, PGP, CMS, post-quantum algorithms
- Secure class loading — classloader isolation, code signing (`jarsigner`), sealed packages
- GraalVM / native-image security — reduced attack surface, reflection configuration, closed-world assumption
- Spring Security overview — filter chain, authentication providers, method security

### Android Security (In Depth)
- Network Security Configuration — pinning certificates, custom trust anchors, domain-specific policies
- Android Keystore system — hardware-backed keys, `KeyGenParameterSpec`, biometric-bound keys
- Biometric authentication — `BiometricPrompt` API, `CryptoObject`, fallback handling
- Content Provider security — `android:permission`, `grantUriPermission`, SQL injection in providers
- Broadcast Receiver security — ordered broadcasts, `LocalBroadcastManager` (deprecated), registered vs. manifest receivers
- Pending Intent security — mutable vs. immutable, hijacking risks, `FLAG_IMMUTABLE`
- Deep link / App Link validation — intent-filter verification, URL hijacking
- ProGuard / R8 — code obfuscation, shrinking, anti-reverse-engineering basics
- Root detection and SafetyNet/Play Integrity API — attestation, device integrity checks
- Secure IPC — `Binder` security, `Messenger`, AIDL permission checks
- File-Based Encryption (FBE) and Full Disk Encryption (FDE) — Direct Boot, device-encrypted vs. credential-encrypted storage
- Scoped storage (Android 10+) — `MediaStore`, `SAF`, security implications
- Android for Work / managed profiles — work profile isolation, device admin policies
- `StrictMode` and security linting — detecting insecure patterns at dev time
- OWASP Mobile Top 10 — overview and Android-specific mitigations
- WebView hardening — disabling file access, safe browsing, `WebViewClient` overrides
- Tapjacking — overlay attacks, `filterTouchesWhenObscured`

### Automotive Security (In Depth)
- CAN bus security — message spoofing, bus-off attacks, replay attacks
- CAN bus intrusion detection — anomaly detection, message frequency analysis
- UDS (Unified Diagnostic Services) — security access levels, seed-key authentication
- Secure boot for ECUs — hardware root of trust, chain of trust verification
- Automotive Ethernet security — MACsec, VLAN segmentation, IP-based protocols in vehicles
- Gateway ECU — bridging CAN domains, firewall rules between vehicle networks
- OTA update security — code signing, delta updates, rollback protection, A/B partitioning
- ISO/SAE 21434 — automotive cybersecurity engineering, TARA (Threat Analysis and Risk Assessment)
- AUTOSAR security modules — SecOC (Secure Onboard Communication), Crypto Service Manager
- Telematics security — cellular modem isolation, remote command authentication
- Key fob attacks in depth — relay attacks, rolling codes, RollJam, signal jamming
- Bluetooth and Wi-Fi attack surface — BLE pairing weaknesses, Wi-Fi hotspot isolation
- HSM in automotive — SHE (Secure Hardware Extension), EVITA HSM, key management in ECUs
- Aftermarket device risks — OBD-II dongle vulnerabilities, third-party telematics
- UNECE WP.29 / R155 — UN regulation on vehicle cybersecurity management systems
- Vehicle SOC (Security Operations Center) — monitoring fleet-wide anomalies

### Embedded Security (Intermediate)
- Secure boot chain — Root of Trust, chain verification
- Firmware signing and verification
- Secure OTA (Over-The-Air) update mechanisms
- Hardware Security Modules (HSM) and Trusted Platform Modules (TPM)
- Secure key storage on embedded devices
- Communication security — TLS on constrained devices (mbed TLS, wolfSSL)
- Memory protection units (MPU) — preventing code execution from data regions
- Buffer overflow basics on embedded targets (stack smashing)
- RTOS security considerations
- Common Weakness Enumeration (CWE) for embedded (CWE-119, CWE-120, CWE-787)
- IoT protocol security — MQTT, CoAP, Zigbee, BLE pairing

---

## Pro

### Advanced TLS & Protocol Security
- TLS 1.3 internals — key schedule (HKDF-Extract, HKDF-Expand), transcript hash, PSK modes
- 0-RTT (early data) — replay attack risks, anti-replay mechanisms, when to allow
- Encrypted Client Hello (ECH) — privacy extension, replacing ESNI
- ALPN in depth — protocol negotiation internals, custom protocol IDs, interaction with HTTP/2 and HTTP/3
- SNI encryption — ECH deployment, DNS-over-HTTPS synergy
- TLS session resumption — session tickets vs. session IDs, PSK-based resumption in TLS 1.3
- Downgrade attack prevention — TLS_FALLBACK_SCSV, TLS 1.3 anti-downgrade sentinel
- BEAST, POODLE, CRIME, BREACH — historical TLS attacks and their mitigations
- Heartbleed — OpenSSL vulnerability, impact, lessons for memory safety
- Renegotiation attacks — client-initiated renegotiation, RFC 5746 secure renegotiation
- Certificate Transparency (CT) — SCTs, CT logs, enforcement in browsers
- DANE (DNS-Based Authentication of Named Entities) — TLSA records, interaction with DNSSEC
- Delegated credentials — short-lived TLS credentials for CDNs
- QUIC / HTTP/3 transport security — TLS 1.3 integration, connection migration, 0-RTT
- TLS in non-HTTP contexts — STARTTLS (SMTP, IMAP), DTLS for UDP, TLS for databases
- Custom cipher suite policy enforcement — compliance scanning, organiztional baselines
- Key transparency and Merkle-tree based certificate verification
- Post-quantum TLS — hybrid key exchange (X25519Kyber768), NIST PQC integration timeline

### Advanced Cryptography
- Post-quantum cryptography — lattice-based, hash-based, code-based schemes
- Cryptographic protocol analysis — formal verification basics
- Side-channel attacks — timing attacks, power analysis, cache attacks
- Key management at scale — rotation, escrow, HSM integration
- Threshold cryptography and secret sharing (Shamir's)
- Zero-Knowledge Proofs — concepts and applications
- Homomorphic encryption overview
- Certificate Transparency and CT logs
- Cryptographic agility — preparing for algorithm migration

### Advanced Web & Application Security
- Deserialization attacks (Java, .NET, PHP, Python)
- Server-Side Template Injection (SSTI)
- Prototype pollution (JavaScript)
- Race conditions and TOCTOU vulnerabilities in web apps
- WebSocket security — origin validation, message integrity
- Browser security internals — process isolation, site isolation
- Supply chain attacks — dependency confusion, typosquatting
- Subdomain takeover
- HTTP/2 and HTTP/3 security considerations
- Advanced CSP — nonce-based, strict-dynamic, bypasses
- DOM clobbering
- Cache poisoning (web cache, DNS cache)
- Business logic vulnerabilities — detection and prevention

### Advanced Authentication & Identity
- OAuth 2.0 advanced flows — PKCE, DPoP, token binding
- OpenID Connect — ID token validation, claims, hybrid flows
- FIDO2 / WebAuthn internals — attestation, assertion, resident keys
- Identity federation at scale — multi-tenant, cross-domain
- Decentralized identity (DIDs, Verifiable Credentials)
- Risk-based / adaptive authentication systems
- Privileged Access Management (PAM)

### Advanced Memory Exploitation & Protection
- Return-Oriented Programming (ROP) — gadgets, chaining, bypassing DEP
- Jump-Oriented Programming (JOP) and Call-Oriented Programming (COP)
- Heap exploitation techniques — tcache poisoning, house of force, fastbin attack, unsorted bin attack
- ASLR bypasses — information leaks, partial overwrites, brute forcing (32-bit)
- Stack pivoting — redirecting the stack pointer for ROP
- Control-Flow Integrity (CFI) — forward-edge and backward-edge protection
- Shadow stacks — hardware-assisted return address protection (Intel CET, ARM BTI)
- Memory tagging — ARM MTE (Memory Tagging Extension), SPARC ADI
- Intel MPX, MPK — memory protection keys and bounds checking
- Spectre and Meltdown — speculative execution attacks, microarchitectural side channels
- Rowhammer — DRAM bit-flip attacks, exploitation for privilege escalation
- Kernel ASLR (KASLR) — protecting the kernel address space
- Sandboxing and process isolation — seccomp-BPF, AppArmor, SELinux, pledge/unveil
- Browser process sandboxing — renderer isolation, site isolation, V8 sandbox
- Memory encryption — AMD SME/SEV, Intel TME/MKTME, ARM Realm Management
- Encrypted virtual machines — confidential computing, attestation
- Runtime Application Self-Protection (RASP) — memory-level anomaly detection
- JIT spraying — exploiting just-in-time compilers for code execution
- Heap isolation — PartitionAlloc (Chrome), jemalloc hardening, scudo allocator
- Memory forensics — Volatility framework, analyzing process memory dumps

### Unix / Linux Security (Advanced)
- Kernel exploitation — privilege escalation via kernel vulnerabilities, dirty COW, dirty pipe
- eBPF security — using eBPF for runtime security monitoring, LSM hooks
- Seccomp deep dive — writing custom BPF filters, Kafel DSL
- Rootkit detection — kernel-mode vs. user-mode rootkits, rkhunter, chkrootkit
- Container escapes — namespace breakouts, privileged containers, CVE examples
- gVisor and Firecracker — microVM and user-space kernel sandboxing
- Pledge and unveil (OpenBSD) — minimal syscall/file access promises
- Ptrace security — anti-debugging, `PTRACE_ATTACH` restrictions, Yama LSM
- Linux Security Modules (LSM) framework — stacking, BPF LSM, Landlock
- Filesystem security — dm-crypt/LUKS, ext4 encryption, fscrypt
- Mandatory Integrity Control — IMA/EVM (Integrity Measurement Architecture)
- Supply chain verification — reproducible builds, in-toto, SLSA for Linux packages
- Systemd attack surface — socket activation exposure, D-Bus policy, timer abuse
- Kernel live patching — kpatch, livepatch, security implications

### Java Security (Advanced)
- Java deserialization deep dive — ysoserial, commons-collections gadgets, exploit chain construction
- Bypassing serialization filters — nested objects, proxy-based gadgets
- JVM attack surface — JMX remote code execution, JNDI injection (Log4Shell CVE-2021-44228)
- JNDI and LDAP injection — lookup exploitation, InitialContext abuse, mitigations
- Java agent instrumentation — `java.lang.instrument`, security implications of `-javaagent`
- Bytecode manipulation attacks — ASM, Javassist, malicious class transformation
- Expression Language (EL) injection — JSP/JSF EL evaluation, Spring EL, OGNL (Struts2)
- Java module system bypass — deep reflection, `--add-opens` abuse, `Unsafe` access
- GC and finalization attacks — resurrection attacks, `finalize()` security risks
- Native code security — JNI boundary validation, memory corruption via native methods
- Secure multi-tenancy in Java — classloader isolation, thread-local security contexts
- Cryptographic implementation pitfalls — IV reuse, ECB mode, padding oracle (Java-specific)
- Annotation-based security — `@RolesAllowed`, `@PreAuthorize`, bypass via reflection
- Java Flight Recorder (JFR) for security — detecting anomalies, monitoring class loading
- Quarkus / Micronaut security — compile-time DI security implications, native image hardening

### Android Security (Advanced)
- Frida and dynamic instrumentation — hooking Java/native methods at runtime, SSL unpinning
- Reverse engineering APKs — `apktool`, `jadx`, `dex2jar`, Smali patching
- Native code exploitation on Android — JNI vulnerabilities, NDK buffer overflows, ARM exploitation
- Magisk and root hiding — how Magisk modules work, Zygisk, DenyList
- SELinux on Android — enforcing mode, sepolicy, neverallow rules, type enforcement
- Android Verified Boot (AVB) — dm-verity, vbmeta, rollback protection
- Kernel hardening on Android — KASAN, CFI, shadow call stack, PAN/PXN
- Binder exploitation — transaction parsing bugs, kernel Binder driver vulnerabilities
- Exploit chains — combining app-level bugs with kernel exploits for full device compromise
- TEE on Android — TrustZone, Trusty OS, secure key operations
- Hardware-backed attestation — key attestation certificates, ID attestation, remote attestation
- Google Play supply chain — app signing key management, Play App Signing, compromised developer accounts
- Accessibility service abuse — keylogging, overlay attacks, screen scraping via accessibility
- Clipboard security — clipboard data leakage, `ClipboardManager` restrictions (Android 12+)
- Side-channel attacks on mobile — sensor-based keylogging, cache timing, GPU side channels

### Automotive Security (Advanced)
- Advanced CAN exploitation — fuzzing ECUs, brute-forcing UDS security access, CAN-FD attacks
- V2X security — PKI for V2X (SCMS), pseudonym certificates, misbehavior detection
- Autonomous vehicle attack surface — LiDAR spoofing, camera adversarial attacks, sensor fusion manipulation
- In-vehicle intrusion detection systems (IDS) — CAN anomaly detection ML models, specification-based detection
- ECU firmware reverse engineering — extracting firmware via JTAG/SWD, binary analysis of automotive MCUs
- Automotive TEE and secure enclaves — eSIM-based identity, EVITA Full HSM, SHE+ extensions
- AUTOSAR Adaptive Platform security — ara::com, IAM, secure communication channels
- Remote exploitation chains — from telematics to CAN bus (Jeep Cherokee/Tesla case studies)
- Supply chain attacks in automotive — compromised tier-1 supplier firmware, counterfeit ECUs
- ISO 21434 TARA deep dive — attack feasibility ratings, risk treatment decisions, cybersecurity goals
- SOTIF (Safety of the Intended Functionality) — ISO 21448, misuse cases, AI/ML safety
- Charging infrastructure security — ISO 15118, Plug & Charge, TLS between EV and charger
- Fleet management security — remote unlock/start, geofencing, multi-vehicle attack scenarios
- Automotive penetration testing — scope, tools (CANalyze, SavvyCAN, Vector CANoe), methodology
- Post-quantum readiness for vehicles — long vehicle lifecycles vs. crypto agility, OTA crypto migration

### Offensive Security Concepts (for Defenders)
- Attack surface mapping and enumeration
- Exploit development fundamentals — buffer overflows, ROP chains
- Privilege escalation techniques (Linux, Windows)
- Lateral movement and post-exploitation
- Social engineering — phishing, pretexting, watering hole attacks
- Red team vs. blue team vs. purple team operations
- Adversary simulation frameworks (MITRE ATT&CK)
- Fuzzing — AFL, libFuzzer, coverage-guided fuzzing

### Secure Architecture & Design
- Zero Trust Architecture — principles and implementation
- Microservices security — service mesh, mTLS, API gateway patterns
- Secure multi-tenancy design
- Data Loss Prevention (DLP) strategies
- Secrets management at scale (HashiCorp Vault, AWS Secrets Manager)
- Security architecture review — threat modeling (PASTA, attack trees)
- Compliance frameworks — SOC 2, ISO 27001, GDPR, PCI DSS (technical controls)

### Advanced Embedded & Hardware Security
- Fault injection attacks — voltage glitching, clock glitching, laser fault injection
- Side-channel attacks on embedded — power analysis (SPA/DPA), electromagnetic analysis
- Reverse engineering firmware — binary analysis, JTAG/SWD exploitation
- Secure enclaves and TEEs (TrustZone, SGX, OP-TEE)
- Physical Unclonable Functions (PUFs) for device identity
- Secure element integration (e.g., ATECC608, SE050)
- Tamper detection and response mechanisms
- Glitch-resistant coding patterns
- Real-time OS hardening — stack canaries, ASLR on embedded, W^X enforcement
- Medical device security — FDA guidance, IEC 62443
- Supply chain security for hardware — counterfeit detection, provenance

### Advanced Infrastructure & Cloud Security
- Advanced container security — runtime security (Falco), image provenance (Sigstore)
- Kubernetes advanced security — admission controllers, OPA/Gatekeeper, supply chain (SLSA)
- Cloud-native security — CSPM, CWPP, CIEM
- Serverless security considerations
- eBPF for security monitoring
- Network security monitoring — IDS/IPS, traffic analysis
- Incident response and forensics — memory forensics, log correlation, chain of custody
- Disaster recovery and business continuity — security perspective

---

## Deck File Plan

Each topic section above will become one or more `.txt` Anki deck files in this folder using the `Front[TAB]Back` format. Files will be organized by domain:

| Domain | Planned Files |
|---|---|
| Fundamentals | `security_fundamentals.txt` |
| TLS & Transport | `tls_basics.txt`, `tls_intermediate.txt`, `tls_advanced.txt` |
| Cryptography | `crypto_basics.txt`, `crypto_advanced.txt` |
| Web Security | `web_security_fundamentals.txt`, `web_security_advanced.txt`, `web_security_pro.txt` |
| Auth & Identity | `auth_fundamentals.txt`, `auth_advanced.txt` |
| API Security | `api_security.txt` |
| Network & Infra | `network_security.txt`, `cloud_security.txt` |
| Memory & Process Security | `memory_security_basics.txt`, `memory_security_intermediate.txt`, `memory_exploitation_advanced.txt` |
| Secure Coding | `secure_coding.txt`, `secure_sdlc.txt` |
| Embedded | `embedded_security_basics.txt`, `embedded_security_advanced.txt`, `embedded_security_pro.txt` |
| Unix / Linux | `unix_security_basics.txt`, `unix_security_intermediate.txt`, `unix_security_advanced.txt` |
| Java Security | `java_security_basics.txt`, `java_security_intermediate.txt`, `java_security_advanced.txt` |
| Android Security | `android_security_basics.txt`, `android_security_intermediate.txt`, `android_security_advanced.txt` |
| Automotive Security | `automotive_security_basics.txt`, `automotive_security_intermediate.txt`, `automotive_security_advanced.txt` |
| Offensive (for defenders) | `offensive_concepts.txt` |
| Architecture | `security_architecture.txt` |
