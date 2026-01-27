---
render_with_liquid: false
---

Status: NORMATIVE  
Lock State: LOCKED  
Version: 1.0.0-beta  
Editor: Charles F. Munat

# Gloss Language Specification — Version 1.0.0-beta

Gloss is an **inline semantic span-binding language** embedded inside Codex `Content`.
It binds spans of opaque text to Codex Concepts without encoding presentation or behavior.

## 1. Scope and Relationship to Codex
Codex is a declarative semantic markup language for expressing meaning independent of presentation or behavior. It uses XML-like syntax to write OWL2/SHACL ontologies and data. A Codex document consists of Concepts (named semantic units that may contain child Concepts or narrative text), Traits (values bound to Concepts), and Content (opaque narrative text preserved without interpretation).

1. Gloss span bindings MAY appear only inside Codex `Content` values.
2. Codex tooling treats `Content` as opaque text; Codex does not parse Gloss.
3. Consuming systems (e.g., target realization and rendering pipelines) parse and resolve Gloss.
4. Gloss MUST NOT be used inside:

	- Codex identifiers
	- Codex Trait values
	- schema definitions

## 2. Design Intent
Gloss encodes semantic binding only.

Gloss MUST NOT:

- define layout, typography, or styling
- define behavior, evaluation, or execution
- introduce new Concepts, Traits, or data

Targets (HTML, PDF, audio, braille, data export) MAY realize the same semantics differently.

## 3. Surface Form
This section defines the user-visible surface form of Gloss span bindings embedded in Codex `Content`.

### 3.1 Span-Binding Forms
A Gloss span binding has one of the following forms:

```text
{@iri}
{@iri | label}

{~token}
{~token | label}
```

Where:

- `@` references a Concept by its `id` (IRI identifier)
- `~` references a Concept by its `key` (lookup token)

### 3.2 Recognition Rule
`{` begins a Gloss span binding **only** when immediately followed by `@` or `~`.
Otherwise `{` is literal text.

`}` is literal text outside span bindings.

#### 3.2.1 Literal Span-Binding-Start Escapes
Because the two-character sequences `{@` and `{~` always begin span bindings,
Gloss provides a way to write these sequences as **literal text**.

When scanning for span bindings (both in top-level `Content` and inside labels):

{% raw %}

- `{{@` MUST be interpreted as the literal two-character sequence `{@`.
- `{{~` MUST be interpreted as the literal two-character sequence `{~`.

{% endraw %}  

These escapes MUST be recognized before applying the span-binding-start rule.

### 3.3 Whitespace Rules
Gloss is intentionally strict:

- No whitespace is permitted between the sigil and the reference token.
- The label separator `|` MUST be written with **exactly one ASCII space** on each side: `{@x | label}`.

These are invalid Gloss span bindings (and MUST be treated as syntax errors with recovery as defined by the parsing model, with a diagnostic):

- `{@ x}`
- `{@x |label}`
- `{@x| label}`
- `{@x|label}`

Note: a `{` followed by whitespace (e.g., `{ @x}`) does not begin a Gloss span binding
under the recognition rule. It is literal text.

Whitespace inside `label` is preserved verbatim.

### 3.4 Tokens
#### 3.4.1 `@iri`
`@` references use a Codex identifier token (an IRI reference).
Gloss parses the reference token according to the Codex lexical grammar in order to determine where the token ends, but beyond that it treats the token as an opaque string: it does not normalize, percent-decode, case-fold, or semantically validate IRI structure.

#### 3.4.2 `~token`
`~` references use a Codex lookup token value.
Lookup tokens are spelled with the leading `~` and follow Codex lookup-token lexical rules.

### 3.5 Labels
`label` is optional.

Rules:

1. If present, `label` is the display text for that span.
2. The semantic binding (the target Concept) is unchanged by the label.
3. Labels MAY contain nested Gloss span bindings.

The `label` portion is everything after the label separator ` ␠|␠ `.

### 3.6 Label Escapes
The `\}` escape is recognized only inside labels.

Note: These escape rules are interpreted by the Gloss parser when it scans Codex `Content`. Codex itself does not parse Gloss.

- `\}` represents a literal `}` character.

Backslash has no special meaning in a label unless followed by `}`.
Outside Gloss span bindings, backslash has no special meaning.

Examples:

```text
{@book:hobbit | A label with | pipes | is fine}
{@x | A label with \} brace}
{@x | path\to\file}

{~linkDoc | See {~foreignTerm | Zeitgeist}}
```

## 4. Parsing Model
This section defines the parsing model for Gloss span bindings embedded in Codex `Content`.

Gloss is embedded in arbitrary text, so parsing MUST be deterministic, streaming-friendly, and unambiguous.

### 4.1 Overview
A consumer parses `Content` into segments:

- literal text segments
- span-binding segments, each with:
  - the reference (`@iri` or `~token`)
   - an optional label string which may itself contain nested span bindings
  - source location metadata

### 4.2 Span-Binding Start
Consumers MUST recognize span-binding starts according to the recognition rule in § 3.2,
including the literal span-binding-start escapes in § 3.2.1.

This rule applies inside labels as well as top-level `Content`.

### 4.3 Span-Binding Structure
Inside a span binding:

1. Parse `{`.
2. Parse a reference:
   - `@` followed immediately by `IriReference`
   - or a `LookupToken` (which includes its leading `~`)
3. After the reference, exactly one of the following MUST occur:
   - the span binding closes immediately with `}`
   - the label separator ` ␠|␠ ` occurs, followed by a label, then the span binding closes with `}`
4. Parse the closing `}` of the current span binding.

#### 4.3.1 Reference Termination
`IriReference` and `LookupToken` are defined by the Codex grammars.

The reference token ends where the Codex token ends.
After the reference token, the consumer MUST NOT accept arbitrary characters (e.g. `{@x extra}` is a syntax error).

### 4.4 Label Parsing and Nesting
Labels are parsed as a stream of `LabelPart` until the current span binding closes.

A label may contain nested span bindings. Nested span bindings are parsed using the same rules as top-level span bindings.

#### 4.4.1 Closing Rule
Within a label:

- A `}` closes the **innermost** open span binding.
- The `}` that closes the current (outer) span binding is the first `}` encountered while not inside a nested span binding.

Because closure is always innermost-first, span bindings are always properly nested; non-nested (crossing) span bindings cannot be expressed.

#### 4.4.2 Escape Precedence
While parsing a label at any nesting depth:

1. If the next two characters are `\}`: consume them and emit a literal `}`.
{% raw %}
2. Else if the next three characters are `{{@` or `{{~`: consume them and emit the corresponding literal two-character sequence (`{@` or `{~`).
{% endraw %}
3. Else if the next characters begin a span binding (i.e., `{` immediately followed by `@` or `~`): parse a nested span binding and emit it as a nested segment.
4. Else if the next character is `}` and the current nesting depth is 0: close the current span binding.
5. Else: consume one character as literal label text.

#### 4.4.3 Pipe Handling
- The label separator for a span binding is the three-character sequence ` ␠|␠ ` occurring in that span binding after its reference.
- Any `|` characters within label text are literal.
- Any label separators inside nested span bindings belong to those nested span bindings.

### 4.5 Syntax Errors and Recovery
If the consumer begins parsing a span binding after recognizing a span-binding start (`{@` or `{~`) and then encounters malformed markup (e.g., missing reference token, illegal characters after the reference, missing closing brace, or pipe-separator violations), it MUST:

1. emit a diagnostic with source location
2. recover using the minimal recovery rule (§ 4.5.1)

This recovery guarantees forward progress and results in the malformed markup being emitted as literal characters, without requiring the consumer to rescan unbounded input to find a matching `}`.

#### 4.5.1 Minimal Recovery Rule
To ensure streaming-friendly behavior, consumers MUST recover without rescanning unbounded input.

When a span-binding parse fails after recognizing a span-binding start (`{@` or `{~`), the consumer MUST:

1. emit the leading `{` as literal text
2. continue scanning from the character immediately after that `{`

This guarantees forward progress even for inputs like `{@x` (unclosed).

Resolution errors (no match / ambiguous match) are not syntax errors and do not change parsing.

## 5. Resolution Semantics
Consuming systems perform Gloss resolution against the Concept model available at runtime.
Gloss does not define how that model is loaded.

### 5.1 Resolution Inputs
A parsed span binding yields:

- a reference: `@iri` or `~token`
- an optional label (which affects display text only)

### 5.2 `@` Resolution
`@iri` MUST resolve to exactly one Concept whose `id` matches `iri`.

- Zero matches: resolution error (unresolved identifier)
- Multiple matches: resolution error (ambiguous identifier)

### 5.3 `~` Resolution
`~token` MUST resolve to exactly one Concept whose `key` matches `~token`.

- Zero matches: resolution error (unresolved lookup token)
- Multiple matches: resolution error (ambiguous lookup token)

Consuming systems—not Codex—perform resolution.

### 5.4 Label Interaction
The presence or content of a label MUST NOT affect resolution.

## 6. Formatting and Canonicalization
Canonical span-binding spellings are:

- `{@iri}`
- `{@iri | label}`
- `{~token}`
- `{~token | label}`

In particular:

- the label separator MUST be written as ` ␠|␠ `
- producers MUST NOT emit the compact form `{@x|label}`

Consumers that emit or rewrite Gloss (formatters, editors, transformations) MUST emit only canonical spellings.

### 6.1 Canonicalization of Literal Span-Binding-Start Escapes
The sequences `{{@` and `{{~` are the canonical way to represent the literal two-character sequences `{@` and `{~` in Gloss source text.

If a consumer emits Gloss back to a text form that will be re-parsed as Gloss, it MUST preserve these escapes and it MUST NOT decode them to `{@` or `{~`, because doing so would change recognition (it would introduce a new span-binding start).

Parsers MUST treat non-canonical spellings that violate the surface-form rules as syntax errors and apply the error recovery rules.

This includes any whitespace-violating span-binding spelling as defined by the whitespace rules in § 3.3.

## 7. Validation Errors and Diagnostics
Gloss processing MUST be deterministic and explainable.

Gloss consumers:

- MUST NOT throw
- MUST preserve source locations for diagnostics

### 7.1 Error Categories
1. **Syntax errors**: malformed Gloss markup.
2. **Resolution errors**: well-formed markup that cannot be resolved.

### 7.2 Syntax Error Recovery
On syntax error, the consumer:

1. MUST recover deterministically and guarantee forward progress.
2. MUST emit a diagnostic with source location.
3. MUST continue parsing subsequent content.

Recovery requirements are defined by the parsing model, including the minimal recovery rule in § 4.5.1.

### 7.3 Resolution Error Recovery
On resolution error, the consumer:

1. MUST preserve the parsed span-binding structure.
2. MUST mark the span binding as unresolved.
3. MUST emit a diagnostic with source location.

Resolution errors are semantic failures, not syntax failures.

### 7.4 Diagnostic Codes
A Gloss diagnostic MUST include:

- `category` — one of the categories in § 7.1.
- `reason` — a stable code identifying the primary failure.

These codes exist so independent implementations can be compared and so the conformance suite can assert the primary failure deterministically.

#### 7.4.1 Primary Diagnostic Selection
When multiple errors are detectable within the same attempted span-binding parse,
the consumer MUST emit multiple diagnostics and it MUST choose exactly one
**primary** diagnostic reason for that parse attempt.

To ensure conformance comparability across different implementation strategies
(streaming, buffered, PEG-driven, etc.), the primary diagnostic MUST be selected
using the following rule:

1. Determine the earliest source position (smallest index) inside the attempted
   span binding at which the text violates the surface form or parsing model.
2. Emit as the primary diagnostic the `reason` corresponding to that earliest
	violation.
3. If multiple violations occur at the same earliest position, break ties by
	choosing the first applicable reason in this priority order:

	| Priority | Reason                                    |
	|----------|-------------------------------------------|
  | 1        | `~gloss-syn-unclosed-nested-span-binding` |
  | 2        | `~gloss-syn-unclosed-span-binding`        |
	| 3        | `~gloss-syn-missing-reference`            |
	| 4        | `~gloss-syn-whitespace-after-sigil`       |
	| 5        | `~gloss-syn-whitespace-after-reference`   |
	| 6        | `~gloss-syn-invalid-nested-compact-pipe`  |
	| 7        | `~gloss-syn-compact-pipe-separator`       |
	| 8        | `~gloss-syn-missing-space-before-pipe`    |
	| 9        | `~gloss-syn-missing-space-after-pipe`     |
	| 10       | `~gloss-syn-extra-space-before-pipe`      |
	| 11       | `~gloss-syn-extra-space-after-pipe`       |
	| 12       | `~gloss-syn-trailing-after-reference`     |

This rule does not require rescanning unbounded input. The “earliest violation”
is the earliest violation encountered by a conforming parser that follows the
normative parsing model.

#### 7.4.2 Syntax Diagnostic Reasons
When `category` is **syntax**, `reason` MUST be one of:

**Reference errors:**

- `~gloss-syn-missing-reference` — a span-binding start is recognized, but the reference token is empty (e.g., `{@}` or `{~}`).

**Whitespace errors:**

- `~gloss-syn-whitespace-after-sigil` — one or more whitespace characters appear immediately after the sigil (`@`/`~`) (e.g., `{@ x}` or `{~ x}`).
- `~gloss-syn-whitespace-after-reference` — after the reference token ends, only `}` or the label separator ` ␠|␠ ` is permitted; this reason applies when whitespace appears after the reference in a way that cannot form a valid label separator, including:
	- trailing whitespace before `}` (e.g., `{@x }`)
	- non-ASCII whitespace adjacent to `|` (e.g., `{@x\t| label}`)

**Pipe separator errors:**

- `~gloss-syn-missing-space-before-pipe` — a `|` follows the reference with no preceding ASCII space (e.g., `{@x| label}`).
- `~gloss-syn-missing-space-after-pipe` — a `|` is preceded by exactly one ASCII space but is not followed by an ASCII space (e.g., `{@x |label}`).
- `~gloss-syn-compact-pipe-separator` — the label separator is written with no surrounding ASCII spaces (e.g., `{@x|label}`).
- `~gloss-syn-extra-space-before-pipe` — two or more ASCII spaces occur immediately before `|` (e.g., `{@x  | label}`).
- `~gloss-syn-extra-space-after-pipe` — two or more ASCII spaces occur immediately after `|` (e.g., `{@x |  label}`).
- `~gloss-syn-invalid-nested-compact-pipe` — a nested span binding inside a label contains an invalid compact pipe separator. This reason MUST be used (as the primary reason for that nested span-binding parse attempt) instead of `~gloss-syn-compact-pipe-separator` when the compact pipe occurs inside a nested span binding.

**Structure errors:**

- `~gloss-syn-trailing-after-reference` — after the reference token ends, the next characters are neither `}` nor a well-formed label separator ` ␠|␠ `. This includes a single ASCII space not followed by `|` (e.g., `{@x extra}`).
- `~gloss-syn-unclosed-span-binding` — a span binding is missing a closing `}`.
- `~gloss-syn-unclosed-nested-span-binding` — a nested span binding is missing a closing `}`.

#### 7.4.3 Resolution Diagnostic Reasons

When `category` is **resolution**, `reason` MUST be one of the following:

**Identifier resolution errors (`@`):**

- `~gloss-res-unresolved-identifier` — no Concept with a matching `id` was found.
- `~gloss-res-ambiguous-identifier` — multiple Concepts with the same `id` were found.

**Lookup token resolution errors (`~`):**

- `~gloss-res-unresolved-token` — no Concept with a matching `key` was found.
- `~gloss-res-ambiguous-token` — multiple Concepts with the same `key` were found.

Resolvers and schemas MAY define additional resolution reason codes for domain-specific validation failures.

## 8. Renderer Contract
This section defines the required interface between a Gloss processor and any target realization system (renderer).

Gloss encodes semantic span binding only. This contract does not specify presentation.

### 8.1 Inputs
A renderer consumes:

1. the original Codex `Content` source text
2. the parsed Gloss structure extracted from that text
3. the resolved Concept references (when resolution is performed)

### 8.2 Output Data Model
A conforming Gloss processor MUST provide the renderer a sequence of segments.
Each segment is either:

- **Text segment**: literal text
- **Span-binding segment**:
  - `addressingForm`: `@` or `~`
  - `referenceToken`: the exact token text (e.g., `book:hobbit` or `~hobbit`)
   - `label`: optional label content, represented as a sequence of nested segments (text/span bindings)
   - `sourceRange`: a source location range covering the entire span binding
  - `resolution`:
    - `resolved`: boolean
    - `targetConceptId`: optional (present when resolved)

A renderer MUST treat nested label content as structured content.

### 8.3 Label Semantics
- If `label` is present, it is the display text for the span-binding span.
- If `label` is absent, the renderer MAY choose display text using renderer policy and Concept data.
- The label MUST NOT affect which Concept the span binding binds to.

### 8.3.1 Span-Binding Stacking Semantics
Gloss span bindings may be nested inside labels. Nesting is structural and always properly nested (crossing span bindings cannot be expressed).

For any output position within the label content of a span-binding segment, the in-scope span bindings form a **stack**:

1. The stack contains the outer span binding and all nested span bindings whose label content contains that position.
2. The stack order is from outermost to innermost.

A conforming Gloss processor MUST preserve this nesting structure in the output data model so that target adapters can inspect the full stack.

When a target adapter maps span-binding stacks to target-specific constructs, it may encounter **conflicts** where only one value or construct can apply at a position for a particular target-specific semantic role (for example, selecting a single `url` to realize as a hyperlink).

In such cases, the adapter MUST resolve the conflict using the following precedence rule:

- The innermost span binding that provides a value for that role wins for that role at that position; outer span bindings provide fallback.

This specification does not define how any particular role is mapped to any particular target (e.g., HTML, PDF, audio). Target adapters MAY preserve losing (outer) values using target-specific metadata or other mechanisms, but they MUST do so deterministically.

### 8.4 Target-Specific Mapping (Informative)

A target realization may map Concept traits (such as `url` or `language`) to target-specific constructs.
This mapping is outside Gloss and is defined by the target adapter.

Examples in the examples directory show one plausible mapping for one target:

- [gloss-lang.dev/examples/1.0.0-beta/index.md](../../examples/1.0.0-beta/index.md)

## Appendix A. Formal Grammar (EBNF)
Notes:

- `IriReference` and `LookupToken` are imported from the Codex grammar.
- This grammar defines the structure of a span binding. Recognition inside an arbitrary text stream is defined by the recognition rule in § 3.2.

### A.1 Span-Binding Grammar
{% raw %}```ebnf
GlossSpanBinding = "{", Reference, [ LabelSeparator, Label ], "}" ;

Reference = AtReference | LookupToken ;

AtReference = "@", IriReference ;

(* The label separator '|' uses balanced spacing:
   exactly one ASCII space on each side: ' | '. *)

LabelSeparator = " ", "|", " " ;

(* Labels may contain nested Gloss span bindings.
   Escaping is context-sensitive and applies only inside Label:

   - "\\}" represents a literal '}' character.

   A backslash is only special when followed by '}'.
*)

Label = { LabelPart } ;

LabelPart = EscapedSpanBindingStart
          | GlossSpanBinding
          | EscapedClosingBrace
          | LabelTextChar ;

(* Literal escapes for reserved span-binding-start sequences.

   - "{{@" represents the literal two-character sequence "{@".
   - "{{~" represents the literal two-character sequence "{~".

   These escapes must be recognized before nested span binding starts.
*)

EscapedSpanBindingStart = "{", "{", ( "@" | "~" ) ;

EscapedClosingBrace = "\\", "}" ;

(* Embedding disambiguation inside labels:

   If a '{' is immediately followed by '@' or '~', it begins a nested GlossSpanBinding.
   Otherwise, '{' is literal label text.

   Additionally, "{{@" and "{{~" are interpreted as literal "{@" and "{~".
*)

(* Any character except '}' may appear as literal label text.
   Escape sequences are interpreted with the precedence rules defined by the parsing model.
*)

LabelTextChar = ? any Unicode scalar value except '}' ? ;
```{% endraw %}

### A.2 External Tokens
The following tokens are defined by Codex and reused by Gloss:

- `IriReference`
- `LookupToken`

In particular, `LookupToken` includes its leading `~` sigil in surface form (e.g., `~hobbit`).

## Appendix B. Formal Grammar (PEG) (Informative)

Notes:

- `IriReference` and `LookupToken` are imported from the Codex grammar.
- Because Gloss is embedded in arbitrary text, this PEG includes a minimal embedding grammar (`GlossText`) showing how to recognize span bindings without requiring escapes for ordinary braces.

### B.1 Embedded Text Grammar (Informative)

{% raw %}```peg
# Start condition for a Gloss span binding.
SpanBindingStart <- '{' [@~]

# Literal escapes for reserved span-binding-start sequences.
# These emit the literal two-character sequences '{@' and '{~' respectively.
EscapedSpanBindingStart <- '{{' [@~]

# A stream of text with embedded span bindings.
# Text consumes any character sequence that does not begin a span binding.
GlossText <- (GlossSpanBinding / TextRun)*

TextRun <- (EscapedSpanBindingStart / (!SpanBindingStart .))+
```{% endraw %}

### B.2 Span-Binding Grammar (Informative)

```peg
GlossSpanBinding <- '{' Reference (LabelSeparator Label)? '}'

Reference <- AtReference / LookupToken

AtReference <- '@' IriReference

# The label separator '|' uses balanced spacing:
# exactly one ASCII space on each side.
LabelSeparator <- ' ' '|' ' '

# Label may contain nested span bindings.
# Escapes apply only inside Label.
Label <- LabelPart*

LabelPart <- EscapedSpanBindingStart / GlossSpanBinding / EscapedClosingBrace / LabelTextChar

EscapedClosingBrace <- '\\' '}'

# Any character except '}', as long as it does not begin a span binding
# and is not the start of an escaped span-binding-start sequence.
# This includes '|' verbatim.
LabelTextChar <- !EscapedSpanBindingStart !SpanBindingStart !'}' .
```

### B.3 External Tokens (Informative)

The following tokens are defined by Codex and reused by Gloss:

- `IriReference`
- `LookupToken`
