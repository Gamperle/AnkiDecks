# Android Anki Decks

Flashcard decks covering Android app development, AOSP internals, and Android Automotive — classified by difficulty level.

## Format

```
Front (question or term)[TAB]Back (answer or definition)
```

---

## Existing Decks

| File | Description |
|------|-------------|
| `android_fundamentals.txt` | Activities, Intents, lifecycle, Manifest |
| `android_ui.txt` | Views, layouts, RecyclerView, ConstraintLayout |
| `android_jetpack.txt` | ViewModel, LiveData, Room, Navigation, WorkManager |
| `android_kotlin.txt` | Kotlin essentials for Android: coroutines, extensions, data classes |
| `android_architecture.txt` | MVVM, Clean Architecture, dependency injection (Hilt) |

---

# Topic Index

## 1. Android App Development

### Beginner

#### 1.1 Core Components & Lifecycle
- Activity, Service, BroadcastReceiver, ContentProvider — the four building blocks
- Activity lifecycle: onCreate → onStart → onResume → onPause → onStop → onDestroy
- Fragment lifecycle and Fragment Manager
- Intent (explicit vs implicit), Intent filters, URI schemes, deep links
- AndroidManifest.xml: permissions, exported components, intent filters
- PendingIntent immutability flags (FLAG_IMMUTABLE / FLAG_MUTABLE)
- Application class, custom Application subclass
- Back stack, task affinity, launch modes (standard, singleTop, singleTask, singleInstance)
- Context: Activity context vs Application context, when to use each
- Configuration changes and state preservation (onSaveInstanceState / onRestoreInstanceState)

#### 1.2 UI Fundamentals
- View, ViewGroup, View hierarchy, measure / layout / draw cycle
- XML layouts: LinearLayout, RelativeLayout, FrameLayout, ConstraintLayout
- ConstraintLayout: chains, barriers, guidelines, ConstraintSet
- RecyclerView, ViewHolder pattern, Adapter, LayoutManager types
- DiffUtil, AsyncListDiffer, ListAdapter
- Material Design components: AppBarLayout, CoordinatorLayout, BottomNavigationView, FloatingActionButton
- Themes, styles, attributes, day/night theming
- Drawables, shapes, selectors, vector drawables
- Menus (options, context, popup), Toolbar vs ActionBar
- Toast, Snackbar, Dialog, BottomSheetDialog

#### 1.3 Kotlin Essentials for Android
- Null safety: ?, !!, let, elvis operator (?:)
- data class, sealed class, sealed interface, enum class
- Extension functions, extension properties
- Scope functions: let, run, with, apply, also
- object keyword: singleton, companion object, object expression
- lateinit var vs by lazy delegation
- Coroutines basics: suspend, launch, async/await, Deferred
- viewModelScope, lifecycleScope
- Flow basics: cold stream, collect, map, filter
- StateFlow, SharedFlow, conflation

#### 1.4 Data Persistence
- SharedPreferences (and its limitations)
- DataStore (Preferences DataStore, Proto DataStore)
- SQLite basics on Android
- Room: @Entity, @Dao, @Database, type converters
- Room migrations, auto-migrations, destructive migration fallback
- Content Providers: URI, ContentResolver, CRUD operations
- File storage: internal vs external, scoped storage (MediaStore, SAF)

#### 1.5 Networking & Serialization
- HTTP basics for Android, OkHttp, interceptors
- Retrofit: @GET, @POST, @Path, @Query, @Body, converters
- Gson vs Moshi vs kotlinx.serialization
- Image loading: Glide, Coil, Picasso — caching, transformations
- WebSocket basics on Android

#### 1.6 Permissions & Security Basics
- Runtime permissions (requestPermissions, onRequestPermissionsResult)
- ActivityResultContracts for permissions
- Normal vs dangerous vs signature permissions
- Encrypted SharedPreferences, Android Keystore basics

---

### Intermediate

#### 1.7 Jetpack Compose
- @Composable functions, recomposition, smart recomposition
- State hoisting, remember, rememberSaveable, mutableStateOf
- Modifier system: ordering, chaining, custom modifiers
- Layouts: Column, Row, Box, LazyColumn, LazyRow, LazyVerticalGrid
- Scaffold, TopAppBar, BottomAppBar, NavigationBar in Material 3
- Side effects: LaunchedEffect, DisposableEffect, SideEffect, rememberCoroutineScope
- derivedStateOf, snapshotFlow, produceState
- CompositionLocal, providing values down the tree
- Navigation in Compose: NavHost, NavController, type-safe routes
- Animations: animateAsState, AnimatedVisibility, Crossfade, updateTransition, InfiniteTransition
- Custom drawing: Canvas composable, DrawScope
- Interop: AndroidView (embedding View in Compose), ComposeView (embedding Compose in View)
- Compose performance: stability, immutability, @Stable, @Immutable, skipping recomposition
- Compose testing: ComposeTestRule, onNodeWithText, semantics

#### 1.8 Advanced Jetpack Libraries
- ViewModel: SavedStateHandle, process death, creation via Factory
- Lifecycle: LifecycleOwner, LifecycleObserver, repeatOnLifecycle
- Navigation: deep links, nested graphs, Safe Args, shared element transitions
- Paging 3: PagingSource, RemoteMediator, PagingData, LoadState
- WorkManager: Constraints, chaining, periodic work, expedited work, CoroutineWorker
- CameraX: Preview, ImageCapture, ImageAnalysis, lifecycle binding
- Media3 (ExoPlayer): MediaSession, playback, streaming, DRM
- App Startup: Initializer, manual vs automatic initialization
- Benchmark library: Macrobenchmark, Microbenchmark, baseline profiles
- SplashScreen API

#### 1.9 Architecture Patterns
- MVVM: ViewModel ↔ Repository ↔ DataSource
- MVI: unidirectional data flow, intent → model → view state
- Clean Architecture: Presentation, Domain, Data layers, use cases
- Repository pattern: single source of truth, offline-first
- Dependency injection with Hilt: @HiltAndroidApp, @AndroidEntryPoint, @Inject, @Module, @Provides, @Binds
- Hilt scopes: @Singleton, @ViewModelScoped, @ActivityScoped, @FragmentScoped
- Hilt multi-bindings, @Qualifier, @EntryPoint
- Kotlin Multiplatform (KMP) architecture considerations
- Modularization: feature modules, core modules, API modules, dependency graph

#### 1.10 Testing
- JUnit 4, JUnit 5, assertion libraries
- Mockito, MockK — mocking frameworks
- Robolectric: unit testing with Android framework on JVM
- Espresso: UI testing, ViewMatchers, ViewActions, ViewAssertions, IdlingResource
- UI Automator: cross-app UI testing
- Compose testing: createComposeRule, semantics, assertIsDisplayed
- Turbine: testing Kotlin Flows
- Hilt testing: @HiltAndroidTest, @UninstallModules
- Test doubles: fake, stub, mock, spy — when to use each
- Coroutine testing: TestDispatcher, runTest, advanceUntilIdle

#### 1.11 Build System & Tooling
- Gradle basics: build.gradle.kts, plugins, dependencies, configurations
- Build variants: buildTypes (debug/release), productFlavors, flavorDimensions
- Signing configs, keystore management, APK vs AAB
- ProGuard / R8: shrinking, obfuscation, @Keep, consumer rules
- Gradle Version Catalogs (libs.versions.toml)
- Build performance: configuration cache, build cache, parallelism
- Lint: built-in checks, custom lint rules
- Android Studio profilers: CPU, Memory, Network, Energy

#### 1.12 Background Processing & Inter-Process Communication
- Services: foreground service, bound service, started service
- Foreground service types (Android 14+)
- JobScheduler, AlarmManager (exact vs inexact alarms)
- BroadcastReceiver: local broadcasts, ordered broadcasts, sticky broadcasts
- AIDL (Android Interface Definition Language) basics
- Messenger IPC, ContentProvider IPC
- Binder basics: transact, onTransact, Parcelable

---

### Pro

#### 1.13 Performance & Optimization
- Systrace / Perfetto: tracing app & system performance
- Baseline Profiles: generation, benchmarking startup & scroll jank
- R8 full mode, aggressive optimizations, reflection keep rules
- Startup optimization: cold/warm/hot start, App Startup, lazy initialization
- Memory leak detection: LeakCanary, MAT, heap dumps
- Bitmap management: inBitmap reuse, downsampling, Region decoder
- RenderThread, GPU overdraw analysis, hardware layers
- StrictMode: detecting disk/network on main thread
- ANR analysis: traces.txt, ANR patterns, background ANR (Android 14+)

#### 1.14 Advanced Kotlin & Coroutines
- Coroutine internals: CPS (Continuation Passing Style), state machine compilation
- CoroutineContext, CoroutineDispatcher, Dispatchers.Main.immediate
- Structured concurrency, SupervisorJob, exception handling (CoroutineExceptionHandler)
- Channels: produce, actor pattern, fan-in/fan-out
- Flow internals: cold vs hot, backpressure, buffer, conflate, collectLatest
- callbackFlow, channelFlow — bridging callbacks to Flow
- Kotlin Symbol Processing (KSP) vs KAPT
- Kotlin compiler plugins: Compose compiler, All-open, No-arg, Serialization

#### 1.15 Advanced Security
- Keystore: keys backed by TEE / StrongBox, key attestation
- BiometricPrompt: Class 2 vs Class 3 biometrics, CryptoObject
- Network Security Config: certificate pinning, cleartext traffic, custom CAs
- SafetyNet / Play Integrity API: device attestation, verdict types
- OWASP Mobile Top 10: insecure data storage, reverse engineering, code tampering
- Root / jailbreak detection strategies and bypass techniques
- SSL/TLS pinning bypass (Frida, Objection)
- ProGuard / R8 obfuscation effectiveness and decompilation (jadx, apktool)

#### 1.16 Gradle Plugin Development & Build Internals
- Custom Gradle plugin development in buildSrc / standalone
- Gradle Task, TaskAction, incremental tasks, up-to-date checks
- Transform API (deprecated) → AsmClassVisitorFactory (AGP 7+)
- Android Gradle Plugin (AGP) extension points: Variant API, Artifacts API
- Custom lint checks: Detector, IssueRegistry, UAST / PSI
- Annotation processing: KAPT internals, KSP migration

---

## 2. AOSP (Android Open Source Project)

### Beginner

#### 2.1 AOSP Overview & Architecture
- Android system architecture: Linux kernel → HAL → native libraries → ART → framework → apps
- AOSP vs manufacturer forks vs Google Play Services vs GMS
- Open-source licensing: Apache 2.0 (userspace) vs GPL v2 (kernel)
- Android version history, API levels, codenames, dessert naming
- Treble architecture: vendor / system separation
- Generic System Image (GSI), Generic Kernel Image (GKI)
- System apps vs privileged apps vs third-party apps
- Android partition layout: system, vendor, boot, recovery, userdata, product, odm

#### 2.2 AOSP Build System Basics
- repo tool: init, sync, manifest, local_manifests
- lunch targets: product-variant (e.g., aosp_arm64-userdebug)
- Build types: user, userdebug, eng — differences and use cases
- Soong build system: Android.bp vs legacy Android.mk
- m, mm, mmm, mma build commands
- envsetup.sh, lunch, build/make
- Device tree basics: device/, vendor/ directories
- Build output structure: out/target/product/

#### 2.3 Android Linux Kernel
- Android-specific kernel patches: Binder, ashmem, ION/DMA-BUF heaps, wakelocks
- Kernel configuration: defconfig, merge_config, GKI modularization
- Device Tree (DT), Device Tree Blob (DTB), Device Tree Overlay (DTO)
- Kernel modules: .ko loading, modprobe, modules.load
- Boot image structure: kernel + ramdisk, boot_image_header versions
- init and first-stage / second-stage init

---

### Intermediate

#### 2.4 System Services & Framework
- SystemServer: boot sequence, system services startup
- ActivityManagerService (AMS): activity lifecycle management, process management
- WindowManagerService (WMS): window hierarchy, z-ordering, input dispatch
- PackageManagerService (PMS): package scanning, intent resolution, permission management
- PowerManagerService: wake locks, doze, battery optimization
- InputManagerService: input event pipeline, key/touch dispatch
- SurfaceFlinger: surface composition, layers, VSYNC, hardware composer (HWC)
- Audio system: AudioFlinger, AudioPolicyService, audio HAL, audio routing
- MediaServer, MediaCodec, Stagefright, codec2
- ConnectivityService, NetworkStack, netd
- ServiceManager, obtaining system service references

#### 2.5 Binder IPC In Depth
- Binder architecture: client, server, ServiceManager, Binder driver
- AIDL compilation: Stub, Proxy, onTransact, transact
- Binder transactions: Parcel, Parcelable, IBinder, death recipients
- Binder thread pool, one-way calls, synchronous calls
- Binder context manager, service lookup, service registration
- /dev/binder, /dev/hwbinder, /dev/vndbinder — Treble separation
- Performance characteristics: maximum transaction size, Binder buffer

#### 2.6 Hardware Abstraction Layer (HAL)
- HAL purpose: separating vendor hardware implementation from framework
- Legacy HAL (C structs, hw_module_t, hw_device_t)
- HIDL (HAL Interface Definition Language): passthrough vs binderized HALs
- AIDL HALs (Android 11+): replacing HIDL, stability guarantees
- VINTF (Vendor Interface) manifest and compatibility matrix
- Common HALs: camera, sensors, audio, graphics (Gralloc), power, health, DRM
- HAL versioning: minor/major versions, interface hash

#### 2.7 Init, Properties & SELinux
- init.rc language: service definitions, triggers, actions, imports
- System properties: ro.*, persist.*, sys.* — scopes and lifetimes
- Property service, property triggers
- SELinux on Android: enforcing, permissive, domain transitions
- sepolicy structure: file_contexts, property_contexts, service_contexts
- Writing SELinux policies: allow rules, neverallow, type_transition
- SELinux denials debugging: audit2allow, dmesg, audit logs
- MAC (Mandatory Access Control) vs DAC (Discretionary Access Control)

#### 2.8 Android Runtime (ART)
- ART vs Dalvik: AOT compilation, JIT compilation, profile-guided optimization
- DEX, ODEX, VDEX, ART class images
- Garbage collection in ART: concurrent copying GC, compaction
- App Zygote: preloading, process forking, shared memory
- ART boot image, boot classpath
- Class loading: PathClassLoader, DexClassLoader, InMemoryDexClassLoader
- Method tracing, ART instrumentation, JVMTI

#### 2.9 Graphics & Display Pipeline
- SurfaceFlinger: compositing strategy, client composition vs hardware composition
- BufferQueue: producer-consumer model, triple buffering
- EGL, OpenGL ES, Vulkan — rendering APIs on Android
- Gralloc HAL: buffer allocation, format negotiation
- Hardware Composer (HWC2 / HWComposer): overlay planes, composition types
- VSYNC, Choreographer, frame scheduling, jank detection
- RenderThread, hardware-accelerated rendering pipeline
- Display HAL: hotplug, virtual displays, WFD (Wi-Fi Display)

#### 2.10 Networking & Connectivity Internals
- netd daemon, iptables/nftables, DNS resolver
- ConnectivityService, NetworkAgent, NetworkFactory, NetworkRequest
- VPN implementation: VpnService, TUN/TAP interface
- Wi-Fi stack: wpa_supplicant, WifiManager, WifiP2pManager
- Bluetooth stack: Fluoride (system/bt), GATT, HCI, profiles (A2DP, HFP, LE Audio)
- Telephony stack: RILD, RIL interface, IMS, SIM management
- NFC stack: NCI, HCE (Host Card Emulation), LLCP

#### 2.11 Security Internals
- UID/GID per-app isolation, AID_ definitions, multi-user
- SELinux policy enforcement for apps and system services
- Verified Boot (AVB): dm-verity, vbmeta, chained partitions, rollback protection
- Keymaster / KeyMint HAL: TEE-backed keys, attestation, hardware security
- Gatekeeper / Weaver: PIN/pattern/password authentication
- FBE (File-Based Encryption): CE (Credential Encrypted) vs DE (Device Encrypted) storage
- DRM framework: MediaDrm, Widevine L1/L3, OEMCrypto
- App sandboxing: Linux UID, seccomp, namespace isolation
- Scoped storage enforcement, MediaProvider

---

### Pro

#### 2.12 AOSP Customization & Porting
- Porting AOSP to a new device: device tree, BoardConfig.mk, kernel bring-up
- Device tree overlays, product makefiles, inheritance (inherit-product)
- Custom system services: adding a new AIDL system service, registering with ServiceManager
- Custom HAL implementation: AIDL/HIDL HAL, SELinux policies, VINTF manifest
- Native daemons: writing C++ system daemons, init.rc integration
- Overlay Resource Management (RRO): runtime resource overlays, static overlays
- System UI customization: StatusBar, NavigationBar, Launcher, LockScreen
- SystemUI plugin architecture, ExtensionController
- Boot animation customization, splash screen
- OTA update system: update_engine, A/B updates, virtual A/B, payload generation

#### 2.13 Build System Deep Dive
- Soong internals: blueprint files, module types, ninja generation
- Soong namespaces, defaults, genrule, cc_library, java_library
- Mixed builds: Bazel + Soong migration
- Product configuration: PRODUCT_PACKAGES, PRODUCT_COPY_FILES, PRODUCT_PROPERTY_OVERRIDES
- Makefile to Soong migration patterns
- Build system extensions: writing custom Soong module types
- Multi-architecture builds: 32+64 bit, TARGET_ARCH, 2ND_ARCH
- Vendor VNDK, VNDK-SP, LLNDK, vendor snapshot, APEX

#### 2.14 APEX & Mainline Modules
- APEX (Android Pony EXpress): modular system components updatable via Play Store
- Mainline modules: ART, Networking, Media, DNS, Conscrypt, etc.
- APEX structure: apex_manifest.pb, payload (ext4/f2fs image), signing
- APEX activation: apexd, bind mounts, versioning, rollback
- Flattened APEX vs compressed APEX
- Module boundaries, stable APIs via APEX stubs

#### 2.15 Debugging & Tracing AOSP
- logcat: log levels, log buffers (main, system, crash, events, kernel)
- adb shell dumpsys: service-specific debugging (battery, activity, window, meminfo)
- Perfetto: system-wide tracing, custom trace points, SQL analysis
- ftrace, atrace categories, systrace integration
- Simpleperf: CPU profiling, call graphs, flame charts
- Tombstone analysis: crash dump format, native crash debugging
- GDB / LLDB remote debugging of native code and system services
- bugreport / bugreportz: comprehensive device state capture

#### 2.16 Kernel & Low-Level
- GKI (Generic Kernel Image): core kernel + vendor modules
- KMI (Kernel Module Interface) stability, ABI monitoring
- eBPF on Android: traffic monitoring, power stats
- Cgroup usage: cpu, memory, io cgroups, LMKD
- Low Memory Killer Daemon (LMKD): oom_adj_score, memory pressure
- ION → DMA-BUF heaps migration
- Android-specific kernel features: ashmem → memfd, binderfs
- Kernel security: seccomp-bpf filters, Integrity Measurement Architecture (IMA)

---

## 3. Android Automotive OS (AAOS)

### Beginner

#### 3.1 AAOS Overview & Architecture
- Android Automotive OS (AAOS) vs Android Auto — embedded OS vs phone projection
- AAOS system architecture: Linux kernel → VHAL → Car Services → Car Apps
- AAOS target hardware: IVI (In-Vehicle Infotainment), digital clusters, rear-seat entertainment
- Google Automotive Services (GAS) vs AOSP-only AAOS
- AAOS app categories: media, navigation, communication, vehicle settings, parking
- Car App Library: template-based apps running on both Auto & Automotive
- Automotive app distribution: Play Store automotive track vs embedded pre-install
- AAOS UI concepts: driver distraction guidelines, multi-display, multi-user

#### 3.2 Vehicle Hardware Basics
- ECU (Electronic Control Unit): types, roles, communication
- CAN bus (Controller Area Network): message format, arbitration, standard vs extended frames
- OBD-II: diagnostic port, PIDs, trouble codes (DTC)
- In-Vehicle Networking: CAN, CAN-FD, LIN, FlexRay, Ethernet (100BASE-T1, 1000BASE-T1)
- Automotive Ethernet: BroadR-Reach, TSN (Time-Sensitive Networking)
- Head unit architecture: SoC, displays, touchscreen, HW buttons, rotary controllers

---

### Intermediate

#### 3.3 Vehicle HAL (VHAL)
- Vehicle HAL purpose: abstracting vehicle properties from framework
- VehicleProperty: property IDs, areas, access modes (READ, WRITE, READ_WRITE)
- VHAL data types: INT32, FLOAT, STRING, MIXED, INT32_VEC
- VHAL property zones: GLOBAL, WINDOW, DOOR, SEAT, WHEEL, MIRROR
- VHAL implementation: AIDL VHAL (Android 14+), legacy HIDL VHAL
- Subscribing to vehicle properties: onChange, continuous, onSet
- VHAL Testing: VehiclePropertyVerifier, default VHAL implementation
- Grpc VHAL for emulator testing

#### 3.4 Car Service & Car APIs
- CarService: system service hosting all car-specific managers
- CarPropertyManager: read/write vehicle properties from apps
- CarUxRestrictionsManager: driver distraction state, UX restriction types
- CarAudioService: audio zones, audio focus per zone, volume groups, occupant zones
- CarOccupantZoneManager: mapping displays to passengers
- CarProjectionManager: Android Auto projection integration
- CarPowerManagementService: vehicle power states, deep sleep, shutdown
- CarWatchdogService: process health monitoring, I/O overuse detection
- CarEvsService: exterior view system (surround view, rear camera)
- CarTelemetryService: collecting in-vehicle metrics per publisher/subscriber
- Car Input Service: handling HW buttons, rotary input, touch input

#### 3.5 Driver Distraction & UX
- UX Restrictions: NO_VIDEO, NO_TEXT_MESSAGE, NO_FILTERING, LIMIT_STRING_LENGTH, LIMIT_CONTENT
- Distraction Optimization (DO) guidelines, app compliance requirements
- Testing UX restrictions: adb shell cmd car_service inject-vhal (driving state)
- Parked vs idling vs moving states
- Template-based UI restrictions (Car App Library)

#### 3.6 Multi-Display & Multi-User on AAOS
- Multi-display architecture: driver display, passenger display, rear-seat displays, cluster
- Display assignment: ActivityOptions.setLaunchDisplayId, CarActivityView
- Multi-user: driver profile switching, guest mode, passenger profiles
- Occupant Zone mapping: display → user → audio zone
- Per-occupant media, per-occupant climate controls

#### 3.7 AAOS Audio System
- Car audio architecture: audio zones, OEM audio service, audio focus
- Audio routing to multiple speakers/zones
- Volume groups per audio zone
- Dynamic audio routing, IAudioControl HAL
- Occupant-aware audio focus policy
- Ducking vs pausing vs mixing for concurrent audio sources
- Audio context: NAVIGATION, MUSIC, CALL, ALARM, NOTIFICATION

#### 3.8 AAOS Cluster & Instrument Display
- Instrument cluster rendering: InstrumentClusterService, ClusterActivity
- DirectRenderingCluster vs NavigationStateProto
- Cluster API: navigation state, instrument data, gauges, telltales
- Rendering to a remote display: VirtualDisplay, Presentation

#### 3.9 AAOS Security
- VHAL property access permissions: system|privileged app restrictions
- AAOS SELinux policies: vehicle HAL domains, car service contexts
- Secure boot chain for IVI: bootloader → kernel → system verification
- AAOS multi-user data isolation
- OTA updates for AAOS: A/B updates, vendor image updates
- Firewall between IVI and safety-critical ECUs (gateway ECU)

---

### Pro

#### 3.10 AAOS System Customization & OEM Integration
- Building AAOS from AOSP: device tree, car product makefiles
- Custom CarService extensions: OEM-specific vehicle features
- Custom VHAL implementation: CAN bus integration, proprietary protocols
- OEM audio service: vendor-specific audio routing, amplifier control
- System UI customization for AAOS: CarSystemUI, CarLauncher, CarSettings
- Rotary controller framework: FocusParkingView, FocusArea, nudge navigation
- Custom cluster rendering pipeline: OpenGL/Vulkan cluster rendering
- Remote device management (MDM) for fleet vehicles

#### 3.11 Vehicle Communication Protocols
- CAN bus deep dive: J1939, ISO-TP, multi-frame messages
- SOME/IP (Scalable service-Oriented MiddlewarE over IP): service discovery, events, methods
- DDS (Data Distribution Service): real-time pub-sub for ADAS
- Automotive Ethernet: DoIP (Diagnostics over IP), UDS over Ethernet
- V2X (Vehicle-to-Everything): V2V, V2I, C-V2X, DSRC, IEEE 802.11p
- AUTOSAR Adaptive Platform: ara::com, Execution Management, Service Discovery
- AUTOSAR Classic: RTE, SWC, BSW modules
- SOA (Service-Oriented Architecture) in automotive: signal-to-service migration

#### 3.12 ADAS & Autonomous Driving Integration
- Sensor fusion: camera, LiDAR, radar, ultrasonic inputs
- Sensor HAL for ADAS: camera HAL with ISP pipeline, high-bandwidth sensor data
- EVS (Exterior View System): surround view, parking assist, camera streaming
- ADAS SoC considerations: GPU, DSP, NPU (Neural Processing Unit)
- Functional safety: ISO 26262 ASIL levels (A through D)
- Safety-critical vs non-safety ECU separation
- Watchdog timers, health monitoring for ADAS components
- Real-time OS (RTOS) coexistence: QNX, Linux RT, hypervisor architectures

#### 3.13 Power Management & Vehicle State
- Vehicle power state machine: ON, SHUTDOWN_PREPARE, DEEP_SLEEP, WAIT_FOR_VHAL, SUSPEND_TO_RAM
- Garage mode: deferred tasks while vehicle is off (OTA, sync)
- CarPowerPolicy: component power policy, custom power policy groups
- Silent mode: system up without display/audio
- Battery management: parasitic drain limits, dark current budgets, 12V battery monitoring
- Cold start optimization: fast boot requirements (< 2s to rear camera)

#### 3.14 AAOS Testing & Validation
- AAOS CTS (Compatibility Test Suite): CtsCarTestCases
- AAOS VTS (Vendor Test Suite): VtsHalAutomotiveVehicle
- VHAL property testing: VehiclePropertyAnnotationValidator
- Cuttlefish automotive emulator
- Trout (virtual AAOS device)
- HIL (Hardware-In-the-Loop) testing for VHAL integration
- CANoe / Vector CANalyzer simulation for CAN bus testing
- AAOS GAS compliance testing

#### 3.15 Automotive Security Advanced
- CAN bus security: authentication (SecOC), intrusion detection (IDS)
- CAN bus attacks: spoofing, fuzzing, replay, bus-off attacks
- ISO/SAE 21434: automotive cybersecurity engineering
- UNECE WP.29 R155/R156: cybersecurity and software update regulations
- Secure communication: TLS over Ethernet, MACSec, IPsec in automotive
- HSM (Hardware Security Module) for ECUs, SHE (Secure Hardware Extension)
- Secure diagnostics: authenticated UDS sessions, security access sequences
- V2X PKI: certificate management, pseudonym certificates, misbehavior detection
- ISO 15118 Plug & Charge: TLS, contract certificates, EXI encoding
- Remote vehicle access: digital key (CCC Digital Key, UWB), backend authentication
- OTA security: signed payloads, delta updates, rollback protection, dual-bank partitioning

---

## 4. Cross-Cutting Topics

### Intermediate

#### 4.1 Compose for Automotive
- Compose in AAOS: template restrictions, custom OEM Compose theming
- CarAppLibrary with Compose: bridging templates and custom surfaces
- Rendering Compose on multiple displays
- Compose for Cluster: performance constraints, reduced recomposition

#### 4.2 Connectivity & Companion Apps
- Android Auto protocol, phone ↔ head unit communication
- Bluetooth profiles for automotive: HFP, PBAP, MAP, AVRCP, A2DP
- Wi-Fi tethering, hotspot management on AAOS
- Companion device integration: phone mirroring, notification bridging
- 5G / LTE embedded modem, eSIM management, carrier integration

#### 4.3 App Development for AAOS
- Car App Library: Screen, Template, ListTemplate, MapTemplate, NavigationTemplate
- Media app development: MediaBrowserService, MediaSession, browse tree
- Navigation app development: NavigationManagerCallback, TurnByTurn API
- Communication apps: calling + messaging templates
- Video apps on AAOS (parked-only templates)
- Testing AAOS apps: Desktop Head Unit (DHU), Automotive emulator

### Pro

#### 4.4 Hypervisors & Virtualization in Automotive
- Type 1 hypervisors: QNX, INTEGRITY, PikeOS — real-time + Android coexistence
- pKVM (Protected KVM): Android-native virtualization framework
- virtio devices: input, GPU, audio, CAN passthrough via virtio
- Android as guest OS: virtual VHAL, display passthrough, GPU virtualization (virtio-gpu)
- Safety island integration: ASIL-D RTOS alongside Android ASIL-QM
- Multi-OS ECU consolidation: cluster RTOS + IVI Android on one SoC

#### 4.5 OTA & Fleet Management
- Full OTA vs incremental/delta OTA
- A/B (seamless) updates, virtual A/B, snapshot merge
- update_engine: payload format, streaming updates, hash verification
- OTA backend integration: device targeting, staged rollouts, rollback
- Fleet management: remote diagnostics, remote lock/unlock, geofencing
- FOTA (Firmware OTA) vs SOTA (Software OTA) distinction

#### 4.6 Performance Engineering for Automotive
- Boot time optimization: bootloader → kernel → AAOS first frame (< 2s to camera)
- Rendering performance: 60fps cluster at guaranteed latency
- Memory budgeting: limited RAM environments, zRAM tuning, LMKD tuning
- Thermal management: thermal HAL, thermal throttling policies, skin temperature
- CPU scheduling: RT priorities for audio/display, cgroups, CPU isolation

---

## Deck File Plan

| Level | Planned File | Topics Covered |
|---|---|---|
| Beginner | `android_app_beginner.txt` | App Development Beginner (1.1–1.6) |
| Intermediate | `android_app_intermediate.txt` | App Development Intermediate (1.7–1.12) |
| Pro | `android_app_pro.txt` | App Development Pro (1.13–1.16) |
| Beginner | `aosp_beginner.txt` | AOSP Beginner (2.1–2.3) |
| Intermediate | `aosp_intermediate.txt` | AOSP Intermediate (2.4–2.11) |
| Pro | `aosp_pro.txt` | AOSP Pro (2.12–2.16) |
| Beginner | `aaos_beginner.txt` | Automotive OS Beginner (3.1–3.2) |
| Intermediate | `aaos_intermediate.txt` | Automotive OS Intermediate (3.3–3.9) + Cross-Cutting Intermediate (4.1–4.3) |
| Pro | `aaos_pro.txt` | Automotive OS Pro (3.10–3.15) + Cross-Cutting Pro (4.4–4.6) |
