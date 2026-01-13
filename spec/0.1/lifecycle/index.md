# Gloss Lifecycle Contract

Status: NORMATIVE
Lock State: LOCKED
Version: 0.1.1
Editor: Charles F. Munat

---

## 1. Purpose

This document defines the **lifecycle, phase boundaries, and invariants** of the Gloss language within the Paperhat system.

Gloss is an **inline semantic annotation language** used to enrich free text with target-independent semantic distinctions.

This contract exists to ensure that Gloss:

* remains purely annotative
* integrates deterministically with the Kernel pipeline
* surfaces errors at the correct semantic phase
* preserves round-trip and explainability guarantees

---

## 2. Scope (Hard)

This document governs:

* when Gloss is parsed
* when Gloss is validated
* when Gloss semantics become observable
* how Gloss participates in planning and rendering
* where Gloss errors are detected and reported

This document does **not** define:

* Gloss syntax
* Gloss vocabulary
* Gloss semantics themselves

Those are defined in the Gloss Language Specification.

---

## 3. High-Level Lifecycle Overview

Gloss progresses through the system in **five distinct phases**:

1. Authoring
2. Compilation
3. Persistence
4. Semantic Realization
5. Planning and Rendering

Each phase has strict responsibilities and prohibitions.

---

## 4. Phase 1 — Authoring (Hard)

Gloss is authored:

* inline within free text content
* inside Codex Concepts
* never inside attributes

At authoring time:

* Gloss is **textual only**
* no validation beyond basic text well-formedness is performed
* no semantic resolution occurs

Gloss is treated as **opaque text** at this stage.

---

## 5. Phase 2 — Compilation (Hard)

During CDX → AST → IR → RDF/Turtle:

* Gloss content is preserved **verbatim**
* Gloss is **not parsed**
* Gloss is **not interpreted**
* Gloss is **not validated**

Kernel MUST:

* preserve source locations for Gloss spans as part of text location metadata
* ensure lossless round-tripping of Gloss text

Gloss MUST NOT influence:

* AST shape
* IR normalization
* RDF emission

---

## 6. Phase 3 — Persistence (Hard)

When stored in a triple store:

* Gloss remains embedded as text
* no Gloss semantics are materialized as triples
* no Gloss parsing occurs

The triple store is **Gloss-agnostic**.

---

## 7. Phase 4 — Semantic Realization (Normative)

Gloss is parsed and semantically realized during:

> **ViewModel shaping**

At this phase:

* Gloss spans are parsed into a Gloss semantic representation
* references (e.g. `#id`) are resolved against available Codex data
* nesting rules are validated
* semantic distinctions become observable inputs

This is the **earliest phase** at which Gloss meaning exists.

---

## 8. Validation and Failure Handling (Hard)

### 8.1 Invalid Gloss Syntax

* Reported as Help
* Attached to source locations
* MUST NOT throw or abort the pipeline

### 8.2 Unresolved References

* Detected during semantic realization
* Reported as Help
* Classified as semantic integrity failures
* Severity MAY be elevated by policy or target

Gloss failures MUST NOT be deferred to rendering.

---

## 9. Phase 5 — Planning and Rendering (Hard)

After semantic realization:

* Design Policy MAY consume Gloss-derived semantics
* Presentation Plans MAY branch on Gloss distinctions
* Renderers MAY map Gloss semantics to target affordances

Rendering:

* MUST NOT introduce new Gloss semantics
* MUST NOT reinterpret Gloss meaning
* MUST remain pure and deterministic

---

## 10. Round-Trip Guarantees (Hard)

Gloss MUST satisfy:

* lossless textual round-trip
* stable semantic interpretation for equivalent inputs
* preservation of author-supplied labels and spans

Gloss parsing and realization MUST NOT mutate original text.

---

## 11. Separation Guarantees (Hard)

Gloss:

* is not behavior
* is not structure
* is not presentation
* does not trigger execution
* does not affect semantic correctness

Gloss provides **semantic signals only**.

---

## 12. Authority and Change Control

This document is governed by:

* the Gloss Language Specification
* the Codex System Contract
* https://paperhat.dev/contracts/KERNEL_PIPELINE_CONTRACT/

In case of conflict, higher-authority documents prevail.

---

**End of Gloss Lifecycle Contract v0.1.1**
