Status: NORMATIVE  
Lock State: LOCKED  
Version: 0.1  
Editor: Charles F. Munat  

# Entity Binding and Metadata Emission

This document defines how **Gloss entity references** bind text spans to
**Codex Entities** and participate in **metadata emission** (e.g. schema.org,
RDF, JSON-LD).

This document governs **semantic association and defaults only**.
It does not define rendering, layout, or behavior.

---

## 1. Purpose

Entity binding exists to allow authors to:

* associate spans of free text with **identified entities**
* enable machine-readable metadata extraction
* support semantic search, knowledge graphs, and linked data
* allow varied realization per target (HTML, audio, PDF, etc.)
* preserve explainability and round-trip integrity

Entity binding is a core reason for Gloss and for Paperhat itself.

---

## 2. Entity References (Normative)

An **entity reference** is a Gloss annotation in one of these forms:

```
{@iri}
{@iri | label}

{~token}
{~token | label}
```

Where:

* `@iri` references an Entity by its `id` (IRI)
* `~token` references an Entity by its `key` (lookup token)
* an Entity is a Concept that declares an `id` Trait and is schema-authorized

Rules:

* `@` and `~` MUST be used only for Entities
* references MUST resolve to exactly one Entity
* failure to resolve is a semantic error (reported as Help)

### 2.1 Direct Reference Resolution (`@`)

When resolving `{@iri}`:

* The system MUST find an Entity whose `id` Trait matches `iri`
* If exactly one match: resolved
* If zero matches: resolution error
* If multiple matches: resolution error (indicates schema violation — `id` must be unique)

### 2.2 Lookup Token Resolution (`~`)

When resolving `{~token}`:

* The system MUST find an Entity whose `key` Trait matches `~token`
* Resolution follows the rules defined in **Codex Naming and Values § 4.15**

Rules:

* If exactly one Entity has `key=~token`: resolved
* If zero matches: resolution error (unresolved lookup token)
* If multiple matches: resolution error (ambiguous lookup token)

The lookup token form exists for authoring ergonomics: authors can write stable, human-friendly tokens in prose without typing full IRIs.

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

* Schemas typically define them **per Concept type**, not per instance
* Schemas select which Traits or projections constitute the label

Example (illustrative):

```cdx
<LabelPolicy id=label:Book:default for=~Book value="title" />
```

When `{~token}` or `{@iri}` is used without a label override, the default label strategy
for the Entity's Concept type is applied.

---

### 4.2 Label Override (Normative)

Gloss allows an explicit label override:

```
{@iri | label}
{~token | label}
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

The system records the **final chosen label** in the Presentation Plan.

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

* The renderer collects Entity references during rendering
* The renderer emits a single `<script type="application/ld+json">` block
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

* **Design Policy** decides whether an entity reference becomes a hyperlink
* Gloss provides no syntax to force or suppress linking
* Renderers take link targets (URIs) from Entity data when available

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


## 9. Authority and Interaction

This document must be read in conjunction with:

* the Gloss Syntax and Naming specification
* the Gloss Lifecycle specification
* the Gloss Design Policy Interaction specification
* the Codex Naming and Values specification

In case of conflict, higher-authority documents prevail.

---

## 10. Summary

* `{@iri}` and `{~token}` create **entity mentions**
* `@` references by IRI, `~` references by lookup token
* Entity binding is semantic, not presentational
* Default metadata emission is **JSON-LD**
* Label defaults live with schema; overrides live in Design Policy
* Linking is a Design Policy decision
* Gloss remains small, stable, and target-independent

---

**End of Entity Binding and Metadata Emission v0.1**
