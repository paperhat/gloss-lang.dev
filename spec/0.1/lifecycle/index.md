Status: NORMATIVE
Lock State: LOCKED
Version: 0.1
Editor: Charles F. Munat

# Gloss Lifecycle

This document defines the **lifecycle, phase boundaries, parsing ownership,
and invariants** of Gloss within Paperhat.

Gloss is an **inline semantic annotation language** used to enrich free text
with target-independent semantic distinctions.

---

## 1. Purpose

This document ensures that Gloss:

- remains purely annotative
- integrates deterministically with the Kernel pipeline
- surfaces errors at the correct semantic phase
- preserves round-trip and explainability guarantees

---

## 2. Scope (Normative)

This document governs:

- when Gloss is parsed
- when Gloss is validated
- when Gloss semantics become observable
- how Gloss participates in planning and rendering
- where Gloss errors are detected and reported
- which system owns Gloss parsing

This document does NOT define:

- Gloss syntax (see Naming specification)
- Gloss vocabulary (see Targetable Concepts)
- Gloss addressing semantics (see Entity Binding)

---

## 3. Lifecycle Overview

Gloss progresses through the system in **five distinct phases**:

1. Authoring
2. Compilation
3. Persistence
4. Semantic Realization
5. Planning and Rendering

Each phase has strict responsibilities and prohibitions.

---

## 4. Phase 1 — Authoring (Normative)

Gloss is authored:

- inline within free text content
- inside Codex Concepts
- never inside attributes

At authoring time:

- Gloss remains **textual only**
- the system performs no validation beyond basic text well-formedness
- the system performs no semantic resolution

The system treats Gloss as **opaque text** at this stage.

---

## 5. Phase 2 — Compilation (Normative)

During CDX → AST → IR → RDF/Turtle:

- Kernel preserves Gloss content **verbatim**
- Kernel does **not parse** Gloss
- Kernel does **not interpret** Gloss
- Kernel does **not validate** Gloss

Kernel MUST:

- preserve source locations for Gloss spans as part of text location metadata
- ensure lossless round-tripping of Gloss text

Gloss MUST NOT influence:

- AST shape
- IR normalization
- RDF emission

---

## 6. Phase 3 — Persistence (Normative)

When stored in a triple store:

- Gloss remains embedded as text
- the store does not materialize Gloss semantics as triples
- the store does not parse Gloss

The triple store is **Gloss-agnostic**.

---

## 7. Phase 4 — Semantic Realization (Normative)

Kernel parses and semantically realizes Gloss during:

> **ViewModel shaping**

At this phase:

- Kernel parses Gloss spans into a semantic representation
- Kernel resolves references (e.g. `#id`) against available Codex data
- Kernel validates nesting rules
- semantic distinctions become observable inputs

This is the **earliest phase** at which Gloss meaning exists.

---

## 8. Phase 5 — Planning and Rendering (Normative)

After semantic realization:

- Design Policy MAY consume Gloss-derived semantics
- Presentation Plans MAY branch on Gloss distinctions
- Renderers MAY map Gloss semantics to target affordances

Rendering:

- MUST NOT introduce new Gloss semantics
- MUST NOT reinterpret Gloss meaning
- MUST remain pure and deterministic

---

## 9. Parsing Ownership (Normative)

**Kernel exclusively owns Gloss parsing and semantic realization.**

No other library may:

- parse Gloss syntax
- interpret Gloss annotations
- resolve Gloss references
- define alternative Gloss semantics
- re-parse Gloss text at render time

Renderers, Design Policy, and behaviors are **consumers only**.

---

## 10. Parsing Location (Normative)

Gloss parsing occurs **only** during:

> **ViewModel shaping**

Gloss MUST NOT be parsed during:

- CDX compilation
- IR normalization
- RDF/Turtle emission
- triple-store persistence
- SPARQL querying
- rendering

This establishes a single, authoritative semantic boundary.

---

## 11. Parsing Inputs (Normative)

The Gloss parser receives:

- free-text content strings
- source-location metadata
- access to Codex-defined data required for reference resolution

The parser MUST NOT require:

- render-target knowledge
- Design Policy knowledge
- behavior configuration
- runtime IO

Parsing is a **pure function**.

---

## 12. Parsing Outputs (Normative)

The Gloss parser produces a **Gloss Semantic Representation** that:

- preserves original text verbatim
- records span boundaries
- records nesting structure
- records semantic labels
- records resolved references (or failure diagnostics)

This representation is:

- deterministic
- serializable
- independent of render targets

---

## 13. Validation and Failure Handling (Normative)

### 13.1 General Rules

Gloss parsing:

- MUST NOT throw
- MUST NOT return `null` or `undefined`
- MUST always return semantic output + Help values

### 13.2 Invalid Gloss Syntax

- Kernel reports errors as Help
- Kernel attaches errors to source locations
- Kernel MUST NOT abort the pipeline

### 13.3 Unresolved References

- Kernel detects unresolved references during semantic realization
- Kernel reports them as Help
- Kernel classifies them as semantic integrity failures
- Policy or target MAY elevate severity

Kernel MUST NOT defer Gloss failures to rendering.

---

## 14. Stability Guarantees (Normative)

For equivalent Gloss inputs, the parser MUST produce:

- identical semantic representations
- identical Help outputs (modulo location metadata)

Parser behavior MUST NOT vary by:

- render target
- execution mode
- Design Policy
- runtime environment

---

## 15. Round-Trip Guarantees (Normative)

Gloss MUST satisfy:

- lossless textual round-trip
- stable semantic interpretation for equivalent inputs
- preservation of author-supplied labels and spans

Gloss parsing and realization MUST NOT mutate original text.

---

## 16. Separation Guarantees (Normative)

Gloss:

- is not behavior
- is not structure
- is not presentation
- does not trigger execution
- does not affect semantic correctness

Gloss provides **semantic signals only**.

---

## 17. Change Control

Any change to:

- parsing rules
- error classification
- semantic representation
- phase boundaries

constitutes a **Gloss language change** and MUST follow Gloss spec change
control.

---

**End of Gloss Lifecycle v0.1**
