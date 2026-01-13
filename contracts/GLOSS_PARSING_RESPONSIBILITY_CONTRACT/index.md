# Gloss Parsing Responsibility Contract

Status: NORMATIVE
Lock State: LOCKED
Version: 0.1
Editor: Charles F. Munat

---

## 1. Purpose

This document defines **ownership, boundaries, and guarantees** for parsing and semantic realization of the Gloss language within the Paperhat system.

Its purpose is to ensure that Gloss parsing is:

* deterministic
* phase-correct
* centrally governed
* consistent across targets
* free from semantic drift

---

## 2. Ownership (Hard)

**Kernel exclusively owns Gloss parsing and semantic realization.**

No other library may:

* parse Gloss syntax
* interpret Gloss annotations
* resolve Gloss references
* define alternative Gloss semantics
* re-parse Gloss text at render time

Renderers, Design Policy, and behaviors are **consumers only**.

---

## 3. Location in the Pipeline (Hard)

Gloss parsing occurs **only** during:

> **ViewModel shaping**

Gloss MUST NOT be parsed during:

* CDX compilation
* IR normalization
* RDF/Turtle emission
* triple-store persistence
* SPARQL querying
* rendering

This establishes a single, authoritative semantic boundary.

---

## 4. Parsing Inputs

The Gloss parser receives:

* free-text content strings
* source-location metadata
* access to Codex-defined data required for reference resolution

The parser MUST NOT require:

* render-target knowledge
* Design Policy knowledge
* behavior configuration
* runtime IO

Parsing is a **pure function**.

---

## 5. Parsing Outputs

The Gloss parser produces a **Gloss Semantic Representation** that:

* preserves original text verbatim
* records span boundaries
* records nesting structure
* records semantic labels
* records resolved references (or failure Helps)

This representation is:

* deterministic
* serializable
* independent of render targets

---

## 6. Error and Help Handling (Hard)

Gloss parsing MUST:

* never throw
* never return `null` or `undefined`
* always return semantic output + Help values

Failures include (non-exhaustive):

* malformed Gloss syntax
* unbalanced delimiters
* invalid nesting
* unresolved references

All failures:

* are reported as Help
* are source-location aware
* do not abort the pipeline

---

## 7. Stability Guarantees (Hard)

For equivalent Gloss inputs, the parser MUST produce:

* identical semantic representations
* identical Help outputs (modulo location metadata)

Parser behavior MUST NOT vary by:

* render target
* execution mode
* Design Policy
* runtime environment

---

## 8. Change Control

Any change to:

* parsing rules
* error classification
* semantic representation

constitutes a **Gloss language change** and MUST follow Gloss spec change control.

---

**End of Gloss Parsing Responsibility Contract v0.1**
