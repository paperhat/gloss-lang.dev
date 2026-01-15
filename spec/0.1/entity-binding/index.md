Status: NORMATIVE  
Lock State: LOCKED  
Version: 0.1  
Editor: Charles F. Munat  

# Entity Binding and Metadata Emission

This document defines how **Gloss entity references** bind spans of text to
**Codex Entities**, and how those bindings participate in **metadata emission**
(e.g. schema.org, RDF, JSON-LD).

This document governs **semantic association and defaults only**.
It does not define rendering, layout, or behavior.

---

## 1. Purpose

Entity binding exists to allow authors to:

* associate spans of free text with **identified entities**
* enable machine-readable metadata extraction
* support semantic search, knowledge graphs, and linked data
* allow rich, target-dependent realization (HTML, audio, PDF, etc.)
* preserve explainability and round-trip integrity

Entity binding is a core reason for Gloss and for Paperhat itself.

---

## 2. Entity References (Normative)

An **entity reference** is a Gloss annotation of the form:

```

{@token}
{@token | label}

````

Where:

* `token` resolves to a **Codex Entity**
* an Entity is a Concept that declares an `id` Trait and is schema-authorized

Rules:

* `@` MUST be used only for Entities
* `@token` MUST resolve to exactly one Entity
* failure to resolve is a semantic error (reported as Help)

### 2.1 Entity Token Resolution (Normative)

When resolving `token` in `{@token}`:

1. The system MUST first attempt to resolve `token` via an Entity’s `key` Trait.
2. If and only if no Entity matches by `key`, the system MUST attempt to resolve `token` as an Entity identity reference (i.e. the Entity’s `id`, using the Codex identity resolution rules).

Rules:

* If exactly one Entity has `key=token`, `token` MUST resolve to that Entity.
* If more than one Entity has `key=token`, resolution MUST fail as a semantic error (ambiguity).
* If no Entity has `key=token`, and exactly one Entity resolves from `id=token`, `token` MUST resolve to that Entity.
* If no Entity has `key=token`, and more than one Entity resolves from `id=token`, resolution MUST fail as a semantic error (ambiguity).
* If no Entity has `key=token`, and no Entity resolves from `id=token`, resolution MUST fail as a semantic error.

This resolution order exists to preserve authoring ergonomics: authors SHOULD be able to write stable, human-friendly tokens in prose without typing UUIDs.

---

## 3. Meaning of an Entity Reference

An entity reference asserts:

> “This span of text refers to, mentions, or is associated with this Entity.”

It does **not** assert:

* that the text is a link
* that the entity is displayed inline
* that the entity is expanded or summarized
* how the association is rendered

Entity binding expresses **association**, not presentation.

---

## 4. Label Selection

### 4.1 Default Label (Normative)

Each Entity type MAY define a **default label strategy**.

Default label strategies:

* are schema-defined (e.g. in Architect or application CDX)
* are typically defined **per Concept type**, not per instance
* select which Traits or projections constitute the label

Example (illustrative):

```cdx
<LabelPolicy id=label:Book:default for=Book value="title" />
````

When `{@token}` is used without a label override, the default label strategy
for the Entity’s Concept type is applied.

---

### 4.2 Label Override (Normative)

Gloss allows an explicit label override:

```
{@token | label}
```

Rules:

* The label replaces the rendered span text
* The semantic association to the Entity remains unchanged
* Overrides are **local** and **authorial**
* Overrides do not affect metadata emission

---

### 4.3 Policy Overrides

**Design Policy** MAY override default label selection based on:

* target class (screen, print, voice, etc.)
* presentation context
* accessibility needs
* space constraints

Design Policy MUST NOT reinterpret entity meaning.

The **final chosen label** is recorded in the Presentation Plan.

---

## 5. Metadata Emission (Normative)

Entity references make Entities **eligible for metadata emission**.

Rules:

* Renderers MAY emit metadata for any Entity that is referenced
* Emission MUST be consistent with the Entity’s schema
* Emission MUST NOT change Entity meaning

---

### 5.1 Default Emission Strategy (Normative)

For HTML-class targets, the **default emission strategy is JSON-LD**.

This means:

* Entity references are collected during rendering
* A single `<script type="application/ld+json">` block is emitted
* The block contains metadata for referenced Entities

JSON-LD emission is preferred because it:

* avoids cluttering inline markup
* is robust across layout changes
* is widely supported by consumers

---

### 5.2 Alternative Emission Strategies

Renderers MAY support alternative strategies, selected by Design Policy
or renderer configuration:

* RDFa (inline attributes)
* Microdata (inline attributes)

Rules:

* The choice of emission strategy is **not controlled by Gloss**
* The choice MUST be explainable
* The choice MUST NOT affect semantic correctness

---

## 6. Linking Behavior (Normative)

Entity binding does **not** imply linking.

Rules:

* Whether an entity reference becomes a hyperlink is decided by **Design Policy**
* Gloss provides no syntax to force or suppress linking
* Link targets (URIs) are taken from Entity data when available

This preserves separation between **association** and **navigation**.

---

## 7. Explainability Requirement (Normative)

The system MUST be able to explain, in plain language:

* why a span is associated with an Entity
* which Entity it refers to
* how the label was chosen
* why metadata was (or was not) emitted
* why a link was (or was not) created

Opaque behavior is forbidden.

---

## 8. Non-Goals (v0.1)

This document does not define:

* schema.org vocabulary itself
* which Entities are Patch/Gloss-addressable
* JSON-LD framing or compaction rules
* graph merging or deduplication strategies
* search engine optimization policy

These belong to Architect, Design Policy, or renderer configuration.

---

## 9. Authority and Interaction

This document must be read in conjunction with:

* the Gloss Language Specification
* the Gloss Lifecycle Contract
* the Patch/Gloss–Design Policy Interaction Contract
* the Codex Naming and Value Contract
* the Architect schema definitions

In case of conflict, higher-authority documents prevail.

---

## 10. Summary

* `{@token}` creates an **entity mention**
* Entity binding is semantic, not presentational
* Default metadata emission is **JSON-LD**
* Label defaults live with schema; overrides live in Design Policy
* Linking is a Design Policy decision
* Gloss remains small, stable, and target-independent

---

**End of Entity Binding and Metadata Emission v0.1**
