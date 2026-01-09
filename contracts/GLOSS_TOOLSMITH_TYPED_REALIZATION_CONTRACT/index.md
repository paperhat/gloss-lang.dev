Status: NORMATIVE
Lock State: LOCKED
Version: 0.1
Editor: Charles F. Munat

# Gloss Toolsmith Typed Realization Contract

This contract defines how Gloss semantic realization produces a **typed semantic
representation** using Toolsmith newtypes, while preserving Gloss and Codex
invariants: **no evaluation**, **no normalization**, **lossless round-trip**, and
**explainability**.

This contract governs the output of **Phase 4 — Semantic Realization** in the
Gloss Lifecycle and the obligations of all consumers (Design Policy, renderers,
and metadata emitters).

---

## 1. Purpose

Toolsmith provides tagged, runtime-guarded newtypes that extend base JS/TS types
with domain-safe semantics (e.g. `PrecisionNumber`, `HexColor`, `Iri`, `Url`).

This contract ensures that when Gloss becomes semantically observable (ViewModel
shaping), the system:

* resolves Gloss references deterministically
* represents resolved values using Toolsmith newtypes where applicable
* surfaces failures as Help values (never throws)
* preserves original author text and literal spellings for round-trip and audit
* enables renderer- and policy-safe consumption without stringly-typed ambiguity

---

## 2. Scope (Hard)

This contract defines:

* the **typed semantic representation** produced by Gloss semantic realization
* which data MUST be preserved verbatim
* how Toolsmith guards are used to improve Help quality
* invariants for consumers (Design Policy, renderers, metadata emission)

This contract does not define:

* Gloss syntax (Gloss Language Specification)
* vocabulary definitions (Architect / domain schemas)
* rendering strategy (Design Policy / renderers)
* Codex parsing, AST/IR shape, or RDF mapping

---

## 3. Phase Boundary (Hard)

Typed realization occurs only in:

> **Gloss Phase 4 — Semantic Realization (ViewModel shaping)**

During authoring, compilation, and persistence, Gloss remains **opaque text** and
MUST NOT be parsed, typed, normalized, or interpreted.

---

## 4. Fundamental Invariants (Hard)

Typed realization MUST preserve the following invariants:

1. **No Throwing**
   * Realization MUST NOT throw.
   * Failures MUST surface as Help values.

2. **No Normalization**
   * Codex and Gloss perform **no conversion** and **no normalization** of values.
   * Typed representations MUST NOT rewrite author-declared forms.

3. **Lossless Round-Trip**
   * Original Content text (including Gloss markup) MUST remain unchanged.
   * Any semantic representation MUST retain enough location data to map back to
     the authored span.

4. **Explainability**
   * Every resolved target MUST be explainable in plain language.
   * Every failure MUST be explainable and location-attached.

5. **Strict `@` / `#` Partition**
   * `@` MUST resolve to exactly one Entity.
   * `#` MUST resolve to a non-Entity Concept and MUST NOT imply identity.

---

## 5. Typed Semantic Output Model

Semantic realization produces a list (or tree, if nesting is preserved) of
**Resolved Gloss Spans**.

### 5.1 `ResolvedGlossSpan` (Normative Shape)

Each resolved span MUST include:

* `addressingKind`: `Entity` | `NonEntity` (from `@` vs `#`)
* `id`: the referenced identifier as authored (opaque string; MAY be IRI-like)
* `labelOverride`: optional author-provided label (verbatim)
* `sourceSpan`: source locations for the annotated range (start/end positions)
* `resolution`:
  * either `ResolvedTarget`
  * or `UnresolvedTarget` with Help

### 5.2 `ResolvedTarget` (Normative)

A resolved target MUST include:

* `conceptName`: Toolsmith `ConceptName` (or equivalent) for the resolved Concept
* `isEntity`: boolean (MUST match addressingKind constraints)
* `authoredValueLiteral`: verbatim value spelling when a value exists
* `typedValue`: optional Toolsmith newtype value when applicable
* `valueKind`: a stable tag describing the typedValue kind, when present
* `explain`: minimal data required for explainability (see §9)

`typedValue` is optional to permit Concepts without values (e.g. discrete state
Concepts like `<Sad id="sad" />`).

---

## 6. Toolsmith Typing Rules

### 6.1 Typing is a Consumer-Safety Guarantee (Hard)

When a resolved Concept’s semantics include a value that has a corresponding
Toolsmith newtype, semantic realization MUST produce `typedValue`.

Examples (non-exhaustive):

* Numeric:
  * `Integer`, `WholeNumber`, `Fraction`, `PrecisionNumber`, `SafeFloat`
* Color:
  * `HexColor`, `OklchColor`, `P3Color`
* Identifiers / Web:
  * `Iri`, `Uri`, `Url`, `UrlFragment`, `HtmlId`, `EmailAddress`, etc.
* Location:
  * `Line`, `Column`, `Offset` for source span coordinates

### 6.2 Guard-Driven Typing (Hard)

Typing MUST be performed using Toolsmith guards.

If a guard fails:

* semantic realization MUST NOT throw
* a Help value MUST be emitted with:
  * the expected type name
  * the received literal (verbatim)
  * a location range
  * an actionable suggestion (when possible)

### 6.3 Dual Representation (Hard)

Whenever a typed value is produced, the system MUST retain:

* `authoredValueLiteral` — verbatim
* `typedValue` — Toolsmith-typed

This preserves “no normalization” while enabling safe consumption.

---

## 7. Value Kind Tags (Normative)

Typed values MUST be tagged with a stable `valueKind` identifier so that
Design Policy and renderers can branch deterministically without inspecting
raw shapes.

Examples (illustrative):

* `Integer`
* `PrecisionNumber`
* `Fraction`
* `HexColor`
* `OklchColor`
* `P3Color`
* `PlainDate`
* `Duration`
* `TextStyleEffects`

`valueKind` is a semantic tag, not a renderer decision.

---

## 8. Capability-Driven Consumption (Normative)

Renderers SHOULD declare supported `valueKind` tags (or Toolsmith types) as a
capability set.

Design Policy MAY branch on:

* `valueKind`
* target class (screen, print, voice, braille, data)
* renderer capabilities

Branching MUST remain explainable and MUST NOT reinterpret meaning.

---

## 9. Explainability Requirements (Hard)

For each resolved span, the system MUST be able to explain:

* what identifier was referenced
* what Concept it resolved to
* whether it was Entity vs non-Entity
* what literal value was carried (if any)
* whether a typed value exists, and what type it is
* how realization decisions were made downstream (policy/renderer), or why ignored

For each failure, the system MUST be able to explain:

* what failed (syntax, unresolved reference, typing guard failure)
* where it failed (sourceSpan)
* what was expected
* what was found
* what the author can do to fix it

Opaque behavior is forbidden.

---

## 10. Interaction with Metadata Emission

Entity references (`@`) make Entities eligible for metadata emission.

Typed realization MUST provide enough information to support:

* consistent entity collection
* schema-consistent JSON-LD emission for HTML-class targets by default
* alternative emission strategies controlled by Design Policy

Gloss does not control emission strategy.

---

## 11. Interaction with Color and Numeric Targetable Concepts

Color Concepts and Numeric Concepts:

* are non-Entities
* MUST be referenced via `#`
* MUST preserve authored color space / precision semantics
* MUST retain authored literal spellings
* MUST produce Toolsmith typed values when corresponding newtypes exist

No conversion, normalization, or evaluation is performed by Codex or Gloss.

---

## 12. Non-Goals (v0.1)

This contract does not define:

* conversion algorithms (color, units, time zones)
* numeric evaluation or expression semantics
* unit systems or dimensional analysis
* conflict/precedence rules for overlapping annotations
* renderer implementation details

---

**End of Gloss Toolsmith Typed Realization Contract v0.1**
