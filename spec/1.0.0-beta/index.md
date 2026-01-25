---
render_with_liquid: false
---

Status: NORMATIVE
Lock State: UNLOCKED
Version: 1.0.0-beta
Editor: Charles F. Munat

# Gloss Language Specification — Version 1.0.0-beta

Gloss is an **inline semantic span-binding language** embedded inside Codex `Content`.
It binds spans of opaque text to Codex Concepts without encoding presentation or behavior.

## 1. Scope and Relationship to Codex (Normative)

1. Gloss annotations MAY appear only inside Codex `Content` values.
2. Codex tooling treats `Content` as opaque text; Codex does not parse Gloss.
3. Gloss is parsed and resolved by consuming systems (e.g., target realization / rendering pipelines).
4. Gloss MUST NOT be used inside:

	- Codex identifiers
	- Codex Trait values
	- schema definitions

## 2. Design Intent (Normative)

Gloss encodes semantic binding only.

Gloss MUST NOT:

- define layout, typography, or styling
- define behavior, evaluation, or execution
- introduce new Concepts, Traits, or data

Targets (HTML, PDF, audio, braille, data export) MAY realize the same semantics differently.

## 3. Surface Form (Normative)

This section defines the user-visible surface form of Gloss annotations embedded in Codex `Content`.

### 3.1 Annotation Forms (Normative)

A Gloss annotation has one of the following forms:

```text
{@iri}
{@iri | label}

{~token}
{~token | label}
```

Where:

- `@` references a Concept by its `id` (IRI identifier)
- `~` references a Concept by its `key` (lookup token)

### 3.2 Recognition Rule (Normative)

`{` begins a Gloss annotation **only** when immediately followed by `@` or `~`.
Otherwise `{` is literal text.

`}` is literal text outside annotations.

#### 3.2.1 Literal Annotation-Start Escapes (Normative)

Because the two-character sequences `{@` and `{~` always begin annotations,
Gloss provides a way to write these sequences as **literal text**.

When scanning for annotations (both in top-level `Content` and inside labels):

- `{{@` MUST be interpreted as the literal two-character sequence `{@`.
- `{{~` MUST be interpreted as the literal two-character sequence `{~`.

These escapes MUST be recognized before applying the annotation-start rule.

### 3.3 Whitespace Rules (Normative)

Gloss is intentionally strict:

- No whitespace is permitted between the sigil and the reference token.
- The label separator `|` MUST be written with **exactly one ASCII space** on each side: `{@x | label}`.

These are invalid Gloss annotations (and MUST be treated as syntax errors with recovery as defined by the parsing model, with a diagnostic):

- `{@ x}`
- `{@x |label}`
- `{@x| label}`
- `{@x|label}`

Note: a `{` followed by whitespace (e.g., `{ @x}`) does not begin a Gloss annotation
under the recognition rule. It is literal text.

Whitespace inside `label` is preserved verbatim.

### 3.4 Tokens (Normative)

#### 3.4.1 `@iri` (Normative)

`@` references use a Codex identifier token (an IRI reference).
Gloss treats the IRI as an opaque token.

#### 3.4.2 `~token` (Normative)

`~` references use a Codex lookup token value.
Lookup tokens are spelled with the leading `~` and follow Codex lookup-token lexical rules.

### 3.5 Labels (Normative)

`label` is optional.

Rules:

1. If present, `label` is the display text for that span.
2. The semantic binding (the target Concept) is unchanged by the label.
3. Labels MAY contain nested Gloss annotations.

The `label` portion is everything after the label separator ` ␠|␠ `.

### 3.6 Escaping (Normative)

Escaping applies only inside labels.

- `\}` represents a literal `}` character.
- `\\` represents a literal `\` character.

Backslash has no special meaning in a label unless followed by `}` or `\`.
Outside Gloss annotations, backslash has no special meaning.

Examples:

```text
{@book:hobbit | A label with | pipes | is fine}
{@x | A label with \} brace}
{@x | path\\to\\file}

{~linkDoc | See {~foreignTerm | Zeitgeist}}
```

## 4. Parsing Model (Normative)

This section defines the parsing model for Gloss annotations embedded in Codex `Content`.

Gloss is embedded in arbitrary text, so parsing MUST be deterministic, streaming-friendly, and unambiguous.

### 4.1 Overview (Normative)

A consumer parses `Content` into segments:

- literal text segments
- annotation segments, each with:
  - the reference (`@iri` or `~token`)
  - an optional label string which may itself contain nested annotations
  - source location metadata

### 4.2 Annotation Start (Normative)

Consumers MUST recognize annotation starts according to the recognition rule in § 3.2,
including the literal annotation-start escapes in § 3.2.1.

This rule applies inside labels as well as top-level `Content`.

### 4.3 Annotation Structure (Normative)

Inside an annotation:

1. Parse `{`.
2. Parse a reference:
   - `@` followed immediately by `IriReference`
   - or a `LookupToken` (which includes its leading `~`)
3. After the reference, exactly one of the following MUST occur:
   - the annotation closes immediately with `}`
   - the label separator ` ␠|␠ ` occurs, followed by a label, then the annotation closes with `}`
4. Parse the closing `}` of the current annotation.

#### 4.3.1 Reference Termination (Normative)

`IriReference` and `LookupToken` are defined by the Codex grammars.

The reference token ends where the Codex token ends.
After the reference token, the consumer MUST NOT accept arbitrary characters (e.g. `{@x extra}` is a syntax error).

### 4.4 Label Parsing and Nesting (Normative)

Labels are parsed as a stream of `LabelPart` until the current annotation closes.

A label may contain nested annotations. Nested annotations are parsed using the same rules as top-level annotations.

#### 4.4.1 Closing Rule (Normative)

Within a label:

- A `}` closes the **innermost** open annotation.
- The `}` that closes the current (outer) annotation is the first `}` encountered while not inside a nested annotation.

#### 4.4.2 Escape Precedence (Normative)

While parsing a label at any nesting depth:

1. If the next two characters are `\}`: consume them and emit a literal `}`.
2. Else if the next two characters are `\\`: consume them and emit a literal `\\`.
3. Else if the next three characters are `{{@` or `{{~`: consume them and emit the corresponding literal two-character sequence (`{@` or `{~`).
4. Else if the next characters begin an annotation (i.e., `{` immediately followed by `@` or `~`): parse a nested annotation and emit it as a nested segment.
5. Else if the next character is `}` and the current nesting depth is 0: close the current annotation.
6. Else: consume one character as literal label text.

#### 4.4.3 Pipe Handling (Normative)

- The label separator for an annotation is the three-character sequence ` ␠|␠ ` occurring in that annotation after its reference.
- Any `|` characters within label text are literal.
- Any label separators inside nested annotations belong to those nested annotations.

### 4.5 Syntax Errors and Recovery (Normative)

If the consumer begins parsing an annotation after recognizing an annotation start (`{@` or `{~`) and then encounters malformed markup (e.g., missing reference token, illegal characters after the reference, missing closing brace, or pipe-separator violations), it MUST:

1. emit a diagnostic with source location
2. recover using the minimal recovery rule (§ 4.5.1)

This recovery guarantees forward progress and results in the malformed markup being emitted as literal characters, without requiring the consumer to rescan unbounded input to find a matching `}`.

#### 4.5.1 Minimal Recovery Rule (Normative)

To ensure streaming-friendly behavior, consumers MUST recover without rescanning unbounded input.

When an annotation parse fails after recognizing an annotation start (`{@` or `{~`), the consumer MUST:

1. emit the leading `{` as literal text
2. continue scanning from the character immediately after that `{`

This guarantees forward progress even for inputs like `{@x` (unclosed).

Resolution errors (no match / ambiguous match) are not syntax errors and do not change parsing.

## 5. Resolution Semantics (Normative)

Consuming systems perform Gloss resolution against the Concept model available at runtime.
Gloss does not define how that model is loaded.

### 5.1 Resolution Inputs (Normative)

A parsed annotation yields:

- a reference: `@iri` or `~token`
- an optional label (which affects display text only)

### 5.2 `@` Resolution (Normative)

`@iri` MUST resolve to exactly one Concept whose `id` matches `iri`.

- Zero matches: resolution error (unresolved identifier)
- Multiple matches: resolution error (ambiguous identifier)

### 5.3 `~` Resolution (Normative)

`~token` MUST resolve to exactly one Concept whose `key` matches `~token`.

- Zero matches: resolution error (unresolved lookup token)
- Multiple matches: resolution error (ambiguous lookup token)

Consuming systems—not Codex—perform resolution.

### 5.4 Label Interaction (Normative)

The presence or content of a label MUST NOT affect resolution.

## 6. Formatting and Canonicalization (Normative)

Canonical annotation spellings are:

- `{@iri}`
- `{@iri | label}`
- `{~token}`
- `{~token | label}`

In particular:

- the label separator MUST be written as ` ␠|␠ `
- producers MUST NOT emit the compact form `{@x|label}`

Consumers that emit or rewrite Gloss (formatters, editors, transformations) MUST emit only canonical spellings.

Parsers MUST treat non-canonical spellings that violate the surface-form rules as syntax errors and apply the error recovery rules.

This includes any whitespace-violating annotation spelling as defined by the whitespace rules in § 3.3.

## 7. Validation Errors and Diagnostics (Normative)

Gloss processing MUST be deterministic and explainable.

Gloss consumers:

- MUST NOT throw
- MUST preserve source locations for diagnostics

### 7.1 Error Categories (Normative)

1. **Syntax errors**: malformed Gloss markup.
2. **Resolution errors**: well-formed markup that cannot be resolved.

### 7.2 Syntax Error Recovery (Normative)

On syntax error, the consumer:

1. MUST recover deterministically and guarantee forward progress.
2. MUST emit a diagnostic with source location.
3. MUST continue parsing subsequent content.

Recovery requirements are defined by the parsing model, including the minimal recovery rule in § 4.5.1.

### 7.3 Resolution Error Recovery (Normative)

On resolution error, the consumer:

1. MUST preserve the parsed annotation structure.
2. MUST mark the annotation as unresolved.
3. MUST emit a diagnostic with source location.

Resolution errors are semantic failures, not syntax failures.

### 7.4 Diagnostic Codes (Normative)

A Gloss diagnostic MUST include:

- `category` — one of the categories in § 7.1.
- `reason` — a stable code identifying the primary failure.

These codes exist so independent implementations can be compared and so the conformance suite can assert the primary failure deterministically.

#### 7.4.1 Primary Diagnostic Selection (Normative)

When multiple errors are detectable within the same attempted annotation parse,
the consumer MAY emit multiple diagnostics, but it MUST choose exactly one
**primary** diagnostic reason for that parse attempt.

To ensure conformance comparability across different implementation strategies
(streaming, buffered, PEG-driven, etc.), the primary diagnostic MUST be selected
using the following rule:

1. Determine the earliest source position (smallest index) inside the attempted
	annotation at which the text violates the surface form or parsing model.
2. Emit as the primary diagnostic the `reason` corresponding to that earliest
	violation.
3. If multiple violations occur at the same earliest position, break ties by
	choosing the first applicable reason in this priority order:

	- `~gloss-syn-unclosed-nested-annotation`
	- `~gloss-syn-unclosed-annotation`
	- `~gloss-syn-missing-reference`
	- `~gloss-syn-whitespace-after-sigil`
	- `~gloss-syn-whitespace-after-reference`
	- `~gloss-syn-invalid-nested-compact-pipe`
	- `~gloss-syn-compact-pipe-separator`
	- `~gloss-syn-missing-space-before-pipe`
	- `~gloss-syn-missing-space-after-pipe`
	- `~gloss-syn-extra-space-before-pipe`
	- `~gloss-syn-extra-space-after-pipe`
	- `~gloss-syn-trailing-after-reference`

This rule does not require rescanning unbounded input. The “earliest violation”
is the earliest violation encountered by a conforming parser that follows the
normative parsing model.

#### 7.4.2 Syntax Diagnostic Reasons (Normative)

When `category` is **syntax**, `reason` MUST be one of:

**Reference errors:**

- `~gloss-syn-missing-reference` — an annotation start is recognized, but the reference token is empty (e.g., `{@}` or `{~}`).

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
- `~gloss-syn-invalid-nested-compact-pipe` — a nested annotation inside a label contains an invalid compact pipe separator. This reason MUST be used (as the primary reason for that nested annotation parse attempt) instead of `~gloss-syn-compact-pipe-separator` when the compact pipe occurs inside a nested annotation.

**Structure errors:**

- `~gloss-syn-trailing-after-reference` — after the reference token ends, the next characters are neither `}` nor a well-formed label separator ` ␠|␠ `. This includes a single ASCII space not followed by `|` (e.g., `{@x extra}`).
- `~gloss-syn-unclosed-annotation` — an annotation is missing a closing `}`.
- `~gloss-syn-unclosed-nested-annotation` — a nested annotation is missing a closing `}`.

#### 7.4.3 Resolution Diagnostic Reasons (Normative)

When `category` is **resolution**, `reason` MUST be a stable `~token` defined by the
resolver and/or schema.

The Gloss 1.0.0-beta conformance suite does not yet define normative resolution reason codes.

## 8. Renderer Contract (Normative)

This section defines the required interface between a Gloss processor and any target realization system (renderer).

Gloss encodes semantic span binding only. This contract does not specify presentation.

### 8.1 Inputs (Normative)

A renderer consumes:

1. the original Codex `Content` source text
2. the parsed Gloss structure extracted from that text
3. the resolved Concept references (when resolution is performed)

### 8.2 Output Data Model (Normative)

A conforming Gloss processor MUST provide the renderer a sequence of segments.
Each segment is either:

- **Text segment**: literal text
- **Annotation segment**:
  - `addressingForm`: `@` or `~`
  - `referenceToken`: the exact token text (e.g., `book:hobbit` or `~hobbit`)
  - `label`: optional label content, represented as a sequence of nested segments (text/annotations)
  - `sourceRange`: a source location range covering the entire annotation
  - `resolution`:
    - `resolved`: boolean
    - `targetConceptId`: optional (present when resolved)

A renderer MUST treat nested label content as structured content.

### 8.3 Label Semantics (Normative)

- If `label` is present, it is the display text for the annotation span.
- If `label` is absent, the renderer MAY choose display text using renderer policy and Concept data.
- The label MUST NOT affect which Concept the annotation binds to.

### 8.4 Target-Specific Mapping (Informative)

A target realization may map Concept traits (such as `url` or `language`) to target-specific constructs.
This mapping is outside Gloss and is defined by the target adapter.

Examples in the examples directory show one plausible mapping for one target:

- [gloss-lang.dev/examples/1.0.0-beta/index.md](../../examples/1.0.0-beta/index.md)

## Appendix A. Formal Grammar (EBNF) (Normative)

Notes:

- `IriReference` and `LookupToken` are imported from the Codex grammar.
- This grammar defines the structure of an annotation. Recognition inside an arbitrary text stream is defined by the recognition rule in § 3.2.

### A.1 Annotation Grammar (Normative)

```ebnf
GlossAnnotation = "{", Reference, [ LabelSeparator, Label ], "}" ;

Reference = AtReference | LookupToken ;

AtReference = "@", IriReference ;

(* The label separator '|' uses balanced spacing:
   exactly one ASCII space on each side: ' | '. *)

LabelSeparator = " ", "|", " " ;

(* Labels may contain nested Gloss annotations.
   Escaping is context-sensitive and applies only inside Label:

   - "\\}" represents a literal '}' character.
   - "\\\\" represents a literal '\\' character.

   A backslash is only special when followed by '}' or '\\'.
*)

Label = { LabelPart } ;

LabelPart = EscapedAnnotationStart
          | GlossAnnotation
          | EscapedClosingBrace
          | EscapedBackslash
          | LabelTextChar ;

(* Literal escapes for reserved annotation-start sequences.

   - "{{@" represents the literal two-character sequence "{@".
   - "{{~" represents the literal two-character sequence "{~".

   These escapes must be recognized before nested annotation starts.
*)

EscapedAnnotationStart = "{", "{", ( "@" | "~" ) ;

EscapedClosingBrace = "\\", "}" ;

EscapedBackslash = "\\", "\\" ;

(* Embedding disambiguation inside labels:

   If a '{' is immediately followed by '@' or '~', it begins a nested GlossAnnotation.
   Otherwise, '{' is literal label text.

   Additionally, "{{@" and "{{~" are interpreted as literal "{@" and "{~".
*)

(* Any character except '}' may appear as literal label text.
   Escape sequences are interpreted with the precedence rules defined by the parsing model.
*)

LabelTextChar = ? any Unicode scalar value except '}' ? ;
```

### A.2 External Tokens (Normative)

The following tokens are defined by Codex and reused by Gloss:

- `IriReference`
- `LookupToken`

In particular, `LookupToken` includes its leading `~` sigil in surface form (e.g., `~hobbit`).

## Appendix B. Formal Grammar (PEG) (Informative)

Notes:

- `IriReference` and `LookupToken` are imported from the Codex grammar.
- Because Gloss is embedded in arbitrary text, this PEG includes a minimal embedding grammar (`GlossText`) showing how to recognize annotations without requiring escapes for ordinary braces.

### B.1 Embedded Text Grammar (Informative)

```peg
# Start condition for a Gloss annotation.
AnnotationStart <- '{' [@~]

# Literal escapes for reserved annotation-start sequences.
# These emit the literal two-character sequences '{@' and '{~' respectively.
EscapedAnnotationStart <- '{{' [@~]

# A stream of text with embedded annotations.
# Text consumes any character sequence that does not begin an annotation.
GlossText <- (GlossAnnotation / TextRun)*

TextRun <- (EscapedAnnotationStart / (!AnnotationStart .))+
```

### B.2 Annotation Grammar (Informative)

```peg
GlossAnnotation <- '{' Reference (LabelSeparator Label)? '}'

Reference <- AtReference / LookupToken

AtReference <- '@' IriReference

# The label separator '|' uses balanced spacing:
# exactly one ASCII space on each side.
LabelSeparator <- ' ' '|' ' '

# Label may contain nested annotations.
# Escapes apply only inside Label.
Label <- LabelPart*

LabelPart <- EscapedAnnotationStart / GlossAnnotation / EscapedClosingBrace / EscapedBackslash / LiteralBackslash / LabelTextChar

EscapedClosingBrace <- '\\' '}'
EscapedBackslash <- '\\' '\\'

# A literal backslash is permitted when it does not form a recognized escape.
LiteralBackslash <- '\\' ![\\}]

# Any character except '}' and '\\', as long as it does not begin an annotation
# and is not the start of an escaped annotation-start sequence.
# This includes '|' verbatim.
LabelTextChar <- !EscapedAnnotationStart !AnnotationStart ![}\\] .
```

### B.3 External Tokens (Informative)

The following tokens are defined by Codex and reused by Gloss:

- `IriReference`
- `LookupToken`
