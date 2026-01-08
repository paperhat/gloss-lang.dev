# Gloss

**Gloss** is a **target-independent inline annotation language** for binding
semantic meaning and data to free text.

Gloss is designed for **authoring**, not programming. It allows writers,
designers, and systems to enrich narrative text with machine-readable semantics
without mixing structure, presentation, or behavior into the text itself.

---

## What Problem Gloss Solves

Legacy markup systems (especially HTML) mix:

* structure and layout
* semantics and presentation
* behavior and data

This makes content brittle, hard to repurpose, and difficult to target beyond
the web.

Gloss solves this by providing a **small, stable inline language** whose sole
responsibility is:

> **Annotating spans of text with meaning.**

Nothing more.

---

## Core Principles

Gloss is:

* **Inline only** — it annotates spans of text
* **Target-independent** — works for HTML, PDF, audio, braille, data export, etc.
* **Declarative** — no logic, no expressions, no behavior
* **Schema-driven** — meaning is defined elsewhere (in Codex schemas)
* **Explainable** — every annotation must be explainable in plain language
* **Open-vocabulary** — domains define their own semantics

Gloss is intentionally **small and boring**.

---

## How Gloss Works

Gloss annotations appear inside free text using curly-brace syntax.

There are two kinds of references:

### Entity references

```

{@id}
{@id | label}

````

Used to reference **Entities** (identified concepts such as books, people,
places, schema.org data).

Example:

```cdx
<Book id="book:hobbit" title="The Hobbit" author="J.R.R. Tolkien" />

I love {@book:hobbit}.
I love {@book:hobbit | The Hobbit — Tolkien}.
````

Entity references enable:

* semantic association
* metadata emission (e.g. JSON-LD)
* knowledge-graph integration

---

### Non-entity annotations

```
{#id}
{#id | label}
```

Used to reference **non-Entities**, such as:

* dates and times
* numeric values
* semantic inline meaning (emotion, tone, emphasis)
* presentation intent (typography, styles)
* domain-specific annotations

Example:

```cdx
<PrecisionNumber id="pi" value=3.141592653589793p15 />

The value of pi is {#pi}.
```

---

## What Gloss Does *Not* Do

Gloss does **not**:

* define structure or layout
* replace markup languages
* encode presentation details
* execute logic or behavior
* evaluate values
* define schemas or ontologies

If it affects correctness, behavior, or layout, it is **not Gloss**.

---

## Relationship to Paperhat Codex

Gloss is part of the **Paperhat** ecosystem and is tightly integrated with
**Codex**:

* Codex defines Concepts, Traits, Values, and Entities
* Architect defines domain vocabularies and meaning
* Gloss binds spans of text to those concepts
* Design Policy determines how meaning is presented
* Renderers realize output for specific targets

Gloss is **subordinate to Codex** and cannot be used meaningfully without it.

---

## Metadata and Linked Data

When Gloss binds text to Entities, renderers may emit metadata such as:

* JSON-LD (default for HTML targets)
* RDFa or microdata (optional)

The choice of emission strategy and linking behavior is controlled by
**Design Policy**, not by Gloss syntax.

---

## Status

* **Specification:** v0.1 (LOCKED)
* **Status:** Normative
* **Stability:** High — changes require explicit versioning

Gloss is intended to evolve **slowly and conservatively**.

---

## License

The specification and documentation in this repository are licensed under the  
**Creative Commons Attribution 4.0 International License (CC BY 4.0)**.

See [`LICENSE.md`](./LICENSE.md) for the full legal text and terms.

This license applies **only to the textual, diagrammatic, and illustrative
content** of this repository. It does **not** grant rights to:

- project, language, or specification names
- trademarks or logos
- software implementations, unless stated otherwise

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
