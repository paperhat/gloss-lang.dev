Status: NORMATIVE  
Lock State: LOCKED  
Version: 0.1  
Editor: Charles F. Munat  

# Gloss Language Specification

Gloss is an **inline semantic annotation language** used to enrich free text
with **target-independent semantic and presentation-relevant information**.

Gloss exists to solve a core problem in markup systems (e.g. HTML):
the conflation of **structure**, **semantics**, and **presentation** inside text.

Gloss provides **semantic span binding only**.
It does not define structure, layout, behavior, or rendering.

---

## 1. Purpose

Gloss enables authors to:

* annotate spans of free text with semantic meaning
* bind text to declarative data defined elsewhere in Codex
* express information unavailable in traditional markup
  (emotion, tone, state, metadata, machine-readable values)
* support rich multi-target rendering (HTML, PDF, audio, braille, etc.)
* preserve round-trip integrity and explainability

Gloss is designed for **authoring**, not programming.

---

## 2. Non-Goals (Normative)

Gloss does **not**:

* define block structure
* alter semantic truth
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

Two addressing forms exist:

```
{@token}
{@token | label}

{#id}
{#id | label}
```

Whitespace inside Gloss syntax is insignificant except inside `label`.

Gloss annotations MAY be nested.

---

## 6. Addressing Semantics

### 6.1 `@` — Entity Reference (Normative)

`@` references a **Codex Entity**.

An Entity is a Concept that declares an `id` Trait and is schema-authorized
as an Entity.

Rules:

* `@token` MUST resolve to an Entity
* Entity references imply **identity**
* Entity references MAY participate in:
  * RDFa / microdata
  * JSON-LD emission
  * graph association
* Entity references MAY supply a default label from data

Entity token resolution for `@token` is defined by **Entity Binding and Metadata Emission**.

Example:

```cdx
<Book id=book:hobbit key=hobbit title="The Hobbit" author="J.R.R. Tolkien" />
```

```cdx
I love {@hobbit}.
I love {@hobbit | The Hobbit — Tolkien}.
```

---

### 6.2 `#` — Non-Entity Target (Normative)

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

Both `@` and `#` references MAY include a label override:

```
{@token | label}
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
normative contracts:

* **Gloss Lifecycle Contract**
* **Gloss Parsing Responsibility Contract**
* **Gloss–Design Policy Interaction Contract**

In summary:

* Gloss is treated as opaque text during compilation and storage
* Gloss is parsed and semantically realized during **ViewModel shaping**
* Gloss errors surface as **Help values**, never as runtime failures
* Rendering MUST NOT introduce new Gloss semantics

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

See **Gloss Naming Contract** for full details.

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

Invalid references, malformed syntax, or unresolved IDs
are semantic failures, not rendering errors.

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

**End of Gloss Language Specification v0.1**
