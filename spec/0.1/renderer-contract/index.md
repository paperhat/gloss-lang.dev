Status: NORMATIVE
Lock State: LOCKED
Version: 0.1
Editor: Charles F. Munat

# Gloss Renderer Contract — Version 0.1

This document defines the **required interface** between a Gloss processor and any target realization system (renderer).

Gloss encodes **semantic span binding** only. This contract does not specify presentation.

---

## 1. Inputs (Normative)

A renderer consumes:

1. the original Codex `Content` source text
2. the parsed Gloss structure extracted from that text
3. the resolved Concept references (when resolution is performed)

## 2. Output Data Model (Normative)

A conforming Gloss processor MUST provide the renderer a sequence of segments.
Each segment is either:

- **Text segment**: literal text
- **Annotation segment**:
  - `addressingForm`: `@` or `~`
  - `referenceToken`: the exact token text (e.g., `book:hobbit` or `~hobbit`)
  - `label`: optional label content, represented as a sequence of nested segments (text/annotations)
  - `sourceRange`: a source location range covering the entire annotation
  - `resolution`:
    - `resolved`: boolean
    - `targetConceptId`: optional (present when resolved)

A renderer MUST treat nested label content as structured content.

## 3. Label Semantics (Normative)

- If `label` is present, it is the display text for the annotation span.
- If `label` is absent, the renderer MAY choose display text using renderer policy and Concept data.
- The label MUST NOT affect which Concept the annotation binds to.

## 4. Target-Specific Mapping (Informative)

A target realization may map Concept traits (such as `url` or `language`) to target-specific constructs.
This mapping is outside Gloss and is defined by the target adapter.

Examples in the examples directory show one plausible mapping for one target.
