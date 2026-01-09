# Gloss Inline Semantic Span-Binding Language

**Gloss** is a **target-independent inline semantic annotation language** for binding
explicit meaning and data to spans of free text.

Gloss is designed for **authoring**, not programming.
It allows writers, designers, and systems to enrich narrative text with
machine-readable semantics **without mixing structure, presentation, or behavior
into the text itself**.

---

## What Problem Gloss Solves

Legacy markup systems (especially HTML) conflate:

* structure and layout
* semantics and presentation
* behavior and data

This makes content brittle, difficult to repurpose, inaccessible to non-visual
targets, and hostile to round-tripping.

Gloss solves this by providing a **small, stable inline language** whose sole
responsibility is:

> **Annotating spans of text with meaning.**

Nothing more.

---

## Core Principles

Gloss is:

* **Inline only** — it annotates spans of text, never structure
* **Target-independent** — usable for HTML, PDF, audio, braille, data export, etc.
* **Declarative** — no logic, no expressions, no behavior
* **Schema-driven** — all meaning is defined elsewhere (Codex schemas)
* **Explainable** — every annotation **must** be explainable in plain language
* **Open-vocabulary** — domains define their own semantics
* **Stable by design** — evolution is slow, explicit, and versioned

Gloss is intentionally **small and boring**.

---

## Two Kinds of Meaning (Foundational)

Gloss makes a strict, enforced distinction between two kinds of references:

### Entities — `@`

* Identity-bearing concepts (people, books, places, works, etc.)
* Participate in metadata and knowledge graphs
* Represent *this specific thing*

### Non-Entities — `#`

* Values, states, intent, and inline semantics
* Do **not** imply identity
* Bind meaning to a span only

This distinction is **foundational** and cannot be blurred.

---

## How Gloss Works

Gloss annotations appear inside free text using curly-brace syntax.

### Entity References

```
{@id}
{@id | label}
```

Used to reference **Codex Entities**.

Example:

```cdx
<Book id="book:hobbit" title="The Hobbit" author="J.R.R. Tolkien" />

I love {@book:hobbit}.
I love {@book:hobbit | The Hobbit — Tolkien}.
```

Entity references:

* create semantic association
* make entities eligible for metadata emission (e.g. JSON-LD)
* support linked data and knowledge graphs
* do **not** imply linking or presentation

---

### Non-Entity Annotations

```
{#id}
{#id | label}
```

Used to reference **non-Entities**, such as:

* dates and times
* numeric and measurement values
* colors
* affective and cognitive state
* semantic inline meaning
* presentation intent
* media references
* domain-specific annotations

Example:

```cdx
<PrecisionNumber id="pi" value=3.141592653589793p15 />

The value of pi is {#pi}.
```

Non-Entity annotations bind **meaning**, not identity.

---

## Where Gloss May Appear

Gloss annotations:

* MAY appear only inside **free text Content**
* MUST NOT appear inside:

  * Traits
  * attribute values
  * identifiers
  * schema definitions

Outside of Content, Gloss is invalid.

---

## When Gloss Is Interpreted

Gloss follows a strict lifecycle:

* During authoring, compilation, and persistence:

  * Gloss is treated as **opaque text**
  * it is preserved verbatim
  * it is not parsed or interpreted
* During **ViewModel shaping**:

  * Gloss is parsed
  * references are resolved
  * semantic meaning becomes observable

This guarantees:

* lossless round-tripping
* stable compilation and storage
* deterministic, explainable semantics

Gloss never affects AST shape, IR normalization, or persistence.

---

## What Gloss Does *Not* Do

Gloss does **not**:

* define structure or layout
* replace markup languages
* encode presentation details
* execute logic or behavior
* evaluate or compute values
* define schemas or vocabularies
* introduce new meaning on its own

If it affects correctness, behavior, or structure, it is **not Gloss**.

---

## Relationship to Paperhat Codex

Gloss is part of the **Paperhat** ecosystem and is strictly subordinate to
**Codex**.

* Codex defines:

  * Concepts
  * Traits
  * Values
  * Entities
* Architect and other domain libraries define vocabularies and meaning
* Gloss binds spans of text to those definitions
* Design Policy determines realization
* Renderers produce target-specific output

Gloss cannot be used meaningfully without Codex.

---

## Metadata and Linked Data

When Gloss binds text to **Entities**, renderers may emit metadata such as:

* JSON-LD (default for HTML targets)
* RDFa or microdata (optional)

The choice of emission strategy and linking behavior is controlled by
**Design Policy**, not by Gloss syntax.

---

## Status

* **Specification:** v0.1
* **Status:** Normative
* **Lock State:** Locked
* **Stability:** High — changes require explicit versioning

Gloss is intended to evolve **slowly and conservatively**.

---

## License

The specification and documentation in this repository are licensed under the
**Creative Commons Attribution 4.0 International License (CC BY 4.0)**.

This license applies **only** to the textual, diagrammatic, and illustrative
content of this repository. It does **not** grant rights to:

* project, language, or specification names
* trademarks or logos
* software implementations, unless explicitly stated

---

## Philosophy

> **Gloss answers one question:**
>
> *“What does this span of text mean?”*
>
> It never answers:
>
> *“How should it look?”*
> *“What should it do?”*

That separation is the entire point.

**Gloss is not a general-purpose markup language and cannot be used independently of Codex and the Paperhat framework.**
