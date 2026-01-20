Status: NORMATIVE
Lock State: LOCKED
Version: 0.1
Editor: Charles F. Munat

# Gloss Resolution Specification — Version 0.1

This document defines how Gloss annotations bind to Codex Concepts.

Gloss resolution is performed by consuming systems against the Concept model available at runtime.
Gloss does not define how that model is loaded.

## 1. Resolution Inputs (Normative)

A parsed annotation yields:

- a reference: `@iri` or `~token`
- an optional label (which affects display text only)

## 2. `@` Resolution (Normative)

`@iri` MUST resolve by finding exactly one Concept whose `id` matches `iri`.

- If zero matches are found: resolution error (unresolved identifier)
- If multiple matches are found: resolution error (ambiguous identifier)

## 3. `~` Resolution (Normative)

`~token` MUST resolve by finding exactly one Concept whose `key` matches `~token`.

- If zero matches are found: resolution error (unresolved lookup token)
- If multiple matches are found: resolution error (ambiguous lookup token)

Resolution is performed by consuming systems, not by Codex itself.

## 4. Label Interaction (Normative)

The presence or content of a label MUST NOT affect resolution.
