Status: NORMATIVE
Lock State: LOCKED
Version: 0.1
Editor: Charles F. Munat

# Gloss Validation Errors Specification — Version 0.1

This document defines Gloss error categories and required recovery behavior.

## 1. Principles (Normative)

Gloss processing MUST be deterministic and explainable.

Gloss consumers:

- MUST NOT throw
- MUST preserve source locations for diagnostics

## 2. Error Categories (Normative)

1. **Syntax errors**: malformed Gloss markup.
2. **Resolution errors**: well-formed markup that cannot be resolved.

## 3. Syntax Error Recovery (Normative)

On syntax error, the consumer:

1. MUST recover deterministically and guarantee forward progress.
2. MUST emit a diagnostic with source location.
3. MUST continue parsing subsequent content.

Recovery requirements are defined by the parsing model, including the minimal recovery rule: [gloss-lang.dev/spec/0.1/parsing-model/index.md](../parsing-model/index.md).

Examples of syntax errors (illustrative):

- Unclosed annotation: `{@x`
- Empty target: `{@}` or `{~}`
- Whitespace violations: `{@ x}` or `{@x|label}` or `{@x |label}`

## 4. Resolution Error Recovery (Normative)

On resolution error, the consumer:

1. MUST preserve the parsed annotation structure.
2. MUST mark the annotation as unresolved.
3. MUST emit a diagnostic with source location.

Resolution errors are semantic failures, not syntax failures.

## 5. Diagnostic Codes (Normative)

A Gloss diagnostic MUST include:

- `category` — one of the categories in § 2.
- `reason` — a stable code identifying the primary failure.

These codes exist so independent implementations can be compared and so the
conformance suite can assert the primary failure deterministically.

### 5.0 Primary Diagnostic Selection (Normative)

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
	- `~gloss-syn-whitespace-after-open-brace`
	- `~gloss-syn-whitespace-after-sigil`
	- `~gloss-syn-whitespace-after-reference`
	- `~gloss-syn-compact-pipe-separator`
	- `~gloss-syn-missing-space-before-pipe`
	- `~gloss-syn-missing-space-after-pipe`
	- `~gloss-syn-extra-space-before-pipe`
	- `~gloss-syn-extra-space-after-pipe`
	- `~gloss-syn-trailing-after-reference`
	- `~gloss-syn-invalid-nested-compact-pipe`

This rule does not require rescanning unbounded input. The “earliest violation”
is the earliest violation encountered by a conforming parser that follows the
normative parsing model.

### 5.1 Syntax Diagnostic Reasons (Normative)

When `category` is **syntax**, `reason` MUST be one of:

- `~gloss-syn-missing-reference` — an annotation start is recognized but the reference token is empty (e.g., `{@}` or `{~}`).
- `~gloss-syn-whitespace-after-open-brace` — whitespace appears between `{` and the sigil (`@`/`~`).
- `~gloss-syn-whitespace-after-sigil` — whitespace appears between the sigil (`@`/`~`) and the first character of the reference token.
- `~gloss-syn-whitespace-after-reference` — whitespace appears after a completed reference token where only `}` or ` ␠|␠ ` is permitted.
- `~gloss-syn-missing-space-before-pipe` — label separator is missing the required single ASCII space before `|`.
- `~gloss-syn-missing-space-after-pipe` — label separator is missing the required single ASCII space after `|`.
- `~gloss-syn-compact-pipe-separator` — label separator is written as `|` with no surrounding spaces.
- `~gloss-syn-extra-space-before-pipe` — label separator has more than one ASCII space before `|`.
- `~gloss-syn-extra-space-after-pipe` — label separator has more than one ASCII space after `|`.
- `~gloss-syn-invalid-nested-compact-pipe` — a nested label contains an invalid compact pipe separator.
- `~gloss-syn-trailing-after-reference` — a reference target contains trailing characters after the target is complete.
- `~gloss-syn-unclosed-annotation` — an annotation is missing a closing `}`.
- `~gloss-syn-unclosed-nested-annotation` — a nested annotation is missing a closing `}`.

### 5.2 Resolution Diagnostic Reasons (Normative)

When `category` is **resolution**, `reason` MUST be a stable `~token` defined by the
resolver and/or schema.

The Gloss v0.1 conformance suite does not yet define normative resolution reason codes.
