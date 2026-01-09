# Gloss vs Codex Contract Scope

This document clarifies the **scope boundary** between **Codex system contracts**
and **Gloss system contracts**, and explains how they relate without overlap or
conflict.

This document is **informative**, not normative.

---

## 1. The Core Distinction

**Codex contracts** govern:

> The definition, validity, identity, structure, and persistence of meaning.

**Gloss contracts** govern:

> How *existing meaning* is referenced, bound to text spans, and realized
> without altering that meaning.

Gloss does **not** define meaning.  
Codex does **not** define inline span binding.

They solve different problems at different layers.

---

## 2. What Codex Contracts Are Responsible For

Codex system contracts define and constrain:

- the Codex language itself
- Concepts, Traits, and Values
- Entity eligibility and identity
- naming and value rules
- schema authorization
- CDX → AST → IR boundaries
- persistence and provenance
- orchestration across the Paperhat system

Codex answers questions such as:

- “What does this Concept mean?”
- “Is this a valid Entity?”
- “What value does this carry?”
- “How is this represented canonically?”

Codex contracts are **authoritative** over meaning.

---

## 3. What Gloss Contracts Are Responsible For

Gloss system contracts define and constrain:

- when Gloss syntax is parsed
- how `@` and `#` references are resolved
- how semantic realization occurs
- how typed semantic representations are produced
- how Design Policy may consume Gloss semantics
- how explainability and Help are enforced

Gloss answers questions such as:

- “What does this span of text refer to?”
- “Is this reference an Entity or not?”
- “When does this meaning become observable?”
- “How is this span typed for safe downstream use?”

Gloss contracts are **procedural**, not semantic.

---

## 4. Subordination and Dependency

Gloss is **subordinate to Codex**.

- Gloss references Codex-defined Concepts and Entities.
- Gloss has no independent vocabulary.
- Gloss has no independent value system.
- Gloss has no independent lifecycle outside Codex/Scribe.

A system **cannot** implement Gloss correctly without implementing Codex first.

Codex contracts are therefore a **prerequisite dependency** for Gloss contracts.

---

## 5. No Overlap, No Substitution

Gloss contracts:

- MUST NOT redefine Codex semantics
- MUST NOT reinterpret values
- MUST NOT normalize, compute, or evaluate
- MUST NOT introduce new meaning

Codex contracts:

- DO NOT define inline span semantics
- DO NOT define author-facing annotation syntax
- DO NOT define presentation or realization behavior

Each contract set is deliberately incomplete on its own.

---

## 6. Architectural Analogy (Informal)

A useful mental model:

- **Codex** is the semantic substrate
- **Gloss** is the inline semantic pointer layer
- **Design Policy** is the realization decision layer
- **Renderers** are execution targets

Trying to use Gloss without Codex is like using pointers without memory.

---

## 7. Why This Separation Matters

This separation:

- prevents semantic drift
- enables multiple render targets
- preserves round-trip integrity
- keeps Gloss small and stable
- allows Codex to evolve independently
- prevents “HTML-style” collapse of concerns

It is a deliberate architectural constraint, not an accident.

---

## 8. Summary

- Codex contracts define **what meaning is**
- Gloss contracts define **how meaning is referenced in text**
- Gloss is dependent, subordinate, and non-authoritative
- Neither replaces the other
- Together, they form a coherent semantic authoring system

---

**End of Gloss vs Codex Contract Scope (Informative)**
