Status: NORMATIVE
Lock State: LOCKED
Version: 0.1
Editor: Charles F. Munat

# Gloss Targetable Concepts

This document defines the **Gloss-targetable Concept vocabulary** for Gloss v0.1.

Targetable Concepts are **non-Entity Codex Concepts** that authors reference
from inline Gloss markup using the `#` addressing form:

- `{#id}`
- `{#id | label}`

These Concepts are:

- inline-renderable
- target-independent
- resolved during Gloss semantic realization
- consumed by Design Policy and renderers

Gloss syntax does not vary by Concept.

**Note:** Entities use `@` or `~` addressing, not `#`. See the Entity Binding
specification for Entity reference semantics.

---

## 1. Concept Classes

Targetable Concepts fall into four classes:

1. **Temporal Concepts** — represent time-related meaning
2. **Semantic Inline Concepts** — represent meaning expressed in text
3. **Presentation Concepts** — express inline typographic intent
4. **Media Concepts** — represent embedded media references

Gloss does not distinguish classes syntactically.

---

## 2. General Rules (Normative)

All targetable Concepts:

- MUST be non-Entities
- MUST be referenced using `#` in Gloss
- MUST declare an `id`
- MUST be schema-authorized by Architect
- MUST preserve authorial intent
- MAY be ignored or variably realized by targets

Gloss binds meaning only; realization is deferred to Design Policy and renderers.

---

## 3. Temporal Concepts

Temporal Concepts represent time-related meaning with machine-readable precision.

### 3.1 `<PlainDate>`

**Meaning:** Calendar date, no time, no zone.

**Required traits:**

- `id`
- `value` — ISO date (`YYYY-MM-DD`) or `{today}`

**Optional traits:**

- `format`
- `calendar`

---

### 3.2 `<PlainTime>`

**Meaning:** Wall-clock time, no date, no zone.

**Required traits:**

- `id`
- `value` — ISO time or `{now}`

**Optional traits:**

- `format`
- `calendar`

---

### 3.3 `<PlainDateTime>`

**Meaning:** Date + time, no zone.

**Required traits:**

- `id`
- `value` — ISO local datetime or `{now}`

**Optional traits:**

- `format`
- `calendar`

---

### 3.4 `<ZonedDateTime>`

**Meaning:** Date + time + time zone.

**Required traits:**

- `id`
- `value` — ISO zoned datetime or `{now}`
- `zone` — IANA zone identifier

**Optional traits:**

- `format`
- `calendar`

---

### 3.5 `<Instant>`

**Meaning:** Absolute moment on the timeline.

**Required traits:**

- `id`
- `value` — ISO instant or `{now}`

**Optional traits:**

- `format`

---

### 3.6 `<PlainYearMonth>`

**Meaning:** Year + month, no day.

**Required traits:**

- `id`
- `value` — ISO year-month (`YYYY-MM`)

**Optional traits:**

- `format`
- `calendar`

---

### 3.7 `<PlainMonthDay>`

**Meaning:** Month + day, no year.

**Required traits:**

- `id`
- `value` — ISO month-day (`--MM-DD`)

**Optional traits:**

- `format`
- `calendar`

---

### 3.8 `<PlainWeekYear>`

**Meaning:** ISO week-date (`YYYY-Www`), aligns with HTML `input type="week"`.

**Required traits:**

- `id`
- `value`

**Optional traits:**

- `format`

---

### 3.9 `<Duration>`

**Meaning:** Length of time.

**Required traits:**

- `id`
- `value` — ISO 8601 duration (e.g. `PT3M15S`)

**Optional traits:**

- `format`

---

## 4. Numeric and Measurement Concepts

Numeric Concepts represent machine-readable numeric values with preserved precision.

### 4.1 `<Integer>`

**Meaning:** Integer numeric value.

**Required traits:**

- `id`
- `value` — integer literal

---

### 4.2 `<Decimal>`

**Meaning:** Decimal or scientific numeric value without explicit precision.

**Required traits:**

- `id`
- `value` — decimal or scientific literal

---

### 4.3 `<PrecisionNumber>`

**Meaning:** Numeric value with explicit or inferred precision.

Precision is significant. Kernel MUST preserve it.

**Required traits:**

- `id`
- `value` — precision number literal (`…p` or `…pN`)

Example:

```cdx
<PrecisionNumber id=pi value=3.141592653589793p15 />
```

---

### 4.4 `<Fraction>`

**Meaning:** Rational number expressed as a fraction.

**Required traits:**

- `id`
- `value` — fraction literal (`numerator/denominator`)

---

### 4.5 `<Imaginary>`

**Meaning:** Imaginary numeric value.

**Required traits:**

- `id`
- `value` — imaginary literal (`…i`)

---

### 4.6 `<Range>`

**Meaning:** Inclusive numeric interval.

Ranges are declarative. Kernel does NOT expand or evaluate them.

**Required traits:**

- `id`
- `value` — range literal (`start..end` or `start..end s step`)

---

### 4.7 `<Quantity>`

**Meaning:** Numeric value with associated unit.

**Required traits:**

- `id`
- `value` — numeric literal

**Optional traits:**

- `unit` — schema-defined unit identifier

---

## 5. Color Concepts

Color Concepts represent machine-readable color values with preserved color space.

Rules:

- Codex and Gloss perform no implicit conversion
- Renderers MAY convert colors as needed, but MUST preserve intent
- Renderers MUST keep the original color space available for explainability

### 5.1 `<HexColor>`

**Meaning:** Color in hexadecimal RGB notation.

**Required traits:**

- `id`
- `value` — hex color literal (`#RRGGBB` or `#RRGGBBAA`)

---

### 5.2 `<RgbColor>`

**Meaning:** Color in RGB color space.

**Required traits:**

- `id`
- `value` — list `[red, green, blue]`

---

### 5.3 `<HslColor>`

**Meaning:** Color in HSL color space.

**Required traits:**

- `id`
- `value` — list `[hue, saturation, lightness]`

---

### 5.4 `<OklchColor>`

**Meaning:** Color in OKLCH color space (perceptually uniform).

**Required traits:**

- `id`
- `value` — list `[lightness, chroma, hue]`

---

### 5.5 `<DisplayP3Color>`

**Meaning:** Color in Display P3 color space.

**Required traits:**

- `id`
- `value` — list `[red, green, blue]`

---

## 6. Semantic Inline Concepts

Semantic Inline Concepts express meaning or intent applied to spans of text.
They are non-structural, non-behavioral, and target-independent.

### 6.1 Emphasis and Importance

#### `<Stress>`

**Meaning:** Prosodic or semantic emphasis.

#### `<Important>`

**Meaning:** Increased semantic importance.

#### `<Highlight>`

**Meaning:** Attention-drawing emphasis without semantic weight.

---

### 6.2 Quotations and Citations

#### `<Quotation>`

**Meaning:** Quoted text.

**Optional traits:**

- `source` — schema-defined source metadata

#### `<Cite>`

**Meaning:** Reference to a cited work.

#### `<Paraphrase>`

**Meaning:** Paraphrased content from another source.

#### `<PullQuote>`

**Meaning:** Extracted quote for emphasis (editorial).

#### `<Epigraph>`

**Meaning:** Introductory quotation at the start of a section.

---

### 6.3 Abbreviations

The following hierarchy applies:

> `Abbreviation` ⊃ `Initialism` ⊃ `Acronym`

An **Abbreviation** is any shortened form of a word or phrase. An **Initialism**
is an abbreviation formed from the initial letters of words in a phrase. An
**Acronym** is an initialism designed to be pronounceable as a word, sometimes
incorporating letters beyond strict initials.

#### `<Abbreviation>`

**Meaning:** Shortened form of a word or phrase (e.g. "etc." for "et cetera").

#### `<Initialism>`

**Meaning:** Abbreviation formed from initial letters (e.g. "FBI", "CIA", "NASA").

#### `<Acronym>`

**Meaning:** Initialism designed to be pronounceable as a word (e.g. "RADAR",
"COMSUBPAC", "MADD").

#### `<Contraction>`

**Meaning:** Shortened form created by omitting letters (e.g. "don't").

---

### 6.4 Code and Technical

#### `<Code>`

**Meaning:** Inline code fragment.

**Optional traits:**

- `language`
- `version`

#### `<Variable>`

**Meaning:** Variable or placeholder symbol.

**Optional traits:**

- `type`
- `mutable`

#### `<Constant>`

**Meaning:** Named constant value.

#### `<KeyboardInput>`

**Meaning:** User keyboard input.

#### `<ProgramOutput>`

**Meaning:** Output produced by a program or system.

#### `<InlineMath>`

**Meaning:** Inline mathematical expression.

Kernel MUST NOT evaluate expressions.

#### `<Formula>`

**Meaning:** Mathematical or scientific formula.

#### `<Equation>`

**Meaning:** Mathematical equation.

#### `<Data>`

**Meaning:** Machine-relevant data value embedded in text.

---

### 6.5 Editorial and Change-Tracking

#### `<Insert>`

**Meaning:** Inserted content.

#### `<Delete>`

**Meaning:** Deleted content.

#### `<Redacted>`

**Meaning:** Intentionally withheld or obscured content.

Redaction is semantic and distinct from deletion.

---

### 6.6 Linguistic

#### `<ForeignTerm>`

**Meaning:** Term from a foreign language.

#### `<Loanword>`

**Meaning:** Foreign word adopted into the current language.

#### `<TransliteratedTerm>`

**Meaning:** Term transliterated from another script.

#### `<Neologism>`

**Meaning:** Newly coined term.

#### `<Jargon>`

**Meaning:** Specialized terminology.

#### `<WordAsWord>`

**Meaning:** A word being discussed as a word itself.

#### `<LetterAsLetter>`

**Meaning:** A letter being discussed as a letter.

#### `<MentionedTerm>`

**Meaning:** A term being mentioned rather than used.

#### `<PhoneticTranscription>`

**Meaning:** Phonetic representation of pronunciation.

---

### 6.7 Bidirectional Text

#### `<Isolate>`

**Meaning:** Bidirectional text isolation.

Equivalent to Unicode bidi isolation / HTML `<bdi>`.

#### `<OverrideDirection>`

**Meaning:** Explicit bidirectional override.

**Required traits:**

- `dir` — `ltr` | `rtl`

Equivalent to HTML `<bdo>`.

---

### 6.8 Ruby Annotations

#### `<Ruby>`

**Meaning:** Ruby annotation pairing base text with annotation text.

Ruby annotations provide pronunciation guides, typically in East Asian
typography.

**Required traits:**

- `base` — the base text being annotated
- `annotation` — the ruby text (e.g. furigana)

**Optional traits:**

- `position` — `above` | `below` (default: `above`)

---

### 6.9 References and Indexing

#### `<Reference>`

**Meaning:** General reference to another source.

#### `<CrossReference>`

**Meaning:** Reference to another location in the same document.

#### `<LegalReference>`

**Meaning:** Citation of a legal source.

#### `<Footnoted>`

**Meaning:** Content associated with a footnote.

#### `<GlossaryTerm>`

**Meaning:** Term that appears in a glossary.

#### `<Synonym>`

**Meaning:** Term that is a synonym of another.

#### `<Indexed>`

**Meaning:** Term that participates in indexing.

#### `<TitleOfWork>`

**Meaning:** Title of a creative work.

---

## 7. Narrative and Rhetorical Concepts

These Concepts express how text is narrated, framed, or perceived.

#### `<Narration>`

**Meaning:** Narrative voice or description.

#### `<Dialogue>`

**Meaning:** Spoken dialogue.

#### `<InternalDialogue>`

**Meaning:** Character's internal speech or thoughts.

#### `<InternalMonologue>`

**Meaning:** Extended internal speech.

#### `<VoiceOver>`

**Meaning:** Narration over action (as in film).

#### `<AlternativeVoice>`

**Meaning:** Voice distinct from the primary narrator.

#### `<PointOfView>`

**Meaning:** Narrative perspective marker.

#### `<DreamSequence>`

**Meaning:** Content occurring in a dream state.

#### `<Flashback>`

**Meaning:** Content depicting past events.

#### `<Foreshadowing>`

**Meaning:** Content hinting at future events.

#### `<Exposition>`

**Meaning:** Explanatory or background content.

#### `<Anecdote>`

**Meaning:** Brief illustrative story.

#### `<Backstory>`

**Meaning:** Background history.

#### `<SceneSetting>`

**Meaning:** Description establishing setting.

#### `<Symbolism>`

**Meaning:** Content with symbolic significance.

#### `<Metafiction>`

**Meaning:** Self-referential narrative content.

#### `<StageDirection>`

**Meaning:** Theatrical direction (as in scripts).

#### `<CharacterThoughts>`

**Meaning:** Representation of character's thoughts.

---

## 8. Affective and Cognitive State Concepts

These Concepts express emotional, cognitive, or mental state applied to text
spans.

### 8.1 Discrete State Concepts

Discrete State Concepts carry meaning by name alone, with no required traits
beyond `id`.

Examples (schema-defined):

- `<Sad>`
- `<Angry>`
- `<Joyful>`
- `<Dream>`

These are preferred when nuance is not required.

### 8.2 Structured State Concepts

When additional precision is required, structured Concepts with qualifying
traits MAY be used.

#### `<Emotion>`

**Meaning:** Emotional state.

**Optional traits:**

- `kind` — schema-defined emotion category
- `intensity` — numeric value (range schema-defined)
- `valence` — positive/negative axis
- `arousal` — activation axis

#### `<Tone>`

**Meaning:** Delivery or manner of expression.

**Optional traits:**

- `kind` — e.g. whisper, shout, flat, sarcastic
- `intensity`

#### `<MentalState>`

**Meaning:** Internal cognitive or perceptual condition.

**Optional traits:**

- `kind` — e.g. dreaming, dissociating, remembering
- `awareness`
- `reliability`

#### `<NarrativeMode>`

**Meaning:** Narrative framing or perspective.

**Optional traits:**

- `kind` — e.g. internalDialogue, unreliableNarration, aside

---

## 9. Cultural and Historical Concepts

### 9.1 Cultural Semantics

#### `<Colloquialism>`

**Meaning:** Informal expression.

#### `<Slang>`

**Meaning:** Very informal or nonstandard vocabulary.

#### `<IdiomaticPhrase>`

**Meaning:** Expression with non-literal meaning.

#### `<Proverb>`

**Meaning:** Traditional saying.

#### `<Archaism>`

**Meaning:** Outdated word or expression.

#### `<Dialect>`

**Meaning:** Regional or social language variety.

#### `<FigurativeLanguage>`

**Meaning:** Non-literal expression (metaphor, simile, etc.).

#### `<Anachronism>`

**Meaning:** Element out of its proper time period.

#### `<MythologicalReference>`

**Meaning:** Reference to mythology.

#### `<Tradition>`

**Meaning:** Traditional practice or custom.

#### `<Holiday>`

**Meaning:** Named holiday or celebration.

#### `<VesselName>`

**Meaning:** Name of a ship or vessel.

### 9.2 Historical Semantics

#### `<HistoricalTerm>`

**Meaning:** Term from a past era.

#### `<HistoricalReference>`

**Meaning:** Reference to a historical context.

Note: Historical figures, places, and events are **Entities** and are
referenced via `@`, not `#`.

---

## 10. Scientific and Technical Concepts

#### `<ScientificTerm>`

**Meaning:** Term from scientific vocabulary.

#### `<TechnicalTerm>`

**Meaning:** Term from technical vocabulary.

#### `<Measurement>`

**Meaning:** A measured value.

#### `<MeasurementUnit>`

**Meaning:** A unit of measurement.

Note: Canonical scientific referents (elements, compounds, taxa, reactions)
are **Entities** and are referenced via `@`, not `#`.

---

## 11. Presentation Concepts

Presentation Concepts express inline typographic intent. They describe
**what the author wants**, not how it should render.

### 11.1 `<TextStyle>`

**Meaning:** Inline typographic intent.

**Required traits:**

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

**Optional traits:**

- `fontFamily` — semantic family (`serif`, `sansSerif`, `monospace`, `cursive`,
  `system`)

`TextStyle` expresses intent only. Realization is target-dependent.

---

## 12. Media Concepts

Media Concepts represent references to embedded media. They are inline
placeholders that renderers realize according to target capabilities.

### 12.1 `<Image>`

**Meaning:** Inline image or graphic.

**Required traits:**

- `id`
- `src` — resource identifier or reference

**Optional traits:**

- `alt` — alternative text description
- `width` — intrinsic or intended width
- `height` — intrinsic or intended height

### 12.2 `<Video>`

**Meaning:** Inline or embedded video media.

**Required traits:**

- `id`
- `src` — resource identifier or reference

**Optional traits:**

- `alt` — alternative text description
- `poster` — preview image reference

### 12.3 `<Audio>`

**Meaning:** Inline or embedded audio media.

**Required traits:**

- `id`
- `src` — resource identifier or reference

**Optional traits:**

- `alt` — alternative text description
- `transcript` — transcript reference

### 12.4 `<Canvas>`

**Meaning:** Embedded dynamic or interactive visual surface.

**Required traits:**

- `id`

**Optional traits:**

- `alt` — alternative text description
- `fallback` — static fallback reference

---

## 13. Nesting and Composition

Gloss annotations MAY nest. Nesting applies multiple semantic layers to the
same span of text.

Rules:

- Annotations MAY nest to arbitrary depth
- Non-Entity references (`#`) MAY contain Entity references (`@`, `~`)
- Entity references MAY contain non-Entity references
- Kernel MUST preserve original text
- Kernel MUST NOT introduce ambiguity

### 13.1 Nesting Semantics

When annotations nest, **both semantics apply** to the innermost text. The
outer annotation wraps the inner annotation, not just the label.

Example:

```cdx
{#internalDialogue | {@character:hamlet | To be, or not to be}}
```

This means:

1. The text "To be, or not to be" is the visible label
2. That text references the Entity `character:hamlet`
3. The entire reference is marked as `internalDialogue`

Both semantics (Entity reference + internal dialogue) apply to the same span.

---

## 14. Target Independence

All targetable Concepts:

- express meaning only
- do not mandate realization
- may be ignored by targets
- must remain explainable

Possible realizations include:

- visual styling
- spoken prosody and pacing
- accessibility cues
- metadata extraction
- no visible change at all

Gloss does not mandate realization.

---

## 15. Explainability Requirement (Normative)

The system MUST be able to explain:

- which Concept is applied to a span
- what that Concept means (per schema)
- whether and how it affected presentation

Opaque interpretation is forbidden.

---

## 16. Non-Goals (v0.1)

This document does not define:

- document structure
- layout or typography decisions
- behavior or execution
- evaluation or computation
- ontology design
- conflict resolution between overlapping semantics
- conversion algorithms (color, units, time zones)
- unit systems or dimensional analysis

These belong to Architect, Design Policy, renderers, or future specifications.

---

**End of Gloss Targetable Concepts v0.1**
