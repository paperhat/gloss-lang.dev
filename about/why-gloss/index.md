# Why Gloss Exists

> **This is what Gloss looks like.**  
> Natural human prose, written normally — with **semantic meaning bound inline**
> to specific spans of text.
>
> No structure. No styling. No behavior.  
> Just meaning attached exactly where it occurs.

Gloss always operates **in the presence of [Codex](https://codex-lang.dev/why-codex/)**.  
Codex defines the meaning; Gloss binds that meaning to text.

---

## What Gloss Looks Like in Use

```cdx
<Emotion id="grief" kind="sadness" intensity=0.8 />
<Emotion id="anger" kind="anger" intensity=0.9 />
<Duration id="time:years" value={P5Y} />
<PrecisionNumber id="count:warnings" value=3 />

<Paragraph>
  She had felt {#grief | sad} for {#time:years | years},
  but this time it was different.
</Paragraph>

<Paragraph>
  “I told you,” he said, his voice {#anger | sharp with anger}.
</Paragraph>

<Paragraph>
  He had warned her {#count:warnings | three times} before,
  and now there was nothing left to say.
</Paragraph>
````

The text reads naturally:

> *She had felt sad for years, but this time it was different.*

But the meaning is now explicit and machine-readable:

* which emotion is present
* how intense it is
* how long it lasted
* which numeric values are significant

That meaning can be consumed by audio systems, accessibility tooling,
analysis pipelines, or ignored entirely — without changing the text.

---

## The Problem Gloss Solves

Many forms of meaning live **inside sentences**, not around them:

* emotion
* tone
* internal dialogue
* emphasis
* numeric precision
* temporal intent
* narrative state

Traditional systems force authors to choose between:

* breaking prose apart
* encoding meaning indirectly
* or losing that meaning entirely

Gloss exists to make those meanings **explicit without damaging the prose**.

---

## What Gloss Is

Gloss is:

* an **inline semantic span-binding language**
* **declarative** — no logic, no evaluation
* **target-independent**
* **schema-driven** — meaning lives in Codex
* **explainable** — every annotation has a reason

Gloss answers one question only:

> **“What does this span of text mean?”**

---

## What Gloss Is Not

Gloss does **not**:

* define structure
* define layout
* define behavior
* encode presentation
* introduce new semantics on its own
* replace Codex Concepts or schemas

If it affects correctness, structure, or execution,
it is **not Gloss**.

---

## How Gloss Works with Codex

* **Codex** defines Concepts, Traits, Values, and identity
* **Architect** authorizes vocabularies and meaning
* **Gloss** references those Concepts inline using `{#id}` or `{@id}`
* **Design Policy** decides how meaning is realized
* **Renderers** produce target-specific output

Gloss is **subordinate to Codex** and cannot be used independently.

---

## Why Inline Binding Matters

Inline binding allows meaning to be:

* precise (span-level, not block-level)
* non-invasive (text remains intact)
* reusable across targets
* accessible to non-visual systems
* preserved through round-trips

The text stays human.
The meaning becomes explicit.

---

## The Core Principle

> **Write naturally.
> Bind meaning explicitly.
> Defer presentation entirely.**

That is what Gloss enforces.

---

## Summary

* Gloss binds semantic meaning to spans of text
* It works only alongside Codex
* It preserves prose while exposing intent
* It is small, stable, and deliberately limited
* It enables richer targets without changing the text

Gloss is not expressive by accident.

It is constrained by design.
