# GoML ecosystem libraries

This repository is the ecosystem catalog, migration history and development
guide. Library implementation changes belong in the corresponding repository;
this catalog has no `goml.toml` and is not an importable GoML module.

Each library lives in an independent [gomlang GitHub repository](https://github.com/gomlang).
Each library repository contains its public API, documentation, tests and examples.
Ordinary examples share the library's root `goml.toml`; `[dev-dependencies]`
contains their test helpers. The verifier, Explorer application and statistics
tool retain separate repositories. The ecosystem requires
[GoML 0.1.57](https://github.com/gomlang/goml/releases/tag/v0.1.57) or newer.
Source files and generated GoML bindings use `.goml`.
Libraries with native integration document their Go adapters and system prerequisites.
The [split manifest](https://github.com/gomlang/ecosystem/blob/main/split-manifest.tsv) records the source commit and the
history and tree IDs used to create each library repository.
The [consumer split manifest](https://github.com/gomlang/ecosystem/blob/main/consumer-split-manifest.tsv) records the history
originally imported into each library's former `consumer/` directory. That historical record is unchanged by the example migration.

The libraries below have implementations, public documentation, independent
downstream checks and executable verification. The table records their implemented scope;
individual READMEs describe API semantics and limits. [ROADMAP.md](https://github.com/gomlang/ecosystem/blob/main/ROADMAP.md)
tracks completed improvements and the remaining functional gaps.

The [library boundary map](https://github.com/gomlang/goml/blob/main/docs/library-boundaries.md)
assigns each A/B capability to std or ecosystem and records dependency order and
acceptance status. Pure GoML migration does not promote a module into std:
request, web, archive, color and markdown remain independently versioned here.
Standard packages must not depend on ecosystem modules.

E1 migration is in progress in [compress](https://github.com/gomlang/compress/blob/main/README.md): incremental
DEFLATE, GZIP, ZLIB and LZW encoding and decoding are exercised by the
isolated compress example. Archive compatibility adapters and the other E1
capabilities remain separate migration work; this is not completion of E1.

## Current improvement audit

The application-library expansion adds four libraries:
`uuid`, `yaml`, `jwt` and `s3`, plus SQLite migrations, Web sessions/CSRF/rate
limiting, HTML DOM/selectors/sanitization, JPEG/WebP codecs and image transforms,
and opt-in Markdown tables/task lists. The
[expansion audit](https://github.com/gomlang/ecosystem/blob/main/ROADMAP.md#application-library-expansion)
records the scope and remaining boundaries.

### Previous per-library audits

The second ecosystem-wide audit adds another bounded improvement to each of the
64 libraries. Changes include numeric stability, indexed lookups, incremental
text APIs, stricter protocol parsing and resource cleanup, plus explicit limits
for collected data and generated output. The
[second per-library audit](https://github.com/gomlang/ecosystem/blob/main/ROADMAP.md#second-ecosystem-wide-improvement-audit)
pairs each original gap with the implemented change; the
[remaining work](https://github.com/gomlang/ecosystem/blob/main/ROADMAP.md#remaining-work)
keeps unsupported cases, ownership rules and resource limits visible.
The [previous ecosystem-wide audit](https://github.com/gomlang/ecosystem/blob/main/ROADMAP.md#ecosystem-wide-improvement-audit)
and all earlier batches remain recorded.

See the [catalog Actions](https://github.com/gomlang/ecosystem/actions) and each
library's Actions page for results on current revisions. The capability table
records established coverage and fixed reference datasets, rather than the live
CI status of every library. Its contents are generated from [catalog.json](catalog.json).

<!-- catalog:start -->

The catalog contains **68 libraries**.

| Module | Implemented scope | Verification coverage |
| --- | --- | --- |
| [ansi](https://github.com/gomlang/ansi/blob/main/README.md) | Structured styles, 16/256/truecolor profiles, streaming UTF-8/escape parsing, hyperlinks, styled graphemes and partial-write adapters | Module tests, downstream tests and 2,800 independent protocol/rendering cases |
| [archive](https://github.com/gomlang/archive/blob/main/README.md) | GoML USTAR/PAX and ZIP/ZIP64 codecs, CRC32, bounded TAR streaming and ZIP indexing, DEFLATE/GZIP codecs, metadata and rooted extraction with an openat fallback for older kernels | Module tests, GNU gzip/tar/Info-ZIP interoperability, downstream check and race checks |
| [asn1](https://github.com/gomlang/asn1/blob/main/README.md) | Bounded canonical DER values, explicit positional schemas, OIDs and TLV time validation | Library and independent example tests for canonical encodings, limits and malformed input |
| [bench](https://github.com/gomlang/bench/blob/main/README.md) | Adaptive sampling, parameterized workloads, setup exclusion, bootstrap statistics, baseline comparisons, throughput, cancellation and JSON/HTML reports | Module tests, deterministic clocks, real sorting downstream check and race checks |
| [bigint](https://github.com/gomlang/bigint/blob/main/README.md) | Immutable signed/unsigned arbitrary-precision integers, arithmetic/division, bitwise operations, radix/byte conversions, number theory and exact Serde | Module tests, downstream tests, race checks and 1,938 Python reference cases |
| [bigmath](https://github.com/gomlang/bigmath/blob/main/README.md) | Immutable bounded arbitrary-precision rationals and binary floating-point values with explicit rounding | Library and downstream tests with frozen Go math/big reference vectors |
| [bitflags](https://github.com/gomlang/bitflags/blob/main/README.md) | Typed integer flag sets, trait and inherent derives, unknown-bit policies, set algebra, name iteration, text and numeric Serde | Module tests, downstream check, derive diagnostics and 4,601 Rust reference comparisons |
| [cache](https://github.com/gomlang/cache/blob/main/README.md) | Generic concurrent weighted LRU, TTL/TTI, injectable clocks, bounded singleflight loading, invalidation generations, copy policy and removal callbacks | Module tests and race checks, versioned downstream check and 42,240 Python reference operations |
| [cli](https://github.com/gomlang/cli/blob/main/README.md) | Command schemas, aliases, inherited globals, groups, nested/flattened Args, typed subcommand derives and Bash/Zsh/Fish completion | Module and downstream check tests |
| [color](https://github.com/gomlang/color/blob/main/README.md) | Checked sRGB/linear/HSL/HSV/XYZ/Lab/Oklab conversions, CSS colors, alpha compositing, gamut mapping, contrast, Delta E and gradients | Pure GoML over standard math; module tests, downstream check tests and 4,659 numerical reference cases |
| [compress](https://github.com/gomlang/compress/blob/main/README.md) | Incremental bounded DEFLATE, GZIP, ZLIB and LZW codecs with dictionary, checksum and bit-order contracts | Module tests, Go codec interoperability, independent downstream check and race checks |
| [config](https://github.com/gomlang/config/blob/main/README.md) | Layered typed JSON/TOML, environment and CLI sources, merge policies, JSON Pointer edits, provenance, validation, immutable snapshots and filesystem hot reload | Module tests, real inotify reloads, versioned downstream check and race checks |
| [csv](https://github.com/gomlang/csv/blob/main/README.md) | Streaming standard I/O, quoted multiline fields, configurable dialects, byte/UTF-8 records, headers, precise positions, limits and typed Serde schemas | Module tests, 1,500 generated roundtrips, versioned file downstream check and race checks |
| [datetime](https://github.com/gomlang/datetime/blob/main/README.md) | Checked calendars and nanosecond instants, explicit arithmetic policies, RFC3339, TZif/POSIX timezones, DST ambiguity resolution and Serde | Module tests and race checks, versioned downstream check and 8,140 calendar/timezone reference cases |
| [decimal](https://github.com/gomlang/decimal/blob/main/README.md) | Exact base-10 arithmetic over bigint, precision contexts, seven rounding modes, quantization, checked conversions and representation-preserving Serde | Module tests, versioned downstream check, race checks and 3,072 Python Decimal value/error/status comparisons |
| [diagnostics](https://github.com/gomlang/diagnostics/blob/main/README.md) | Checked source caches/spans, Unicode multi-file labels, themes, clipping, suggestions and conflict-checked edits | Module tests, downstream tests and 6,236 independent source/edit/rendering cases |
| [diff](https://github.com/gomlang/diff/blob/main/README.md) | Myers and linear-space Hirschberg differences, unified patches, checked application, context and newline preservation | Tests and GNU interoperability |
| [dwarf](https://github.com/gomlang/dwarf/blob/main/README.md) | Bounded DWARF32 v2–5 units, DIEs, forms and line tables over standard random-access input | Library and downstream tests with checked-in compiler-produced binary fixtures and reference line tables |
| [fuzzy](https://github.com/gomlang/fuzzy/blob/main/README.md) | Unicode ranked subsequences, full case folding, grapheme-safe highlights, anchored modes, stable Top-K, persistent incremental queries and cancellable parallel search | Module tests, 1,270 exhaustive reference cases, versioned downstream check and race checks |
| [go_doc](https://github.com/gomlang/go_doc/blob/main/README.md) | Go documentation-comment AST and bounded comment, plain-text, Markdown and HTML rendering | Library and downstream examples covering indentation, links and output limits |
| [graph](https://github.com/gomlang/graph/blob/main/README.md) | Mutable directed/undirected graphs, stable IDs, traversal, components, topological order, cycle witnesses, shortest paths and spanning trees | Independent algorithm checks and downstream check tests |
| [highlight](https://github.com/gomlang/highlight/blob/main/README.md) | Extensible logos grammars, GoML/JSON/TOML/Markdown scopes, nested and cross-line regions, embedded fences, persistent incremental documents and ANSI/HTML output | Module tests, 200 incremental/full rebuild comparisons, rope downstream check and race checks |
| [html](https://github.com/gomlang/html/blob/main/README.md) | Entity utilities, immutable HTML5 DOM, CSS selectors and conservative HTML sanitization | Existing pure GoML entity code plus managed document backend, independent recovery and hostile-input fixtures |
| [http](https://github.com/gomlang/http/blob/main/README.md) | Transport-independent HTTP header validation, hop-by-hop filtering and HTTP/1.1 response framing | Library and downstream tests for framing ambiguity, syntax errors and output limits |
| [ignore](https://github.com/gomlang/ignore/blob/main/README.md) | Glob sets, hierarchical Git ignore rules, match explanations, worktree metadata, bounded traversal, cancellation and parallel callbacks | Module tests and race checks, versioned downstream check and 9,400 real Git reference queries |
| [image](https://github.com/gomlang/image/blob/main/README.md) | PNG/JPEG/WebP codecs, premultiplied images, drawing, strict crop and nearest/bilinear resize | Native JPEG/WebP backends, independent image fixtures and consumer checks |
| [incremental](https://github.com/gomlang/incremental/blob/main/README.md) | Typed heterogeneous inputs/queries, dynamic dependencies, revision validation, unchanged-result cutoff, atomic updates, cancellation and bounded memoization | Module tests and race checks, versioned downstream check and 15,847 from-scratch oracle queries |
| [jwt](https://github.com/gomlang/jwt/blob/main/README.md) | Compact JWS signing/verification with HS256, RS256, ES256 and EdDSA, key selection and claims policies | Standard Go crypto backend, strict parsing and independent signature vectors |
| [llvm](https://github.com/gomlang/llvm/blob/main/README.md) | LLVM 18 typed handles, SSA construction/editing, mutable-local promotion, IR traversal, target machines, ABI layouts, optimization and cross-target output | Module tests, native tests, downstream tests, race checks, four target formats and 12,420 linked-function comparisons |
| [logos](https://github.com/gomlang/logos/blob/main/README.md) | Typed UTF-8 lexers, regex/literal rules, longest match, priorities, callbacks/extras, mode switching, checked source ranges and bounded Thompson NFA matching | Module tests, downstream check, race checks and 3,155 Python reference cases |
| [lsp](https://github.com/gomlang/lsp/blob/main/README.md) | JSON-RPC framing, persistent document snapshots, UTF-8/16/32 negotiation, synchronous/deferred dispatch and bidirectional request deadlines | Module tests, downstream tests and independent position/edit/protocol checks |
| [mail](https://github.com/gomlang/mail/blob/main/README.md) | Bounded mailbox/address lists and header blocks with MIME encoded-word integration | Library and downstream tests for address grammar, folding, encoded words and resource limits |
| [markdown](https://github.com/gomlang/markdown/blob/main/README.md) | CommonMark AST/rendering plus opt-in GFM tables and task lists with a separate extension AST | Existing 652 CommonMark examples retained; official GFM fixtures and consumer checks |
| [metrics](https://github.com/gomlang/metrics/blob/main/README.md) | Concurrent counters/gauges/histograms, descriptor and label validation, cardinality limits, consistent snapshots, atomic gauge collection, timers and Prometheus exposition | Module tests, live HTTP scrape downstream check and race checks |
| [mime](https://github.com/gomlang/mime/blob/main/README.md) | MIME media types, RFC 2231 parameters, RFC 2047 encoded words and streaming multipart bodies | Library and downstream tests for malformed parameters, encoding boundaries and bounded multipart streams |
| [msgpack](https://github.com/gomlang/msgpack/blob/main/README.md) | MessagePack wire types, direct Serde and standard stream integration, typed/dynamic frames, malformed-input limits and interoperability | Module tests, downstream checks and 2,490 reference interoperability cases |
| [ndarray](https://github.com/gomlang/ndarray/blob/main/README.md) | Generic shared views, slicing, broadcasting, checked arithmetic, reductions, batched multiplication, LU/Cholesky/QR solves and SIMD | Module tests, versioned downstream check, 2,929 NumPy cases and native/SSE2/scalar builds |
| [notify](https://github.com/gomlang/notify/blob/main/README.md) | Linux inotify watchers, recursive maintenance, event filters, ignored subtrees, multi-path registrations, cancellable reads and bounded subscriptions | Module tests, the complete migrated downstream check suite and race checks |
| [object](https://github.com/gomlang/object/blob/main/README.md) | Bounded ELF32/ELF64 metadata, sections, program headers, symbols and extended numbering in either byte order | Library and downstream tests for binary layouts, extended indexes, range validation and ownership |
| [parser](https://github.com/gomlang/parser/blob/main/README.md) | Text/binary combinators, recursive grammars, shared work/depth budgets, explicit multi-error recovery, linear literal scans, spans, contextual errors and operator precedence | Module and downstream check tests |
| [pipeline](https://github.com/gomlang/pipeline/blob/main/README.md) | Lazy streams, bounded parallel transforms, filtering, ordering, batching/windows, merge/zip, backpressure and cancellation | Module tests and race checks, versioned downstream check and 1,253 Python oracle cases |
| [progress](https://github.com/gomlang/progress/blob/main/README.md) | Concurrent bars/spinners, snapshots, rate/ETA, throttling, coordinated logging, redirected output and cancellable shutdown | Module tests, independent downstream check, 400 numerical cases, race detector and real PTY checks |
| [prompt](https://github.com/gomlang/prompt/blob/main/README.md) | Typed text/password/integer input, validation, history/completion, searchable single/multiple choices and confirmation | Module tests, independent downstream check and real PTY sessions |
| [proptest](https://github.com/gomlang/proptest/blob/main/README.md) | Composable generators, lazy budgeted shrinking, failure campaigns, distributions, persistent replay, opt-in rejection sampling, model/system execution and IEEE edge cases | Module tests and independent downstream tests |
| [redis](https://github.com/gomlang/redis/blob/main/README.md) | RESP2/3 codec, typed commands, pipelining, transactions, Pub/Sub, bounded pools, DNS/TLS, injectable transport, context cancellation and total deadlines | Module tests and race checks, versioned downstream fixtures, 2,391 protocol cases, Redis 7.2.5 RESP2/3 interoperability and DNS/TLS cases in normal/race builds |
| [regexp](https://github.com/gomlang/regexp/blob/main/README.md) | Bounded regular-expression syntax and Thompson NFA matching with captures, lazy match/split iteration and replacement | Library and downstream tests for UTF-8 boundaries, capture behavior, syntax diagnostics and shared work limits |
| [request](https://github.com/gomlang/request/blob/main/README.md) | GoML HTTP(S)/HTTP2 clients with pooled multiplexed connections, request builders, JSON/form/multipart, redirects, per-stream cancellation, TLS policy and bounded responses | Module tests, race checks, downstream checks and HTTP/TLS/proxy interoperability with native reference servers |
| [rope](https://github.com/gomlang/rope/blob/main/README.md) | Persistent balanced UTF-8 text, shared snapshots, checked edits/slices, UTF-16 and line indexing, forward/reverse cursors and streaming I/O | Module tests and race checks, versioned downstream check and 3,266 Python reference edits |
| [s3](https://github.com/gomlang/s3/blob/main/README.md) | S3-compatible SigV4 client, object operations, listing, presigning and multipart lifecycle | AWS signing vectors and local independent wire-protocol checks |
| [sql](https://github.com/gomlang/sql/blob/main/README.md) | Typed database contracts and pools, SQLite adaptation, transactional migrations and checksum history | Real SQLite upgrade, drift, rollback and concurrent migration checks |
| [sqlite](https://github.com/gomlang/sqlite/blob/main/README.md) | Typed binding/rows, prepared statements, streaming queries, nested savepoints, rollback, cancellation and explicit resource management | Module tests, native tests, versioned downstream check, 2,754 SQLite comparisons and race checks |
| [syntax](https://github.com/gomlang/syntax/blob/main/README.md) | Immutable lossless green trees, red navigation, typed AST views, bounded interning/builders, checked ranges, range token iteration and persistent subtree edits | Module tests and race checks, versioned downstream check, 3,840 model-checked edits and 240 lossless rewrites |
| [tabwriter](https://github.com/gomlang/tabwriter/blob/main/README.md) | Bounded streaming tab alignment with byte or terminal-column measurement | Library and downstream tests for fragmented input, CRLF handling and buffer/output limits |
| [tempfile](https://github.com/gomlang/tempfile/blob/main/README.md) | Secure temporary files/directories, anonymous files, atomic persistence, ownership transfer, scoped cleanup and memory-to-disk spooling | Module tests and race checks, downstream check and 160 concurrent filesystem comparisons |
| [template](https://github.com/gomlang/template/blob/main/README.md) | Expressions, lexical scopes, conditions, loops, filters, includes, inheritance, escaping and contextual diagnostics | Module tests, downstream tests and 1,367 Jinja shared-syntax comparisons |
| [terminal](https://github.com/gomlang/terminal/blob/main/README.md) | Linux raw sessions, typed keyboard/mouse/paste/focus/resize events, capability detection, cancellable I/O and explicit restoration | Module tests, independent downstream check, race detector and real PTY checks |
| [textproto](https://github.com/gomlang/textproto/blob/main/README.md) | Bounded CRLF lines, folded-header framing and dot-encoded text streams over standard I/O | Library and downstream tests for fragmented frames, clean EOF and malformed protocol input |
| [tracing](https://github.com/gomlang/tracing/blob/main/README.md) | Structured events, nested spans, explicit task contexts, filtering/sampling, composed sinks, bounded asynchronous output and coordinated cleanup | Module tests and race checks, downstream tests and 1,307 Python reference records |
| [tui](https://github.com/gomlang/tui/blob/main/README.md) | Unicode cell buffers, incremental rendering, constrained layout, tables/trees/charts, focus and grapheme-aware editing | Module tests, downstream tests, 2,505 model-checked ANSI frames and real PTY checks |
| [tui_markdown](https://github.com/gomlang/tui_markdown/blob/main/README.md) | CommonMark terminal layout, themed blocks/inlines, tables, links, scrolling and searchable previews | Module tests, downstream tests, 1,118 independent cases and real PTY checks |
| [unicode_text](https://github.com/gomlang/unicode_text/blob/main/README.md) | Unicode 16 grapheme/word/line segmentation, terminal width policies, truncation, padding, tab expansion and bounded wrapping | Module tests, downstream tests and all 19,591 official Unicode segmentation cases |
| [uuid](https://github.com/gomlang/uuid/blob/main/README.md) | UUID values, strict text/byte conversions, secure v4/v7, ordering/Hash and Serde | RFC 9562 vectors, concurrent generation and independent consumer checks |
| [walkdir](https://github.com/gomlang/walkdir/blob/main/README.md) | Lazy directory traversal, depth bounds, pruning, symlink policies, metadata snapshots and contextual errors | Module tests, the complete migrated traversal/syscall downstream check suite and race checks |
| [web](https://github.com/gomlang/web/blob/main/README.md) | HTTP/1.1 routing, streaming/SSE, bounded sessions, CSRF and per-peer/custom-key rate limiting | Module, independent live HTTP consumer and concurrent-state race checks |
| [websocket](https://github.com/gomlang/websocket/blob/main/README.md) | RFC 6455 handshakes, frames, masking, fragmented UTF-8 messages, control/close state machines, bounded queues and cancellable duplex TCP/TLS/standard I/O | Module tests, live TCP downstream check, fixed protocol vectors and race checks |
| [x509](https://github.com/gomlang/x509/blob/main/README.md) | PKIX distinguished names, extensions, algorithm identifiers and typed BasicConstraints DER structures | Library and downstream DER roundtrips, canonical ordering and malformed-structure checks; certificate verification is outside scope |
| [xml](https://github.com/gomlang/xml/blob/main/README.md) | Bounded incremental UTF-8 XML 1.0 token reading/writing with namespaces and checked character references | Library and downstream tests for chunk boundaries, namespaces, XML declarations and malformed documents |
| [yaml](https://github.com/gomlang/yaml/blob/main/README.md) | Bounded YAML block/flow parsing and emission, multi-document streams, aliases, dynamic values and Serde | Managed YAML backend, explicit core-schema policy and configuration consumer |

Applications are listed separately from importable libraries:

| Application | Purpose |
| --- | --- |
| [explorer](https://github.com/gomlang/explorer/blob/main/README.md) | Interactive terminal file explorer and deterministic snapshot mode |
| [goml_stats](https://github.com/gomlang/goml_stats/blob/main/README.md) | GoML project statistics with Git ignore rules and text/JSON reports |

<!-- catalog:end -->

Validation includes module-local public API tests, named examples, isolated downstream modules,
deterministic negative cases, reference interoperability where applicable, and
fresh/cached builds. Build products belong in each module's `_artifact/` and are
ignored by its repository.

Install GoML 0.1.57 or newer and Go 1.26+ on `PATH`. With a library's dependencies
available in the selected registry, run these commands from that library's root:

```sh
goml fmt --check
goml test --timeout 300s
goml verify --timeout 300s
```

Modules with ecosystem dependencies need those versions in the selected registry.
Use the verification command below to create the isolated
registry snapshot and check the library, its examples and independent downstream behavior.
The verifier reads sibling library repositories from its parent directory by default.
Set `GOMLANG_LIBRARIES` to an absolute or relative path for another layout.
The native Go fixtures with local `replace` directives use the sibling layout.

For example, from this catalog checkout, create a private registry containing
the sibling libraries and use it for an individual library. This does not
change the default registry or persist an environment setting:

```sh
(cd ../verification && goml build)
registry_path="$(cd ../verification && _artifact/bin/verification --registry-only)"
(
    cd ../color
    GOML_HOME="$registry_path" goml test --timeout 300s
    GOML_HOME="$registry_path" goml verify --timeout 300s
)
```

## Maintaining this catalog

Edit library names, implemented scope and verification coverage in
[catalog.json](catalog.json), then regenerate the README tables. Applications
are separate entries and are excluded from the library count. Repository links
and alphabetical ordering are generated from the names.

Python 3.11+ is sufficient for catalog checks; GoML and sibling checkouts are
not needed for the standalone commands:

```sh
python3 tools/catalog.py --write
python3 tools/catalog.py --check
python3 -m unittest discover -s tools -p 'test_*.py' -v
```

Checks reject duplicate names/JSON keys, malformed metadata, changed generated
tables, inconsistent historical manifests, and broken inline links or heading
anchors within this catalog's Markdown documents. Historical manifests record
the original split; new libraries belong in `catalog.json`, not those manifests.
The checker validates their structure and module membership without rewriting
their commit/tree IDs. It does not fetch external links or run library tests.

With sibling repositories available, additionally check their READMEs, module
coordinates and the verifier's repository inventory:

```sh
python3 tools/catalog.py --check --libraries ..
```

`--inventory /path/to/verification/ci/repositories.json` compares the catalog's
complete library/application list and repository roles without requiring all
library checkouts. CI uses this mode against its pinned verification revision.
Adding or removing a repository also requires updating the inventory and runner
in `verification`, then updating the workflow's pinned verification references
together. A catalog entry alone does not register a library with the verifier.

## Examples and development dependencies

Most libraries use a named example with no extra manifest. Most use `examples/basic/`;
`diff` uses `examples/patch/`, `csv` uses `examples/inventory/`, and `cli` uses
`examples/parse/`. Run `goml run --example <name>` from the library root.
`goml test` builds examples and runs their tests alongside library tests.
`goml verify --timeout 300s` copies examples into independent modules and checks
them against an isolated registry snapshot. Cross-module API, generic and derive
coverage is preserved without maintaining a manifest for every sample.

The bench, llvm, redis, sql, sqlite, web and yaml repositories retain explicit native
fixtures under `testdata/downstream/native/`. Their Go module settings and test
servers are part of those scenarios. `goml verify` builds and tests these fixtures
automatically. Fixture-only helpers are declared in root `[dev-dependencies]`;
normal downstream users do not inherit them. The verification runner retains
reference interoperability, native adapter, cache, PTY, SIMD and race checks.

## Terminal application stack

`color` and `unicode_text` supply reusable numeric and text foundations. `ansi`
adds structured styles; `terminal` owns one application's input/output session.
`tui` draws frames on that session, while `prompt` and `tui_markdown` supply
application models. `progress` can own a separate progress region or expose pure
snapshots for a TUI, and `diagnostics` produces explicit plain or colored reports.
Keep one output owner per live terminal region when composing the libraries.

`fuzzy` supplies reusable ranking and grapheme-safe match ranges for file pickers
and completion menus. `highlight` adds lexical scopes, cross-line state and
incremental ANSI/HTML code previews; its example composes edits with `rope` and
highlights embedded GoML inside Markdown fences. These are separate public
libraries, so applications can use their models with either a TUI or another UI.

[`explorer`](https://github.com/gomlang/explorer/blob/main/README.md) combines a directory tree,
Markdown preview, background scan progress and filesystem refresh. It provides
both an interactive application and a deterministic textual snapshot mode:

```sh
cd ../verification
GOML="$(command -v goml)" just ecosystem-test explorer
```

## Tools

[`goml_stats`](https://github.com/gomlang/goml_stats/blob/main/README.md) is a standalone GoML project statistics tool
using the `ignore` library for hierarchical Git ignore rules. It counts files,
code/comment/blank lines, bytes, test files, modules and package directories, with exclusions, detailed
tables and JSON output. Its lexer-aware counting handles raw and multiline
strings without mistaking their contents for comments.

```sh
cd ../verification
GOML="$(command -v goml)" just ecosystem-test goml_stats
../goml_stats/_artifact/bin/cmd/goml_stats/goml_stats ../parser
```

## Library verification

Run the library, example and independent downstream checks from the verifier repository:

```sh
cd ../verification
GOML="$(command -v goml)" just ecosystem-test
GOML="$(command -v goml)" just ecosystem-test lsp markdown diff
GOML="$(command -v goml)" just ecosystem-test color unicode_text ansi terminal tui prompt progress diagnostics tui_markdown
GOML="$(command -v goml)" just ecosystem-test fuzzy config csv websocket highlight archive metrics bench
goml test --timeout 300s
```

With no module arguments, the verifier checks all registered libraries and their
examples and native fixtures, the statistics CLI and the Explorer application. A missing module or
failed check is an error. The verifier is a standalone GoML module; all test
orchestration and assertions run through GoML without Python. It creates an isolated,
content-addressed registry snapshot under `verification/_artifact/`, leaving the
user's registry untouched. Ordinary module tests resolve dependencies from that snapshot; `goml verify` materializes examples and native fixtures against a separate snapshot with workspace discovery disabled. Snapshot contents are captured once and published atomically so
parallel verifiers cannot observe a partially populated registry. Verification
logs and command timings are written under
`verification/_artifact/verification/`. Real terminal checks run automatically for
terminal, tui, prompt, progress, tui_markdown and Explorer; they use local
pseudo-terminals and do not require a human-controlled terminal. Race checks
build and run GoML test suites with `GOFLAGS=-race`, including declared native
adapter tests. `--no-race` skips that extra pass for focused development.

The explicit `GOML` setting selects the installed release for both building and
running the verifier. `just` is required for these recipes. Alternatively, run
`goml build` in `verification`, then invoke
`_artifact/bin/verification --goml "$(command -v goml)" lsp` directly.

Each implemented library has a README describing its API, semantics, limits and
tests. [FINDINGS.md](https://github.com/gomlang/ecosystem/blob/main/FINDINGS.md) records language capabilities and compiler/API boundaries discovered during this work.

SQLite also requires its declared native Go dependencies to be fetched before
readonly compilation (`cd ../sqlite && go mod download all`). Its
bidirectional database-file check uses the system `libsqlite3.so.0` and the C
compiler; SQLite development headers are not required. Independent
numeric, protocol and state-machine oracle results are checked-in text fixtures
with documented source versions and generation provenance; GoML tests compare
public library behavior with those expected values. These are fixed reference
vectors, not fresh runs of Python, NumPy or Rust reference implementations.
Real process, filesystem, network, PTY and GNU diff/patch checks still execute
against the host. Race checks require the repository's C compiler prerequisite.
Redis checks use a checksum-pinned reference server and local TLS peers.
Unicode conformance checks freshly download the checksum-pinned Unicode source
files on every invocation; compressed datasets are not versioned.
The LLVM binding requires LLVM 18 development headers and `libLLVM-18` under
`/usr/lib/llvm-18`, plus a C compiler and enabled cgo. Its verification also uses
the LLVM command-line tools in that installation to check emitted IR and bitcode.

Compiler limitations found during implementation remain documented in
[FINDINGS.md](https://github.com/gomlang/ecosystem/blob/main/FINDINGS.md). Compiler regression cases live in the
compiler's pipeline and module fixtures.

## GitHub Actions

Every library, application, catalog and verification repository has a `CI`
workflow for pushes, pull requests and manual runs. This catalog first checks
its generated tables, documentation links, historical manifests and library/
application inventory. It then runs the verifier's own tests and compares the
runner's registered modules with the pinned repository inventory. A green
catalog run does not mean that every library suite was run on its latest commit.

Library and application workflows reuse the
[verification infrastructure](https://github.com/gomlang/verification/tree/main/ci)
at a full commit SHA and test the triggering candidate against pinned sibling
revisions with the released GoML toolchain. Their checks include formatting, tests,
independent dependency verification, smoke/cached builds and the applicable
race, PTY, SIMD and native interoperability suites. Failure logs are uploaded.

## Native adapters in the application expansion

`yaml`, `jwt`, `html` and `image` declare managed Go adapters. Their consumers
need a module-root `go.mod` using Go 1.26+, including callers of existing HTML
entity and image APIs. The affected `template`, `markdown`, `go_doc`,
`tui_markdown` and `explorer` repositories include minimal manifests. Native
module requirements, checksums and local replacements are managed by GoML; CI
prepares the pinned backend dependencies before readonly builds. JPEG/WebP
codecs in this expansion require no additional C library.

UUID uses standard cryptographic entropy without a native adapter. JWT uses Go
standard cryptography; YAML, HTML and image documents identify their pinned
third-party backends. S3 tests use published signing vectors and local peers,
without cloud account credentials. Library source publication and CI do not
constitute an immutable public-registry version release.
