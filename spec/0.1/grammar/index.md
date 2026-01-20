Status: NORMATIVE
Lock State: LOCKED
Version: 0.1
Editor: Charles F. Munat

# Gloss Formal Grammar Specification — Version 0.1

This section defines the **formal grammar** for Gloss annotations embedded in Codex `Content`.

Gloss is **not** a standalone document format. It is an inline annotation syntax that may appear inside arbitrary text. Therefore the grammar is presented in two layers:

1. **Annotation grammar** (normative): the internal structure of a single annotation such as `{@x | label}`.
2. **Embedding rule** (normative): how a consumer recognizes the start of an annotation in a larger text stream.

## 1. Embedding Rule (Normative)

An annotation begins at a `{` character **only when** the next character is `@` or `~`.

- If `{` is not immediately followed by `@` or `~`, it is literal text.
- This rule is the only mechanism by which Gloss avoids requiring escaping for ordinary braces in prose.

This embedding rule applies both in top-level `Content` and inside annotation labels.

## 2. Strict Whitespace (Normative)

Gloss is intentionally strict:

- No whitespace is permitted between `{` and the sigil.
- No whitespace is permitted between the sigil and the reference token.
- The label separator `|` MUST be written with exactly one ASCII space on each side: `{@x | label}`.

The compact form `{@x|label}` is invalid.

Examples:

- Valid: `{@book:hobbit | The Hobbit}`
- Invalid: `{@book:hobbit|The Hobbit}`

## 2.1 Conformance and Canonicalization (Normative)

Conforming consumers:

1. MUST treat any whitespace-violating annotation spelling as a **syntax error**.
2. MUST apply the syntax error recovery rules defined by [gloss-lang.dev/spec/0.1/validation-errors/index.md](../validation-errors/index.md).

Canonical annotation spellings are:

- `{@iri}`
- `{@iri | label}`
- `{~token}`
- `{~token | label}`

Consumers that emit or rewrite Gloss (formatters, editors, transformations) MUST emit the canonical spellings above.

Canonical spellings and producer obligations are defined by [gloss-lang.dev/spec/0.1/formatting-and-canonicalization/index.md](../formatting-and-canonicalization/index.md).

## 3. External Token Definitions (Normative)

Gloss reuses Codex token definitions:

- `IriReference` — the Codex identifier token (IRI reference)
- `LookupToken` — the Codex lookup token (e.g., `~hobbit`)

These tokens are defined in the Codex formal grammars.

## 4. Grammar Dialects

- EBNF: [gloss-lang.dev/spec/0.1/grammar/ebnf/index.md](ebnf/index.md)
- PEG (informative): [gloss-lang.dev/spec/0.1/grammar/peg/index.md](peg/index.md)
