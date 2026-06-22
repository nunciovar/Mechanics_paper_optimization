# Paper Optimization Skills Inventory

This document lists the reusable skills and support files that make up the
paper-optimization harness.

## Core Files

- `AGENTS.md`: repository-level editing constitution.
- `PROJECT_CONFIG.example.yml`: copy this to `PROJECT_CONFIG.yml` for each paper.
- `style/paper_optimization_rules.md`: consolidated editing rules.
- `style/terminology.yml`: preferred terms, variants, and acronym checks.
- `style/banned_phrases.txt`: warning phrases for template-like prose.
- `style/preferred_patterns.txt`: preferred writing patterns.

## Skills

- `skills/paper-optimize/SKILL.md`
  Top-level orchestration entry point.

- `skills/structure-diagnose/SKILL.md`
  Diagnose section logic before rewriting.

- `skills/intro-rebuild/SKILL.md`
  Rebuild introduction flow: background, prior work, gap, objective, contribution.

- `skills/abstract-optimize/SKILL.md`
  Compress and calibrate abstracts while preserving scientific scope.

- `skills/anti-template-rewrite/SKILL.md`
  Reduce template-like academic phrasing without making the text informal.

- `skills/redundancy-reduce/SKILL.md`
  Remove self-overlap while preserving section-specific roles.

- `skills/terminology-guard/SKILL.md`
  Guard terminology, acronym, and notation consistency.

- `skills/writing-coach/SKILL.md`
  Explain editing principles behind revisions.

## Deterministic Scripts

- `scripts/check_terminology.py`
  Checks mixed variants, banned phrases, and acronym first-use issues.

- `scripts/scan_repetition.py`
  Reports repeated paragraph openers and repeated n-grams.

- `scripts/detect_long_sentences.py`
  Reports sentences above a configurable word threshold.

## Recommended Minimal Upload

For a new project, keep at least:

- `AGENTS.md`
- `PROJECT_CONFIG.example.yml`
- `style/`
- `skills/paper-optimize/`
- `skills/structure-diagnose/`
- `skills/anti-template-rewrite/`
- `skills/terminology-guard/`
- `scripts/`
- `docs/codex_workflow.md`
- `review/templates/`
