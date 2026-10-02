# Functional backlog

The modules are usable within their documented scope. This list tracks the
remaining gaps from the ecosystem audit; an implemented module is not a claim
of feature parity with every mature library in that category.

## First improvement batch

| Module | Added |
| --- | --- |
| proptest | Lazy shrinking with shared work limits, structured pass/fail/discard reports, classification and coverage, persistent regression seeds, unique collections, model-valid command sequences and full-width numeric edge cases |
| redis | Injectable duplex transports and dialing with a shared setup/operation deadline, adapter validation and failure cleanup |
| lsp | Deferred request acceptance/completion, cooperative cancellation, deadline polling, pending-request cleanup on exit and persistent rope document snapshots |
| cli | Argument/command aliases, inherited global options, cardinality-constrained argument groups and derive support for option aliases/globals |
| diff | Explicit linear-space Hirschberg algorithm for sequences, text and patches, with work/workspace limits |
| parser | Shared text/binary work and depth limits, contextual custom parsers, iterative alternatives and binary backtracking/lookahead primitives |

Each addition has library and independently resolved consumer coverage. The
verification entry point is `just ecosystem-test` in the sibling `verification`
repository, implemented in GoML. Each repository now runs these checks through
the shared GitHub Actions configuration in `verification`.

## Adoption of GoML 0.1.50

| Module | Improved |
| --- | --- |
| cli | Ordinary command schemas through erased generic functions, including generic forwarding and function values; existing typed wrappers remain compatible |
| ndarray | Specialized `Array::[f64]::linspace` constructor and scalar `ToFloat` count conversion |
| template | Direct standard integer-to-float conversion for numeric coercion |
| sqlite | Direct standard I/O in the FFI consumer; removed the error-alias transport workaround |
| tempfile | Standard resource cleanup/error combination with compatible scope results |
| request | Immutable request/response/multipart byte snapshots and shared snapshot accessors |
| msgpack | Standard reader/writer integration, direct typed frame decoding, bounded concatenated values and partial-I/O handling |
| redis | Bundled DNS/TLS connectors, mTLS and standard Context cancellation/deadlines composed with existing operation controls |
| bitflags | Optional `FlagValues` inherent derive for named flag constructors without trait imports |

## Second improvement batch

| Module | Added |
| --- | --- |
| proptest | Bounded multi-failure campaigns with shared shrink budgets, categorical histograms and text reports, atomic batch replay persistence, and state-machine execution with reset/invariant/cleanup handling |
| redis | Bounded connection pools, shared-deadline checkout, idempotent leases, configurable PING health checks, idle/lifetime expiry and replacement of unusable connections without replaying user commands |
| lsp | UTF-8/UTF-16/UTF-32 position-encoding negotiation, consistent document queries/edits, outgoing request deadlines and combined event-loop wakeup scheduling |
| cli | Nested flattened Args, typed required/optional subcommand derives, generic payloads, multilevel aliases/help/globals and composition diagnostics |
| notify / walkdir | Complete filesystem notification and traversal packages moved from `lib/std/fs` into normal versioned dependencies, with their original behavior suites retained as independent consumers |

## Terminal and color batch

| Module | Added |
| --- | --- |
| color | Checked color spaces, CSS values, alpha compositing, contrast and differences, gamut policies, hue interpolation and gradients |
| unicode_text | Version-pinned Unicode 16 tables, full grapheme/word/line conformance, terminal width policies and bounded text layout |
| ansi | Typed styles and hyperlinks, palette reduction, streaming escape tokenizer, styled Unicode text and standard writer adapters |
| terminal | Linux raw sessions, incremental typed input, mouse/paste/focus/resize, cancellable I/O, synchronized aliases and explicit restoration |
| tui | Cell invariants, constrained layout, incremental frames, common widgets, focus, Unicode editing and bounded history |
| prompt | Generic validators, history/completion, password display, search/select/multiselect, confirmation and cancellable model execution |
| progress | Concurrent job state, pure snapshots, rate/ETA, throttled bars/spinners, coordinated logs, plain output and bounded shutdown |
| diagnostics | Owned source identity, byte spans, multi-file labels, Unicode/tab alignment, themes, clipping and checked multi-file suggestions |
| tui_markdown | CommonMark terminal rendering, optional pipe tables, link handling, themes, scrolling and search |

The Explorer example composes the libraries with `walkdir` and `notify`.
Verification uses independent registry consumers, official/reference data,
pseudo-terminals and race checks where relevant. These checks also run in GitHub Actions.

## Application libraries batch

| Module | Added |
| --- | --- |
| fuzzy | Unicode case-folded matching, original grapheme ranges, explicit anchored modes, bounded maximum-score DP, stable Top-K, immutable incremental search sessions and parallel cancellation |
| config | Layered sources, typed Serde, JSON Pointer overrides, array policies, provenance, validators, immutable concurrent snapshots and caller-driven inotify reloads |
| websocket | Shared RFC 6455 protocol core, client/server handshakes, strict frames, fragmented UTF-8, control/close states, queue bounds and concurrent cancellable TCP/TLS I/O |
| highlight | Extensible logos grammars, built-in language scopes, nested/multiline state, embedded Markdown code, immutable incremental documents and bounded ANSI/HTML renderers |
| archive | USTAR/PAX and classic ZIP read/write, CRC32, bounded standard I/O, GoML DEFLATE/GZIP codecs, metadata, rooted extraction and GNU/Info-ZIP interoperability |
| metrics | Concurrent metric handles, checked counters/gauges/histograms, consistent snapshots, registration/cardinality policies, atomic gauge collection, timers and Prometheus text output |
| csv | Standard reader/writer streaming, configurable dialects and quoting, multiline fields, BOM and header policies, byte/UTF-8 records, positions, resource bounds and typed Serde schemas |
| bench | Adaptive warmup/sampling, setup exclusion, checked monotonic clocks, bootstrap intervals, outlier statistics, baseline comparisons, throughput and standalone JSON/HTML reports |

The batch uses native GoML tests and independent versioned consumers. Local
verification includes race checks; the shared GitHub Actions workflow runs the same checks.

## Reliability and developer workflow batch

| Module | Added |
| --- | --- |
| sql | Concurrent bounded SQLite pools, cancellable deadline-aware acquisition, close wakeups and synchronized lease invalidation for connections, cursors and transactions |
| parser | Explicit recovery reports, synchronization markers, nested/quoted recovery scanning and composable partial results with shared work/depth budgets |
| cli | Static Bash, Zsh and Fish completion generated from command schemas, including nested commands, aliases, inherited options and value choices |
| request | Scoped streaming test-peer lifetimes, cancellation-aware bounded accepts and deterministic lifecycle regressions |
| verification | Pinned reusable GitHub Actions CI for every ecosystem repository, native prerequisites, preserved candidate checkouts, independent verification and race checks |

## Ecosystem-wide improvement audit

This batch reviews all 64 library repositories individually. The tables pair the
observed gap with the bounded change selected for this round; the backlog below
records further work rather than claiming parity with mature libraries. Each
module link leads to its public API, limits and regression tests.

All 64 libraries have implementation, documentation and regression changes with
module-local tests and isolated downstream verification. Integrated verification
and CI status remain pending the coordinated final run.

### Numeric and graph libraries

| Module | Finding and improvement |
| --- | --- |
| [bigint](https://github.com/gomlang/bigint/blob/main/README.md) | Modular inversion was missing; add bounded signed/unsigned inverses with canonical residues, non-coprime results and zero-modulus errors. |
| [bigmath](https://github.com/gomlang/bigmath/blob/main/README.md) | Exact integer conversion rejected fractions; add rational rounding to arbitrary-size integers in six modes without a floating intermediate. |
| [decimal](https://github.com/gomlang/decimal/blob/main/README.md) | Exact division rejected representable boundary scales; normalize or pad finite quotients before checking representation limits. |
| [ndarray](https://github.com/gomlang/ndarray/blob/main/README.md) | Finite mean/variance inputs could overflow intermediate sums; retry in scaled coordinates while preserving ordinary and IEEE special-value paths. |
| [graph](https://github.com/gomlang/graph/blob/main/README.md) | Hub deletion repeatedly scanned incident adjacency; batch removals and clear slots directly while preserving ordering and stable handles. |
| [bitflags](https://github.com/gomlang/bitflags/blob/main/README.md) | Name iteration could not expose unnamed or partial-composite bits; add ascending, fused one-bit iteration preserving all in-width bits. |

### Codecs and formats

| Module | Finding and improvement |
| --- | --- |
| [archive](https://github.com/gomlang/archive/blob/main/README.md) | A ZIP descriptor CRC equal to the signature was misclassified; match classic/ZIP64 signed and unsigned layouts against indexed metadata. |
| [compress](https://github.com/gomlang/compress/blob/main/README.md) | Exact-budget GZIP EOF was rejected; allow one documented EOF probe after complete members, preserving sticky limits and provider errors. |
| [msgpack](https://github.com/gomlang/msgpack/blob/main/README.md) | Impossible declarations waited for payloads; reject announced byte/value budgets at headers, including extension framing and map child counts. |
| [csv](https://github.com/gomlang/csv/blob/main/README.md) | Excess columns were rejected only after reading their fields; fail immediately at the delimiter, retaining precise positions and sticky errors. |
| [asn1](https://github.com/gomlang/asn1/blob/main/README.md) | DER validation omitted restricted string repertoires and ENUMERATED encoding rules; validate them recursively while retaining raw TLV framing APIs. |
| [xml](https://github.com/gomlang/xml/blob/main/README.md) | Short comments and document/end-tag whitespace were mishandled; recognize short comments and enforce literal XML whitespace and end-tag grammar. |

### Protocols and certificates

| Module | Finding and improvement |
| --- | --- |
| [request](https://github.com/gomlang/request/blob/main/README.md) | Chunk extensions were silently ignored without grammar checks; share strict bounded validation across buffered and streaming HTTP/1.1 responses. |
| [http](https://github.com/gomlang/http/blob/main/README.md) | Add bounded Content-Length normalization for repeated/list values and transfer-encoding conflicts; limit Connection whitespace to HTTP SP/HTAB. |
| [websocket](https://github.com/gomlang/websocket/blob/main/README.md) | Required tokens could hide malformed later members; validate every Upgrade/Connection member on client and server handshakes. |
| [textproto](https://github.com/gomlang/textproto/blob/main/README.md) | Add bounded numeric multiline replies with repeated-code checks, exact consumption, byte/count limits and existing reader failure semantics. |
| [mime](https://github.com/gomlang/mime/blob/main/README.md) | Encoded words accepted malformed payloads and unsafe phrase punctuation; validate RFC 2047 encoded text and emit phrase-safe Q encoding. |
| [mail](https://github.com/gomlang/mail/blob/main/README.md) | Comments obscured trailing commas and group boundaries; track separators explicitly, validate group labels and retain valid empty groups. |
| [x509](https://github.com/gomlang/x509/blob/main/README.md) | Add typed BasicConstraints DER encoding/decoding with canonical defaults, checked path lengths and extension integration. |

### Storage and servers

| Module | Finding and improvement |
| --- | --- |
| [sql](https://github.com/gomlang/sql/blob/main/README.md) | Cursor cleanup errors were lost; close exactly once on returns/unwinding and preserve primary errors alongside close failures. |
| [sqlite](https://github.com/gomlang/sqlite/blob/main/README.md) | Mutable binary inputs/row values could alias retained storage; copy Blob/TextBytes parameters, row accessors and Bytes conversions. |
| [redis](https://github.com/gomlang/redis/blob/main/README.md) | Panicking WATCH callbacks could leak established transactions; defer connection cleanup through WATCH/MULTI scopes and preserve panic propagation. |
| [web](https://github.com/gomlang/web/blob/main/README.md) | Static responses lacked strong If-Match handling and applied ranges to HEAD; enforce precondition precedence and restrict ranges to GET. |

### Parsing and persistent text

| Module | Finding and improvement |
| --- | --- |
| [parser](https://github.com/gomlang/parser/blob/main/README.md) | Add budgeted many_until with termination-first probing, committed-error preservation, merged diagnostics and zero-progress rejection. |
| [syntax](https://github.com/gomlang/syntax/blob/main/README.md) | Small text slices traversed preceding tokens; seek overlapping tokens by cached child offsets while preserving checked UTF-8/subtree bounds. |
| [logos](https://github.com/gomlang/logos/blob/main/README.md) | Repeated position queries rescanned prefixes; cache scalar line/column traversal while preserving independent forks and shared morph state. |
| [regexp](https://github.com/gomlang/regexp/blob/main/README.md) | All-match collection was eager; add lazy matches with one shared work/match budget, fused failure and explicit cursor/input ownership. |
| [diff](https://github.com/gomlang/diff/blob/main/README.md) | Myers reconstruction expanded every unchanged element; reconstruct coalesced ranges directly, preserving tie policy and patch behavior. |
| [rope](https://github.com/gomlang/rope/blob/main/README.md) | Backward scalar traversal was absent; add reverse scalar iterators and checked exclusive-boundary starts over persistent snapshots. |
| [proptest](https://github.com/gomlang/proptest/blob/main/README.md) | Subnormal interpolation could escape finite bounds; clamp rounding and preserve singleton signed zero, including replay/shrink cases. |

### Documents and language tooling

| Module | Finding and improvement |
| --- | --- |
| [template](https://github.com/gomlang/template/blob/main/README.md) | Add stable forward/reverse sorting by a nested attribute path, with checked keys and charged operation budgets. |
| [markdown](https://github.com/gomlang/markdown/blob/main/README.md) | Escaping could allocate beyond the output budget before rejection; preflight escape expansion and emit URL encoding through checked fragments. |
| [html](https://github.com/gomlang/html/blob/main/README.md) | Decoding bounded output only after construction; add exact decoded-length preflight, bounded construction and efficient literal runs. |
| [highlight](https://github.com/gomlang/highlight/blob/main/README.md) | Lone CR and ATX indentation were misclassified; preserve LF/CRLF/CR boundaries and recognize heading indentation using ASCII spaces only. |
| [go_doc](https://github.com/gomlang/go_doc/blob/main/README.md) | Literal comments became Markdown syntax and code labels broke spans; escape punctuation/destinations and choose safe code-span delimiters. |
| [lsp](https://github.com/gomlang/lsp/blob/main/README.md) | Content-Type splitting mishandled quoted semicolons/escapes; parse bounded parameters, validate charset values and preserve poison/reset behavior. |

### State and filesystem libraries

| Module | Finding and improvement |
| --- | --- |
| [cache](https://github.com/gomlang/cache/blob/main/README.md) | Related invalidations could interleave; add atomic multi-key invalidation with one expiration pass, load cancellation and callbacks after batch commit. |
| [incremental](https://github.com/gomlang/incremental/blob/main/README.md) | Several public reads needed synthetic queries for one revision; add scoped coherent evaluations with expiring capabilities and cancellable admission. |
| [pipeline](https://github.com/gomlang/pipeline/blob/main/README.md) | Per-run generators lacked a cleanup hook; add resource acquisition and exactly-once release across exhaustion, early stop, errors and cancellation. |
| [config](https://github.com/gomlang/config/blob/main/README.md) | Cancellation stopped event waiting but not queued reload/publication; add cancellable reload admission and preserve the previous snapshot/error state for abandoned candidates. |
| [tempfile](https://github.com/gomlang/tempfile/blob/main/README.md) | Seek-based random access disturbed shared cursors; add positioned I/O across anonymous, named and spooled files, preserving offsets through rollover. |
| [ignore](https://github.com/gomlang/ignore/blob/main/README.md) | Exclusion callbacks could close/cancel a walker yet still yield entries; recheck lifecycle immediately after either predicate result. |
| [notify](https://github.com/gomlang/notify/blob/main/README.md) | Cancellable reads could block on watcher locks; make admission cancellable, restore locks on unwind and drain final poll readiness before completion. |
| [walkdir](https://github.com/gomlang/walkdir/blob/main/README.md) | Traversal had no cancellation-aware descriptor cleanup; add contexts, boundary/batch checks and one Interrupted error followed by permanent exhaustion. |

### Terminal applications

| Module | Finding and improvement |
| --- | --- |
| [ansi](https://github.com/gomlang/ansi/blob/main/README.md) | Tab wrapping discarded remaining line capacity; fill it before continuing expanded styled/link-bearing spaces across wrapped lines. |
| [terminal](https://github.com/gomlang/terminal/blob/main/README.md) | SOS payloads leaked as keys; retain bounded opaque strings until ST or timeout/flush, with fragmented input and exact restoration tested through a real PTY. |
| [tui](https://github.com/gomlang/tui/blob/main/README.md) | Vertical navigation lost its target column on short lines; retain the intended display column across short, wide and tabbed lines. |
| [prompt](https://github.com/gomlang/prompt/blob/main/README.md) | Unhandled terminal notifications erased validation/completion state; preserve it when the editor reports no handled action. |
| [progress](https://github.com/gomlang/progress/blob/main/README.md) | No-op job updates scheduled duplicate output; mark only changed state dirty while preserving already-pending changes and explicit resets. |
| [tui_markdown](https://github.com/gomlang/tui_markdown/blob/main/README.md) | Reflow reset active search navigation; retain/clamp the match ordinal and keep it visible, preserving selected-link priority. |
| [tabwriter](https://github.com/gomlang/tabwriter/blob/main/README.md) | Small chunks repeatedly copied/rescanned incomplete lines; buffer incrementally while preserving CRLF, limits and block alignment; clarify control-byte preservation. |

### Text, diagnostics and observability

| Module | Finding and improvement |
| --- | --- |
| [color](https://github.com/gomlang/color/blob/main/README.md) | Tiny premultiplied distances squared to zero; use scaled Euclidean norms while retaining deterministic first-entry ties. |
| [unicode_text](https://github.com/gomlang/unicode_text/blob/main/README.md) | Trimmed spaces after oversized graphemes lost hard-break metadata; compute continuation before assigning the break flag. |
| [diagnostics](https://github.com/gomlang/diagnostics/blob/main/README.md) | Editor UTF-16 coordinates lacked checked conversion; add strict byte/UTF-16 mapping with scalar/surrogate and line-boundary validation. |
| [fuzzy](https://github.com/gomlang/fuzzy/blob/main/README.md) | Impossible subsequences allocated scoring matrices or hit their limits; reject them with a cancellation-aware linear feasibility scan first. |
| [metrics](https://github.com/gomlang/metrics/blob/main/README.md) | Snapshots insertion-sorted under the registry gate; use stable O(n log n) ordering while preserving deterministic labels and detached snapshots. |
| [tracing](https://github.com/gomlang/tracing/blob/main/README.md) | MemorySink retained records indefinitely; add checked bounded storage and atomic drain, with explicit overflow/failure semantics. |
| [bench](https://github.com/gomlang/bench/blob/main/README.md) | Imported summaries could contradict raw observations; validate extrema, estimate ranges and total outlier counts with defined rounding tolerance. |

### CLI and native tooling

| Module | Finding and improvement |
| --- | --- |
| [cli](https://github.com/gomlang/cli/blob/main/README.md) | Boolean flags rejected defaults/environment values; support normalized true/false/1/0 values with explicit > environment > default precedence and documented provenance. |
| [object](https://github.com/gomlang/object/blob/main/README.md) | ELF extended symbol-index companions accepted invalid links/layouts; validate uniqueness, correspondence, unused entries and escaped section indexes. |
| [dwarf](https://github.com/gomlang/dwarf/blob/main/README.md) | Line rows discarded operation/transient state; add parse_sections_detailed with operation index, flags, ISA and discriminator while preserving the original public records and entry point. |
| [image](https://github.com/gomlang/image/blob/main/README.md) | PNG encoding always used filter zero; select all five row filters with bounded residual scoring and deterministic tie breaking while preserving pixels. |
| [datetime](https://github.com/gomlang/datetime/blob/main/README.md) | Full-range durations lacked checked scaling; add exact signed integer multiplication through bounded doubling/addition with recoverable overflow. |
| [llvm](https://github.com/gomlang/llvm/blob/main/README.md) | Integer constants were limited to 64 input bits; add bounded checked text constants in bases 2/8/10/16 under existing context lifetime/locking guards. |

## Remaining work

| Module | Remaining capabilities and limits |
| --- | --- |
| [bigint](https://github.com/gomlang/bigint/blob/main/README.md) | Faster large-operand multiplication/division and radix conversion, Montgomery reduction, higher roots and prime generation; modular inverses now exist, but arithmetic remains variable-time and has no operation cancellation or constant-time guarantee. |
| [bigmath](https://github.com/gomlang/bigmath/blob/main/README.md) | Decimal Float parsing/formatting, nonfinite/subnormal values and transcendental functions; rational cross-cancellation could reduce large intermediate products within existing representation limits. |
| [decimal](https://github.com/gomlang/decimal/blob/main/README.md) | Context precision padding can still exceed stored-scale limits; exact factor removal remains bounded. Roots, transcendental functions, binary-float conversion and special-value/trap models are absent. |
| [ndarray](https://github.com/gomlang/ndarray/blob/main/README.md) | Masked selection/scatter, sorting/quantiles, NPY interchange, batched factorizations, SVD/eigen and rank-deficient solves; approximate statistics still permit cancellation/underflow, and stddev derives from variance. |
| [graph](https://github.com/gomlang/graph/blob/main/README.md) | Flow/matching, serialization, configurable weights and dynamic shortest paths; individual edge deletion scans adjacency, deleted slots remain retained for handle identity, and mutable storage is unsynchronized. |
| [bitflags](https://github.com/gomlang/bitflags/blob/main/README.md) | Associated constants/operators, arbitrary declaration expressions and generic storage derives; one-bit iteration is available, but iterator aliases share a serial cursor. |
| [archive](https://github.com/gomlang/archive/blob/main/README.md) | Strict PAX fractional timestamps and faster global metadata merging; split/encrypted ZIP, other compression methods, sparse TAR, devices/FIFOs and legacy filename encodings. Documented ZIP buffering bounds still apply. |
| [compress](https://github.com/gomlang/compress/blob/main/README.md) | Expose optional GZIP header metadata and consider additional formats; codecs retain sequential-owner semantics, and exact-budget GZIP EOF detection may consume one rejected excess source byte. |
| [msgpack](https://github.com/gomlang/msgpack/blob/main/README.md) | Incremental field processing and richer typed extensions; readers still buffer complete bounded frames. Legal nonminimal encodings and arbitrary ordered map keys remain accepted without canonical map ordering. |
| [csv](https://github.com/gomlang/csv/blob/main/README.md) | Reduce duplicated raw/decoded bytes used for precise error positions; asynchronous I/O, seeking, dialect inference, comments, nested schemas, transcoding and formula sanitization remain outside the explicit API. |
| [asn1](https://github.com/gomlang/asn1/blob/main/README.md) | Schema-aware SET versus SET OF ordering, time/REAL/other string validation, relative OIDs and high-tag-number form; generic DER validation is not complete schema validation, and typed schemas omit the newly checked opaque primitives. |
| [xml](https://github.com/gomlang/xml/blob/main/README.md) | Validate declaration pseudo-attributes/placement and restrict hexadecimal references to lowercase x; DTD/XSD, external/custom entities, nested object mapping and non-UTF-8 encodings remain unsupported. |
| [request](https://github.com/gomlang/request/blob/main/README.md) | HTTP/2 streaming and streaming reuse, HTTP/3, custom DNS, persistent cookies and general retries; streaming callbacks still use bounded HTTP/1.1 connections, and trailer validation remains duplicated. |
| [http](https://github.com/gomlang/http/blob/main/README.md) | Live-stream parsing, method/status body semantics and transfer-coding validation; Content-Length checks do not reconcile actual body bytes, and dump helpers are diagnostic rather than byte-exact round trips. |
| [websocket](https://github.com/gomlang/websocket/blob/main/README.md) | Compression/extensions, HTTP/2 CONNECT, proxy/redirect integration and Autobahn certification; origin/authentication/routes remain application policy, and adapters control interruption of blocked I/O. |
| [textproto](https://github.com/gomlang/textproto/blob/main/README.md) | SMTP enhanced-status interpretation and FTP unprefixed intermediate replies; reply text remains byte-oriented and callers choose charset/success policy. |
| [mime](https://github.com/gomlang/mime/blob/main/README.md) | More charsets, structured-field recognition and folding policy; multipart extraction/form policy remains separate from the strict byte-oriented codecs. |
| [mail](https://github.com/gomlang/mail/blob/main/README.md) | Obsolete route syntax, internationalized addr-specs and broader phrase/CFWS/domain-literal grammar; SMTP delivery, DNS and body decoding are outside this package. |
| [x509](https://github.com/gomlang/x509/blob/main/README.md) | Complete certificates, signature/chain validation and trust roots; extension criticality, key usage and path enforcement need certificate context. Typed path lengths are bounded to i64. |
| [sql](https://github.com/gomlang/sql/blob/main/README.md) | Additional backend adapters, generic prepared statements, row derives and batch helpers; pool contexts bound acquisition rather than execution, and collection caps rows rather than retained bytes. |
| [sqlite](https://github.com/gomlang/sqlite/blob/main/README.md) | Backup, incremental BLOBs, custom SQL functions and byte-bounded collection; one serialized connection is owned by Database, with pooling supplied by the separate sql adapter. |
| [redis](https://github.com/gomlang/redis/blob/main/README.md) | Cluster/Sentinel and sharded subscriptions; no ambiguous-write replay or forced preemption of uncooperative callbacks/connectors. Panic cleanup covers established WATCH/MULTI scopes rather than arbitrary connector panics. |
| [web](https://github.com/gomlang/web/blob/main/README.md) | Date validators, multipart ranges, HTTP/2/3 and streaming compression/proxying; static responses remain bounded but fully buffered, and unknown range units currently return 416. |
| [parser](https://github.com/gomlang/parser/blob/main/README.md) | Token streams, resumable text parsing and further binary/text parity; recovery needs configured delimiters/quotes, left recursion needs rewriting, and callbacks are cooperatively bounded. |
| [syntax](https://github.com/gomlang/syntax/blob/main/README.md) | Incremental parsing, revision-stable syntax pointers, range-limited public token iterators and multi-edit transactions; covering_element still scans children to preserve leftmost/zero-width selection. |
| [logos](https://github.com/gomlang/logos/blob/main/README.md) | Compile-time derives/DFA generation, streaming/byte input, captures, named patterns and broader Unicode properties; fallback may revisit input, so matching has no whole-input linear-time guarantee. |
| [regexp](https://github.com/gomlang/regexp/blob/main/README.md) | Lazy replacement/splitting, named captures, inline flags, lookarounds and backreferences; the iterator retains complete UTF-8 input and is not transport streaming. |
| [diff](https://github.com/gomlang/diff/blob/main/README.md) | Multi-file/Git metadata, binary patches, three-way merge and fuzzy application; Myers retains bounded quadratic trace space in edit distance, while explicit Hirschberg has O(NM) worst-case time. |
| [rope](https://github.com/gomlang/rope/blob/main/README.md) | Grapheme, reverse byte/chunk/line and double-ended iteration, search, editing history and memory-mapped backing; reverse scalar iteration is now available over immutable snapshots. |
| [proptest](https://github.com/gomlang/proptest/blob/main/README.md) | Unbiased generator choices and value-based persistent replay; stores currently retain seeds/sizes, generator changes can alter replay, and custom callbacks cannot be preempted. |
| [template](https://github.com/gomlang/template/blob/main/README.md) | Macros/imports/call blocks, keyword arguments, recursive loops, file-loader invalidation and incremental output; attribute sorting supports one dot-separated numeric/string key, without multi-key or case-fold syntax. |
| [markdown](https://github.com/gomlang/markdown/blob/main/README.md) | GFM, footnotes, math, highlighting and finer inline spans; unsuccessful searches can remain quadratic under work budgets, and output bounds do not cover every caller-owned AST or parser allocation. |
| [html](https://github.com/gomlang/html/blob/main/README.md) | Streaming decoding and tokenizer state; these whole-string utilities do not provide sanitization, URL policy or template-context analysis. |
| [highlight](https://github.com/gomlang/highlight/blob/main/README.md) | Semantic scopes, full Markdown, interpolation and TextMate/Sublime compatibility; incremental edits still reconstruct/split full source even when lexical suffixes are reused. |
| [go_doc](https://github.com/gomlang/go_doc/blob/main/README.md) | Go source/symbol extraction, import resolution, automatic URLs, directives, legacy headings and nested list blocks; code-span newlines retain CommonMark normalization. |
| [lsp](https://github.com/gomlang/lsp/blob/main/README.md) | Broader feature schemas and workspace-edit execution, worker/timer scheduling and concurrent server/session mutation; media-type names remain unrestricted, and applications own language semantics/deadline polling. |
| [cache](https://github.com/gomlang/cache/blob/main/README.md) | Frequency-based admission, sharding, indexed/background expiry and refresh-ahead; expiry still scans, loader dependency cycles are caller-managed, and batch sizes/callback work remain caller-controlled. |
| [incremental](https://github.com/gomlang/incremental/blob/main/README.md) | Parallel branch evaluation, persistent snapshots/caches, durability classes and cycle fixed points; roots serialize, callbacks cannot reenter blocking database methods, and failed reads do not roll back valid memoization. |
| [pipeline](https://github.com/gomlang/pipeline/blob/main/README.md) | Error recovery/retry, time operators, parallel flat-map, durable replay/checkpoints and cleanup-error reporting; resource callbacks are cooperative, release must return normally and external aliases remain caller-owned. |
| [config](https://github.com/gomlang/config/blob/main/README.md) | Interpolation, more formats/secret providers, debounce/background scheduling and source-line provenance; reads/validators are synchronous and cancelled consumed event batches need an explicit resynchronizing reload. |
| [tempfile](https://github.com/gomlang/tempfile/blob/main/README.md) | Positioned read_exact/write_all helpers, non-Linux backends and crash-durable persistence; native transfers may be partial, overlapping buffers/writes need synchronization, and cleanup retains depth/concurrent-filesystem limits. |
| [ignore](https://github.com/gomlang/ignore/blob/main/README.md) | Multipattern automata, tracked-file selection, file-type groups and other platforms; walking remains path-based, bind-mount loops rely on depth/work limits and one walker requires one consumer. |
| [notify](https://github.com/gomlang/notify/blob/main/README.md) | Other backends, bind-mount aliases and non-UTF-8 event policies; cancellation observes kernel polling within 50 ms but cannot preempt running callbacks, and discarded racing batches may require rescanning. |
| [walkdir](https://github.com/gomlang/walkdir/blob/main/README.md) | Other platforms and interruptible filesystem operations; active ancestors retain descriptors, early abandonment still needs close, and traversal provides neither a filesystem snapshot nor confinement. |
| [ansi](https://github.com/gomlang/ansi/blob/main/README.md) | Screen emulation, single-byte C1 mode, extended underline/color models and palette discovery; wrapping remains grapheme-based, with word-aware layout delegated to unicode_text. |
| [terminal](https://github.com/gomlang/terminal/blob/main/README.md) | Other operating systems, suspend/resume, signal subscriptions, Kitty/modifyOtherKeys, X10 mouse and terminfo negotiation; applications retain exclusive session ownership and cleanup does not install global exit/signal handlers. |
| [tui](https://github.com/gomlang/tui/blob/main/README.md) | Configurable width policies, soft-wrapped persistent editing, clipboard, mouse-hit routing and graphics protocols; editing remains a single-event-loop model without bidi shaping or IME composition. |
| [prompt](https://github.com/gomlang/prompt/blob/main/README.md) | Ranked completion menus, date/file pickers, batch policies and persistent/background providers; validation/completion callbacks are synchronous and password values remain ordinary GC strings. |
| [progress](https://github.com/gomlang/progress/blob/main/README.md) | Byte-stream adapters, recursive jobs, pause/resume and templates; applications drive ticks, and convenience updates may wait behind output unless callers use context-aware operations. |
| [tui_markdown](https://github.com/gomlang/tui_markdown/blob/main/README.md) | Full GFM and syntax highlighting; searches are literal, case-sensitive and confined to displayed lines. Reflow retains match ordinal rather than source identity, and selected links take visibility priority. |
| [tabwriter](https://github.com/gomlang/tabwriter/blob/main/README.md) | Alignment still buffers an entire tabbed block until a boundary or flush; widths do not parse ANSI, and caller control/escape bytes are preserved rather than sanitized. |
| [color](https://github.com/gomlang/color/blob/main/README.md) | CSS Color 4, RGB/ICC profiles, chromatic adaptation and HDR; palette lookup remains linear and scaled norms cannot recover coordinates already lost to floating rounding. |
| [unicode_text](https://github.com/gomlang/unicode_text/blob/main/README.md) | Unicode upgrades, locale/dictionary tailoring, normalization, bidi and sentence segmentation; deterministic terminal policies do not perform font shaping. |
| [diagnostics](https://github.com/gomlang/diagnostics/blob/main/README.md) | Indexed UTF-16 mapping, bidi/font shaping, graphical label routing and persistent source revisions; mapping scans a line prefix, cache mutation is application-synchronized and edits return text without writing files. |
| [fuzzy](https://github.com/gomlang/fuzzy/blob/main/README.md) | Normalization/transliteration, richer queries and larger-corpus Top-K; feasible candidates still need DP budgets and prepared vectors, with no streaming source or aggregate corpus byte limit. |
| [metrics](https://github.com/gomlang/metrics/blob/main/README.md) | OpenMetrics/native histograms, exporters, runtime instrumentation and sharding; snapshot copying/sorting remains under the registry gate and registration/collector lookups retain linear scans. |
| [tracing](https://github.com/gomlang/tracing/blob/main/README.md) | Distributed propagation, exporters, richer sampling and byte-budget admission; bounded MemorySink limits records only, the original constructor stays unbounded, and draining cannot reset a latched tracer failure. |
| [bench](https://github.com/gomlang/bench/blob/main/README.md) | Allocation/CPU counters, process isolation, dashboards and baseline selection; report validation checks necessary consistency without recomputing every statistic, and workloads remain cooperatively cancellable. |
| [cli](https://github.com/gomlang/cli/blob/main/README.md) | Counter defaults/environment values, automatic negated flags and dynamic/filesystem/constraint-aware completion; boolean flag defaults/environment are now supported, with false environment values counting as provided. |
| [object](https://github.com/gomlang/object/blob/main/README.md) | Relocations, compressed sections, notes and dynamic-linker interpretation; metadata text limits remain per name/count rather than a cumulative decoded-text budget. |
| [dwarf](https://github.com/gomlang/dwarf/blob/main/README.md) | DWARF64, indexed/supplementary/split/type units and v5 define_file; line-file/row limits are per table, with a separate cumulative decoded-text budget. |
| [image](https://github.com/gomlang/image/blob/main/README.md) | Palette/grayscale encoder optimization, interlacing and filter-policy selection; output remains noninterlaced 8-bit RGBA, without color-management metadata, animation, JPEG or other formats. |
| [datetime](https://github.com/gomlang/datetime/blob/main/README.md) | Duration division/rounding, recurrence, arbitrary-pattern/localized parsing and automatic timezone updates; arithmetic uses elapsed POSIX time without leap-second/TAI or calendar-month scaling. |
| [llvm](https://github.com/gomlang/llvm/blob/main/README.md) | Dominance/loop/MemorySSA analysis, sealed-block SSA, JIT/ORC, globals, recursive structs, vectors/atomics, debug metadata and broader ABI/linkage controls; LLVM 18 remains required and native processing is not hostile-IR isolation. |
| [goml_stats](https://github.com/gomlang/goml_stats/blob/main/README.md) | Manifest-based canonical identities, declaration counts and historical comparisons; hierarchical Git ignore rules are provided by the ignore dependency |

Further work should preserve resource bounds, recoverable errors, normal
versioned dependency consumption and the independent reference checks already
present. Bundled networking adapters and concurrent resource pools need actual
I/O and race coverage, beyond a public interface or a mock implementation.
