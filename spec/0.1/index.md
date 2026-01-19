Status: NORMATIVE
Lock State: LOCKED
Version: 0.1
Editor: Charles F. Munat

# Gloss Language Specification — Version 0.1

## Entry Point and Table of Contents

This document is the **authoritative entry point** for the Gloss Language
Specification, version **0.1**.

It defines the **scope, structure, authority, and immutability** of the
specification and enumerates the **Normative documents** that together define
Gloss.

---

## Purpose of This Document

This document exists to:

- establish the scope of Gloss 0.1
- declare which documents are Normative
- define immutability and versioning rules
- provide a stable table of contents for implementers, auditors, and tooling

All Gloss language rules are defined in the documents listed below.

---

## Scope of Gloss 0.1

Gloss 0.1 defines:

- inline span-binding surface forms
- naming and identifier constraints for bindings
- binding semantics for Entities and non-Entity concepts
- lifecycle, parsing, and preservation requirements
- semantic realization output model
- Design Policy interaction rules
- targetable concept categories for consistent realization

Gloss 0.1 does NOT define:

- structural document modeling (owned by Codex)
- rendering, styling, layout, or navigation behavior (owned by targets/policy)
- executable behavior or evaluation semantics

---

## Normative Documents

### Core Language

- [**Syntax and Naming**](./naming/) — Surface syntax, addressing forms, vocabulary model

### Binding Semantics

- [**Entity Binding**](./entity-binding/) — Entity references, metadata emission,
  label selection
- [**Targetable Concepts**](./targetable-concepts/) — Concept vocabulary for
  Gloss-targetable annotations

### Lifecycle and Processing

- [**Lifecycle**](./lifecycle/) — Phase boundaries, parsing ownership,
  preservation guarantees
- [**Semantic Realization**](./semantic-realization/) — Typed output model,
  invariants, value kinds
- [**Design Policy Interaction**](./design-policy/) — Consumer rules, permitted
  and prohibited uses

### Formal Grammar

- [**Grammar**](./grammar/) — EBNF formal grammar for Gloss syntax

---

## Stability and Immutability

Gloss 0.1 is **immutable**.

Once published:

- documents under `/spec/0.1/` MUST NOT be edited
- clarifications or changes require a new version
- superseding versions live alongside this version

No implementation-led reinterpretation is permitted.

---

## Relationship to Other Versions

- `/spec/current/` points to the most recent published version
- draft or experimental work lives under `/spec/DRAFT/`
- implementations MUST target a specific published version

---

## Authority

This specification is maintained under the governance rules defined in
`GOVERNANCE.md`.

Final authority over Gloss 0.1 rests with the **Specification Editor**.

---

**End of Gloss Language Specification v0.1 — Entry Point**
