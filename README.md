# Gloss Inline Semantic Span-Binding Language

**Gloss** is a **target-independent inline semantic annotation language** for binding **meaning and data** to spans of free text.

Gloss is designed for **authoring**, not programming.
It allows writers, designers, and systems to enrich narrative text with machine-readable semantics **without mixing structure, presentation, or behavior into the text itself**.

Gloss answers one question only:

> **“What does this span of text mean?”**

---

## What Problem Gloss Solves

Markup systems—especially HTML and Markdown—collapse multiple concerns into a single syntax:

* structure and layout
* semantics and presentation
* navigation and meaning
* content and behavior

This makes content:

* brittle
* difficult to repurpose
* inaccessible to non-visual targets
* hostile to semantic analysis
* tightly coupled to the web

Gloss solves this by doing **one thing only**:

> **Binding semantic meaning to spans of text.**

Nothing else.

---

## What Gloss Is (and Is Not)

Gloss **is**:

* **Inline only** — applies to spans of text, never blocks
* **Declarative** — no logic, no evaluation, no execution
* **Target-independent** — works for HTML, PDF, audio, braille, data export, etc.
* **Schema-driven** — meaning is defined elsewhere
* **Explainable** — every annotation must be explainable in plain language
* **Open-vocabulary** — domains define their own semantics

Gloss **is not**:

* a document format
* a layout system
* a replacement for Codex
* a replacement for renderers
* a general markup language

---

## How Gloss Works

Gloss annotations appear inline using curly-brace syntax.

There are exactly **two addressing forms**.

---

### Entity References (`@`)

```
{@id}
{@id | label}
```

Used to reference **Entities**—Concepts with identity.

Example:

```cdx
<Book id="book:hobbit" title="The Hobbit" author="J.R.R. Tolkien" />

I love {@book:hobbit}.
I love {@book:hobbit | The Hobbit — Tolkien}.
```

Entity references express **association**, not linking.

They MAY participate in:

* metadata emission (e.g. JSON-LD)
* knowledge graphs
* semantic search

Linking behavior is decided by **Design Policy**, not Gloss.

---

### Non-Entity Semantic References (`#`)

```
{#id}
{#id | label}
```

Used to reference **non-Entity Concepts**, such as:

* dates and times
* numeric values
* colors
* emotion and tone
* narrative framing
* linguistic distinctions
* code, math, and technical semantics

Example:

```cdx
<PrecisionNumber id="pi" value=3.141592653589793p15 />

The value of pi is {#pi}.
```

These annotations express **meaning**, not appearance.

---

## Lifecycle and Guarantees

Gloss follows a strict lifecycle:

1. Authored as plain text
2. Preserved verbatim through compilation and storage
3. Parsed and realized during **ViewModel shaping**
4. Consumed by Design Policy and renderers

Gloss guarantees:

* lossless round-tripping
* deterministic semantics
* no runtime failures
* explainable behavior
* no influence on structural correctness

Errors surface as **Help**, never as crashes.

---

## Metadata and Linked Data

When Gloss binds text to Entities:

* renderers MAY emit metadata (e.g. JSON-LD)
* the default strategy for HTML is **JSON-LD**
* RDFa or microdata MAY be used by policy

Gloss does not control emission format or placement.

---

## Status

* **Specification:** v0.1
* **Status:** Normative
* **Lock State:** Locked
* **Stability:** High

Gloss is intended to evolve **slowly and conservatively**.

---

## Governance

Gloss documentation is maintained under a **formal governance model**.

Normative content is authoritative and versioned.
LOCKED documents change only through explicit revision.

See **`GOVERNANCE.md`** for governance rules.

---

## Licensing and Copyright

All documentation in this repository is licensed under the
**Creative Commons Attribution 4.0 International License (CC BY 4.0)**.

The license applies to **textual and illustrative content only**.

No rights are granted to:

* project or language names
* trademarks or logos
* software implementations

See:

* **`LICENSE.md`**
* **`COPYRIGHT.md`**
