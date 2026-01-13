Status: NORMATIVE  
Lock State: LOCKED  
Version: 0.1.1  
Editor: Charles F. Munat  

# Gloss System Contracts

This section contains **contracts** governing systems, libraries, and pipelines
that implement or operate on the **Gloss** language.

Contracts define **required behavior** for compliant systems.  
They do **not** define the Gloss language itself.

Unless explicitly stated otherwise, all contracts listed here are **Normative**.

---

## 1. Purpose

Gloss contracts exist to:

- define obligations and invariants for Gloss-based systems
- allocate responsibility across libraries and pipeline phases
- prevent semantic and lifecycle drift
- ensure explainable, deterministic behavior across targets

Violation of a Normative contract constitutes **non-compliance**.

---

## 2. Relationship to the Gloss Specification

- The **Gloss Language Specification** (under `/spec/`) defines the language:
  - syntax
  - addressing rules
  - semantic intent
- Contracts define how systems must:
  - preserve Gloss
  - parse Gloss
  - validate Gloss
  - realize Gloss semantics
  - interact with Design Policy and rendering

In the event of conflict:

1. The Gloss Language Specification takes precedence.
2. Contracts must conform to the specification.
3. Informative documents have no authority.

---

## 3. Relationship to Codex Contracts

Gloss is **subordinate to Codex**.

- Codex contracts define:
  - Concepts, Traits, Values, and Entities
  - schema authorization
  - semantic meaning
- Gloss contracts define:
  - when and how that meaning becomes observable inline
  - how spans bind to Codex-defined meaning
  - how errors are surfaced

A system cannot implement Gloss correctly without complying with the relevant
Codex contracts.

In case of conflict, **Codex contracts prevail**.

---

## 4. Authority and Governance

Gloss contracts are governed under the same editorial model as the Gloss
specification.

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

Lock State does not change the conflict rules in §2 or §3.

---

## 6. Contract Index

The following contracts are currently defined for Gloss:

- **[GLOSS_LIFECYCLE_CONTRACT](../spec/0.1/lifecycle/)**  
  Defines the **lifecycle, phase boundaries, and invariants** governing how Gloss
  text is preserved, parsed, validated, and realized within the Paperhat system.

- **[GLOSS_PARSING_RESPONSIBILITY_CONTRACT](./GLOSS_PARSING_RESPONSIBILITY_CONTRACT/)**  
  Defines **which system is responsible** for parsing Gloss, **when parsing
  occurs**, and **what systems must not do** with Gloss text.

- **[GLOSS_TYPED_REALIZATION_CONTRACT](./GLOSS_TYPED_REALIZATION_CONTRACT/)**  
  Defines the **typed semantic representation** produced during Gloss semantic
  realization, including invariants required for consumers.

- **[GLOSS_DESIGN_POLICY_INTERACTION_CONTRACT](./GLOSS_DESIGN_POLICY_INTERACTION_CONTRACT/)**  
  Defines the **permitted and forbidden interactions** between Gloss-derived
  semantics and **Design Policy**, including constraints on reinterpretation and
  realization.

Contract names appearing in ALL_CAPS are canonical identifiers.

---

## 7. Scope of Compliance

A system may:

- comply with all Gloss contracts
- comply with a documented subset of Gloss contracts
- intentionally diverge

A system that diverges from a contract MUST NOT claim compliance with that
contract.

Only systems that meet all applicable requirements may claim compliance with
the referenced contract(s).

---

## 8. Informative Notes

This index defines **contract authority and structure only**.

Rationale, design discussion, inventories, and scope clarification belong in
`/notes/` and are **not binding**.

---

**End of Gloss System Contracts v0.1.1**
