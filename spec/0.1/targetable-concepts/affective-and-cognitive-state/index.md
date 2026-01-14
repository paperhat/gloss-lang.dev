Status: NORMATIVE  
Lock State: LOCKED  
Version: 0.1  
Editor: Charles F. Munat  

# Affective and Cognitive State Concepts

This document defines the **rules and shapes** for expressing affective,
cognitive, narrative, and internal-state semantics in **Gloss**.

These semantics apply to **spans of text** and are used to convey meaning such as:

- emotion
- tone
- mental state
- narrative mode
- internal vs external speech
- subjective or altered states

This document defines **how such semantics are represented**, not **which
specific vocabularies must exist**.

---

## 1. Purpose

Many forms of meaning expressed in natural language are **not structural** and
are **not representable in HTML or traditional markup**, including:

- emotion (“sad”, “angry”)
- tone (“whispered”, “shouted”)
- internal dialogue
- dream or memory states
- irony, detachment, unreliability
- subjective perception

Gloss exists in part to make these meanings **explicit, machine-readable, and
target-independent**, especially for non-visual targets such as audio.

---

## 2. Open Vocabulary Rule (Normative)

Gloss uses an **open vocabulary** for affective and cognitive state.

Rules:

- Any schema-authorized Concept MAY represent an affective or cognitive state
- Gloss does **not** enumerate or constrain allowed state names
- Meaning is defined entirely by schema (e.g. Architect)

Examples of valid Concepts (illustrative, not normative):

```cdx
<Sad id="sad" />
<Angry id="angry" />
<Joyful id="joy" />
<InternalDialogue id="inner" />
<Dream id="dream" />
<Flashback id="flashback" />
````

Used as:

```cdx
{#sad | "I can’t believe he died."}
{#angry | "It wasn’t supposed to happen!"}
```

---

## 3. Discrete State Concepts

### 3.1 Definition

A **Discrete State Concept** represents a single, named affective or cognitive
state with no internal structure.

Characteristics:

* no required Traits beyond `id`
* meaning conveyed by Concept name alone
* author-friendly
* suitable for most prose

Discrete state Concepts are preferred when:

* nuance is not required
* the author wants minimal ceremony
* the target may ignore or subtly render the state

---

## 4. Structured State Concepts

### 4.1 Purpose

When additional precision is required (for analysis, accessibility, audio
rendering, or research), **structured Concepts** MAY be used.

These Concepts carry Traits that further qualify the state.

---

### 4.2 `<Emotion>`

Represents an emotional state.

**Required Traits**

* `id`

**Optional Traits**

* `kind` — schema-defined emotion category
* `intensity` — numeric value (range and scale schema-defined)
* `valence` — optional positive/negative axis
* `arousal` — optional activation axis

Example:

```cdx
<Emotion id="e1" kind="sadness" intensity=0.7 />
```

Used as:

```cdx
{#e1 | "I can’t believe he died."}
```

---

### 4.3 `<Tone>`

Represents delivery or manner of expression.

**Required Traits**

* `id`

**Optional Traits**

* `kind` — e.g. whisper, shout, flat, sarcastic
* `intensity`

Example:

```cdx
<Tone id="t1" kind="angry" intensity=0.9 />
```

---

### 4.4 `<MentalState>`

Represents an internal cognitive or perceptual condition.

**Optional Traits**

* `kind` — e.g. dreaming, dissociating, remembering
* `awareness` — schema-defined
* `reliability` — schema-defined

Example:

```cdx
<MentalState id="m1" kind="dreaming" />
```

---

### 4.5 `<NarrativeMode>`

Represents narrative framing or perspective.

Examples of `kind` (schema-defined):

* internalDialogue
* unreliableNarration
* aside
* streamOfConsciousness

Example:

```cdx
<NarrativeMode id="n1" kind="internalDialogue" />
```

---

## 5. Usage Rules (Normative)

* All affective and cognitive state Concepts MUST be referenced using `#`
* These Concepts MUST NOT be Entities
* These Concepts express **meaning**, not presentation
* Renderers MAY choose how to realize or ignore these semantics
* Design Policy MAY influence realization, but MUST NOT reinterpret meaning

---

## 6. Target Independence

These semantics are intentionally **non-visual**.

Possible realizations include:

* audio prosody and pacing
* subtle typographic changes
* annotations or metadata
* accessibility cues
* no visible change at all

Gloss does not mandate realization.

---

## 7. Explainability Requirement (Normative)

The system MUST be able to explain:

* which state Concept is applied to a span
* what that Concept means (per schema)
* whether and how it affected presentation

Opaque interpretation is forbidden.

---

## 8. Non-Goals (v0.1)

This document does not define:

* a canonical emotion taxonomy
* psychological theory alignment
* limits on state nesting
* conflict resolution between overlapping states
* behavioral triggers

These may be addressed by schema or future versions.

---

## 9. Summary

* Gloss supports rich affective and cognitive semantics
* Vocabulary is open and schema-owned
* Discrete Concepts are preferred for authoring
* Structured Concepts exist for precision
* Meaning is explicit, machine-readable, and target-independent

---

**End of Affective and Cognitive State Concepts v0.1**
