Status: NORMATIVE
Lock State: LOCKED
Version: 0.1
Editor: Charles F. Munat

# Gloss Targetable Concepts

This document defines the **Gloss-targetable Concept vocabulary** for Gloss v0.1.

Targetable Concepts are **Codex Concepts** that MAY be referenced from inline Gloss markup using:

- `{#id}`
- `{#id | label}`

These Concepts are:

* inline-renderable
* target-independent
* resolved during Gloss semantic realization
* consumed by Design Policy and renderers

Gloss syntax does not vary by Concept.

---

## 1. Concept Classes

Targetable Concepts fall into three classes:

1. **Temporal Concepts** — represent time-related meaning
2. **Semantic Inline Concepts** — represent meaning expressed in text
3. **Presentation Concepts** — express inline typographic intent

Gloss does not distinguish classes syntactically.

---

## 2. Temporal Concepts

### 2.1 `<PlainDate>`

**Meaning:** Calendar date, no time, no zone.

**Required traits**
- `id`
- `value` — ISO date (`YYYY-MM-DD`) or `{today}`

**Optional traits**
- `format`
- `calendar`

---

### 2.2 `<PlainTime>`

**Meaning:** Wall-clock time, no date, no zone.

**Required traits**
- `id`
- `value` — ISO time or `{now}`

**Optional traits**
- `format`
- `calendar`

---

### 2.3 `<PlainDateTime>`

**Meaning:** Date + time, no zone.

**Required traits**
- `id`
- `value` — ISO local datetime or `{now}`

**Optional traits**
- `format`
- `calendar`

---

### 2.4 `<ZonedDateTime>`

**Meaning:** Date + time + time zone.

**Required traits**
- `id`
- `value` — ISO zoned datetime or `{now}`
- `zone` — IANA zone identifier

**Optional traits**
- `format`
- `calendar`

---

### 2.5 `<Instant>`

**Meaning:** Absolute moment on the timeline.

**Required traits**
- `id`
- `value` — ISO instant or `{now}`

**Optional traits**
- `format`

---

### 2.6 `<PlainYearMonth>`

**Meaning:** Year + month, no day.

**Required traits**
- `id`
- `value` — ISO year-month (`YYYY-MM`)

**Optional traits**
- `format`
- `calendar`

---

### 2.7 `<PlainMonthDay>`

**Meaning:** Month + day, no year.

**Required traits**
- `id`
- `value` — ISO month-day (`--MM-DD`)

**Optional traits**
- `format`
- `calendar`

---

### 2.8 `<PlainWeekYear>`

**Meaning:** ISO week-date (`YYYY-Www`), aligns with HTML `input type="week"`.

**Required traits**
- `id`
- `value`

**Optional traits**
- `format`

---

### 2.9 `<Duration>`

**Meaning:** Length of time.

**Required traits**
- `id`
- `value` — ISO 8601 duration (e.g. `{PT3M15S}`)

**Optional traits**
- `format`

---

## 3. Semantic Inline Concepts

### 3.1 `<Stress>`

**Meaning:** Prosodic or semantic emphasis.

---

### 3.2 `<Important>`

**Meaning:** Increased semantic importance.

---

### 3.3 `<Highlight>`

**Meaning:** Attention-drawing emphasis without semantic weight.

---

### 3.4 `<Cite>`

**Meaning:** Reference to a cited work.

---

### 3.5 `<Quotation>`

**Meaning:** Quoted text.

**Optional traits**
- source metadata (schema-defined)

---

### 3.6 `<Abbreviation>`

**Meaning:** Abbreviation read as its expansion (e.g. “etc.” → “et cetera”).

---

### 3.7 `<Initialism>`

**Meaning:** Abbreviation read letter-by-letter (e.g. “CIA”).

---

### 3.8 `<Acronym>`

**Meaning:** Abbreviation read as a word (e.g. “ComSubPac”).

**Hierarchy:**
`Abbreviation` ⊃ `Initialism` ⊃ `Acronym`

---

### 3.9 `<Variable>`

**Meaning:** Variable or placeholder symbol.

**Optional traits**
- `type`
- `mutable`

---

### 3.10 `<Input>`

**Meaning:** User input (conceptual).

---

### 3.11 `<Output>`

**Meaning:** System or program output.

---

### 3.12 `<Code>`

**Meaning:** Inline code fragment.

**Optional traits**
- `language`
- `version`

---

### 3.13 `<Data>`

**Meaning:** Machine-relevant data value embedded in text.

---

### 3.14 `<Ruby>`

**Meaning:** Ruby annotation (base text + annotation).

---

### 3.15 `<Delete>`

**Meaning:** Deleted content.

---

### 3.16 `<Insert>`

**Meaning:** Inserted content.

---

### 3.17 `<Isolate>`

**Meaning:** Bidirectional text isolation.

Equivalent to Unicode bidi isolation / HTML `<bdi>`.

---

### 3.18 `<OverrideDirection>`

**Meaning:** Explicit bidirectional override.

**Required traits**
- `dir` — `ltr` | `rtl`

Equivalent to HTML `<bdo>`.

---

## 4. Presentation Concepts

### 4.1 `<TextStyle>`

**Meaning:** Inline typographic intent.

**Required traits**
- `id`
- `effects` — list of effects

**Allowed effects (closed set v0.1):**
- `bold`
- `italic`
- `smallCaps`
- `subscript`
- `superscript`
- `underline`
- `overline`
- `strikethrough`

**Optional traits**
- `fontFamily` — semantic family (`serif`, `sansSerif`, `monospace`, `cursive`, `system`)

`TextStyle` expresses intent only. Realization is target-dependent.

---

## 5. Media Concepts

### 5.1 `<Image>`

**Meaning:** Inline image or graphic.

Rendering MAY use responsive mechanisms per target.

---

### 5.2 `<Video>`

**Meaning:** Inline or embedded video media.

---

### 5.3 `<Audio>`

**Meaning:** Inline or embedded audio media.

---

### 5.4 `<Canvas>`

**Meaning:** Embedded dynamic or interactive visual surface.

---

## 6. Shared Rules (Hard)

* All targetable Concepts:
  * MUST have an `id`
  * MUST be referencable via Gloss
* Gloss syntax is invariant across Concepts
* Meaning is defined by the Concept, not by Gloss
* Presentation decisions are deferred to Design Policy and renderers

---

## 7. Explicit Non-Goals (v0.1)

This document does not define:

* ranges or intervals
* recurrence rules
* business calendars
* locale policy
* HTML-specific mappings
* widget behavior

---

**End of Gloss Targetable Concepts v0.1**
