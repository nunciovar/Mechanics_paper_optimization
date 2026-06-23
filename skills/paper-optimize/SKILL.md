---
name: paper-optimize
description: Router for mechanics/peridynamics manuscript optimization. Use when the user asks to diagnose, revise, polish, compress, de-template, terminology-check, or accept-review a scientific manuscript passage and the task may require selecting among phases, sections, domains, or language modes.
---

# Paper Optimize Router

This skill is the routing entry point for the paper-optimization harness.

It must not behave as a generic writing tool. It preserves the repository's
scientific editing stance: diagnose before rewriting, preserve scientific
meaning before fluency, and never invent data, citations, equations,
mechanisms, figures, or unsupported claims.

## Router Load Order

For every task:

1. Read `../../AGENTS.md`.
2. Read `../../PROJECT_CONFIG.yml` when present; otherwise ask for scope if the manuscript path matters.
3. Load `manifest.yaml`.
4. Load shared core files:
   - `../_shared/core/stance.md`
   - `../_shared/core/workflow.md`
   - `../_shared/core/output-format.md`
   - `../_shared/core/qa-checklist.md`
   - `../_shared/core/terminology-ledger.md`
5. Detect the relevant axes:
   - `task_phase`
   - `section`
   - `domain`
   - `language`
6. Load only the matching fragments under `static/`.
7. Load `../../style/terminology.yml` and `../../style/banned_phrases.txt` only when terminology, acronym, tone, or de-templating checks are relevant.

Avoid loading every rule file by default. The manifest is the source of truth
for fragment selection.

## Axis Detection Hints

### task_phase

- `diagnose`: what is wrong, review only, assess, find problems.
- `rebuild`: restructure, reorganize, rebuild section logic.
- `polish`: polish, improve English, de-template, make concise.
- `reduce_redundancy`: remove repetition, compress overlap.
- `terminology_check`: terminology, acronym, notation, consistency.
- `acceptance`: final check, verification, acceptance summary.

### section

Detect explicit section names such as abstract, introduction, methods, results,
discussion, and conclusion. If no section is clear, use no section fragment or
ask for scope when needed.

### domain

Use mechanics, peridynamics, CNT/epoxy, advisor-style, or generic scientific
fragments according to the user's request and provided manuscript context.

### language

Use Chinese academic, Chinese-to-English, or English-polish fragments according
to the requested language operation.

## Mandatory Execution Contract

1. Confirm the local scope before broad edits.
2. Choose the phase before editing.
3. Preserve scientific meaning, numerical fidelity, notation integrity, and claim scope.
4. Flag author-confirmation items instead of resolving missing evidence.
5. Return results using the shared output format.
6. Run deterministic scripts when the task asks for verification or when a check is directly relevant.

## Specialist Skills

When a narrower skill is a better fit, route to it rather than duplicating its
logic:

- `structure-diagnose`
- `intro-rebuild`
- `abstract-optimize`
- `anti-template-rewrite`
- `redundancy-reduce`
- `terminology-guard`
- `writing-coach`
- `mechanics-reviewer`

Use specialist skills after loading only the relevant shared core and fragments.

## Guardrails

- Do not add Nature-specific style rules.
- Do not add citation search, figure generation, presentation, patent, or grant-writing behavior.
- Do not convert this repository into a generic writing assistant.
- Do not rewrite all sections for consistency unless the user asks.
- Do not silently alter equations, symbols, references, figure labels, or values.
