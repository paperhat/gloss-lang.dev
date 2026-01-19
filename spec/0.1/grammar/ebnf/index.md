Status: NORMATIVE
Lock State: UNLOCKED
Version: 0.1
Editor: Charles F. Munat

# Gloss Formal Grammar (EBNF) — Version 0.1

This document defines the normative EBNF for Gloss annotations.

Notes:

- `IriReference` and `LookupToken` are imported from the Codex grammar.
- This grammar defines the structure of an annotation. Recognition inside an arbitrary text stream is defined by the embedding rule in [gloss-lang.dev/spec/0.1/grammar/index.md](../index.md).

---

## 1. Annotation Grammar (Normative)

```ebnf
GlossAnnotation = "{", Reference, [ LabelSeparator, Label ], "}" ;

Reference = AtReference | LookupToken ;

AtReference = "@", IriReference ;

(* The label separator '|' MUST use balanced spacing:
   exactly one ASCII space on each side: ' | '. *)

LabelSeparator = " ", "|", " " ;

(* Labels may contain nested Gloss annotations.
   Escaping is context-sensitive and applies only inside Label:

   - "\\}" represents a literal '}' character.
   - "\\\\" represents a literal '\\' character.

   A backslash is only special when followed by '}' or '\\'.
*)

Label = { LabelPart } ;

LabelPart = GlossAnnotation
          | EscapedClosingBrace
          | EscapedBackslash
          | LabelTextChar ;

EscapedClosingBrace = "\\", "}" ;

EscapedBackslash = "\\", "\\" ;

LabelTextChar = ? any Unicode scalar value except '}' and '\\' ? ;
```

## 1.1 Conformance and Canonicalization (Normative)

1. Whitespace is not part of the annotation grammar. Any annotation containing whitespace in positions not permitted by this grammar MUST be treated as a syntax error.
2. Canonical spellings are exactly:

   - `{@iri}`
   - `{@iri | label}`
   - `{~token}`
   - `{~token | label}`

3. Producers (formatters, editors, transformations) MUST emit canonical spellings.

---

## 2. External Tokens (Normative)

The following tokens are defined by Codex and reused by Gloss:

- `IriReference`
- `LookupToken`

In particular, `LookupToken` includes its leading `~` sigil in surface form (e.g., `~hobbit`).
