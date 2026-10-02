# GoML ecosystem libraries

Each library lives in an independent [gomlang GitHub repository](https://github.com/gomlang).
Each library repository contains its public API, documentation, tests and examples.
Ordinary examples share the library's root `goml.toml`; `[dev-dependencies]`
contains their test helpers. The verifier, Explorer application and statistics
tool retain separate repositories. The ecosystem requires
[GoML 0.1.56](https://github.com/gomlang/goml/releases/tag/v0.1.56) or newer.
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

This round reviewed all 64 libraries for concrete correctness, resource,
and API gaps. It adds bounded numeric and parsing APIs, tightens format and
protocol validation, preserves cleanup and snapshot ownership, and improves
Unicode terminal behavior and costly collection operations. The
[per-library audit and remaining work](https://github.com/gomlang/ecosystem/blob/main/ROADMAP.md#ecosystem-wide-improvement-audit)
keeps each change and its limits explicit, alongside earlier batches.

All 64 libraries passed their module-local tests and isolated downstream
verification for this batch. Applicable checks include races, real I/O, PTYs and
native interoperability. See the [catalog Actions](https://github.com/gomlang/ecosystem/actions)
and each library's Actions page for current revision results. The capability
table records established coverage and fixed reference datasets.

| Module | Functional target | Status |
| --- | --- | --- |
| [parser](https://github.com/gomlang/parser/blob/main/README.md) | Text/binary combinators, recursive grammars, shared work/depth budgets, explicit multi-error recovery, spans, contextual errors and operator precedence | Implemented; module and downstream check tests pass |
| [proptest](https://github.com/gomlang/proptest/blob/main/README.md) | Composable generators, lazy budgeted shrinking, failure campaigns, distributions, persistent replay, model/system execution and IEEE edge cases | Implemented; module tests and independent downstream tests pass |
| [cli](https://github.com/gomlang/cli/blob/main/README.md) | Command schemas, aliases, inherited globals, groups, nested/flattened Args, typed subcommand derives and Bash/Zsh/Fish completion | Implemented; module and downstream check tests pass |
| [msgpack](https://github.com/gomlang/msgpack/blob/main/README.md) | MessagePack wire types, direct Serde and standard stream integration, typed/dynamic frames, malformed-input limits and interoperability | Implemented; module tests, downstream checks and 2,490 reference interoperability cases pass |
| [graph](https://github.com/gomlang/graph/blob/main/README.md) | Mutable directed/undirected graphs, stable IDs, traversal, components, topological order, shortest paths and spanning trees | Implemented; independent algorithm checks and downstream check tests pass |
| [template](https://github.com/gomlang/template/blob/main/README.md) | Expressions, lexical scopes, conditions, loops, filters, includes, inheritance, escaping and contextual diagnostics | Implemented; module tests, downstream tests and 1,367 Jinja shared-syntax comparisons pass |
| [html](https://github.com/gomlang/html/blob/main/README.md) | Shared bounded escaping and text/attribute character-reference decoding | Shared entity data, explicit quote policies and template/markdown-compatible wrappers; whole-string APIs |
| [compress](https://github.com/gomlang/compress/blob/main/README.md) | Incremental bounded DEFLATE, GZIP, ZLIB and LZW codecs with dictionary, checksum and bit-order contracts | Implemented; module tests, Go codec interoperability, independent downstream check and race checks pass |
| [redis](https://github.com/gomlang/redis/blob/main/README.md) | RESP2/3 codec, typed commands, pipelining, transactions, Pub/Sub, bounded pools, DNS/TLS, injectable transport, context cancellation and total deadlines | Implemented; module tests and race checks, versioned downstream fixtures, 2,391 protocol cases, Redis 7.2.5 RESP2/3 interoperability and DNS/TLS cases in normal/race builds pass |
| [pipeline](https://github.com/gomlang/pipeline/blob/main/README.md) | Lazy streams, bounded parallel transforms, filtering, ordering, batching/windows, merge/zip, backpressure and cancellation | Implemented; module tests and race checks, versioned downstream check and 1,253 Python oracle cases pass |
| [ndarray](https://github.com/gomlang/ndarray/blob/main/README.md) | Generic shared views, slicing, broadcasting, checked arithmetic, reductions, batched multiplication, LU/Cholesky/QR solves and SIMD | Implemented; module tests, versioned downstream check, 2,929 NumPy cases and native/SSE2/scalar builds pass |
| [sqlite](https://github.com/gomlang/sqlite/blob/main/README.md) | Typed binding/rows, prepared statements, streaming queries, nested savepoints, rollback, cancellation and explicit resource management | Implemented; module tests, native tests, versioned downstream check, 2,754 SQLite comparisons and race checks pass |
| [lsp](https://github.com/gomlang/lsp/blob/main/README.md) | JSON-RPC framing, persistent document snapshots, UTF-8/16/32 negotiation, synchronous/deferred dispatch and bidirectional request deadlines | Implemented; module tests, downstream tests and independent position/edit/protocol checks pass |
| [markdown](https://github.com/gomlang/markdown/blob/main/README.md) | Block and inline parsing, AST, HTML rendering, escaping, links, code, lists and reference conformance | Implemented; 652/652 CommonMark examples, entity, module and downstream checks pass |
| [diff](https://github.com/gomlang/diff/blob/main/README.md) | Myers and linear-space Hirschberg differences, unified patches, checked application, context and newline preservation | Implemented; tests and GNU interoperability pass |
| [bitflags](https://github.com/gomlang/bitflags/blob/main/README.md) | Typed integer flag sets, trait and inherent derives, unknown-bit policies, set algebra, name iteration, text and numeric Serde | Implemented; module tests, downstream check, 19 derive diagnostics and 4,601 Rust reference comparisons pass |
| [logos](https://github.com/gomlang/logos/blob/main/README.md) | Typed UTF-8 lexers, regex/literal rules, longest match, priorities, callbacks/extras, mode switching and bounded Thompson NFA matching | Implemented; module tests, downstream check, race checks and 3,155 Python reference cases pass |
| [tempfile](https://github.com/gomlang/tempfile/blob/main/README.md) | Secure temporary files/directories, anonymous files, atomic persistence, ownership transfer, scoped cleanup and memory-to-disk spooling | Implemented; module tests and race checks, downstream check and 160 concurrent filesystem comparisons pass |
| [notify](https://github.com/gomlang/notify/blob/main/README.md) | Linux inotify watchers, recursive maintenance, event filters, ignored subtrees, multi-path registrations, cancellable reads and bounded subscriptions | Implemented; module tests, the complete migrated downstream check suite and race checks pass |
| [walkdir](https://github.com/gomlang/walkdir/blob/main/README.md) | Lazy directory traversal, depth bounds, pruning, symlink policies, metadata snapshots and contextual errors | Implemented; module tests, the complete migrated traversal/syscall downstream check suite and race checks pass |
| [request](https://github.com/gomlang/request/blob/main/README.md) | GoML HTTP(S)/HTTP2 clients with pooled multiplexed connections, request builders, JSON/form/multipart, redirects, per-stream cancellation, TLS policy and bounded responses | Implemented; module tests and race, downstream check and HTTP/TLS/proxy interoperability checks pass; native servers are test-only reference peers |
| [llvm](https://github.com/gomlang/llvm/blob/main/README.md) | LLVM 18 typed handles, SSA construction/editing, mutable-local promotion, IR traversal, target machines, ABI layouts, optimization and cross-target output | Implemented; module tests, native tests, downstream tests, race checks, four target formats and 12,420 linked-function comparisons pass |
| [rope](https://github.com/gomlang/rope/blob/main/README.md) | Persistent balanced UTF-8 text, shared snapshots, checked edits/slices, UTF-16 and line indexing, chunk iterators and streaming I/O | Implemented; module tests and race checks, versioned downstream check and 3,266 Python reference edits pass |
| [tracing](https://github.com/gomlang/tracing/blob/main/README.md) | Structured events, nested spans, explicit task contexts, filtering/sampling, composed sinks, bounded asynchronous output and coordinated cleanup | Implemented; module tests and race checks, downstream tests and 1,307 Python reference records pass |
| [web](https://github.com/gomlang/web/blob/main/README.md) | GoML HTTP/1.1 server routing, typed request extraction, middleware, streaming I/O/SSE, panic isolation, cancellation, bounds and graceful shutdown | Implemented; module tests, downstream tests, live HTTP interoperability and race checks pass |
| [bigint](https://github.com/gomlang/bigint/blob/main/README.md) | Immutable signed/unsigned arbitrary-precision integers, arithmetic/division, bitwise operations, radix/byte conversions, number theory and exact Serde | Implemented; module tests, downstream tests, race checks and 1,938 Python reference cases pass |
| [decimal](https://github.com/gomlang/decimal/blob/main/README.md) | Exact base-10 arithmetic over bigint, precision contexts, seven rounding modes, quantization, checked conversions and representation-preserving Serde | Implemented; module tests, versioned downstream check, race checks and 3,072 Python Decimal value/error/status comparisons pass |
| [incremental](https://github.com/gomlang/incremental/blob/main/README.md) | Typed heterogeneous inputs/queries, dynamic dependencies, revision validation, unchanged-result cutoff, atomic updates, cancellation and bounded memoization | Implemented; module tests and race checks, versioned downstream check and 15,847 from-scratch oracle queries pass |
| [datetime](https://github.com/gomlang/datetime/blob/main/README.md) | Checked calendars and nanosecond instants, explicit arithmetic policies, RFC3339, TZif/POSIX timezones, DST ambiguity resolution and Serde | Implemented; module tests and race checks, versioned downstream check and 8,140 calendar/timezone reference cases pass |
| [cache](https://github.com/gomlang/cache/blob/main/README.md) | Generic concurrent weighted LRU, TTL/TTI, injectable clocks, bounded singleflight loading, invalidation generations, copy policy and removal callbacks | Implemented; module tests and race checks, versioned downstream check and 42,240 Python reference operations pass |
| [ignore](https://github.com/gomlang/ignore/blob/main/README.md) | Glob sets, hierarchical Git ignore rules, match explanations, worktree metadata, bounded traversal, cancellation and parallel callbacks | Implemented; module tests and race checks, versioned downstream check and 9,400 real Git reference queries pass |
| [syntax](https://github.com/gomlang/syntax/blob/main/README.md) | Immutable lossless green trees, red navigation, typed AST views, bounded interning/builders, checked ranges and persistent subtree edits | Implemented; module tests and race checks, versioned downstream check, 3,840 model-checked edits and 240 lossless rewrites pass |
| [color](https://github.com/gomlang/color/blob/main/README.md) | Checked sRGB/linear/HSL/HSV/XYZ/Lab/Oklab conversions, CSS colors, alpha compositing, gamut mapping, contrast, Delta E and gradients | Pure GoML over standard math; module tests, downstream check tests and 4,659 numerical reference cases pass |
| [unicode_text](https://github.com/gomlang/unicode_text/blob/main/README.md) | Unicode 16 grapheme/word/line segmentation, terminal width policies, truncation, padding, tab expansion and bounded wrapping | Implemented; module tests, downstream tests and all 19,591 official Unicode segmentation cases pass |
| [ansi](https://github.com/gomlang/ansi/blob/main/README.md) | Structured styles, 16/256/truecolor profiles, streaming UTF-8/escape parsing, hyperlinks, styled graphemes and partial-write adapters | Implemented; module tests, downstream tests and 2,800 independent protocol/rendering cases pass |
| [terminal](https://github.com/gomlang/terminal/blob/main/README.md) | Linux raw sessions, typed keyboard/mouse/paste/focus/resize events, capability detection, cancellable I/O and explicit restoration | Implemented; module tests, independent downstream check, race detector and real PTY checks pass |
| [tui](https://github.com/gomlang/tui/blob/main/README.md) | Unicode cell buffers, incremental rendering, constrained layout, tables/trees/charts, focus and grapheme-aware editing | Implemented; module tests, downstream tests, 2,505 model-checked ANSI frames and real PTY checks pass |
| [prompt](https://github.com/gomlang/prompt/blob/main/README.md) | Typed text/password/integer input, validation, history/completion, searchable single/multiple choices and confirmation | Implemented; module tests, independent downstream check and real PTY sessions pass |
| [progress](https://github.com/gomlang/progress/blob/main/README.md) | Concurrent bars/spinners, snapshots, rate/ETA, throttling, coordinated logging, redirected output and cancellable shutdown | Implemented; module tests, independent downstream check, 400 numerical cases, race detector and real PTY checks pass |
| [diagnostics](https://github.com/gomlang/diagnostics/blob/main/README.md) | Checked source caches/spans, Unicode multi-file labels, themes, clipping, suggestions and conflict-checked edits | Implemented; module tests, downstream tests and 6,236 independent source/edit/rendering cases pass |
| [tui_markdown](https://github.com/gomlang/tui_markdown/blob/main/README.md) | CommonMark terminal layout, themed blocks/inlines, tables, links, scrolling and searchable previews | Implemented; module tests, downstream tests, 1,118 independent cases and real PTY checks pass |
| [fuzzy](https://github.com/gomlang/fuzzy/blob/main/README.md) | Unicode ranked subsequences, full case folding, grapheme-safe highlights, anchored modes, stable Top-K, persistent incremental queries and cancellable parallel search | Implemented; module tests, 1,270 exhaustive reference cases, versioned downstream check and race checks pass |
| [config](https://github.com/gomlang/config/blob/main/README.md) | Layered typed JSON/TOML, environment and CLI sources, merge policies, JSON Pointer edits, provenance, validation, immutable snapshots and filesystem hot reload | Implemented; module tests, real inotify reloads, versioned downstream check and race checks pass |
| [csv](https://github.com/gomlang/csv/blob/main/README.md) | Streaming standard I/O, quoted multiline fields, configurable dialects, byte/UTF-8 records, headers, precise positions, limits and typed Serde schemas | Implemented; module tests, 1,500 generated roundtrips, versioned file downstream check and race checks pass |
| [websocket](https://github.com/gomlang/websocket/blob/main/README.md) | RFC 6455 handshakes, frames, masking, fragmented UTF-8 messages, control/close state machines, bounded queues and cancellable duplex TCP/TLS/standard I/O | Implemented; module tests, live TCP downstream check, fixed protocol vectors and race checks pass |
| [highlight](https://github.com/gomlang/highlight/blob/main/README.md) | Extensible logos grammars, GoML/JSON/TOML/Markdown scopes, nested and cross-line regions, embedded fences, persistent incremental documents and ANSI/HTML output | Implemented; module tests, 200 incremental/full rebuild comparisons, rope downstream check and race checks pass |
| [archive](https://github.com/gomlang/archive/blob/main/README.md) | GoML USTAR/PAX and ZIP/ZIP64 codecs, CRC32, bounded TAR streaming and ZIP indexing, DEFLATE/GZIP codecs, metadata and rooted extraction with an openat fallback for older kernels | Implemented; module tests, GNU gzip/tar/Info-ZIP interoperability, downstream check and race checks pass |
| [metrics](https://github.com/gomlang/metrics/blob/main/README.md) | Concurrent counters/gauges/histograms, descriptor and label validation, cardinality limits, consistent snapshots, atomic gauge collection, timers and Prometheus exposition | Implemented; module tests, live HTTP scrape downstream check and race checks pass |
| [bench](https://github.com/gomlang/bench/blob/main/README.md) | Adaptive sampling, parameterized workloads, setup exclusion, bootstrap statistics, baseline comparisons, throughput, cancellation and JSON/HTML reports | Implemented; module tests, deterministic clocks, real sorting downstream check and race checks pass |

Other independent library repositories are [asn1](https://github.com/gomlang/asn1/blob/main/README.md),
[bigmath](https://github.com/gomlang/bigmath/blob/main/README.md), [dwarf](https://github.com/gomlang/dwarf/blob/main/README.md),
[go_doc](https://github.com/gomlang/go_doc/blob/main/README.md), [http](https://github.com/gomlang/http/blob/main/README.md),
[image](https://github.com/gomlang/image/blob/main/README.md), [mail](https://github.com/gomlang/mail/blob/main/README.md),
[mime](https://github.com/gomlang/mime/blob/main/README.md), [object](https://github.com/gomlang/object/blob/main/README.md),
[regexp](https://github.com/gomlang/regexp/blob/main/README.md), [sql](https://github.com/gomlang/sql/blob/main/README.md),
[tabwriter](https://github.com/gomlang/tabwriter/blob/main/README.md), [textproto](https://github.com/gomlang/textproto/blob/main/README.md),
[x509](https://github.com/gomlang/x509/blob/main/README.md), and [xml](https://github.com/gomlang/xml/blob/main/README.md).

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
The verifier reads sibling library repositories from its parent directory by default.
Set `GOMLANG_LIBRARIES` to an absolute or relative path for another layout.
The native Go fixtures with local `replace` directives use the sibling layout.


## Examples and development dependencies

Most libraries use a named example with no extra manifest. Most use `examples/basic/`;
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

[`explorer`](https://github.com/gomlang/explorer/blob/main/README.md) combines a directory tree,
Markdown preview, background scan progress and filesystem refresh. It provides
both an interactive application and a deterministic textual snapshot mode:

```sh
cd ../verification
just ecosystem-test explorer
```

## Tools

[`goml_stats`](https://github.com/gomlang/goml_stats/blob/main/README.md) is a standalone GoML project statistics tool
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
workflow for pushes, pull requests and manual runs. Workflows reuse the
[verification infrastructure](https://github.com/gomlang/verification/tree/main/ci)
at a full commit SHA and test the triggering candidate against pinned sibling
revisions with the released GoML toolchain. Checks include formatting, tests,
independent dependency verification, smoke/cached builds and the applicable
race, PTY, SIMD and native interoperability suites. Failure logs are uploaded.
