Status: NORMATIVE  
Lock State: LOCKED  
Version: 0.1  
Editor: Charles F. Munat  

# Numeric and Measurement Concepts

This document defines **numeric and measurement-related Concepts** that may be
referenced by **Gloss** to annotate spans of free text with **machine-readable,
target-independent numeric meaning**.

These Concepts exist to eliminate “magic numbers”, support precise authoring,
and enable consistent interpretation across targets (text, audio, data export,
analysis).

---

## 1. Purpose

Numbers in prose are often:

* ambiguous (“about three”, “roughly ten”)
* contextless
* repeated without identity
* difficult for machines to interpret correctly

Gloss numeric and measurement Concepts allow authors to:

* define numeric values declaratively in Codex
* give those values identity
* reference them inline without re-encoding the value
* preserve precision, intent, and structure
* support audio, accessibility, analytics, and validation

These Concepts label meaning; they do not compute or evaluate values.

---

## 2. General Rules (Normative)

* All numeric and measurement Concepts defined here are **non-Entities**
* They MUST be referenced using `#` in Gloss
* Each Concept MUST declare an `id`
* Numeric meaning is carried by **Codex Value literals**
* Codex performs **no evaluation or normalization**

---

## 3. Core Numeric Concepts

### 3.1 `<Integer>`

Represents an integer numeric value.

**Required Traits**
- `id`
- `value` — integer literal

Example:

```cdx
<Integer id="count:apples" value=7 />
````

Usage:

```cdx
She bought {#count:apples} apples.
```

---

### 3.2 `<Decimal>`

Represents a decimal or scientific numeric value without explicit precision
semantics.

**Required Traits**

* `id`
* `value` — decimal or scientific literal

Example:

```cdx
<Decimal id="speed" value=88.5 />
```

---

### 3.3 `<PrecisionNumber>`

Represents a numeric value with **explicit or inferred precision**.

Precision is significant and MUST be preserved.

**Required Traits**

* `id`
* `value` — precision number literal (`…p` or `…pN`)

Example:

```cdx
<PrecisionNumber id="pi" value=3.141592653589793p15 />
```

Usage:

```cdx
The value of pi is {#pi}.
```

---

### 3.4 `<Fraction>`

Represents a rational number expressed as a fraction.

**Required Traits**

* `id`
* `value` — fraction literal (`numerator/denominator`)

Example:

```cdx
<Fraction id="oneThird" value=1/3 />
```

---

### 3.5 `<Imaginary>`

Represents an imaginary numeric value.

**Required Traits**

* `id`
* `value` — imaginary literal (`…i`)

Example:

```cdx
<Imaginary id="imag" value=2i />
```

---

## 4. Range Concepts

### 4.1 `<Range>`

Represents an inclusive numeric interval.

Ranges are declarative and are **not expanded or evaluated**.

**Required Traits**

* `id`
* `value` — range literal (`start..end`)

Example:

```cdx
<Range id="ageRange" value=3..6 />
```

---

### 4.2 Stepped Ranges

Ranges MAY include an explicit step.

**Form**

```
start..end s step
```

Example:

```cdx
<Range id="temperatureSteps" value=1.25..1.75s0.05 />
```

Codex does not require exact alignment or termination.

---

## 5. Measurement and Quantity Concepts

This specification does **not** mandate a unit system.

However, schemas MAY define measurement Concepts that combine numeric values
with units.

Illustrative examples (schema-defined):

```cdx
<Quantity id="length" value=2.5 unit="meter" />
<Quantity id="weight" value=70 unit="kilogram" />
```

Gloss treats these identically to other numeric Concepts.

---

## 6. Constants

Architect MAY define numeric constants as Concepts.

Rules:

* Constant Concepts MUST use **spelled-out names**
* Symbol-only names are forbidden
* Constants MAY be implemented as specialized Concepts or as numeric Concepts
  with fixed values

Examples:

```cdx
<Pi id="pi" value=3.141592653589793p15 />
<EulerNumber id="e" value=2.718281828459045p15 />
```

Constants are referenced via `#`:

```cdx
The ratio is approximately {#pi}.
```

---

## 7. Usage with Gloss

All numeric and measurement Concepts defined here:

* are referenced using `{#id}` or `{#id | label}`
* MAY be nested with other Gloss annotations
* MAY be ignored or realized differently by targets

Example:

```cdx
The area is approximately {#pi | π} square meters.
```

---

## 8. Target Independence

Numeric meaning is target-independent.

Possible realizations include:

* spoken forms (“three point one four”)
* formatted numbers
* symbolic representations
* metadata extraction
* analytical processing

Gloss does not mandate realization.

---

## 9. Explainability Requirement (Normative)

The system MUST be able to explain:

* what numeric Concept is referenced
* what literal value it carries
* whether precision or structure is significant
* why a particular rendering or pronunciation was chosen

Opaque behavior is forbidden.

---

## 10. Non-Goals (v0.1)

This document does not define:

* arithmetic or expressions
* unit conversion
* dimensional analysis
* numeric normalization
* comparison semantics

These belong to consuming systems or future specifications.

---

## 11. Summary

* Numeric values are first-class, declarative data
* Values are defined once and referenced by identity
* Precision and structure are preserved
* Gloss eliminates magic numbers in prose
* Architect defines constants and units
* Meaning is explicit and explainable
