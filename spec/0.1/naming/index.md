Status: NORMATIVE  
Lock State: LOCKED  
Version: 0.1  
Editor: Charles F. Munat  

# Gloss Syntax and Naming

Gloss is an **inline semantic annotation language** that enriches free text
with **target-independent semantic information**.

Gloss exists to solve a core problem in markup systems (e.g. HTML):
the conflation of **structure**, **semantics**, and **presentation** inside text.

Gloss provides **semantic span binding only**.
It does not define structure, layout, behavior, or rendering.

---

## 1. Purpose

Gloss enables authors to:

* annotate spans of free text with semantic meaning
* bind text to declarative data defined elsewhere in Codex
* express emotion, tone, state, and machine-readable values unavailable in
  traditional markup
* support rich multi-target rendering (HTML, PDF, audio, braille, etc.)
* preserve round-trip integrity and explainability

Gloss is designed for **authoring**, not programming.

---

## 2. Non-Goals (Normative)

Gloss does **not**:

* define block structure
* alter the meaning of referenced Concepts or Entities
* encode presentation markup
* define behavior or logic
* evaluate values or expressions
* replace Codex Concepts, Traits, or schemas

If it affects correctness or structure, it is **not Gloss**.

---

## 3. Relationship to Codex

Gloss is **subordinate to Codex**.

* Codex defines:
  * Concepts
  * Traits
  * Values
  * Entity identity
* Gloss references Codex Concepts by `id`
* Gloss never introduces new data or meaning on its own

Gloss is valid **only in the presence of Codex schemas**.

---

## 4. Where Gloss Appears (Normative)

Gloss annotations MAY appear:

* inside **Content** (free text) of Codex Concepts

Gloss annotations MUST NOT appear:

* inside Traits
* inside attribute values
* inside identifiers
* inside schema definitions

Content is otherwise opaque to Codex.

---

## 5. Gloss Syntax (Normative)

Gloss annotations use **curly braces** to mark spans.

Three addressing forms exist:

```
{@iri}
{@iri | label}

{~token}
{~token | label}

{#id}
{#id | label}
```

Where:

* `@` references an Entity by IRI
* `~` references an Entity by lookup token (resolves via `key` Trait)
* `#` references a non-Entity Concept

The parser collapses and ignores whitespace inside Gloss syntax (outside of `label`). Whitespace inside `label` is preserved verbatim.

Gloss annotations MAY be nested.

---

## 5.1 Escaping Rules (Normative)

Gloss uses **context-sensitive escaping** to minimize the need for escape
sequences in typical content.

### Opening Brace

`{` starts a Gloss annotation **only** when immediately followed by `@`, `~`,
or `#`. Otherwise, `{` is literal text.

```
{@entity}         — Gloss annotation
{#concept}        — Gloss annotation
{curly braces}    — literal text, not an annotation
{foo}             — literal text, not an annotation
```

### Pipe Character

Inside a Gloss annotation, the **first** `|` separates the reference from the
label. Subsequent `|` characters are part of the label.

```
{@entity | label with | pipes | is fine}
```

Here, `label with | pipes | is fine` is the complete label.

### Closing Brace

Inside a label, `}` closes the annotation. To include a literal `}` in a label,
escape it with a backslash: `\}`.

```
{@entity | label with \} brace}
```

### Backslash

Inside a label, `\\` produces a literal backslash. Backslash only has special
meaning when followed by `}` or `\`.

```
{@entity | path\\to\\file}     — label is "path\to\file"
{@entity | ends with \\}       — label is "ends with \"
```

Outside of Gloss annotations, backslash has no special meaning.

### Summary

| Context | Character | Rule |
|---------|-----------|------|
| Content | `{` | Literal unless followed by `@`, `~`, `#` |
| Content | `}` | Always literal |
| Content | `\` | Always literal |
| Label | `|` | First is separator; rest are literal |
| Label | `}` | Closes annotation; escape as `\}` |
| Label | `\` | Escape character before `}` or `\`; otherwise literal |

---

## 6. Addressing Semantics

### 6.1 `@` — Direct Entity Reference (Normative)

`@` references a **Codex Entity** by its IRI.

An Entity is a Concept that declares an `id` Trait and is schema-authorized
as an Entity.

Rules:

* `@iri` MUST resolve to an Entity by its `id` Trait
* Entity references imply **identity**
* Entity references MAY participate in:
  * RDFa / microdata
  * JSON-LD emission
  * graph association
* Entity references MAY supply a default label from data

Example:

```cdx
<Book id=book:hobbit key=~hobbit title="The Hobbit" author="J.R.R. Tolkien" />
```

```cdx
I love {@book:hobbit}.
I love {@book:hobbit | The Hobbit — Tolkien}.
```

---

### 6.2 `~` — Lookup Token Entity Reference (Normative)

`~` references a **Codex Entity** by its lookup token.

Rules:

* `~token` MUST resolve to an Entity via its `key` Trait
* Resolution follows the rules defined in **Codex Naming and Values § 4.15**
* Entity references imply **identity**
* Entity references MAY participate in:
  * RDFa / microdata
  * JSON-LD emission
  * graph association
* Entity references MAY supply a default label from data

Example:

```cdx
<Book id=book:hobbit key=~hobbit title="The Hobbit" author="J.R.R. Tolkien" />
```

```cdx
I love {~hobbit}.
I love {~hobbit | The Hobbit — Tolkien}.
```

The lookup token form is preferred for authoring ergonomics.

---

### 6.3 `#` — Non-Entity Target (Normative)

`#` references a **non-Entity Concept**.

These include:

* temporal values
* numeric values
* semantic inline annotations
* presentation intent
* media references
* domain-specific annotations (emotion, tone, state, etc.)

Rules:

* `#id` MUST NOT resolve to an Entity
* `#` references do not imply identity
* `#` references bind meaning or intent to a span only

Example:

```cdx
<PrecisionNumber id=pi value=3.141592653589793p15 />
```

```cdx
The value of pi is {#pi}.
```

---

## 7. Label Overrides

All reference forms MAY include a label override:

```
{@iri | label}
{~token | label}
{#id | label}
```

Rules:

* The label replaces the rendered text for that span
* The semantic binding remains unchanged
* Label overrides are authorial, not semantic redefinitions

---

## 8. Open Vocabulary Model (Normative)

Gloss supports an **open vocabulary**.

Rules:

* Gloss MAY reference any schema-authorized Concept (including Entities) by a resolvable identifier token
* Gloss does not enumerate or constrain domain vocabularies
* Meaning is defined entirely by the Concept’s schema

### 8.1 Vocabulary Ownership

* **Architect** (and other domain libraries) own:

  * semantic vocabularies
  * emotion, tone, narrative state, domain meaning
* Gloss defines:

  * how spans are bound
  * when semantics become observable
  * how targets may consume them

Examples of valid open vocabulary Concepts:

```cdx
<Sad id=sad />
<Angry id=angry />
<InternalDialogue id=inner />
<Dream id=dream />
<Emotion id=e1 kind="sadness" intensity=0.7 />
```

Used as:

```cdx
{#sad | "I can’t believe he died."}
{#angry | "It wasn’t supposed to happen!"}
```

---

## 9. Target Independence (Normative)

Gloss encodes **meaning only**, never presentation.

Renderers MAY realize Gloss semantics differently by target:

* HTML → elements, attributes, RDFa
* PDF → typography, annotations
* Audio → prosody, pacing, voice modulation
* Braille → markers
* Data export → structured metadata

Gloss meaning MUST NOT change by target.

---

## 10. Lifecycle and Processing

Gloss lifecycle, parsing, and validation are defined in the following
normative documents:

* **Lifecycle** — phase boundaries, parsing ownership, preservation guarantees
* **Semantic Realization** — typed output model, invariants
* **Design Policy Interaction** — consumer rules, permitted and prohibited uses

In summary:

* Kernel treats Gloss as opaque text during compilation and storage
* Kernel parses and semantically realizes Gloss during **ViewModel shaping**
* Kernel surfaces Gloss errors as **Help values**, never as runtime failures
* Renderers MUST NOT introduce new Gloss semantics

---

## 11. Naming Rules (Normative)

Gloss naming follows Codex naming rules:

* Concept names: **PascalCase**
* Trait names: **camelCase**
* No shorthand or symbol-only names
* Spelled-out names are required

Examples:

* `<Stress>` ✔
* `<Important>` ✔
* `<Pi>` ✔ (spelled-out concept name)
* `<EulerNumber>` ✔
* `<E>` ✘
* `<Bold>` ✘ (presentation effect, not semantic)

Naming rules are defined in the Codex specification.

---

## 12. Identifiers

* Gloss treats identifier tokens as **opaque**
* Identifier tokens MAY be IRIs
* Colons, slashes, and other IRI characters are permitted
* Gloss performs no namespace interpretation

Resolution rule:

> The identifier token must resolve to a schema-authorized Concept (including Entities).

---

## 13. Error Handling (Normative)

Gloss processing:

* MUST NOT throw
* MUST NOT return `null` or `undefined`
* MUST surface failures as Help values
* MUST preserve source locations

### 13.1 Error Categories

Two categories of errors exist:

**Syntax errors:** Malformed Gloss markup.

* Unclosed annotation: `{@entity` (no closing `}`)
* Empty reference: `{@}` or `{#}` (sigil but no identifier)

**Resolution errors:** Valid syntax, but reference cannot be resolved.

* Unresolved reference: `{@nonexistent}` (Entity not found)
* Wrong addressing form: `{@concept}` where `concept` is not an Entity

### 13.2 Syntax Error Recovery (Normative)

When Kernel encounters a syntax error:

1. Kernel treats the malformed markup as **literal text**
2. Kernel emits a **Help diagnostic** with source location
3. Kernel continues parsing subsequent content

Examples:

| Input | Output | Help |
|-------|--------|------|
| `{@entity` | Literal text `{@entity` | "Unclosed annotation" |
| `{@}` | Literal text `{@}` | "Empty reference after @" |
| `{#a | {#b | x}` | `{#b | x}` parses; `{#a | ` is literal | "Unclosed annotation" |

### 13.3 Resolution Error Recovery (Normative)

When Kernel encounters a resolution error:

1. Kernel parses the annotation successfully
2. Kernel marks the resolution as **failed**
3. Kernel emits a **Help diagnostic** with source location
4. Renderers receive the annotation with failure metadata

Resolution errors are **semantic failures**, not syntax errors. The annotation
structure is preserved for debugging and tooling.

### 13.4 Nesting and Errors

When nested annotations have errors:

* Valid inner annotations parse normally
* Invalid outer annotations fall back to literal text
* Each error emits its own Help diagnostic

The principle: errors are **localized**. One malformed annotation does not
invalidate surrounding content.

---

## 14. Summary

Gloss provides:

* inline semantic span binding
* strict separation of concerns
* open, extensible vocabulary
* target-independent meaning
* explainable, deterministic behavior

Gloss answers:

> **“What does this span mean?”**

Never:

> “How should it look?”
> “What should it do?”

---

**End of Gloss Syntax and Naming v0.1**
