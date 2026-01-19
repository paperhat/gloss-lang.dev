Status: INFORMATIVE
Lock State: UNLOCKED
Version: 0.1
Editor: Charles F. Munat

# Gloss Formal Grammar (PEG) — Version 0.1

This document defines a PEG for Gloss annotations.

Notes:

- `IriReference` and `LookupToken` are imported from the Codex grammar.
- Because Gloss is embedded in arbitrary text, this PEG includes a minimal embedding grammar (`GlossText`) showing how to recognize annotations without requiring escapes for ordinary braces.

---

## 1. Embedded Text Grammar (Normative)

```peg
# Start condition for a Gloss annotation.
AnnotationStart <- '{' [@~]

# A stream of text with embedded annotations.
# Text consumes any character sequence that does not begin an annotation.
GlossText <- (GlossAnnotation / TextRun)*

TextRun <- (!AnnotationStart .)+
```

---

## 2. Annotation Grammar (Normative)

```peg
GlossAnnotation <- '{' Reference (LabelSeparator Label)? '}'

Reference <- AtReference / LookupToken

AtReference <- '@' IriReference

# The label separator '|' MUST use balanced spacing:
# exactly one ASCII space on each side.
LabelSeparator <- ' ' '|' ' '

# Label may contain nested annotations.
# Escapes apply only inside Label.
Label <- LabelPart*

LabelPart <- GlossAnnotation / EscapedClosingBrace / EscapedBackslash / LabelTextChar

EscapedClosingBrace <- '\\' '}'
EscapedBackslash <- '\\' '\\'

# Any character except '}' and '\\', as long as it does not begin an annotation.
# This includes '|' verbatim.
LabelTextChar <- !AnnotationStart ![}\\] .
```

## 2.1 Conformance and Canonicalization (Normative)

1. Any annotation spelling that does not match `GlossAnnotation` (including any whitespace around structural tokens) MUST be treated as a syntax error.
2. Canonical spellings are exactly:

	- `{@iri}`
	- `{@iri | label}`
	- `{~token}`
	- `{~token | label}`

3. Producers (formatters, editors, transformations) MUST emit canonical spellings.

---

## 3. External Tokens (Normative)

The following tokens are defined by Codex and reused by Gloss:

- `IriReference`
- `LookupToken`
