Status: NORMATIVE
Lock State: LOCKED
Version: 0.1
Editor: Charles F. Munat

# Gloss Parsing Model Specification — Version 0.1

This document defines the normative parsing model for Gloss annotations embedded in Codex `Content`.

Gloss is embedded in arbitrary text. Parsing MUST therefore be deterministic, streaming-friendly, and unambiguous.

## 1. Overview (Normative)

A consumer parses a `Content` string into a sequence of segments:

- literal text segments
- annotation segments, each with:
  - the reference (`@iri` or `~token`)
  - an optional label string which may itself contain nested annotations
  - source location metadata

## 2. Annotation Start (Normative)

At any position in text, `{` begins an annotation if and only if the next character is `@` or `~`.

- If `{` is not immediately followed by `@` or `~`, it is literal text.
- This rule applies inside labels as well as top-level `Content`.

### 2.1 Literal Annotation-Start Escapes (Normative)

Because the two-character sequences `{@` and `{~` always begin annotations,
consumers MUST recognize the following three-character sequences as **literal
text** when scanning for annotations (both top-level and inside labels):

- `{{@` emits the literal two-character sequence `{@`.
- `{{~` emits the literal two-character sequence `{~`.

These escapes MUST be recognized before applying the annotation-start rule.

## 3. Annotation Structure (Normative)

Inside an annotation:

1. Parse `{`.
2. Parse a reference:
   - `@` followed immediately by `IriReference`
   - or a `LookupToken` (which includes its leading `~`)
3. After the reference, exactly one of the following MUST occur:
   - the annotation closes immediately with `}`
   - the label separator ` ␠|␠ ` occurs, followed by a label, then the annotation closes with `}`
4. Parse the closing `}` of the current annotation.

### 3.1 Reference Termination (Normative)

`IriReference` and `LookupToken` are defined by the Codex grammars.

The reference token ends where the Codex token ends.
After the reference token, the consumer MUST NOT accept arbitrary characters (e.g. `{@x extra}` is a syntax error).

## 4. Label Parsing and Nesting (Normative)

Labels are parsed as a stream of `LabelPart` until the current annotation closes.

A label may contain nested annotations. Nested annotations are parsed using the same rules as top-level annotations.

### 4.1 Closing Rule

Within a label:

- A `}` closes the **innermost** open annotation.
- The `}` that closes the current (outer) annotation is the first `}` encountered while not inside a nested annotation.

### 4.2 Escape Precedence

While parsing a label at any nesting depth:

1. If the next two characters are `\}`: consume them and emit a literal `}`.
2. Else if the next two characters are `\\`: consume them and emit a literal `\\`.
3. Else if the next three characters are `{{@` or `{{~`: consume them and emit the corresponding literal two-character sequence (`{@` or `{~`).
4. Else if the next characters begin an annotation (i.e., `{` immediately followed by `@` or `~`): parse a nested annotation and emit it as a nested segment.
5. Else if the next character is `}` and the current nesting depth is 0: close the current annotation.
6. Else: consume one character as literal label text.

### 4.3 Pipe Handling

- The label separator for an annotation is the three-character sequence ` ␠|␠ ` occurring in that annotation after its reference.
- Any `|` characters within label text are literal.
- Any label separators inside nested annotations belong to those nested annotations.

## 5. Syntax Errors and Recovery (Normative)

If the consumer encounters malformed markup (e.g., missing reference token, illegal characters after the reference, missing closing brace, or pipe-separator violations), it MUST:

1. treat the malformed markup as literal text
2. emit a diagnostic with source location
3. continue parsing subsequent content

### 5.1 Minimal Recovery Rule (Normative)

To ensure streaming-friendly behavior, consumers MUST recover without rescanning unbounded input.

When an annotation parse fails after recognizing an annotation start (`{@` or `{~`), the consumer MUST:

1. emit the leading `{` as literal text
2. continue scanning from the character immediately after that `{`

This guarantees forward progress even for inputs like `{@x` (unclosed).

Resolution errors (no match / ambiguous match) are not syntax errors and do not change parsing.
