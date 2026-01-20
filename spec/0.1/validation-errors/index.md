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

### 5.1 Syntax Diagnostic Reasons (Normative)

When `category` is **syntax**, `reason` MUST be one of:

- `~gloss-syn-whitespace-after-sigil` — whitespace appears after `{` or after the sigil (`@`/`~`).
- `~gloss-syn-missing-space-before-pipe` — label separator is missing the required single ASCII space before `|`.
- `~gloss-syn-missing-space-after-pipe` — label separator is missing the required single ASCII space after `|`.
- `~gloss-syn-compact-pipe-separator` — label separator is written as `|` with no surrounding spaces.
- `~gloss-syn-invalid-nested-compact-pipe` — a nested label contains an invalid compact pipe separator.
- `~gloss-syn-trailing-after-reference` — a reference target contains trailing characters after the target is complete.
- `~gloss-syn-unclosed-annotation` — an annotation is missing a closing `}`.
- `~gloss-syn-unclosed-nested-annotation` — a nested annotation is missing a closing `}`.

### 5.2 Resolution Diagnostic Reasons (Normative)

When `category` is **resolution**, `reason` MUST be a stable `~token` defined by the
resolver and/or schema.

The Gloss v0.1 conformance suite does not yet define normative resolution reason codes.
