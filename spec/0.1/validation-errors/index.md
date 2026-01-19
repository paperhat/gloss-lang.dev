Status: NORMATIVE
Lock State: UNLOCKED
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

1. MUST treat the malformed markup as literal text.
2. MUST emit a diagnostic with source location.
3. MUST continue parsing subsequent content.

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
