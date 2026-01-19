Status: INFORMATIVE
Lock State: LOCKED
Version: 0.1
Editor: Charles F. Munat

# Gloss Formal Grammar — PEG (Informative)

This document defines the **formal grammar** of Gloss inline annotations using
Parsing Expression Grammar (PEG) notation.

This grammar is **informative**. It provides an implementation-ready,
unambiguous grammar suitable for direct translation to recursive descent
parsers. In case of discrepancy with the EBNF grammar, the EBNF takes
precedence.

---

## 1. Notation

This grammar uses standard PEG notation:

* `<-` defines a production
* `''` literal string
* `""` literal string (alternative)
* `/` ordered choice (try left first, then right)
* `*` zero or more (greedy)
* `+` one or more (greedy)
* `?` optional (zero or one)
* `( )` grouping
* `!` negative lookahead (does not consume)
* `&` positive lookahead (does not consume)
* `[a-z]` character class
* `.` any character

---

## 2. Content with Gloss Annotations

```peg
# Content is a sequence of literal text and Gloss annotations

Content         <- ContentItem*

ContentItem     <- GlossAnnotation / LiteralText

LiteralText     <- LiteralChar+

LiteralChar     <- NonBraceChar
                 / '{' !Sigil

NonBraceChar    <- !'{' .

# Note: '}' outside annotations is literal text
```

---

## 3. Gloss Annotations

```peg
# A Gloss annotation binds semantics to a text span

GlossAnnotation <- '{' Spacing Sigil Spacing Identifier Spacing Label? '}'

Sigil           <- '@' / '~' / '#'

Label           <- '|' LabelContent

Spacing         <- [ \t\n\r]*
```

---

## 4. Identifiers

```peg
# Identifiers are opaque to Gloss; may contain IRI characters

Identifier      <- IdentifierStart IdentifierCont*

IdentifierStart <- [a-zA-Z_]

IdentifierCont  <- [a-zA-Z0-9_\-:/.%]
```

---

## 5. Labels

```peg
# Labels may contain nested annotations and escaped characters
# Whitespace in labels is preserved verbatim

LabelContent    <- LabelItem*

LabelItem       <- NestedAnnotation
                 / LabelEscape
                 / LabelChar

NestedAnnotation <- GlossAnnotation

LabelEscape     <- '\\' [}\\]

LabelChar       <- !'}' !('\\' [}\\]) !'{'  .
                 / '{' !Sigil
                 / '\\' ![}\\]
```

---

## 6. Whitespace Handling

```peg
# Spacing is collapsed outside labels, preserved inside labels

Spacing         <- [ \t\n\r]*

# Inside labels, all characters including whitespace are preserved
# The LabelContent rule captures whitespace as LabelChar
```

---

## 7. Complete Grammar

```peg
# === Gloss PEG Grammar v0.1 ===

# Entry point for parsing content with embedded Gloss
Content         <- ContentItem*
ContentItem     <- GlossAnnotation / LiteralText

# Literal text (not Gloss)
LiteralText     <- LiteralChar+
LiteralChar     <- NonBraceChar / '{' !Sigil
NonBraceChar    <- !'{' .

# Gloss annotation structure
GlossAnnotation <- '{' Spacing Sigil Spacing Identifier Spacing Label? '}'
Sigil           <- '@' / '~' / '#'
Label           <- '|' LabelContent

# Identifiers (opaque, IRI-compatible)
Identifier      <- IdentifierStart IdentifierCont*
IdentifierStart <- [a-zA-Z_]
IdentifierCont  <- [a-zA-Z0-9_\-:/.%]

# Label content (may contain nested annotations)
LabelContent    <- LabelItem*
LabelItem       <- NestedAnnotation / LabelEscape / LabelChar
NestedAnnotation <- GlossAnnotation
LabelEscape     <- '\\' [}\\]
LabelChar       <- !'}' !('\\' [}\\]) !'{' .
                 / '{' !Sigil
                 / '\\' ![}\\]

# Whitespace (collapsed outside labels)
Spacing         <- [ \t\n\r]*
```

---

## 8. Parsing Examples

### 8.1 Simple Entity Reference

Input: `{@book:hobbit}`

```
GlossAnnotation
├── '{'
├── Sigil: '@'
├── Identifier: 'book:hobbit'
├── Label: (none)
└── '}'
```

### 8.2 Reference with Label

Input: `{@book:hobbit | The Hobbit}`

```
GlossAnnotation
├── '{'
├── Sigil: '@'
├── Identifier: 'book:hobbit'
├── Label
│   ├── '|'
│   └── LabelContent: ' The Hobbit'
└── '}'
```

### 8.3 Label with Multiple Pipes

Input: `{@cmd:grep | grep foo | bar}`

```
GlossAnnotation
├── '{'
├── Sigil: '@'
├── Identifier: 'cmd:grep'
├── Label
│   ├── '|'
│   └── LabelContent: ' grep foo | bar'
└── '}'
```

First `|` matches Label rule; subsequent `|` are LabelChar.

### 8.4 Label with Escaped Brace

Input: `{@x | a \} b}`

```
GlossAnnotation
├── '{'
├── Sigil: '@'
├── Identifier: 'x'
├── Label
│   ├── '|'
│   └── LabelContent
│       ├── LabelChar: ' a '
│       ├── LabelEscape: '\}'
│       └── LabelChar: ' b'
└── '}'
```

### 8.5 Nested Annotation

Input: `{#outer | {@inner | text}}`

```
GlossAnnotation (outer)
├── '{'
├── Sigil: '#'
├── Identifier: 'outer'
├── Label
│   ├── '|'
│   └── LabelContent
│       ├── LabelChar: ' '
│       └── NestedAnnotation
│           ├── '{'
│           ├── Sigil: '@'
│           ├── Identifier: 'inner'
│           ├── Label
│           │   ├── '|'
│           │   └── LabelContent: ' text'
│           └── '}'
└── '}'
```

### 8.6 Literal Braces (Not Annotations)

Input: `The set {1, 2, 3} is finite.`

```
Content
└── LiteralText: 'The set {1, 2, 3} is finite.'
```

`{1` does not match because `1` is not a Sigil.

---

## 9. Implementation Notes

### 9.1 Ordered Choice

PEG uses ordered choice (`/`). In `LabelItem`, try alternatives in order:

1. `NestedAnnotation` — if `{` followed by Sigil, parse nested annotation
2. `LabelEscape` — if `\` followed by `}` or `\`, parse escape
3. `LabelChar` — otherwise, consume one character

### 9.2 Greedy Matching

All repetition operators (`*`, `+`) are greedy. `LabelContent` consumes all
valid label characters until `}` closes the annotation.

### 9.3 Negative Lookahead

`!'{' .` matches any character except `{`. The lookahead does not consume input.

### 9.4 Error Recovery

This grammar defines valid syntax only. On parse failure:

1. Treat malformed text as literal
2. Emit Help diagnostic
3. Continue parsing from next potential annotation

---

## 10. Differences from EBNF

| Aspect | EBNF | PEG |
|--------|------|-----|
| Choice | Unordered (`\|`) | Ordered (`/`) |
| Ambiguity | Possible | Impossible |
| Lookahead | Not standard | Built-in (`!`, `&`) |
| Repetition | Non-greedy | Greedy |
| Authority | Normative | Informative |

The PEG grammar resolves all ambiguities through ordered choice and greedy
matching. This makes it suitable for direct implementation.

---

**End of Gloss Formal Grammar — PEG v0.1**
