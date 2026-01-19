Status: NORMATIVE
Lock State: LOCKED
Version: 0.1
Editor: Charles F. Munat

# Gloss Formal Grammar — EBNF (Normative)

This document defines the **formal grammar** of Gloss inline annotations using
Extended Backus-Naur Form (EBNF).

This grammar is **normative**. A conforming parser MUST recognize all
annotations that match this grammar.

---

## 1. Notation

This grammar uses ISO/IEC 14977 EBNF notation:

* `=` defines a production
* `,` concatenation
* `|` alternation
* `[ ... ]` optional (zero or one)
* `{ ... }` repetition (zero or more)
* `( ... )` grouping
* `" ... "` terminal string
* `' ... '` terminal string (alternative)
* `(* ... *)` comment
* `;` end of production

Character classes use the following extensions:

* `#x0000` Unicode code point
* `[a-z]` character range

---

## 2. Content with Gloss Annotations

```ebnf
(* Content is a sequence of literal text and Gloss annotations *)

Content = { ContentItem } ;

ContentItem = GlossAnnotation | LiteralText ;

LiteralText = LiteralChar, { LiteralChar } ;

LiteralChar = NonBraceChar
            | "{", NonSigilChar
            | "}" ;

(* { only starts annotation when followed by @, ~, or # *)
NonSigilChar = AnyChar - ( "@" | "~" | "#" ) ;

NonBraceChar = AnyChar - "{" ;
```

---

## 3. Gloss Annotations

```ebnf
(* A Gloss annotation binds semantics to a text span *)

GlossAnnotation = "{", Sigil, Reference, [ Label ], "}" ;

Sigil = "@" | "~" | "#" ;

Reference = Identifier ;

Label = "|", LabelContent ;
```

---

## 4. Identifiers

```ebnf
(* Identifiers are opaque to Gloss; may contain IRI characters *)

Identifier = IdentifierStart, { IdentifierContinue } ;

IdentifierStart = Letter | "_" ;

IdentifierContinue = Letter | Digit | "_" | "-" | ":" | "/" | "." | "%" ;

Letter = UppercaseLetter | LowercaseLetter ;

UppercaseLetter = "A" | "B" | "C" | "D" | "E" | "F" | "G" | "H" | "I" | "J"
                | "K" | "L" | "M" | "N" | "O" | "P" | "Q" | "R" | "S" | "T"
                | "U" | "V" | "W" | "X" | "Y" | "Z" ;

LowercaseLetter = "a" | "b" | "c" | "d" | "e" | "f" | "g" | "h" | "i" | "j"
                | "k" | "l" | "m" | "n" | "o" | "p" | "q" | "r" | "s" | "t"
                | "u" | "v" | "w" | "x" | "y" | "z" ;

Digit = "0" | "1" | "2" | "3" | "4" | "5" | "6" | "7" | "8" | "9" ;
```

---

## 5. Labels

```ebnf
(* Labels may contain nested annotations and escaped characters *)

LabelContent = { LabelItem } ;

LabelItem = NestedAnnotation
          | LabelEscape
          | LabelChar ;

NestedAnnotation = GlossAnnotation ;

LabelEscape = "\", ( "}" | "\" ) ;

LabelChar = AnyChar - ( "}" | "\" | "{" )
          | "{", NonSigilChar
          | "\", NonEscapeChar ;

(* Backslash only escapes } and \ *)
NonEscapeChar = AnyChar - ( "}" | "\" ) ;
```

---

## 6. Whitespace Handling

```ebnf
(* Whitespace outside labels is collapsed and ignored *)
(* Whitespace inside labels is preserved verbatim *)

OptionalWhitespace = { WhitespaceChar } ;

WhitespaceChar = " " | "\t" | "\n" | "\r" ;
```

In parsing:

* Between `{` and Sigil: whitespace forbidden
* Between Sigil and Identifier: whitespace collapsed and ignored
* Between Identifier and `|`: whitespace collapsed and ignored
* Between `|` and LabelContent: whitespace preserved (part of label)
* Between LabelContent and `}`: whitespace preserved (part of label)

---

## 7. Nesting

```ebnf
(* Annotations may nest to arbitrary depth *)
(* Nesting is captured by NestedAnnotation in LabelItem *)

(* Example: {#outer | text {@inner | more} text} *)
(* Parses as: outer annotation with label containing inner annotation *)
```

Nesting rules:

* Entity references (`@`, `~`) MAY contain non-Entity references (`#`)
* Non-Entity references (`#`) MAY contain Entity references (`@`, `~`)
* Same-type nesting is permitted
* Depth is unbounded

---

## 8. Character Classes (Informative)

The following character classes are used but not fully enumerated:

* `AnyChar` — any Unicode scalar value
* `NonBraceChar` — any Unicode scalar except `{`
* `NonSigilChar` — any Unicode scalar except `@`, `~`, `#`
* `NonEscapeChar` — any Unicode scalar except `}`, `\`

---

## 9. Examples

### 9.1 Simple Annotations

```
{@book:hobbit}                    (* Entity by IRI *)
{~hobbit}                         (* Entity by lookup token *)
{#important}                      (* Non-Entity concept *)
```

Parsed as:

| Input | Sigil | Reference | Label |
|-------|-------|-----------|-------|
| `{@book:hobbit}` | `@` | `book:hobbit` | (none) |
| `{~hobbit}` | `~` | `hobbit` | (none) |
| `{#important}` | `#` | `important` | (none) |

### 9.2 Annotations with Labels

```
{@book:hobbit | The Hobbit}
{#stress | This is important!}
{@person:tolkien | J.R.R. Tolkien}
```

Parsed as:

| Input | Sigil | Reference | Label |
|-------|-------|-----------|-------|
| `{@book:hobbit \| The Hobbit}` | `@` | `book:hobbit` | `The Hobbit` |
| `{#stress \| This is important!}` | `#` | `stress` | `This is important!` |

### 9.3 Labels with Pipes

```
{@cmd:grep | grep foo | bar | baz}
```

Parsed as:

| Sigil | Reference | Label |
|-------|-----------|-------|
| `@` | `cmd:grep` | `grep foo \| bar \| baz` |

First `|` is separator; subsequent `|` are literal.

### 9.4 Labels with Escaped Braces

```
{@example | contains \} brace}
{@path | C:\\Users\\file}
```

Parsed as:

| Sigil | Reference | Label |
|-------|-----------|-------|
| `@` | `example` | `contains } brace` |
| `@` | `path` | `C:\Users\file` |

### 9.5 Nested Annotations

```
{#dialogue | {@character:hamlet | To be, or not to be}}
```

Parsed as:

* Outer: `#dialogue` with label containing inner annotation
* Inner: `@character:hamlet` with label `To be, or not to be`
* Both semantics apply to the innermost text

### 9.6 Literal Braces in Content

```
The set {1, 2, 3} is finite.
Call the function {foo} now.
```

Parsed as literal text (no annotations). `{` not followed by `@`, `~`, `#`.

---

## 10. Error Productions (Informative)

The following are **not** valid Gloss and result in syntax errors:

```ebnf
(* Unclosed annotation — missing } *)
ErrorUnclosed = "{", Sigil, Reference, [ Label ] ;

(* Empty reference — sigil with no identifier *)
ErrorEmptyRef = "{", Sigil, [ "|", LabelContent ], "}" ;
```

On syntax error, Kernel treats the malformed text as literal and emits Help.

---

**End of Gloss Formal Grammar — EBNF v0.1**
