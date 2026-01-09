Status: NORMATIVE  
Lock State: LOCKED  
Version: 0.1  
Editor: Charles F. Munat  

# Inline Semantic Concepts

This document defines the **inline semantic Concept vocabulary** that MAY be
referenced by **Gloss** using `{#id}` or `{#id | label}`.

Inline Semantic Concepts:

* apply to **spans of free text**
* express **meaning or intent**, not structure or behavior
* are **non-Entities**
* are **target-independent**
* are **schema-defined and Architect-owned**

Gloss syntax does not vary by Concept.

---

## 1. Scope and Purpose

Inline Semantic Concepts exist to make meaning that is commonly implicit in prose
**explicit, machine-readable, and explainable**, without introducing structure,
layout, or behavior.

They are used to express:

* narrative framing
* linguistic and rhetorical intent
* affective and cognitive state
* editorial state
* code and technical distinctions
* scientific, cultural, and historical semantics
* indexing and reference intent

They do **not** define:

* document structure
* collections or hierarchy
* rendering behavior
* evaluation or computation

---

## 2. General Rules (Hard)

All Inline Semantic Concepts defined or referenced here:

* MUST be referenced using `#` in Gloss
* MUST NOT be Entities
* MUST declare an `id`
* MUST be schema-authorized by Architect
* MUST preserve authorial intent
* MUST be ignorable or variably realized by targets

Gloss binds meaning only; realization is deferred.

---

## 3. Editorial and Change-Tracking Semantics

### 3.1 `<Insert>`

**Meaning:** Inserted content.

---

### 3.2 `<Delete>`

**Meaning:** Deleted content.

---

### 3.3 `<Redacted>`

**Meaning:** Intentionally withheld or obscured content.

Redaction is semantic and distinct from deletion.

---

## 4. Narrative and Rhetorical Semantics

These Concepts express **how text is narrated, framed, or perceived**.

Examples include but are not limited to:

* `<Narration>`
* `<Dialogue>`
* `<InternalDialogue>`
* `<InternalMonologue>`
* `<VoiceOver>`
* `<AlternativeVoice>`
* `<PointOfView>`
* `<DreamSequence>`
* `<Flashback>`
* `<Foreshadowing>`
* `<Cliffhanger>`
* `<NonlinearNarrative>`
* `<Exposition>`
* `<Anecdote>`
* `<Backstory>`
* `<SceneSetting>`
* `<Setting>`
* `<Symbolism>`
* `<Metafiction>`
* `<StageDirection>`
* `<CharacterThoughts>`

These Concepts:

* do not define structure
* do not imply identity
* may be nested
* may be ignored or subtly realized

---

## 5. Affective and Cognitive State

Inline Concepts may express emotional, cognitive, or mental state.

Architect MAY define:

### 5.1 Discrete State Concepts

Examples:

* `<Sad>`
* `<Angry>`
* `<Joyful>`
* `<Dream>`

These carry meaning by name alone.

---

### 5.2 Structured State Concepts

Architect MAY define structured Concepts such as:

* `<Emotion>`
* `<Tone>`
* `<MentalState>`
* `<NarrativeMode>`

Structured Concepts MAY include Traits such as `kind`, `intensity`, or
schema-defined qualifiers.

---

## 6. Linguistic Semantics

These Concepts clarify **how words are to be understood or spoken**.

Examples include:

* `<Abbreviation>`
* `<Acronym>`
* `<Initialism>`
* `<Contraction>`
* `<ForeignTerm>`
* `<Loanword>`
* `<TransliteratedTerm>`
* `<Neologism>`
* `<Jargon>`
* `<WordAsWord>`
* `<LetterAsLetter>`
* `<MentionedTerm>`
* `<PhoneticTranscription>`

These are especially relevant for audio, accessibility, and analysis targets.

---

## 7. Code and Technical Semantics

### 7.1 `<Code>`

**Meaning:** Inline code fragment.

Optional Traits MAY include:

* `language`
* `version`

---

### 7.2 `<InlineMath>`

**Meaning:** Inline mathematical expression.

Evaluation is explicitly forbidden.

---

### 7.3 `<ProgramOutput>`

**Meaning:** Output produced by a program or system.

---

### 7.4 `<KeyboardInput>`

**Meaning:** User keyboard input.

---

### 7.5 Technical Markers

Architect MAY define Concepts such as:

* `<Variable>`
* `<Constant>`
* `<Formula>`
* `<Equation>`

These express semantic role, not computation.

---

## 8. Quotations and References

### 8.1 Quotation Semantics

Examples include:

* `<Quote>`
* `<CitedQuote>`
* `<Paraphrase>`
* `<PullQuote>`
* `<Testimonial>`
* `<Epigraph>`

These Concepts express **relationship to another utterance**, not layout.

---

### 8.2 Reference Semantics

Examples include:

* `<Reference>`
* `<Cited>`
* `<LegalReference>`
* `<CrossReference>`
* `<Footnoted>`
* `<TitleOfWork>`

These Concepts often nest Entity references (`@`) but are themselves non-Entities.

---

## 9. Cultural and Historical Semantics

### 9.1 Cultural Semantics

Examples include:

* `<Colloquialism>`
* `<Slang>`
* `<IdiomaticPhrase>`
* `<Proverb>`
* `<Archaism>`
* `<Dialect>`
* `<FigurativeLanguage>`
* `<Anachronism>`
* `<MythologicalReference>`
* `<Tradition>`
* `<Holiday>`
* `<VesselName>`

---

### 9.2 Historical Semantics

Examples include:

* `<HistoricalTerm>`
* `<HistoricalReference>`

Historical figures, places, and events are **Entities** and referenced via `@`.

---

## 10. Scientific and Technical Semantics

Examples include:

* `<ScientificTerm>`
* `<TechnicalTerm>`
* `<Measurement>`
* `<MeasurementUnit>`
* `<Quantity>`

Canonical scientific referents (elements, compounds, taxa, reactions) are
Entities and referenced via `@`.

---

## 11. Indexing and Terminology

### 11.1 `<GlossaryTerm>`

**Meaning:** This span corresponds to a defined glossary term.

---

### 11.2 `<Synonym>`

**Meaning:** This span is a synonym of another term.

---

### 11.3 `<Indexed>`

**Meaning:** This span participates in indexing.

---

## 12. Nesting and Composition

Inline Semantic Concepts:

* MAY be nested
* MAY wrap Entity references
* MUST preserve original text
* MUST NOT introduce ambiguity

Example:

```cdx
{#internalDialogue {@character:hamlet | To be, or not to be}}
````

---

## 13. Target Independence

Inline Semantic Concepts:

* express meaning only
* do not mandate realization
* may be ignored by targets
* must remain explainable

---

## 14. Non-Goals (v0.1)

This document does not define:

* document structure
* layout or typography
* behavior or execution
* evaluation or computation
* ontology design
* conflict resolution between overlapping semantics

---

## 15. Summary

* Inline Semantic Concepts express span-level meaning
* They are non-Entities and Architect-owned
* They are referenced uniformly via `#`
* Gloss remains small, stable, and target-independent
* Structure belongs to Architect; realization belongs to Design Policy

---

**End of Inline Semantic Concepts v0.1**
