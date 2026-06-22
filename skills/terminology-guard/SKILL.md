---
name: terminology-guard
description: Enforce consistent technical terminology, acronym introduction, and naming conventions across manuscript drafts. Use when Codex needs to audit or lightly correct term drift in LaTeX or Markdown papers, especially before section rewrites, final polishing, or rebuttal preparation.
---

# Terminology Guard

## Overview

Treat terminology control as a narrow, high-precision pass. The goal is consistency, not stylistic reinvention. This skill should feel closer to copyediting plus technical risk detection than to broad rewriting.
This skill inherits the mandatory execution contract in `../../skills/paper-optimize/SKILL.md`.

## Workflow

1. Load governing rules and the project glossary.
   Read `../../skills/paper-optimize/SKILL.md`, `../../AGENTS.md`, `../../style/paper_optimization_rules.md`, and `../../style/terminology.yml` before editing.
2. Scan before editing.
   Prefer running `../../scripts/check_terminology.py` to detect mixed variants, banned phrases, and acronym-first-use issues.
3. Make only narrow edits.
   Change the term, acronym expansion, or naming pattern that is inconsistent. Avoid broader rewriting unless required for grammar.
4. Check local notation collisions.
   When a newly introduced counter or index symbol could be confused with an existing local meaning, prefer a non-conflicting symbol and flag the rationale.
5. Preserve scientific intent.
   When a variant might reflect a true technical distinction, flag it instead of normalizing it automatically.
6. Return the fixes plus any unresolved ambiguity.
7. Compile after edits when feasible.
   After applying terminology edits to the manuscript source, compile the manuscript path defined in `../../PROJECT_CONFIG.yml` when available, unless the user explicitly says not to.

## What To Check

- Mixed term variants for the same concept
- Acronyms used before their long forms
- After first introduction, prefer the acronym alone instead of repeatedly writing `full term (ACRONYM)`
- Symbol-style consistency when notation cleanup is part of the task: scalar variables in italic, explanatory labels in roman, vectors in bold, PD state quantities with an underline, and material-point pair indices written with parentheses such as `(k)(j)` when needed to distinguish them from tensor indices
- In the current manuscript convention, reserve the underline for vector state quantities such as `\underline{\boldsymbol{T}}`; keep the scalar force state `t[\boldsymbol{x},t]\langle\boldsymbol{\xi}\rangle` and the deformed-bond direction vector `\boldsymbol{M}` non-underlined unless the notation system is globally redefined
- Displayed equations should end with a comma or period according to the sentence structure, and long formulas should be line-broken when needed for double-column readability
- Inconsistent capitalization or hyphenation
- Shifts between broad and narrow names that may blur meaning
- Banned stock phrases listed in `../../style/banned_phrases.txt`
- Inconsistent naming between text, figures, tables, and equation discussion when visible in the current scope
- Term drift introduced by local rewrites, especially around methods, material systems, and boundary-condition language
- Bond-family taxonomy drift across setup paragraphs, constitutive paragraphs, and figure captions
- Local counter or index symbols that may collide with existing meanings such as time-step count, node count, or sample count
- Formula-to-prose mismatches where an index range, label mapping, or value mapping appears in the equation but is omitted or blurred in the explanatory sentence
- Local citation-anchor gaps where a standard theory, calibration, influence function, or constitutive parameter relation is invoked in prose without nearby source support
- Figure-text mismatches in panel order, field-variable names, colorbar units, or whether plotted CNT-interior values are omitted for visualization.
- In CNT results, preserve `bending offset parameter q` as the parameter definition; use `curvature` or `curved CNT geometry` only for morphology, not as a substitute for `q`.
- Distinguish damage and failure terms by scale: use `damage field` for damage-variable contours/cloud maps, `damage evolution` for loading-process descriptions, `damage bands` for localized damage bands, `bond failure` for PD bond-level failure, and `fracture process` for broader macroscopic descriptions.
- Keep figure-reference formatting consistent: use `Figure` at sentence start and avoid `Fig.` in that position; `3D` may be used directly in this manuscript.

## Priority Order

If terminology rules conflict, use this priority order:

1. Scientifically distinct meaning
2. Venue- or author-mandated terminology
3. Project glossary in `../../style/terminology.yml`
4. Local prose smoothness

Advisor-style sentence revisions must not override established terminology or acronym rules unless the advisor explicitly requests a terminology change.

## Guardrails

- Do not merge genuinely different concepts under one label.
- Do not standardize away journal-mandated capitalization if the user specifies a venue rule.
- If the manuscript intentionally alternates singular and plural forms, keep that distinction.
- Do not rename equation symbols, variable names, or figure labels unless the task explicitly includes notation cleanup.
- For bond families or method abbreviations, introduce the full term once and then use only the acronym unless repetition of the full term is required for clarity.
- If symbol-style cleanup is requested, apply the notation convention consistently across the whole local scope rather than mixing old and new index styles.
- When notation cleanup is in scope, prefer resolving ambiguous local symbol reuse early rather than preserving a confusing counter such as `n` if the surrounding section already uses it with another common meaning.
- When a displayed equation carries an essential local mapping such as `1,2,\dots,m`, preserve or restore a matching prose cue if the sentence would otherwise become harder to parse.

## Output Template

1. Issues found
2. Narrow edits proposed or applied
3. Terms intentionally left untouched
4. Ambiguities requiring author confirmation
