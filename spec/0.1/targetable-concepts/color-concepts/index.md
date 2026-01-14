Status: NORMATIVE  
Lock State: LOCKED  
Version: 0.1  
Editor: Charles F. Munat  

# Color Concepts

This document defines **color-related Concepts** that may be referenced by
**Gloss** to annotate spans of free text with **explicit, machine-readable color
meaning**.

Color Concepts are **data**, not presentation instructions.
They exist to eliminate ambiguity, preserve intent, and support rich,
target-independent realization across visual, print, audio, and data targets.

---

## 1. Purpose

Color is frequently used in prose, documentation, and design descriptions, but
is often:

* ambiguous (“light blue”, “warm red”)
* underspecified
* presentation-bound
* inaccessible to non-visual targets

Color Concepts allow authors to:

* define colors declaratively in Codex
* give colors identity
* reference them inline without magic values
* preserve the original color space and intent
* support accessibility, audio description, and analysis

Gloss annotates *what color is meant*, not *how it is rendered*.

---

## 2. General Rules (Normative)

* All Color Concepts defined here are **non-Entities**
* They MUST be referenced using `#` in Gloss
* Each Concept MUST declare an `id`
* Color values are expressed using **Codex Value literals**
* Codex performs **no conversion or normalization**

---

## 3. Color Space Preservation (Normative)

Color Concepts MUST preserve the **author-declared color space**.

Rules:

* No implicit conversion is performed by Codex or Gloss
* Renderers MAY convert colors as needed, but MUST preserve intent
* The original color space MUST remain available for explainability

---

## 4. Core Color Concepts

### 4.1 `<HexColor>`

Represents a color specified using hexadecimal RGB notation.

**Required Traits**
- `id`
- `value` — hex color literal (`#RRGGBB` or `#RRGGBBAA`)

Example:

```cdx
<HexColor id="brandBlue" value="#0057B8" />
````

Usage:

```cdx
The logo uses {#brandBlue}.
```

---

### 4.2 `<RgbColor>`

Represents a color in the RGB color space.

**Required Traits**

* `id`
* `value` — list of numeric channel values

Channel order: `[red, green, blue]`

Example:

```cdx
<RgbColor id="alertRed" value=[255, 0, 0] />
```

---

### 4.3 `<HslColor>`

Represents a color in the HSL color space.

**Required Traits**

* `id`
* `value` — list `[hue, saturation, lightness]`

Example:

```cdx
<HslColor id="softGreen" value=[120, 40, 60] />
```

---

### 4.4 `<OklchColor>`

Represents a color in the OKLCH color space.

This space is perceptually uniform and preferred for accessibility-aware
systems.

**Required Traits**

* `id`
* `value` — list `[lightness, chroma, hue]`

Example:

```cdx
<OklchColor id="accessibleBlue" value=[0.65, 0.12, 240] />
```

---

### 4.5 `<DisplayP3Color>`

Represents a color in the Display P3 color space.

**Required Traits**

* `id`
* `value` — list `[red, green, blue]`

Example:

```cdx
<DisplayP3Color id="vividOrange" value=[1.0, 0.4, 0.0] />
```

---

## 5. Named Colors

Architect MAY define named colors as Concepts.

Rules:

* Named color Concepts MUST use **spelled-out names**
* Names MUST be schema-authorized
* Names MUST NOT be ambiguous within the schema

Example:

```cdx
<Crimson id="crimson" value="#DC143C" />
```

Named colors are treated identically to other Color Concepts.

---

## 6. Color Collections and Palettes

Schemas MAY define collections of related colors.

Example (schema-defined):

```cdx
<ColorPalette id="brandPalette">
  <HexColor id="brandPrimary" value="#0057B8" />
  <HexColor id="brandSecondary" value="#FFD100" />
</ColorPalette>
```

Gloss references individual colors by `id`.

---

## 7. Usage with Gloss

All Color Concepts defined here:

* are referenced using `{#id}` or `{#id | label}`
* MAY be nested with other Gloss annotations
* MAY be ignored or realized differently by targets

Example:

```cdx
The warning text appears in {#alertRed | red}.
```

---

## 8. Target Independence

Color meaning is target-independent.

Possible realizations include:

* visual color rendering
* pattern or texture substitution
* spoken descriptions (“dark blue”)
* accessibility cues
* metadata extraction

Gloss does not mandate realization.

---

## 9. Explainability Requirement (Normative)

The system MUST be able to explain:

* which Color Concept is referenced
* which color space was used
* the exact declared value
* how the color was realized or substituted

Opaque behavior is forbidden.

---

## 10. Non-Goals (v0.1)

This document does not define:

* color conversion algorithms
* gamut mapping rules
* contrast calculations
* accessibility compliance thresholds
* blending or compositing

These belong to Design Policy or renderers.

---

## 11. Summary

* Colors are first-class declarative data
* Color space is preserved
* Values are defined once and referenced by identity
* Gloss eliminates magic colors in prose
* Accessibility and non-visual targets are supported
* Presentation remains target-controlled

---

**End of Color Concepts v0.1**
