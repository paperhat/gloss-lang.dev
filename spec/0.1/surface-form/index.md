Status: NORMATIVE
Lock State: LOCKED
Version: 0.1
Editor: Charles F. Munat

# Gloss Surface Form Specification — Version 0.1

This document defines the user-visible **surface form** of Gloss annotations embedded in Codex `Content`.

## 1. Annotation Forms (Normative)

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

## 2. Recognition Rule (Normative)

`{` begins a Gloss annotation **only** when immediately followed by `@` or `~`.
Otherwise `{` is literal text.

`}` is never special outside an annotation.

This rule applies both in top-level `Content` and inside annotation labels.

## 3. Whitespace Rules (Normative)

Gloss is intentionally strict:

- No whitespace is permitted between `{` and the sigil.
- No whitespace is permitted between the sigil and the reference token.
- The label separator `|` MUST be written with **exactly one ASCII space** on each side: `{@x | label}`.

The compact form `{@x|label}` is invalid.

Therefore these are invalid Gloss annotations (and MUST be treated as syntax errors with recovery as defined by the parsing model, with a diagnostic):

- `{@ x}`
- `{@x |label}`
- `{@x| label}`
- `{@x|label}`

Whitespace inside `label` is preserved verbatim.

## 4. Tokens (Normative)

### 4.1 `@iri`

`@` references use a Codex identifier token (an IRI reference).
Gloss treats the IRI as an opaque token.

### 4.2 `{~token}`

`~` references use a Codex lookup token value.
Lookup tokens are spelled with the leading `~` and follow Codex lookup-token lexical rules.

## 5. Labels (Normative)

`label` is optional.

Rules:

1. If present, `label` is the literal text to display for that span.
2. The semantic binding (the target Concept) is unchanged by the label.
3. Labels MAY contain nested Gloss annotations.

The `label` portion is everything after the label separator ` | `.

## 6. Escaping (Normative)

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
