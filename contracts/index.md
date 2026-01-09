Status: NORMATIVE  
Lock State: LOCKED  
Version: 0.1  
Editor: Charles F. Munat  

# Gloss System Contracts

This section contains **contracts** governing systems, libraries, and pipelines
that implement or operate on the **Gloss inline semantic annotation language**.

Contracts define **required behavior** for compliant systems.  
They do **not** define the Gloss language itself.

Unless explicitly stated otherwise, all contracts listed here are **Normative**.

---

## 1. Purpose

Gloss contracts exist to:

- define obligations and invariants for Gloss-aware systems
- allocate responsibility across parsing, realization, policy, and rendering
- prevent semantic drift between implementations
- preserve Gloss’s core guarantees:
  - opacity outside semantic realization
  - strict separation of meaning and presentation
  - explainability and round-trip integrity

Violation of a Normative contract constitutes **non-compliance**.

---

## 2. Relationship to the Gloss Specification

- The **Gloss Language Specification** (under `/spec/`) defines the language:
  - syntax
  - addressing semantics
  - lifecycle
  - naming rules
- Contracts define how systems must:
  - parse
  - resolve
  - type
  - interpret
  - plan
  - render
  Gloss annotations.

In the event of conflict:

1. The Gloss Language Specification takes precedence.
2. Contracts must conform to the specification.
3. Informative documents have no authority.

---

## 3. Relationship to Codex

Gloss is **subordinate to Codex** and cannot be used independently.

- Codex defines:
  - Concepts
  - Traits
  - Values
  - Entities
- Gloss binds spans of free text to those definitions.
- Gloss contracts assume Codex compliance as a prerequisite.

Contracts in this section govern **Gloss-specific behavior only** and do not
override Codex system contracts.

---

## 4. Authority and Governance

Gloss contracts are maintained under the same strong editorial governance model
as the Gloss specification.

- Contracts are public.
- Contracts are open to review.
- Contracts are not crowd-designed.

Final authority over Normative contracts rests with the
**Specification Editor**.

---

## 5. Status and Lock State

Every contract MUST declare:

- **Status**: `DRAFT`, `NORMATIVE`, or `INFORMATIVE`
- **Version**: a monotonic version identifier

A contract MAY additionally declare:

- **Lock State**: `LOCKED`

### 5.1 Meaning of LOCKED

If a contract declares `Lock State: LOCKED`, then:

- its requirements are considered stable
- changes MUST be introduced only by publishing a new version
- editorial clarification MAY be published only as an Informative note
  (never by modifying the locked contract text)

Lock State does not change the conflict rules in §2.

---

## 6. Versioning and Stability

- Each contract is versioned independently.
- Once a contract version is published, it is **immutable**.
- New requirements result in a new version, not modification of an existing one.

Contracts may evolve at different rates.

---

## 7. Contract Index

The following Gloss contracts are currently defined:

- **[GLOSS_PARSING_RESPONSIBILITY_CONTRACT](./GLOSS_PARSING_RESPONSIBILITY_CONTRACT/)**  
  Defines **where, when, and by whom Gloss is parsed**, and enforces the rule that
  Gloss remains opaque until semantic realization.

- **[GLOSS_DESIGN_POLICY_INTERACTION_CONTRACT](./GLOSS_DESIGN_POLICY_INTERACTION_CONTRACT/)**  
  Defines the **exclusive responsibilities and limits** of Design Policy when
  consuming Gloss semantics, including prohibitions on reinterpretation.

- **[GLOSS_TOOLSMITH_TYPED_REALIZATION_CONTRACT](./GLOSS_TOOLSMITH_TYPED_REALIZATION_CONTRACT/)**  
  Defines how **Gloss semantic realization produces a typed representation**
  using Toolsmith newtypes, while preserving no-normalization, explainability,
  and round-trip guarantees.

Additional contracts may be added as the Gloss ecosystem expands.

Contract names appearing in ALL_CAPS are canonical identifiers.

---

## 8. Scope of Compliance

A system may:

- comply with all Gloss contracts
- comply with a documented subset of Gloss contracts
- intentionally diverge

A system that diverges from a contract MUST NOT claim compliance with that
contract.

Only systems that meet all applicable requirements may claim compliance with
the referenced contract(s).

---

## 9. Informative Notes

This index defines contract authority and structure only.

Rationale, comparisons, and design discussion belong in `/notes/` and are
**not binding**.
