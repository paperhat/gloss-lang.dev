Status: NORMATIVE
Lock State: LOCKED
Version: 0.1
Editor: Charles F. Munat

# Gloss Formal Grammar Specification — Version 0.1

This specification defines the **formal grammar** of Gloss inline annotations.

Two grammar notations are provided:

* **EBNF** (Normative) — ISO/IEC 14977 Extended Backus-Naur Form
* **PEG** (Informative) — Parsing Expression Grammar for implementation

---

## 1. Purpose

This specification exists to:

* provide an unambiguous definition of Gloss syntax
* enable mechanical parser construction
* support conformance testing
* eliminate ambiguity in the syntax specification

---

## 2. Authority

### 2.1 Syntactic Authority

The EBNF grammar is **normative for syntax**. Conforming parsers MUST accept
all annotations matching the EBNF grammar.

The PEG grammar is **informative**. It provides an implementation-ready,
unambiguous grammar. In case of discrepancy between EBNF and PEG, the EBNF
grammar takes precedence.

### 2.2 Semantic Authority

Prose specifications are **normative for semantics**. The grammar defines what
is syntactically valid but does not assign meaning.

* **Syntax and Naming Specification**: normative for surface syntax and escaping
* **Entity Binding Specification**: normative for Entity reference semantics
* **Targetable Concepts Specification**: normative for non-Entity semantics

In case of discrepancy between grammar and prose:

* For syntactic precision (what parses): EBNF takes precedence
* For semantic intent (what it means): prose specifications take precedence

---

## 3. Included Documents

* [**EBNF Grammar**](./ebnf/) — Normative formal grammar
* [**PEG Grammar**](./peg/) — Informative implementation grammar

---

## 4. Scope

This grammar defines:

* Annotation delimiters (`{` and `}`)
* Addressing sigils (`@`, `~`, `#`)
* Reference identifiers
* Label syntax and escaping
* Nesting structure

This grammar does **not** define:

* Schema validation rules
* Reference resolution semantics
* Content outside of Gloss annotations

---

## 5. Context-Sensitive Parsing

Gloss uses context-sensitive rules to minimize escaping in typical content:

* `{` starts an annotation **only** when followed by `@`, `~`, or `#`
* First `|` in an annotation separates reference from label
* `}` closes an annotation; escape as `\}` inside labels
* `\` is only special before `}` or `\` inside labels

These rules are formalized in the EBNF grammar.

---

**End of Gloss Formal Grammar Specification v0.1**
