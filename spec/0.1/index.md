Status: NORMATIVE  
Version: 0.1  
Editor: Charles F. Munat

# Gloss Language Specification — Version 0.1  
## Entry Point and Table of Contents

This document is the **authoritative entry point** for the Gloss Language Specification, version **0.1**.

It defines the **scope, structure, authority, and immutability** of the specification and enumerates the **Normative documents** that together define Gloss.

This document does **not** itself define parsing rules beyond the included normative documents.

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
- lifecycle and preservation requirements for annotated text
- targetable concept categories intended for consistent realization

Gloss 0.1 does **not** define:

- structural document modeling (owned by Codex)
- rendering, styling, layout, or navigation behavior (owned by targets/policy)
- executable behavior or evaluation semantics

---

## Included Normative Documents

### Core Binding Semantics

- [**Entity Binding**](./entity-binding/)
- [**Targetable Concepts**](./targetable-concepts/)

### Surface Rules

- [**Naming**](./naming/)

### Lifecycle and Preservation

- [**Lifecycle**](./lifecycle/)

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

This specification is maintained under the governance rules defined in `GOVERNANCE.md`.

Final authority over Gloss 0.1 rests with the **Specification Editor**.

---

End of Gloss Language Specification v0.1 — Entry Point
