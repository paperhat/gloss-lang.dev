# Gloss Inline Semantic Span-Binding Language

Gloss is a target-independent inline semantic span-binding language for binding meaning and data to spans of free text.

Gloss is designed for authoring, not programming. It allows writers, designers, and systems to enrich narrative text with machine-readable semantics without mixing structure, presentation, or behavior into the text itself.

Gloss answers one question: "What does this span of text mean?"

---

## Codex and Gloss

Gloss is embedded inside Codex Content. Codex is a declarative semantic markup language for expressing meaning independent of presentation or behavior. It uses XML-like syntax to write OWL2/SHACL ontologies and data. A Codex document consists of Concepts (named semantic units), Traits (values bound to Concepts), and Content (opaque narrative text). Gloss binds spans within that Content.

---

## What Problem Gloss Solves

Markup systems—especially HTML and Markdown—collapse multiple concerns into a single syntax:

* structure and layout
* semantics and presentation
* navigation and meaning
* content and behavior

For example, HTML's `<strong>` conflates semantic intent (importance) with visual presentation (bold). A screen reader or audio renderer must guess what the author meant.

This makes content:

* brittle
* difficult to repurpose
* inaccessible to non-visual targets
* hostile to semantic analysis
* tightly coupled to the web

Gloss solves this by doing one thing: binding semantic meaning to spans of text.

---

## What Gloss Is (and Is Not)

Gloss is:

* Inline only — applies to spans of text, never blocks
* Declarative — no logic, no evaluation, no execution
* Target-independent — works for HTML, PDF, audio, braille, data export, etc.
* Schema-driven — meaning is defined elsewhere
* Explainable — every span binding must be explainable in plain language
* Open-vocabulary — domains define their own semantics

Gloss is not:

* a document format
* a layout system
* a replacement for Codex
* a replacement for renderers
* a general markup language

---

## How Gloss Works

Gloss span bindings appear inline using curly-brace syntax. There are two addressing forms.

---

### Entity References (`@`)

```
{@id}
{@id | label}
```

Used to reference Entities — Concepts with identity.

Example:

```cdx
<Book id="book:hobbit" title="The Hobbit" author="J.R.R. Tolkien" />

I love {@book:hobbit}.
I love {@book:hobbit | The Hobbit — Tolkien}.
```

Entity references express semantic association, not linking. The span binding binds a span to a Concept; whether that binding becomes a hyperlink, tooltip, footnote, or nothing visible depends on Design Policy and the target renderer. Gloss does not prescribe presentation.

---

### Lookup References (`~`)

```
{~token}
{~token | label}
```

Used to reference Concepts by lookup token rather than by identity. Common uses include:

* dates and times
* numeric values
* colors
* emotion and tone
* narrative framing
* linguistic distinctions
* code, math, and technical semantics

Example:

```cdx
<PrecisionNumber key=~pi value=3.141592653589793p15 />

The value of pi is {~pi}.
```

These span bindings express meaning, not appearance.

---

## Lifecycle and Guarantees

Gloss follows a strict lifecycle:

1. Authored as plain text
2. Preserved verbatim through compilation and storage
3. Parsed and realized during ViewModel shaping
4. Consumed by Design Policy and renderers

Gloss guarantees:

* lossless round-tripping
* deterministic semantics
* no runtime failures
* explainable behavior
* no influence on structural correctness

Errors surface as Help, never as crashes.

---

## Metadata and Linked Data

When Gloss binds text to Entities, renderers may emit metadata (e.g., JSON-LD). The default strategy for HTML is JSON-LD; RDFa or microdata may be used by policy. Gloss does not control emission format or placement.

---

## Status

* Specification: 1.0.0
* Status: Normative
* Lock State: LOCKED
* Stability: High

Gloss is intended to evolve slowly and conservatively.

---

## Governance

Gloss documentation is maintained under a formal governance model. Normative content is authoritative and versioned. LOCKED documents change only through explicit revision.

See `GOVERNANCE.md` for governance rules.

---

## Licensing and Copyright

All documentation in this repository is licensed under the Creative Commons Attribution 4.0 International License (CC BY 4.0). The license applies to textual and illustrative content only.

No rights are granted to project or language names, trademarks or logos, or software implementations.

See `LICENSE.md` and `COPYRIGHT.md`.
