Status: NORMATIVE
Lock State: LOCKED
Version: 0.1
Editor: Charles F. Munat

# Gloss Formatting and Canonicalization Specification — Version 0.1

This document defines canonical spellings for Gloss annotations and the obligations of producers (formatters, editors, transformations).

## 1. Canonical Spellings (Normative)

Canonical annotation spellings are:

- `{@iri}`
- `{@iri | label}`
- `{~token}`
- `{~token | label}`

In particular:

- the label separator MUST be written as ` ␠|␠ `
- producers MUST NOT emit the compact form `{@x|label}`

## 2. Producer Obligations (Normative)

Consumers that emit or rewrite Gloss (formatters, editors, transformations) MUST emit only canonical spellings.

## 3. Non-Canonical Input Handling (Normative)

Parsers MUST treat non-canonical spellings that violate the surface-form rules as syntax errors and apply the error recovery rules.
