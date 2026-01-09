# Gloss vs HTML and Markdown

This document explains **why Gloss exists**, how it differs from HTML and
Markdown, and why it is intentionally *not* a replacement for either.

---

## Gloss vs HTML

### HTML’s Model

HTML inline elements mix concerns:

* `<em>` means *emphasis* **and** italics
* `<strong>` means *importance* **and** bold
* `<a>` means *reference*, *link*, *navigation*, and *presentation*
* attributes encode data, behavior, and styling together

Consequences:

* semantics are presentation-biased
* non-visual targets are second-class
* round-trip editing is fragile
* meaning is difficult to extract cleanly

---

### Gloss’s Model

Gloss separates concerns explicitly:

* **Gloss**: semantic intent only
* **Codex**: meaning and data
* **Design Policy**: realization decisions
* **Renderers**: target-specific output

Example:

```cdx
{#important | This matters.}
```

This expresses **importance**, not bold text.

Whether that becomes:

* bold text
* a spoken emphasis
* a braille marker
* metadata
* nothing at all

is decided elsewhere.

Gloss refuses to collapse these layers.

---

## Gloss vs Markdown

### Markdown’s Model

Markdown is optimized for:

* visual readability
* lightweight authoring
* HTML generation

Inline semantics are implicit:

* `*emphasis*`
* `**strong**`
* `` `code` ``
* links double as references and navigation

Markdown cannot express:

* identity
* numeric precision
* temporal semantics
* emotion or tone
* accessibility intent
* machine-readable meaning

---

### Gloss’s Model

Gloss assumes:

* text already exists
* structure is defined elsewhere
* meaning matters beyond visual output

Gloss can express:

* identity vs non-identity
* values with precision
* dates and durations
* emotion, tone, and narrative state
* semantic emphasis vs visual emphasis
* metadata-ready associations

Gloss is not “lighter Markdown”.
It solves a different problem.

---

## Why Gloss Is Not a Replacement

Gloss deliberately does **not** replace:

* HTML (structure, layout, interaction)
* Markdown (lightweight prose authoring)
* CSS (presentation)
* programming languages (behavior)

Gloss **complements** them by handling what they cannot:
**explicit, target-independent semantic meaning inside text**.

---

## The Design Trade-Off

Gloss is:

* more precise than HTML or Markdown
* less convenient for casual styling
* intentionally constrained

That trade-off is deliberate.

Gloss optimizes for:

* correctness
* reuse
* accessibility
* explainability
* multi-target longevity

Not for quick visual hacks.

---

## Summary

* HTML answers: *“How is this structured and displayed?”*
* Markdown answers: *“How can I write this simply?”*
* Gloss answers: **“What does this mean?”**

They are not competitors.
They are layers.
