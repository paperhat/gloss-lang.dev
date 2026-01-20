Status: INFORMATIVE
Version: 0.1

# Gloss 0.1 Conformance Fixtures

This directory contains **versioned conformance fixtures** for Gloss Language Specification v0.1.

These fixtures are intentionally stored **outside** `spec/0.1/` so the spec tree can remain stable/lockable.

## Goals

- Provide a shared corpus of **valid** and **invalid** Gloss-annotated text inputs.
- Provide expected **canonical output** for inputs that are valid and already in canonical form.
- Provide expected **primary error class** for invalid inputs.

## Scope

This fixture pack focuses on **parsing + surface-form validation + canonical spelling**.

It does not attempt to test resolution (`@`/`~` binding) because resolution requires an external Concept model.

## Layout

- `manifest.cdx` — the Codex-native index of cases.
- `cases/valid/*.cdx` — Codex documents whose Content contains Gloss.
- `cases/invalid/*.cdx` — Codex documents whose Content contains Gloss and is expected to fail.
- `expected/canonical/*.cdx` — expected canonical form for some valid inputs.
- `expected/errors/*.cdx` — expected error classification for invalid inputs.

## Running the smoke check

From the repo root:

```bash
python3 gloss-lang.dev/tools/conformance_smokecheck_cdx.py gloss-lang.dev/conformance/0.1/manifest.cdx
```

## Running the "no JSON" gate

From the repo root:

```bash
python3 gloss-lang.dev/tools/no_json_gate.py
```

## Running the spec header gate

From the repo root:

```bash
python3 gloss-lang.dev/tools/spec_header_check.py gloss-lang.dev/spec/0.1
```

## Running the spec link gate

From the repo root:

```bash
python3 gloss-lang.dev/tools/spec_link_check.py gloss-lang.dev/spec/0.1
```

## Spec references

- Surface form: `gloss-lang.dev/spec/0.1/surface-form/`
- Parsing model: `gloss-lang.dev/spec/0.1/parsing-model/`
- Formatting and canonicalization: `gloss-lang.dev/spec/0.1/formatting-and-canonicalization/`
- Validation errors: `gloss-lang.dev/spec/0.1/validation-errors/`
