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
module-local tests and isolated downstream verification. Repository CI uses the
[shared verification workflow](https://github.com/gomlang/verification/tree/main/ci)
for the applicable race, I/O, PTY and native checks.

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
| [html](https://github.com/gomlang/html/blob/main/README.md) | Decoding lacked exact size planning and copied literal bytes individually; add decoded-length preflight before construction and efficient literal runs. |
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

## Second ecosystem-wide improvement audit

This second audit pairs a newly observed gap in each library with its bounded
implementation change. The ten groups below cover all 64 libraries; the
remaining-work table records the final scope and limitations after review.
Earlier batches above are retained as their historical record. Each module
link leads to public documentation and the repository's regression tests.

### Numeric and graph libraries

| Module | Finding and improvement |
| --- | --- |
| [bigint](https://github.com/gomlang/bigint/blob/main/README.md) | Higher integer roots required callers to construct their own search; add bounded unsigned nth roots and exact remainders, using a separate RootError to preserve existing exhaustive Error matches. |
| [bigmath](https://github.com/gomlang/bigmath/blob/main/README.md) | Rational products built large intermediates before reduction; cross-cancel multiplication and division operands first, preserving canonical signs, zero and result limits. |
| [decimal](https://github.com/gomlang/decimal/blob/main/README.md) | Context division rejected exact quotients when precision padding exceeded the scale limit; remove only redundant trailing zeros while retaining rounded/inexact flags. |
| [ndarray](https://github.com/gomlang/ndarray/blob/main/README.md) | Taking sqrt of variance lost representable deviations to overflow, underflow or subnormal rounding; normalize before restoring scale and add the same stable calculation to axis reductions. |
| [graph](https://github.com/gomlang/graph/blob/main/README.md) | Cycle errors lacked an explainable path; add iterative directed-cycle search returning an ordered closed witness with original edge IDs, including loops and parallel edges. |
| [bitflags](https://github.com/gomlang/bitflags/blob/main/README.md) | Repeated flag aliases recursively re-evaluated prior expressions; cache bounded declaration masks in both derives while retaining existing validation and diagnostic behavior. |

### Codecs and formats

| Module | Finding and improvement |
| --- | --- |
| [archive](https://github.com/gomlang/archive/blob/main/README.md) | PAX timestamps silently ignored malformed fractional suffixes; validate the full nonnegative decimal lexeme before truncating valid fractions, preserving bounded reader failures. |
| [compress](https://github.com/gomlang/compress/blob/main/README.md) | GZIP readers discarded optional header metadata; add opt-in bounded capture and detached last-header snapshots, publishing only fully parsed and CRC-checked headers. |
| [msgpack](https://github.com/gomlang/msgpack/blob/main/README.md) | Timestamp values could not participate directly in typed or derived Serde; add generic serialization/deserialization using canonical timestamp extensions while preserving opaque Extension behavior. |
| [csv](https://github.com/gomlang/csv/blob/main/README.md) | Unquoted fields retained identical decoded and wire buffers; share storage until quoting requires transformation, preserving snapshots, UTF-8 error positions and public copy semantics. |
| [asn1](https://github.com/gomlang/asn1/blob/main/README.md) | Primitive DER time contents escaped validation; check canonical UTC/GeneralizedTime lexemes, fractions and calendar ranges while retaining raw TLV framing and explicit century/leap-second scope. |
| [xml](https://github.com/gomlang/xml/blob/main/README.md) | XML declarations had weak placement/grammar checks and numeric references accepted uppercase X; validate reader/writer declarations and lowercase hexadecimal references while retaining documented XML 1.x declaration handling. |

### Protocols and certificates

| Module | Finding and improvement |
| --- | --- |
| [request](https://github.com/gomlang/request/blob/main/README.md) | Buffered HTTP/1 and HTTP/2 trailer checks differed from streaming HTTP/1; share framing/routing field validation across all three paths while retaining unknown extension trailers. |
| [http](https://github.com/gomlang/http/blob/main/README.md) | Content-Length alone could not determine response framing; add method/status-aware framing with no-body and CONNECT precedence, ordered transfer-coding validation and strict TE/CL conflict handling. |
| [websocket](https://github.com/gomlang/websocket/blob/main/README.md) | Invalid fragmented text survived until FIN; validate UTF-8 continuation ranges after each complete frame, preserving legal scalar splits and independent control/binary frames. |
| [textproto](https://github.com/gomlang/textproto/blob/main/README.md) | Numeric replies lacked enhanced SMTP status inspection; add RFC 3463 parsing/formatting and class/multiline consistency checks without changing generic reply consumption. |
| [mime](https://github.com/gomlang/mime/blob/main/README.md) | Multipart framing rejected permitted boundary padding and writers missed matching collisions; accept bounded SP/HTAB padding and reject ambiguous payloads across chunk boundaries. |
| [mail](https://github.com/gomlang/mail/blob/main/README.md) | Address scanners treated domain-literal punctuation as outer syntax; isolate modern dtext while validating literal contents and unquoted display-name brackets so illegal comment syntax cannot hide in a name. |
| [x509](https://github.com/gomlang/x509/blob/main/README.md) | KeyUsage extensions required manual BIT STRING handling; add nine typed flags with bounded canonical DER encoding/decoding and rejection of empty, unknown or noncanonical bits. |

### Storage and servers

| Module | Finding and improvement |
| --- | --- |
| [sql](https://github.com/gomlang/sql/blob/main/README.md) | Row-count limits allowed large TEXT/BLOB collections; add explicit row/payload CollectionLimits and query_all_with_limits, charging before decoding and retaining cursor cleanup. |
| [sqlite](https://github.com/gomlang/sqlite/blob/main/README.md) | Collection APIs bounded rows but not payload bytes; add Rows, Statement and Executor collection limits with exact byte accounting, validation before execution and cursor release on every exit. |
| [redis](https://github.com/gomlang/redis/blob/main/README.md) | Connector, validation and lease-release callback panics could strand pool slots or its lock; guard ownership through checkout/recycle/discard and run transport callbacks outside bookkeeping locks, preserving cleanup and waiter notification. |
| [web](https://github.com/gomlang/web/blob/main/README.md) | Static ranges rejected valid oversized endpoints and unknown units; use saturating decimal parsing, ignore unknown units and handle valid empty-file suffixes while preserving conditional-request precedence. |

### Parsing and persistent text

| Module | Finding and improvement |
| --- | --- |
| [parser](https://github.com/gomlang/parser/blob/main/README.md) | Composed character/sentinel parsing repeated overlapping prefix work; add linear take_until with charged sentinel preprocessing/comparisons, UTF-8 byte spans and an unconsumed delimiter. |
| [syntax](https://github.com/gomlang/syntax/blob/main/README.md) | Narrow source ranges lacked public token iteration; add checked lazy tokens_in_range preserving identity and absolute ranges, and reuse it for text_slice. |
| [logos](https://github.com/gomlang/logos/blob/main/README.md) | lexer_at always scanned to source EOF; add checked lexer_range with absolute spans/positions and a boundary preserved by callbacks, remainder, fork and morph. |
| [regexp](https://github.com/gomlang/regexp/blob/main/README.md) | Splitting materialized all results before consumption; add lazy split iterators sharing match/work limits and cumulative output bounds, with Unicode-safe empty matches and fused errors. |
| [diff](https://github.com/gomlang/diff/blob/main/README.md) | Myers budgets missed initial row storage and failed comparisons; charge allocations, diagonal visits and every comparison before work, guarding trace-width arithmetic against overflow. |
| [rope](https://github.com/gomlang/rope/blob/main/README.md) | Reverse traversal exposed scalars but no raw bytes or chunks; add snapshot-preserving reverse/prefix cursors with direct tree seeks and checked chunk UTF-8 boundaries. |
| [proptest](https://github.com/gomlang/proptest/blob/main/README.md) | Modulo choices introduced bias while legacy seed sequences needed stability; add opt-in bounded rejection-sampled numeric ranges and snapshotted choices with deterministic replay and shrinking. |

### Documents and language tooling

| Module | Finding and improvement |
| --- | --- |
| [template](https://github.com/gomlang/template/blob/main/README.md) | JSON escaping allocated complete expanded strings before checking output limits; emit checked literal/escape fragments and apply tojson HTML escaping in the same traversal. |
| [markdown](https://github.com/gomlang/markdown/blob/main/README.md) | Walking wide caller-built ASTs expanded unbounded sibling stacks and skipped charging empty list items; use depth-bounded cursors and a separate list-item work limit. |
| [html](https://github.com/gomlang/html/blob/main/README.md) | Character-reference decoding required a complete string; add a bounded incremental Decoder preserving incomplete references and EOF semantics, with sticky failures and checked cumulative input/output. |
| [highlight](https://github.com/gomlang/highlight/blob/main/README.md) | TOML closing runs of four/five quotes could reopen strings; consume valid multiline closing runs together, preserving following comments and incremental lexical state. |
| [go_doc](https://github.com/gomlang/go_doc/blob/main/README.md) | Removing one indentation byte corrupted code layout and blank lines split code blocks; remove the common literal whitespace prefix and preserve relative indentation and interior blank lines. |
| [lsp](https://github.com/gomlang/lsp/blob/main/README.md) | Document edit batches allocated final text without a selectable bound; add exact final-byte preflight after coordinate/overlap validation, preserving original-coordinate ordering and snapshots. |

### State and filesystem libraries

| Module | Finding and improvement |
| --- | --- |
| [cache](https://github.com/gomlang/cache/blob/main/README.md) | TTL reads scanned and snapshotted every resident entry; replace expiry scans with an indexed deadline heap, preserving exact TTL/TTI boundaries, admission and callbacks after unlocking. |
| [incremental](https://github.com/gomlang/incremental/blob/main/README.md) | Cancellation inside memo copy/equality callbacks could still publish results; recheck context after each callback before replacing memo values, dependencies or equality-cutoff statistics. |
| [pipeline](https://github.com/gomlang/pipeline/blob/main/README.md) | Sequential flattening could not express fallible resource acquisition; add cancellation-aware try_flat_map with lazy ordered expansion, outer error provenance and prompt sibling cancellation. |
| [config](https://github.com/gomlang/config/blob/main/README.md) | Sources could not refresh generated/remote text through normal builds; add lazy dynamic providers under existing bounds/provenance and guard watch ownership through initial reload errors or panics. |
| [tempfile](https://github.com/gomlang/tempfile/blob/main/README.md) | Positioned I/O exposed only partial transfers; add read_exact_at/write_all_at with full-range checks, interruption retries, zero-progress errors and lifecycle protection across the complete operation. |
| [ignore](https://github.com/gomlang/ignore/blob/main/README.md) | Glob matching allocated a new dynamic-programming row for every token; reuse two call-local rows while preserving precharged work limits and matching behavior. |
| [notify](https://github.com/gomlang/notify/blob/main/README.md) | Recursive registration or subscription callback panics leaked owned watchers; guard construction and worker lifetimes so unwinding closes resources before event channels. |
| [walkdir](https://github.com/gomlang/walkdir/blob/main/README.md) | Traversal could not stay on the root filesystem; add an opt-in device-boundary policy that yields foreign entries but skips descent, including followed symlink targets. |

### Terminal applications

| Module | Finding and improvement |
| --- | --- |
| [ansi](https://github.com/gomlang/ansi/blob/main/README.md) | One-byte fragmented opaque strings repeatedly rescanned and copied retained input; resume scanning from the previous boundary while preserving split terminators, UTF-8 validation, offsets and poisoning. |
| [terminal](https://github.com/gomlang/terminal/blob/main/README.md) | A newly pending escape inherited the completed sequence's timeout; restart ambiguity timing when output completes the old sequence, while preserving deadlines for its continuing fragments. |
| [tui](https://github.com/gomlang/tui/blob/main/README.md) | Horizontally clipped expanded tabs lost selection/cursor styling; paint each visible tab cell while preserving whole-grapheme drawing, masks and editor offsets. |
| [prompt](https://github.com/gomlang/prompt/blob/main/README.md) | Raw candidate limits missed expansion during control sanitization; sanitize and validate history and complete completion batches before retention, preserving atomic failures and snapshots. |
| [progress](https://github.com/gomlang/progress/blob/main/README.md) | Clock callback panics stranded manager/shutdown locks; return recoverable errors, preserve retryable state and finish shutdown with the last timestamp and defined error priority. |
| [tui_markdown](https://github.com/gomlang/tui_markdown/blob/main/README.md) | Wide graphemes became blank in one-column paragraphs/tables; use the existing replacement-character policy before wrapping, retaining first-scalar style and link metadata. |
| [tabwriter](https://github.com/gomlang/tabwriter/blob/main/README.md) | Completed rows were concatenated before limits and failed writers retained buffers; preflight retained-line budgets and release shared pending/row storage on sticky failure. |

### Text, diagnostics and observability

| Module | Finding and improvement |
| --- | --- |
| [color](https://github.com/gomlang/color/blob/main/README.md) | CSS parsing accepted non-CSS Unicode whitespace and direct hex bypassed raw input limits; use exact CSS whitespace and enforce the input cap before trimming. |
| [unicode_text](https://github.com/gomlang/unicode_text/blob/main/README.md) | Repeated grapheme position queries rebuilt boundary data; add an immutable, optionally input-bounded index with constant-time cluster boundaries, binary byte lookup and detached copies. |
| [diagnostics](https://github.com/gomlang/diagnostics/blob/main/README.md) | Repeated UTF-16 queries rescanned long line prefixes; add immutable sparse checkpoint indexes with binary search and bounded interval decoding, retaining CRLF/EOF diagnostics. |
| [fuzzy](https://github.com/gomlang/fuzzy/blob/main/README.md) | Top-K retention moved up to K elements per accepted candidate; use bounded worst-first heaps and sort only final results, preserving scores, stable ties and parallel equivalence. |
| [metrics](https://github.com/gomlang/metrics/blob/main/README.md) | Gauge collection repeatedly scanned families/series and allocated keys before label checks; build temporary indexed lookups within each atomic batch and validate labels before key construction. |
| [tracing](https://github.com/gomlang/tracing/blob/main/README.md) | Record-count limits left individual payloads and hidden spans unbounded; add opt-in field/byte admission limits, including merged updates and retained unsampled spans, without changing existing constructor behavior. |
| [bench](https://github.com/gomlang/bench/blob/main/README.md) | Plausible stored statistics could disagree with raw samples; add opt-in strict replay with shared bootstrap preflight, cancellation and tolerance-aware comparison of every reported statistic. |

### CLI and native tooling

| Module | Finding and improvement |
| --- | --- |
| [cli](https://github.com/gomlang/cli/blob/main/README.md) | Counter flags rejected defaults/environment values; store compact nonnegative fallback counts with explicit-occurrence precedence, stable provenance and bounded allocation. |
| [object](https://github.com/gomlang/object/blob/main/README.md) | Repeated ELF string-table references multiplied decoded names beyond per-name limits; add an aggregate name budget without changing public Limits fields, and apply it to existing entry points. |
| [dwarf](https://github.com/gomlang/dwarf/blob/main/README.md) | Line-table limits multiplied across compilation units; share row/file/directory budgets across distinct tables, count runtime definitions and preserve legacy public record shapes. |
| [image](https://github.com/gomlang/image/blob/main/README.md) | PNG encoding only emitted RGBA8 with adaptive filtering; add checked RGB/grayscale/grayscale-alpha options and fixed filters with channel-aware prediction, preserving defaults and rejecting data loss. |
| [datetime](https://github.com/gomlang/datetime/blob/main/README.md) | Full-range durations lacked division without overflowing total nanoseconds; add bounded magnitude division with truncation toward zero and recoverable zero-divisor/endpoint errors. |
| [llvm](https://github.com/gomlang/llvm/blob/main/README.md) | Runtime aggregate access required memory temporaries or textual IR; add checked struct/array extract_value and insert_value with lifetime, ownership, index and exact-type validation. |

## Application library expansion

Four new libraries and five existing-library extensions focus on application
integration. Existing public APIs remain available; GFM uses an explicit new
entry point and Web middleware is opt-in. HTML/image native dependency setup is
a documented consumer requirement, with affected ecosystem manifests migrated.

| Module | Added capabilities |
| --- | --- |
| [uuid](https://github.com/gomlang/uuid/blob/main/README.md) | Immutable UUID values, strict parsing/formatting, secure v4/v7, byte conversion, ordering, Hash and Serde. |
| [yaml](https://github.com/gomlang/yaml/blob/main/README.md) | Bounded block/flow parsing and emission, document streams, aliases, source diagnostics, dynamic values and typed Serde; an example adapts YAML into config. |
| [jwt](https://github.com/gomlang/jwt/blob/main/README.md) | HS256/RS256/ES256/EdDSA compact JWS, explicit key/algorithm binding, key IDs, strict decoding and configurable issuer/audience/time validation. |
| [s3](https://github.com/gomlang/s3/blob/main/README.md) | SigV4, configurable endpoints, object CRUD, ListObjectsV2 pagination, presigned operations and multipart completion/abort with cleanup. |
| [sql](https://github.com/gomlang/sql/blob/main/README.md) | Forward SQLite migrations with ordered versions, SHA-256 history, drift checks, write serialization and transactional rollback. |
| [web](https://github.com/gomlang/web/blob/main/README.md) | Bounded in-memory sessions, ID rotation/logout, explicit cookie policy, synchronizer-token CSRF and bounded token-bucket rate limiting. |
| [html](https://github.com/gomlang/html/blob/main/README.md) | Immutable HTML5 documents/fragments, navigation, CSS selectors, bounded output and conservative sanitization profiles. |
| [image](https://github.com/gomlang/image/blob/main/README.md) | JPEG encode/decode, still WebP decode/lossless encode, strict crop and nearest/bilinear resize over existing premultiplied pixels. |
| [markdown](https://github.com/gomlang/markdown/blob/main/README.md) | Opt-in GFM tables/alignment and task lists, independent extension AST, existing CommonMark behavior retained. |

## Capability review: 2026-10-04

The [per-library capability review](CAPABILITY_REVIEW.md) covers all 68 current
libraries, with source references and a disposition for every finding. Twelve
compatible additions were delivered: configurable ANSI width layout, ASN.1 BIT
STRING codecs, batch cache reads, undirected cycle witnesses, HTTP request
framing, lossless image orientation, early-stopping pipeline folds, literal
regular-expression replacement, reverse rope lines, numeric reply writing, GUID
byte interchange and custom directory ordering.

The report records 44 deferred candidates and 12 explicit scope boundaries.
Local module tests and isolated consumer verification cover the changed
libraries; each delivered commit has a linked GitHub Actions run. This round
does not replace the historical migration manifests or expand the verifier
inventory.

## Capability follow-up round: 2026-10-04

The [follow-up review](CAPABILITY_REVIEW_ROUND3.md) rechecks all 68 libraries and
implements twelve candidates from the preceding audit:

| Module | Added |
| --- | --- |
| bigint | Signed nth roots with truncation toward zero, signed remainders and explicit limits |
| decimal | Exact integral quotient/remainder and remainder-only operations |
| csv | Opt-in record-start comments with existing byte and record accounting |
| go_doc | Automatic HTTP(S) links in HTML prose, with bounded output and linear bracket handling |
| mail | Structured address lists retaining group names, empty groups and order |
| lsp | Checked completion items/lists with optional request-position validation |
| mime | Bounded discard of the current multipart body |
| parser | Binary sentinel-terminated collections with incomplete-input and shared-budget behavior |
| proptest | State-machine cleanup after execution panics while preserving the original panic |
| tabwriter | Explicit left/right alignment by column, including final numeric columns |
| x509 | Bounded Extended Key Usage DER codec and standard purpose OID helpers |
| xml | Optional scalar attribute/child mappings distinguishing missing and empty values |

Each changed library passed local module tests, independent consumer verification
and CI for its linked delivered revision. Cross-review corrected an automatic-URL
rescan issue; a decimal formatting gate was fixed before final CI success.
The previous report, historical split manifests and verifier inventory retain
their existing historical role. The new report records the next gaps in the
libraries changed during the prior round as well.

## Capability round 4: 2026-10-04

The [round 4 review](CAPABILITY_REVIEW_ROUND4.md) rechecks all 68 libraries and
adds twelve compatible capabilities:

| Module | Added |
| --- | --- |
| archive | Explicit UTC-offset interpretation of ZIP DOS modification timestamps |
| asn1 | Arbitrary-width canonical two's-complement INTEGER byte codecs |
| cache | Ordered batch writes with prevalidation, copied input and one critical section |
| fuzzy | Anchored match modes for collection, parallel and persistent-session search |
| graph | Deterministic dependency generations for topological scheduling |
| metrics | Bounded string and streaming Prometheus export |
| object | Bounded typed ELF notes with explicit alignment and byte order |
| prompt | Caller-supplied choice filtering/ranking with stable ties |
| regexp | Match/capture callbacks for replacement, including typed callback failures |
| textproto | Checked header replacement and removal with preserved field ordering |
| uuid | A synchronized monotonic v7 generator with rollback and exhaustion policies |
| xml | Repeated scalar child mappings and incremental bounded encoding |

A separate CSV documentation correction removes an obsolete claim that comment
records are unsupported. Local module tests and independent consumer checks
cover the twelve functional changes; the review links the final successful CI
runs for all thirteen changed library repositories. Cross-review found and
fixed a cache input-alias issue before final delivery. Earlier reports and
historical split manifests remain preserved.

## WebAssembly interpreter

The independent [`wasm`](https://github.com/gomlang/wasm/blob/main/README.md)
repository adds the 69th ecosystem library, `ecosystem::wasm`.

| Capability | Delivered scope |
| --- | --- |
| Binary modules | Bounded Core 2 scalar sections, data count, UTF-8 names, signed/unsigned LEB128, block signatures and malformed-input errors |
| Validation | Function and block typing, index checks, initializer rules, imports/exports and memory/table limits |
| Execution | Scalar integer/float instructions including sign extension and saturating conversions, multi-value blocks, references, multiple tables, bulk operations and Wasm backtraces |
| Embedding | Typed multi-result host functions, external references and objects, named linking, reusable validated modules and isolated store ownership |
| WASI Preview 1 | All 46 import signatures, explicit arguments/environment, buffered standard I/O, capability-relative in-memory files/directories, explicit clocks/randomness and process exit codes |
| Resource limits | Module/structural limits, local and operand/control storage, call depth, memory/table allocation and execution fuel |
| Verification | Module tests, independent example tests, pinned official specification fixtures, real wasi-sdk C commands/reactors and independent WASI ABI checks |

WASI host filesystem mounts, symbolic links, sockets and process signals remain
unsupported; symbolic-link calls return `NOTSUP`, sockets/signals return `NOSYS`.
WAT parsing, SIMD, threads, components, memory64, multiple memories, tail calls,
exceptions, GC and JIT compilation remain separate work. Host callbacks
are synchronous trusted application code; instruction fuel does not preempt their
work. WASI charges fuel for variable byte/metadata work and bounds I/O, file
storage, descriptors and polling; its default configuration inherits no process
resources. Stores require serial use, and the documented limits count logical resources
rather than every byte of allocator overhead.

## LSP initialization and workspace edits

The `lsp` library now bounds historical request/deadline/document map storage
through shared map compaction. Initialization exposes checked client/workspace
parameters with isolated JSON snapshots and a callback for dynamic capabilities;
failed initialization leaves protocol state unchanged and permits retry.

Workspace edit helpers represent versioned text edits, resource operations and
change annotations, validate ranges and references, and check client capabilities.
Only unversioned, unannotated edits with distinct document URIs can be lowered to
legacy `changes` without losing semantics. Applications still own filesystem/editor
execution and the language logic producing edits. Stress tests and independent
consumer tests cover lifecycle cleanup, capability negotiation and edit validation.

## Catalog maintenance

The catalog now records every library's scope and verification coverage in
[catalog.json](catalog.json), including the 13 libraries previously listed only
as links. Generated README tables keep the library count, alphabetical ordering
and application classification consistent. Historical split manifests continue
to describe the original 64-library extraction.

The standalone Python checker validates metadata, generated content, historical
manifest structure/membership and catalog document links. Its regression suite
covers malformed metadata, drift, duplicate entries, broken references and
module-coordinate mismatches. CI compares the catalog with the pinned verifier
inventory before running the existing infrastructure checks. Library tests and
current per-library CI results remain separate evidence.

Development examples select an installed GoML release explicitly, document the
private registry setup, and distinguish catalog validation from full ecosystem
verification. See [Maintaining this catalog](README.md#maintaining-this-catalog).

## Remaining work

| Module | Remaining capabilities and limits |
| --- | --- |
| [uuid](https://github.com/gomlang/uuid/blob/main/README.md) | Generates v4/v7 only. The default v7 random generator has no monotonic guarantee; MonotonicGenerator supplies a shared local sequence with explicit rollback/exhaustion behavior, without persistence or coordination across generators. Serde uses canonical strings; raw storage uses explicit byte conversion. |
| [yaml](https://github.com/gomlang/yaml/blob/main/README.md) | The documented YAML core-schema subset excludes arbitrary custom tags, complex mapping keys and cyclic aliases. Typed Serde/JSON bridges require string mapping keys and finite representable values. Native parse allocations precede some tree checks; normalization retries and input/work budgets remain explicit. |
| [jwt](https://github.com/gomlang/jwt/blob/main/README.md) | Compact JWS only; no JWE, OAuth, remote key fetching or JWK/JWKS import. Applications configure trusted issuers/audiences and provision/rotate keys. Supported algorithms and NumericDate limits are explicit. |
| [s3](https://github.com/gomlang/s3/blob/main/README.md) | Object and multipart APIs have explicit per-request budgets. Bucket administration, automatic region discovery, automatic retries and built-in cloud credential-provider discovery remain separate work. Protocol checks use AWS vectors and local independent peers, not a live cloud account. |
| [bigint](https://github.com/gomlang/bigint/blob/main/README.md) | Random-prime generation, Karatsuba/FFT multiplication and Montgomery reduction are still absent. Signed odd-degree roots truncate toward zero and return same-sign remainders. Root work has no cancellation or cryptographic constant-time guarantee; limits bound input magnitude rather than elapsed work. Root scratch products can reach twice the input bit length; exponent limits do not bound degree. |
| [bigmath](https://github.com/gomlang/bigmath/blob/main/README.md) | Addition and comparison still construct full cross products. Binary Float still lacks decimal parsing/formatting, subnormals, special values and transcendental functions. Cross-cancellation keeps the existing representation limits and adds workload-dependent GCD cost. |
| [decimal](https://github.com/gomlang/decimal/blob/main/README.md) | Results requiring nonzero digits outside the scale range still fail; the API does not silently reduce requested precision or underflow to zero. Lower-scale context limits, exact factor-removal limits, missing square root/transcendentals and absence of binary floating conversion remain. |
| [ndarray](https://github.com/gomlang/ndarray/blob/main/README.md) | Statistics remain floating-point approximations; extreme dynamic-range contributions and cancellation can still lose precision. No batched factorization, SVD, eigenvalue solver or rank-deficient least-squares support. |
| [graph](https://github.com/gomlang/graph/blob/main/README.md) | Directed and undirected searches return one cycle witness; cycle enumeration remains absent. Graph serialization, flow algorithms, floating weights and dynamic shortest-path maintenance remain absent; mutable storage is unsynchronized. |
| [bitflags](https://github.com/gomlang/bitflags/blob/main/README.md) | Name lookup and collision checks are still quadratic in declaration count; compiler derive budgets still apply. FlagValues emits inherent constructor methods; generated associated constants and overloaded bitwise operators remain absent. Runtime and declaration grammars remain separate. |
| [archive](https://github.com/gomlang/archive/blob/main/README.md) | Negative PAX timestamps remain unsupported; accepted fractions are reduced to whole seconds. Global PAX key merging remains a candidate for indexed lookup and explicit work bounds. Archive writer bodies/ZIP metadata remain bounded but partly materialized as documented. |
| [compress](https://github.com/gomlang/compress/blob/main/README.md) | GZIP writer still emits fixed headers and has no custom metadata API. Only the latest accepted header is exposed; empty concatenated members can be traversed in one read and are not separately enumerated. FEXTRA remains opaque bytes; application subfield semantics and Latin-1-to-Unicode conversion are caller concerns. Per-member metadata capture can retain previous and current headers; publication does not establish payload validity. |
| [msgpack](https://github.com/gomlang/msgpack/blob/main/README.md) | No calendar/timezone conversion API or automatic interpretation of opaque Extension values. Timestamp dynamic errors use InvalidTimestamp while generic typed paths surface Serde errors according to existing protocol. |
| [csv](https://github.com/gomlang/csv/blob/main/README.md) | Quoted fields still keep decoded and wire buffers for precise UTF-8 error mapping. Trimming still allocates a separate decoded field; further memory reduction would require a different position-tracking representation. Dialect inference and transcoding remain unsupported. Comments are opt-in at the start of a logical record and retain byte limits. |
| [asn1](https://github.com/gomlang/asn1/blob/main/README.md) | Time values remain TLV content; no Value/Schema time variants or native timestamp conversion. GeneralizedTime permits possible month-end 23:59:60 syntax but does not consult historical/future leap-second announcements. UTCTime leaves century selection to applications; year 00 may denote a leap century. Generic SET/SET OF distinctions, unknown primitive semantics, high tag numbers, and certificate policy remain outside the supported subset. |
| [xml](https://github.com/gomlang/xml/blob/main/README.md) | DTD/external entities, non-UTF-8 encodings and general schema validation remain intentionally unsupported. Incomplete-token scanning still rescans pending data across feeds; a cursor/work-budget redesign could bound adversarial one-byte feeding more tightly. Ordinary PI payload whitespace behavior is unchanged. |
| [request](https://github.com/gomlang/request/blob/main/README.md) | Trailer policy rejects the known framing/routing trio; it is not an exhaustive application-specific field allowlist. Unknown extension trailers remain accepted. Buffered responses still discard trailer values after validation; only streaming responses expose them. HTTP/2 streaming, HTTP/3 and async/await remain outside current support. |
| [http](https://github.com/gomlang/http/blob/main/README.md) | Transfer-coding parameters are explicitly unsupported. No stream decoding, actual byte-limit enforcement, connection reuse or 101 switching implementation is provided. |
| [websocket](https://github.com/gomlang/websocket/blob/main/README.md) | Validation runs when a complete frame is processed, not on every partial transport read. Frame and aggregate message limits continue to bound buffered bytes. Compression/extensions and Autobahn certification remain outside the supported contract. |
| [textproto](https://github.com/gomlang/textproto/blob/main/README.md) | No registry descriptions, retry policy or command-specific SMTP policy. Candidate detection is explicitly one ASCII digit followed by a dot at the start of each line; arbitrary text is not guessed to be an enhanced code. |
| [mime](https://github.com/gomlang/mime/blob/main/README.md) | Caller still supplies boundary and part policy; multipart semantic Content-Disposition handling is outside this streaming framing API. Inside a part body, boundary candidates exceeding max_line_bytes fail early, even if a later byte would prove the prefix to be ordinary body data. Before the first part, complete lines are buffered within max(max_preamble_bytes, max_line_bytes, closing marker length)+2 and recognized delimiters are then checked against max_line_bytes. |
| [mail](https://github.com/gomlang/mail/blob/main/README.md) | Domain literal FWS, obsolete quoted-pair syntax and non-ASCII dtext remain unsupported. Literal contents are not interpreted as IP addresses, and parsing does not resolve domains. |
| [x509](https://github.com/gomlang/x509/blob/main/README.md) | Complete certificates, signature/chain validation, trust roots and typed subject alternative names remain out of scope. Caller enforces algorithm-specific combinations, CA/key-usage consistency and extension criticality. |
| [sql](https://github.com/gomlang/sql/blob/main/README.md) | The payload budget does not cap peak memory, native current-row allocation, metadata, snapshot copies or allocations in custom FromRow implementations. The existing query_all remains row-bounded only; pooled callers choose the new budget through scoped executor access. Generic prepared statements, checked batch operations and non-SQLite adapters remain separate work. SQLite migrations are forward-only and require transactional journaling; cross-connection concurrency is verified on file-backed databases. |
| [sqlite](https://github.com/gomlang/sqlite/blob/main/README.md) | Limits bound collected input payload rather than SQLite engine allocations or process memory. Streaming remains appropriate for large results. Backup, incremental BLOB I/O and custom SQL functions remain unsupported. No changes to the single-connection native serialization or existing transaction/cancellation semantics. |
| [redis](https://github.com/gomlang/redis/blob/main/README.md) | Connectors remain responsible for resources they create before returning a Connection; the pool cannot recover an unreturned handle after a connector panic. Noncooperative connector/transport callbacks cannot be forcibly preempted. Cluster/Sentinel/sharded subscriptions remain outside this bounded change; panic handling is not a general conversion of arbitrary application panics into Result errors. |
| [web](https://github.com/gomlang/web/blob/main/README.md) | Only one buffered byte range is served; multipart ranges and date validators remain unsupported. Static file content still must fit the configured max_bytes and is read fully before hashing or slicing. HTTP/2, HTTP/3 and streaming compression remain separate work. Session storage is in-memory; distributed persistence and application-specific authentication remain separate integrations. |
| [parser](https://github.com/gomlang/parser/blob/main/README.md) | Token-stream parsing, resumable transport input and language-specific recovery remain outside this byte-string parser. The scanner allocates O(marker bytes) prefix storage and retains the input string. |
| [syntax](https://github.com/gomlang/syntax/blob/main/README.md) | Zero-width token occurrences are intentionally excluded from range intersection. General covering lookup, transactional multiple edits and source revision tracking remain separate future work. Iterator aliases share a serial cursor; each token seek costs tree depth and returns the complete token. |
| [logos](https://github.com/gomlang/logos/blob/main/README.md) | The complete source remains retained and source() exposes it for explicit inspection. Streaming input, captures and incremental DFA rebuilding remain absent. Ranges restrict matching/cursor movement; callbacks can inspect the complete retained source and must bound their own work. |
| [regexp](https://github.com/gomlang/regexp/blob/main/README.md) | Replacement remains eager and this iterator retains its full input snapshot rather than accepting streaming transport data. Named captures and broader regex syntax remain outside the current engine. Iterator aliases share state, and a consumer can see earlier segments before a later error. |
| [diff](https://github.com/gomlang/diff/blob/main/README.md) | No deadline/cancellation callback or byte-accurate heap budget is provided. Worst-case Myers complexity and custom comparator cost still depend on the inputs and callback. Work units count comparator calls, not work inside user callbacks. |
| [rope](https://github.com/gomlang/rope/blob/main/README.md) | Reverse line traversal, bidirectional cursors and grapheme segmentation remain absent. Chunk prefix creation may copy at most one bounded leaf; raw byte cursors intentionally permit positions inside UTF-8 scalars. Reverse chunks retain forward byte order within each UTF-8 chunk; copied cursors share state. |
| [proptest](https://github.com/gomlang/proptest/blob/main/README.md) | Legacy weighted/composite/collection choices retain modulo selection; callers opt into the new standalone generators. A finite rejection budget can return Err; this is deterministic pseudorandom testing support rather than cryptographic randomness. Rejection sampling is opt-in; half-open ranges use an explicit draw budget and full-width endpoints remain available through any_u64/any_i64. |
| [template](https://github.com/gomlang/template/blob/main/README.md) | Macros/imports/call blocks, keyword arguments, recursive loops and file-loader invalidation remain unsupported. String scans and caller-owned context allocation are not independently bounded by the output limit; this change bounds escaped-output construction. |
| [markdown](https://github.com/gomlang/markdown/blob/main/README.md) | GFM tables and task lists are implemented through opt-in APIs; other GFM extensions, footnotes, math, highlighting and finer inline spans remain separate work. Existing parser work budgets and walker auxiliary-storage bounds do not bound caller-owned AST allocations. |
| [html](https://github.com/gomlang/html/blob/main/README.md) | DOM nodes are immutable; incremental DOM mutation, browser execution/layout and automatic template-context analysis remain separate work. Selectors use a documented subset and conservative structural-work admission, which can reject expensive queries before matching. Sanitizers have explicit conservative policies and output-context limits. Native parsing allocates its tree before validating node/depth limits; input bytes are bounded. The existing entity decoder remains a serial UTF-8 string stream. |
| [highlight](https://github.com/gomlang/highlight/blob/main/README.md) | Full Markdown parsing, interpolation, semantic symbol scopes and TextMate/Sublime compatibility are still unsupported. Incremental edits still reconstruct and split full source even when lexical suffixes are reused. |
| [go_doc](https://github.com/gomlang/go_doc/blob/main/README.md) | Go source/symbol extraction, import resolution, directives, legacy headings and nested list blocks remain unsupported. Automatic HTTP(S) links apply to HTML prose rendering; other render formats and the AST remain unchanged. The parser still implements a bounded comment subset, not every Go doc heuristic. |
| [lsp](https://github.com/gomlang/lsp/blob/main/README.md) | Checked initialization and WorkspaceEdit models are available, including capability checks and lossless legacy conversion. Semantic-token builders, extended completion fields and workspace-edit execution remain application work. Worker/timer scheduling and concurrent server/session mutation remain outside the library. Output limits exclude caller-owned replacements and edit-span storage; coordinate/overlap errors retain precedence. |
| [cache](https://github.com/gomlang/cache/blob/main/README.md) | Single global cache gate; sharding and proactive background expiry remain absent. Generic key hashing/equality and user copy/removal policies still have their documented panic and aliasing contracts. Weight measures caller-supplied units, not retained bytes. TTI updates and removals cost O(log n); backing storage can retain its high-water capacity. |
| [incremental](https://github.com/gomlang/incremental/blob/main/README.md) | Evaluation is serialized; no parallel independent query branches or persistent revision snapshots. User policies must honor purity/copy rules and cannot be preempted while running. Cancellation in the later caller-result copy can occur after a valid memo has already been published. |
| [pipeline](https://github.com/gomlang/pipeline/blob/main/README.md) | Expansion remains sequential; no bounded parallel flatten operator was added. Arbitrary callbacks and external blocking operations require cooperative cancellation; no typed panic recovery. |
| [config](https://github.com/gomlang/config/blob/main/README.md) | Providers have no automatic polling/file registration; a file source is still required for HotReload. YAML is available through the yaml library dynamic-source example; no built-in YAML Format variant, INI/interpolation or integrated secret-store client. Callback allocation/work happens before returned-document limits and cannot be forcibly interrupted. Providers run synchronously, must synchronize shared state and cannot reenter the same Live reload. |
| [tempfile](https://github.com/gomlang/tempfile/blob/main/README.md) | Linux target; no asynchronous or cancellation-specific file I/O. Positioned operations do not provide an atomic snapshot against external mutation. No cross-filesystem persistence fallback or automatic durability fsync. Completed I/O prefixes remain visible on failure; exact operations are not transactional. |
| [ignore](https://github.com/gomlang/ignore/blob/main/README.md) | Rule matching still scans flat applicable rule arrays; no combined automaton or compiled ruleset index. Pattern matching remains byte-oriented with documented ASCII case-folding rather than Unicode case folding. |
| [notify](https://github.com/gomlang/notify/blob/main/README.md) | Linux inotify only; no other OS backend. No conversion of user panic into typed notify errors. Callbacks must respect existing synchronization/reentrancy constraints. Cleanup failures during panic unwinding are discarded; synchronous watcher ownership remains with the caller. |
| [walkdir](https://github.com/gomlang/walkdir/blob/main/README.md) | Device equality cannot distinguish bind mounts on the same device. Synchronous filesystem calls cannot be preempted by cancellation. No security sandbox or hostile mount/rename isolation is provided. The option controls descent, not entry visibility. |
| [ansi](https://github.com/gomlang/ansi/blob/main/README.md) | CSI and intermediate ESC sequences still rescan their bounded retained prefix; this optimization specifically targets long opaque strings. Single-byte C1 mode and terminal screen emulation remain unsupported. |
| [terminal](https://github.com/gomlang/terminal/blob/main/README.md) | Kitty keyboard negotiation, modifyOtherKeys, legacy X10 mouse and terminfo-specific keys remain unsupported. Independent sessions require exclusive terminal ownership; no signal/process-exit cleanup handlers are installed. |
| [tui](https://github.com/gomlang/tui/blob/main/README.md) | Wide glyphs are drawn only when their complete cells fit; no bidirectional shaping or IME composition is implemented. Editor state is intended for one event loop and does not synchronize concurrent mutations. |
| [prompt](https://github.com/gomlang/prompt/blob/main/README.md) | Completion and validation callbacks remain synchronous and must be responsive. History/completion are bounded in-memory facilities without persistence or background providers. |
| [progress](https://github.com/gomlang/progress/blob/main/README.md) | Clock callbacks still run under the manager lock and must be quick/non-reentrant; blocking callbacks cannot be recovered by panic handling. No background renderer, recursive job tree or pause/resume accounting is provided; context-aware updates remain the cancellable choice behind synchronous output. |
| [tui_markdown](https://github.com/gomlang/tui_markdown/blob/main/README.md) | Search remains literal, case-sensitive and restricted to each displayed line; reflow retains the active ordinal rather than source identity. Pipe tables are a limited top-level extension, and deeply nested prefixes can still consume a narrow viewport. |
| [tabwriter](https://github.com/gomlang/tabwriter/blob/main/README.md) | Column alignment still requires buffering complete tabbed blocks until a plain line or flush. Width policies do not interpret ANSI escapes; cell control bytes are preserved and untrusted terminal content needs caller sanitization. Limits cover logical input/output bytes rather than container overhead. |
| [color](https://github.com/gomlang/color/blob/main/README.md) | CSS currentcolor/none, escapes, comments, variables and typed Lab/Oklab CSS syntax remain unsupported. |
| [unicode_text](https://github.com/gomlang/unicode_text/blob/main/README.md) | No incremental edit tracking or streaming index; construction and retained storage remain input-proportional. Dictionary/locale segmentation, normalization, bidi reordering, hyphenation and sentence segmentation remain outside scope. Indexes retain original string storage; the convenience constructor is uncapped. |
| [diagnostics](https://github.com/gomlang/diagnostics/blob/main/README.md) | Index construction scans once; original occasional-query APIs still scan prefixes. Display-column/grapheme layout has no corresponding cached position index; source revisions remain immutable snapshots. Sparse indexes retain their immutable source and add input-proportional checkpoint storage. |
| [fuzzy](https://github.com/gomlang/fuzzy/blob/main/README.md) | Corpus preparation and session eligibility still retain input-proportional state; scoring DP budgets unchanged. Final bounded sort cannot be interrupted midway; context is checked immediately before and after sorting. |
| [metrics](https://github.com/gomlang/metrics/blob/main/README.md) | Registry still uses a global lock and some registration/lifecycle scans; no sharding or persistent cache. Lookup construction can cost more for tiny batches targeting a large family; temporary maps are bounded by configured existing cardinality and labels. |
| [tracing](https://github.com/gomlang/tracing/blob/main/README.md) | Per-record logical bounds are not an aggregate bound on all caller-retained spans/sink-retained records. Existing constructor remains unbounded; arbitrary blocking sink callbacks remain non-preemptible. Logical byte accounting excludes JSON expansion, allocator overhead and backing storage pinned by slices. |
| [bench](https://github.com/gomlang/bench/blob/main/README.md) | Strict arithmetic reproducibility does not establish raw timing, workload or environment authenticity. Ordinary import remains inexpensive structural validation; callers choose strict replay explicitly. Sorting cannot be preempted mid-sort, and the documented tolerance permits tiny statistical perturbations. |
| [cli](https://github.com/gomlang/cli/blob/main/README.md) | Automatic negated flags and dynamic completion remain unsupported. Completion remains static and does not suppress constraints or used scalar options. |
| [object](https://github.com/gomlang/object/blob/main/README.md) | Relocations, section decompression and dynamic-linker views remain outside the metadata reader scope. Raw note records are available with explicit 4/8-byte alignment; vendor-specific descriptors still require interpretation. Existing entry points now apply an aggregate name budget; larger expanded metadata requires an explicit allowance. |
| [dwarf](https://github.com/gomlang/dwarf/blob/main/README.md) | DWARF64, indexed/supplementary/split/type units and v5 define_file remain unsupported. Legacy parse results temporarily materialize detailed rows before projection, as in the previous round. Line row/file/directory budgets are aggregate across tables; implicit sentinels consume no real-item allowance. |
| [image](https://github.com/gomlang/image/blob/main/README.md) | JPEG and still WebP are supported, including lossless WebP encoding. Animated WebP, lossy WebP encoding, metadata/color-profile preservation and additional codecs remain unsupported. Existing PNG output still lacks palette/lower-bit-depth/16-bit/interlaced encoding. Image dimensions and pixel counts retain explicit bounds. |
| [datetime](https://github.com/gomlang/datetime/blob/main/README.md) | Other rounding modes, recurrence scheduling, localized rendering, leap-second/TAI arithmetic and automatic timezone-data updates remain outside scope. Elapsed-time division discards sub-nanosecond remainders toward zero and retains endpoint asymmetry. |
| [wasm](https://github.com/gomlang/wasm/blob/main/README.md) | WASI Preview 1 has an explicit bounded in-memory filesystem; host mounts, symbolic links, sockets and signals remain unsupported. Text-format parsing, SIMD, threads, components and Core 3 features remain separate work. Host callbacks require their own work/deadline limits. Stores require serial use. |
| [llvm](https://github.com/gomlang/llvm/blob/main/README.md) | JIT/ORC, global construction, named recursive structs, vector operations, atomics, debug metadata and general ABI/linkage controls remain outside scope. Native LLVM parsing and code generation are not a process isolation boundary for hostile IR or LLVM internal failures. LLVM 18 is required; aggregate access uses one immediate member index per call, and callers still own SSA/ABI correctness. |
| [goml_stats](https://github.com/gomlang/goml_stats/blob/main/README.md) | Manifest-based canonical identities, declaration counts and historical comparisons; hierarchical Git ignore rules are provided by the ignore dependency |

Further work should preserve resource bounds, recoverable errors, normal
versioned dependency consumption and the independent reference checks already
present. Bundled networking adapters and concurrent resource pools need actual
I/O and race coverage, beyond a public interface or a mock implementation.
