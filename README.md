# GoML ecosystem libraries

The libraries live in independent sibling Git repositories under `~/git/gomlang/`.
Each library repository contains its public API, documentation, tests and examples.
Ordinary examples share the library's root `goml.toml`; `[dev-dependencies]`
contains their test helpers. The verifier, Explorer application and statistics
tool retain separate repositories. The ecosystem requires
[GoML 0.1.56](https://github.com/gomlang/goml/releases/tag/v0.1.56) or newer.
Source files and generated GoML bindings use `.goml`.
Libraries with native integration document their Go adapters and system prerequisites.
The [split manifest](split-manifest.tsv) records the source commit and the
history and tree IDs used to create each library repository.
The [consumer split manifest](consumer-split-manifest.tsv) records the history
originally imported into each library's former `consumer/` directory. That historical record is unchanged by the example migration.

The libraries below have implementations, public documentation, independent
downstream checks and executable verification. The table records their implemented scope;
individual READMEs describe API semantics and limits. [ROADMAP.md](ROADMAP.md)
tracks completed improvements and the remaining functional gaps.

The [library boundary map](../../goml-dev/docs/library-boundaries.md)
assigns each A/B capability to std or ecosystem and records dependency order and
acceptance status. Pure GoML migration does not promote a module into std:
request, web, archive, color and markdown remain independently versioned here.
Standard packages must not depend on ecosystem modules.

E1 migration is in progress in [compress](../compress/README.md): incremental
DEFLATE, GZIP, ZLIB and LZW encoding and decoding are exercised by the
isolated compress example. Archive compatibility adapters and the other E1
capabilities remain separate migration work; this is not completion of E1.

| Module | Functional target | Status |
| --- | --- | --- |
| [parser](../parser/README.md) | Text/binary combinators, recursive grammars, shared work/depth budgets, spans, contextual errors and operator precedence | Implemented; module and downstream check tests pass |
| [proptest](../proptest/README.md) | Composable generators, lazy budgeted shrinking, failure campaigns, distributions, persistent replay, model/system execution and IEEE edge cases | Implemented; 32 library tests and 3 independent downstream check tests pass |
| [cli](../cli/README.md) | Command schemas, aliases, inherited globals, groups, nested/flattened Args and typed subcommand derives | Implemented; module and downstream check tests pass |
| [msgpack](../msgpack/README.md) | MessagePack wire types, direct Serde and standard stream integration, typed/dynamic frames, malformed-input limits and interoperability | Implemented; 20 library tests, downstream check checks and 2,490 reference interoperability cases pass |
| [graph](../graph/README.md) | Mutable directed/undirected graphs, stable IDs, traversal, components, topological order, shortest paths and spanning trees | Implemented; independent algorithm checks and downstream check tests pass |
| [template](../template/README.md) | Expressions, lexical scopes, conditions, loops, filters, includes, inheritance, escaping and contextual diagnostics | Implemented; 11 library tests, 2 downstream check tests and 1,367 Jinja shared-syntax comparisons pass |
| [html](../html/README.md) | Shared bounded escaping and text/attribute character-reference decoding | Shared entity data, explicit quote policies and template/markdown-compatible wrappers; whole-string APIs |
| [compress](../compress/README.md) | Incremental bounded DEFLATE, GZIP, ZLIB and LZW codecs with dictionary, checksum and bit-order contracts | 26 library tests, Go codec interoperability, independent downstream check and race checks pass |
| [redis](../redis/README.md) | RESP2/3 codec, typed commands, pipelining, transactions, Pub/Sub, bounded pools, DNS/TLS, injectable transport, context cancellation and total deadlines | Implemented; 29 library tests and race checks, versioned downstream fixtures, 2,391 protocol cases, Redis 7.2.5 RESP2/3 interoperability and 15 DNS/TLS cases in normal/race builds pass |
| [pipeline](../pipeline/README.md) | Lazy streams, bounded parallel transforms, filtering, ordering, batching/windows, merge/zip, backpressure and cancellation | Implemented; 21 library tests and race checks, versioned downstream check and 1,253 Python oracle cases pass |
| [ndarray](../ndarray/README.md) | Generic shared views, slicing, broadcasting, checked arithmetic, reductions, batched multiplication, LU/Cholesky/QR solves and SIMD | Implemented; 17 library tests, versioned downstream check, 2,929 NumPy cases and native/SSE2/scalar builds pass |
| [sqlite](../sqlite/README.md) | Typed binding/rows, prepared statements, streaming queries, nested savepoints, rollback, cancellation and explicit resource management | Implemented; 13 GoML tests, 4 native tests, versioned downstream check, 2,754 SQLite comparisons and race checks pass |
| [lsp](../lsp/README.md) | JSON-RPC framing, persistent document snapshots, UTF-8/16/32 negotiation, synchronous/deferred dispatch and bidirectional request deadlines | Implemented; 19 library tests, 3 downstream check tests and independent position/edit/protocol checks pass |
| [markdown](../markdown/README.md) | Block and inline parsing, AST, HTML rendering, escaping, links, code, lists and reference conformance | Implemented; 652/652 CommonMark examples, entity, module and downstream check checks pass |
| [diff](../diff/README.md) | Myers and linear-space Hirschberg differences, unified patches, checked application, context and newline preservation | Implemented; tests and GNU interoperability pass |
| [bitflags](../bitflags/README.md) | Typed integer flag sets, trait and inherent derives, unknown-bit policies, set algebra, name iteration, text and numeric Serde | Implemented; 11 library tests, downstream check, 19 derive diagnostics and 4,601 Rust reference comparisons pass |
| [logos](../logos/README.md) | Typed UTF-8 lexers, regex/literal rules, longest match, priorities, callbacks/extras, mode switching and bounded Thompson NFA matching | Implemented; 11 library tests, downstream check, race checks and 3,155 Python reference cases pass |
| [tempfile](../tempfile/README.md) | Secure temporary files/directories, anonymous files, atomic persistence, ownership transfer, scoped cleanup and memory-to-disk spooling | Implemented; 24 library tests and race checks, downstream check and 160 concurrent filesystem comparisons pass |
| [notify](../notify/README.md) | Linux inotify watchers, recursive maintenance, event filters, ignored subtrees, multi-path registrations, cancellable reads and bounded subscriptions | Implemented; 30 library tests, the complete migrated downstream check suite and race checks pass |
| [walkdir](../walkdir/README.md) | Lazy directory traversal, depth bounds, pruning, symlink policies, metadata snapshots and contextual errors | Implemented; 14 library tests, the complete migrated traversal/syscall downstream check suite and race checks pass |
| [request](../request/README.md) | GoML HTTP(S)/HTTP2 clients with pooled multiplexed connections, request builders, JSON/form/multipart, redirects, per-stream cancellation, TLS policy and bounded responses | 49 library tests and race, downstream check and HTTP/TLS/proxy interoperability checks pass; native servers are test-only reference peers |
| [llvm](../llvm/README.md) | LLVM 18 typed handles, SSA construction/editing, mutable-local promotion, IR traversal, target machines, ABI layouts, optimization and cross-target output | Implemented; 19 library tests, 12 native tests, 5 downstream check tests, race checks, four target formats and 12,420 linked-function comparisons pass |
| [rope](../rope/README.md) | Persistent balanced UTF-8 text, shared snapshots, checked edits/slices, UTF-16 and line indexing, chunk iterators and streaming I/O | Implemented; 11 library tests and race checks, versioned downstream check and 3,266 Python reference edits pass |
| [tracing](../tracing/README.md) | Structured events, nested spans, explicit task contexts, filtering/sampling, composed sinks, bounded asynchronous output and coordinated cleanup | Implemented; 26 library tests and race checks, 3 downstream check tests and 1,307 Python reference records pass |
| [web](../web/README.md) | GoML HTTP/1.1 server routing, typed request extraction, middleware, streaming I/O/SSE, panic isolation, cancellation, bounds and graceful shutdown | 32 library tests, 5 downstream check tests, live HTTP interoperability and race checks pass |
| [bigint](../bigint/README.md) | Immutable signed/unsigned arbitrary-precision integers, arithmetic/division, bitwise operations, radix/byte conversions, number theory and exact Serde | Implemented; 19 library tests, 2 downstream check tests, race checks and 1,938 Python reference cases pass |
| [decimal](../decimal/README.md) | Exact base-10 arithmetic over bigint, precision contexts, seven rounding modes, quantization, checked conversions and representation-preserving Serde | Implemented; 18 library tests, versioned downstream check, race checks and 3,072 Python Decimal value/error/status comparisons pass |
| [incremental](../incremental/README.md) | Typed heterogeneous inputs/queries, dynamic dependencies, revision validation, unchanged-result cutoff, atomic updates, cancellation and bounded memoization | Implemented; 13 library tests and race checks, versioned downstream check and 15,847 from-scratch oracle queries pass |
| [datetime](../datetime/README.md) | Checked calendars and nanosecond instants, explicit arithmetic policies, RFC3339, TZif/POSIX timezones, DST ambiguity resolution and Serde | Implemented; 18 library tests and race checks, versioned downstream check and 8,140 calendar/timezone reference cases pass |
| [cache](../cache/README.md) | Generic concurrent weighted LRU, TTL/TTI, injectable clocks, bounded singleflight loading, invalidation generations, copy policy and removal callbacks | Implemented; 22 library tests and race checks, versioned downstream check and 42,240 Python reference operations pass |
| [ignore](../ignore/README.md) | Glob sets, hierarchical Git ignore rules, match explanations, worktree metadata, bounded traversal, cancellation and parallel callbacks | Implemented; 21 library tests and race checks, versioned downstream check and 9,400 real Git reference queries pass |
| [syntax](../syntax/README.md) | Immutable lossless green trees, red navigation, typed AST views, bounded interning/builders, checked ranges and persistent subtree edits | Implemented; 18 library tests and race checks, versioned downstream check, 3,840 model-checked edits and 240 lossless rewrites pass |
| [color](../color/README.md) | Checked sRGB/linear/HSL/HSV/XYZ/Lab/Oklab conversions, CSS colors, alpha compositing, gamut mapping, contrast, Delta E and gradients | Pure GoML over standard math; 22 library tests, downstream check tests and 4,659 numerical reference cases pass |
| [unicode_text](../unicode_text/README.md) | Unicode 16 grapheme/word/line segmentation, terminal width policies, truncation, padding, tab expansion and bounded wrapping | Implemented; 13 library tests, 2 downstream check tests and all 19,591 official Unicode segmentation cases pass |
| [ansi](../ansi/README.md) | Structured styles, 16/256/truecolor profiles, streaming UTF-8/escape parsing, hyperlinks, styled graphemes and partial-write adapters | Implemented; 13 library tests, 2 downstream check tests and 2,800 independent protocol/rendering cases pass |
| [terminal](../terminal/README.md) | Linux raw sessions, typed keyboard/mouse/paste/focus/resize events, capability detection, cancellable I/O and explicit restoration | Implemented; 18 library tests, independent downstream check, race detector and real PTY checks pass |
| [tui](../tui/README.md) | Unicode cell buffers, incremental rendering, constrained layout, tables/trees/charts, focus and grapheme-aware editing | Implemented; 21 library tests, 2 downstream check tests, 2,505 model-checked ANSI frames and real PTY checks pass |
| [prompt](../prompt/README.md) | Typed text/password/integer input, validation, history/completion, searchable single/multiple choices and confirmation | Implemented; 15 library tests, independent downstream check and nine real PTY sessions pass |
| [progress](../progress/README.md) | Concurrent bars/spinners, snapshots, rate/ETA, throttling, coordinated logging, redirected output and cancellable shutdown | Implemented; 12 library tests, independent downstream check, 400 numerical cases, race detector and real PTY checks pass |
| [diagnostics](../diagnostics/README.md) | Checked source caches/spans, Unicode multi-file labels, themes, clipping, suggestions and conflict-checked edits | Implemented; 22 library tests, 3 downstream check tests and 6,236 independent source/edit/rendering cases pass |
| [tui_markdown](../tui_markdown/README.md) | CommonMark terminal layout, themed blocks/inlines, tables, links, scrolling and searchable previews | Implemented; 13 library tests, 2 downstream check tests, 1,118 independent cases and real PTY checks pass |
| [fuzzy](../fuzzy/README.md) | Unicode ranked subsequences, full case folding, grapheme-safe highlights, anchored modes, stable Top-K, persistent incremental queries and cancellable parallel search | Implemented; 16 library tests, 1,270 exhaustive reference cases, versioned downstream check and race checks pass |
| [config](../config/README.md) | Layered typed JSON/TOML, environment and CLI sources, merge policies, JSON Pointer edits, provenance, validation, immutable snapshots and filesystem hot reload | Implemented; 19 library tests, real inotify reloads, versioned downstream check and race checks pass |
| [csv](../csv/README.md) | Streaming standard I/O, quoted multiline fields, configurable dialects, byte/UTF-8 records, headers, precise positions, limits and typed Serde schemas | Implemented; 22 library tests, 1,500 generated roundtrips, versioned file downstream check and race checks pass |
| [websocket](../websocket/README.md) | RFC 6455 handshakes, frames, masking, fragmented UTF-8 messages, control/close state machines, bounded queues and cancellable duplex TCP/TLS/standard I/O | Implemented; 23 library tests, live TCP downstream check, fixed protocol vectors and race checks pass |
| [highlight](../highlight/README.md) | Extensible logos grammars, GoML/JSON/TOML/Markdown scopes, nested and cross-line regions, embedded fences, persistent incremental documents and ANSI/HTML output | Implemented; 17 library tests, 200 incremental/full rebuild comparisons, rope downstream check and race checks pass |
| [archive](../archive/README.md) | GoML USTAR/PAX and classic ZIP codecs, CRC32, bounded TAR streaming and ZIP indexing, DEFLATE/GZIP codecs, metadata and rooted extraction with an openat fallback for older kernels | 17 library tests, GNU gzip/tar/Info-ZIP interoperability, downstream check and race checks pass |
| [metrics](../metrics/README.md) | Concurrent counters/gauges/histograms, descriptor and label validation, cardinality limits, consistent snapshots, atomic gauge collection, timers and Prometheus exposition | Implemented; 16 library tests, live HTTP scrape downstream check and race checks pass |
| [bench](../bench/README.md) | Adaptive sampling, parameterized workloads, setup exclusion, bootstrap statistics, baseline comparisons, throughput, cancellation and JSON/HTML reports | Implemented; 14 library tests, deterministic clocks, real sorting downstream check and race checks pass |

Other independent library repositories are [asn1](../asn1/README.md),
[bigmath](../bigmath/README.md), [dwarf](../dwarf/README.md),
[go_doc](../go_doc/README.md), [http](../http/README.md),
[image](../image/README.md), [mail](../mail/README.md),
[mime](../mime/README.md), [object](../object/README.md),
[regexp](../regexp/README.md), [sql](../sql/README.md),
[tabwriter](../tabwriter/README.md), [textproto](../textproto/README.md),
[x509](../x509/README.md), and [xml](../xml/README.md).

Validation includes module-local public API tests, named examples, isolated downstream modules,
deterministic negative cases, reference interoperability where applicable, and
fresh/cached builds. Build products belong in each module's `_artifact/` and are
ignored by its repository.

Current development commands from a library repository:

```sh
../../goml-dev/stage2/bin/goml fmt
../../goml-dev/stage2/bin/goml test
```

Modules with ecosystem dependencies need those versions in the selected registry.
Use the verification command below to create the isolated
registry snapshot and check the library, its examples and independent downstream behavior.
The verifier reads libraries from its parent `~/git/gomlang/` directory by default.
Set `GOMLANG_LIBRARIES` to an absolute or relative path for another layout.
The native Go fixtures with local `replace` directives use the sibling layout.


## Examples and development dependencies

58 libraries use a named example with no extra manifest. Most use `examples/basic/`;
`diff` uses `examples/patch/`, `csv` uses `examples/inventory/`, and `cli` uses
`examples/parse/`. Run `goml run --example <name>` from the library root.
`goml test` builds examples and runs their tests alongside library tests.
`goml verify --timeout 300s` copies examples into independent modules and checks
them against an isolated registry snapshot. Cross-module API, generic and derive
coverage is preserved without maintaining a manifest for every sample.

The bench, llvm, redis, sql, sqlite and web repositories retain explicit native
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

[`explorer`](../explorer/README.md) combines a directory tree,
Markdown preview, background scan progress and filesystem refresh. It provides
both an interactive application and a deterministic textual snapshot mode:

```sh
cd ../verification
just ecosystem-test explorer
```

## Tools

[`goml_stats`](../goml_stats/README.md) is a standalone GoML project statistics tool
using the `ignore` library for hierarchical Git ignore rules. It counts files,
code/comment/blank lines, bytes, test files, modules and package directories, with exclusions, detailed
tables and JSON output. Its lexer-aware counting handles raw and multiline
strings without mistaking their contents for comments.

```sh
cd ../verification
just ecosystem-test goml_stats
../goml_stats/_artifact/bin/cmd/goml_stats/goml_stats .
```

## Library verification

Run the library, example and independent downstream checks from the verifier repository:

```sh
cd ../verification
just ecosystem-test
just ecosystem-test lsp markdown diff
just ecosystem-test color unicode_text ansi terminal tui prompt progress diagnostics tui_markdown
just ecosystem-test fuzzy config csv websocket highlight archive metrics bench
../../goml-dev/stage2/bin/goml test
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

Each implemented library has a README describing its API, semantics, limits and
tests. [FINDINGS.md](FINDINGS.md) records language capabilities and compiler/API boundaries discovered during this work.

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
[FINDINGS.md](FINDINGS.md). The four compiler regression cases live in the
compiler's pipeline and module fixtures.
