# Gloss–Design Policy Interaction Contract

Status: NORMATIVE
Lock State: LOCKED
Version: 0.1
Editor: Charles F. Munat

---

## 1. Purpose

This document defines the **contractual relationship** between Gloss semantics and Design Policy.

It ensures that:

* Gloss provides meaning
* Design Policy interprets appearance
* neither subsumes the other

---

## 2. Direction of Dependency (Hard)

The dependency is strictly one-way:

> **Design Policy MAY depend on Gloss semantics.
> Gloss MUST NOT depend on Design Policy.**

Gloss is defined and realized **before** Design Policy is applied.

---

## 3. What Gloss Provides

Gloss provides Design Policy with:

* inline semantic distinctions
* span boundaries
* nesting relationships
* resolved references
* semantic labels and classifications

Gloss does **not** provide:

* layout hints
* stylistic intent
* priority rules
* behavioral affordances

---

## 4. What Design Policy May Do (Normative)

Design Policy MAY:

* group content differently based on Gloss semantics
* apply emphasis or de-emphasis
* alter ordering or flow
* select alternative presentation strategies
* respond differently per target class

All such responses are **policy decisions**, not semantic reinterpretations.

---

## 5. Prohibited Uses (Hard)

Design Policy MUST NOT:

* redefine Gloss semantics
* reinterpret Gloss meaning
* infer semantics not present in Gloss
* treat Gloss as behavior triggers
* treat Gloss distinctions as correctness constraints

Gloss meaning is **authoritative**.

---

## 6. Failure Interaction (Hard)

If Gloss semantic realization produced Help values:

* Design Policy MAY respond to their presence
* Design Policy MUST NOT suppress or alter them
* Rendering MUST surface them according to system rules

Design Policy MUST NOT “repair” Gloss errors.

---

## 7. Target Variability (Normative)

Different render targets MAY:

* realize the same Gloss semantics differently
* ignore certain Gloss distinctions by policy
* degrade gracefully when affordances are unavailable

Such differences MUST NOT affect:

* Gloss validity
* Gloss meaning
* semantic integrity

---

## 8. Explainability Requirement (Hard)

Design Policy decisions based on Gloss MUST be explainable in plain language, including:

* “This span is emphasized because it is marked as X.”
* “This reference is rendered differently on this target.”

Opaque coupling is forbidden.

---

## 9. Change Control

Any change to how Design Policy may consume Gloss semantics requires updates to:

* this contract
* the Design Policy Contract
* the Gloss Lifecycle Contract (if phase boundaries change)

---

**End of Gloss–Design Policy Interaction Contract v0.1**
