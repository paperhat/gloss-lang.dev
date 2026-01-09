# Architect vs Gloss Concept Inventory

This document records the **current authoritative classification** of former
and proposed Paperhat concepts into:

- **Architect / Codex responsibilities**
- **Gloss targetable Concepts**
- **Codex Entities (referenced by Gloss via `@`)**

This document is **informative**, not normative.  
It exists to prevent scope drift, duplication, and HTML-style collapse of concerns.

---

## 1. Classification Rules (Summary)

A concept belongs in **Gloss** iff it is:

- inline (span-level)
- semantic or intent-expressing
- non-structural
- non-behavioral
- target-independent
- explainable as “this span means X”

A concept belongs in **Architect** iff it:

- defines structure, hierarchy, or containment
- represents document layout or block organization
- defines collections or ordered groups
- replaces HTML structural elements

A concept is a **Codex Entity** iff it:

- has identity
- represents a real or conceptual referent
- participates in graphs or metadata
- may be referenced with `@`

---

## 2. Architect / Codex Structure (NOT Gloss)

### Tables
- Table
- TableHeader
- TableBody
- TableFooter
- TableRow
- TableCell
- TableCaption

### Lists
- NumberedList
- BulletedList
- ListItem
- Dictionary
- DictionaryTerm (structural)
- DictionaryDefinition

### Document Structure
- Article
- Section
- Heading
- Sidebar
- Abstract
- Appendix
- AppendixEntry
- BlockQuote

### Collections & Reference Sections
- Bibliography
- References
- Glossary
- GlossaryEntry

### Full schema.org hierarchy
- All schema.org Types
- All schema.org Properties
- All schema.org Classes

Architect is the **exclusive owner** of these concepts.

---

## 3. Codex Entities (Gloss `@` references)

### Narrative / Fictional
- CharacterName
- Protagonist
- Antagonist
- SideCharacter
- CharacterRole
- CharacterRelationship

### Historical
- HistoricalFigure
- HistoricalPlace
- HistoricalEvent

### Scientific
- Element
- Compound
- Reaction
- TaxonomicTerm
- BiologicalSequence (when canonical)
- ScientificTerm (when treated as referent)

### Cultural / Works
- Book
- Article
- LegalCase
- Title-bearing Works
- MythologicalFigure (when treated as entity)

These are defined by schemas and referenced inline via `@`.

---

## 4. Gloss Targetable Concepts (`#`, non-Entities)

### Temporal & Numeric
- Date
- Time
- DateTime
- Instant / Timestamp
- Duration
- YearMonth
- MonthDay
- Week
- WeekDay
- Quarter
- RelativeTime
- PrecisionNumber
- Integer
- Fraction
- Quantity
- Measurement
- MeasurementUnit

### Color
- HexColor
- RgbColor
- HslColor
- OklchColor
- DisplayP3Color
- Named color Concepts (schema-defined)

### Editorial / Change Tracking
- Insert
- Delete
- Redacted

### Code & Technical
- Code
- InlineMath
- ProgramOutput
- KeyboardInput
- Variable
- Constant
- Formula
- Equation

### Linguistic
- Abbreviation
- Acronym
- Initialism
- Contraction
- ForeignTerm
- Loanword
- TransliteratedTerm
- Neologism
- Jargon
- WordAsWord
- LetterAsLetter
- MentionedTerm
- PhoneticTranscription

### Narrative & Rhetorical
- Narration
- Dialogue
- InternalDialogue
- InternalMonologue
- VoiceOver
- AlternativeVoice
- PointOfView
- DreamSequence
- Flashback
- Foreshadowing
- Cliffhanger
- NonlinearNarrative
- Exposition
- Anecdote
- Backstory
- SceneSetting
- Setting
- Symbolism
- Metafiction
- StageDirection
- CharacterThoughts

### Quotations & References
- Quote
- CitedQuote
- Paraphrase
- PullQuote
- Testimonial
- Epigraph
- CrossReference
- Footnoted
- LegalReference
- Cited
- Reference
- TitleOfWork

### Cultural & Idiomatic
- Colloquialism
- Slang
- IdiomaticPhrase
- Proverb
- Archaism
- Dialect
- FigurativeLanguage
- Anachronism
- MythologicalReference
- Tradition
- Holiday
- VesselName

### Indexing & Terminology
- GlossaryTerm
- Synonym
- Indexed

All Gloss targetables:
- are non-Entities
- are referenced via `#`
- express meaning, not presentation
- may be ignored or variably realized by targets

---

## 5. Explicit Rejections (Do Not Reintroduce)

The following concepts were rejected as Gloss targetables because they are
presentation-biased or structurally ambiguous:

- Linked
- Highlighted (use `Highlight`)
- Emphasized (use `Stress` / `Important`)
- Output (replaced by `ProgramOutput`)
- Input (replaced by `KeyboardInput`)

---

## 6. Status

This inventory reflects the **current complete design intent** for Gloss v0.1
and Architect scope as discussed.

Future additions should be evaluated against the rules in §1 and recorded here
before being added to any specification.

---

**End of Architect vs Gloss Concept Inventory**
