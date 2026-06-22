# Paper Optimization System Overview

This repository packages a reusable manuscript-editing harness.

The goal is not to let an agent rewrite a paper freely. The goal is to make
paper editing repeatable, auditable, and conservative:

1. Diagnose the requested scope.
2. Preserve scientific meaning and evidence boundaries.
3. Apply style, terminology, and section-role rules.
4. Run deterministic checks.
5. Record verification results and open author questions.

## Main Components

- `AGENTS.md`: editing constitution and operating rules.
- `PROJECT_CONFIG.example.yml`: template for project-specific manuscript paths.
- `skills/`: reusable editing workflows.
- `style/`: terminology, phrase, and writing-pattern controls.
- `scripts/`: deterministic checks for terminology, repetition, and long sentences.
- `docs/`: workflow and system documentation.
- `review/templates/`: persistent review-output templates.

## Editing Phases

1. **Diagnosis**: identify structural, logical, terminology, and style issues.
2. **Structure revision**: repair section function and paragraph order.
3. **Sentence revision**: reduce template phrasing and improve precision.
4. **Redundancy reduction**: compress repeated statements without erasing section roles.
5. **Verification**: run scripts and record remaining risks.

## What This System Does Not Do

- It does not invent experiments, data, equations, citations, or numerical results.
- It does not silently change scientific meaning.
- It does not auto-resolve ambiguous technical terms.
- It does not assume that every future paper uses the same manuscript path or domain terms.

## First-Pass Cleanup Scope

This repository is currently a lightweight harness. Later upgrades can add richer
configuration parsing, CI checks, examples, and project-specific skill tuning.
