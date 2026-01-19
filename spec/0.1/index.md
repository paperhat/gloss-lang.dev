Status: NORMATIVE
Lock State: UNLOCKED
Version: 0.1
Editor: Charles F. Munat

# Gloss Language Specification — Version 0.1

Gloss is an **inline semantic span-binding language** embedded inside Codex `Content`.
It binds spans of opaque text to Codex Concepts without encoding presentation or behavior.

## 1. Scope and Relationship to Codex (Normative)

1. Gloss annotations MAY appear only inside Codex `Content` values.
2. Codex tooling treats `Content` as opaque text; Codex does not parse Gloss.
3. Gloss is parsed and resolved by consuming systems (e.g., target realization / rendering pipelines).
4. Gloss MUST NOT be used inside:

	- Codex identifiers
	- Codex Trait values
	- schema definitions

## 2. Design Intent (Normative)

Gloss encodes semantic binding only.

Gloss MUST NOT:

- define layout, typography, or styling
- define behavior, evaluation, or execution
- introduce new Concepts, Traits, or data

Targets (HTML, PDF, audio, braille, data export) MAY realize the same semantics differently.

## 3. Specification Contents

This specification is organized as a set of focused documents.

- Surface form: [gloss-lang.dev/spec/0.1/surface-form/index.md](surface-form/index.md)
- Parsing model (including nesting): [gloss-lang.dev/spec/0.1/parsing-model/index.md](parsing-model/index.md)
- Resolution semantics: [gloss-lang.dev/spec/0.1/resolution/index.md](resolution/index.md)
- Formatting and canonicalization: [gloss-lang.dev/spec/0.1/formatting-and-canonicalization/index.md](formatting-and-canonicalization/index.md)
- Validation errors and recovery: [gloss-lang.dev/spec/0.1/validation-errors/index.md](validation-errors/index.md)

## 4. Related Documents

- Formal grammars (EBNF and PEG): [gloss-lang.dev/spec/0.1/grammar/index.md](grammar/index.md)
- Examples (informative): [gloss-lang.dev/examples/0.1/index.md](../../examples/0.1/index.md)


