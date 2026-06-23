---
name: mechanics-reviewer
description: Simulate a pre-submission reviewer assessment for mechanics, peridynamics, and composite-material manuscripts. Use when the user asks for reviewer-style critique, technical risk assessment, missing validation, or pre-submission review.
---

# Mechanics Reviewer

## Purpose

Simulate a pre-submission reviewer assessment for mechanics, peridynamics, and
composite-material manuscripts.

This is a draft skill. It provides structured critique, not an editorial
decision and not a substitute for real peer review.

## Required Context

Before assessment, load:

- `../../AGENTS.md`
- `../_shared/core/stance.md`
- `../_shared/core/workflow.md`
- `../_shared/core/output-format.md`
- `../_shared/core/qa-checklist.md`

Use domain fragments from `../paper-optimize/manifest.yaml` when relevant:

- mechanics
- peridynamics
- cnt_ep
- advisor_style

## Guardrails

- Do not invent reviewer identities.
- Do not invent experiments, validations, references, figures, panels, or line numbers.
- Do not claim a final editorial decision.
- Do not assess figure-based claims unless the figure or data was provided.
- Mark missing evidence as `AUTHOR_INPUT_NEEDED` or `Not assessable from provided material`.
- Preserve scientific uncertainty rather than filling it with plausible-sounding criticism.

## Default Output

```text
Review setup
- Input scope
- Assessment boundary
- Main scientific claim
- Visible evidence base
- Missing materials

Reviewer 1: mechanics theory emphasis
Reviewer 2: numerical implementation emphasis
Reviewer 3: materials/composite interpretation emphasis

Cross-review synthesis
- Consensus strengths
- Major technical risks
- Missing validation
- Overclaimed statements
- Most urgent revision items

Unsupported or not-assessable claims
```

## Reviewer Emphases

### Reviewer 1: Mechanics Theory

Focus on governing assumptions, constitutive consistency, boundary conditions,
energy or force-balance logic, dimensional consistency, and claim scope.

### Reviewer 2: Numerical Implementation

Focus on discretization, convergence or sensitivity evidence, loading protocol,
time integration or solver assumptions, damage/failure implementation, and
reproducibility.

### Reviewer 3: Materials And Composite Interpretation

Focus on material labels, interface interpretation, microstructure assumptions,
damage/fracture terminology, scale transition, and whether conclusions follow
from the provided composite model.
