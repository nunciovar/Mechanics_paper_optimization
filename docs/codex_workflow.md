# Codex Workflow

This repository is a lightweight harness for manuscript-editing loops.

## Before Editing

1. Read `AGENTS.md`.
2. Read `PROJECT_CONFIG.yml` if it exists.
3. Confirm the requested scope: full manuscript, one section, paragraph group, or review only.
4. Read the relevant style controls in `style/`.
5. Diagnose before rewriting unless the user explicitly asks for direct editing.

## Editing Loop

```text
inspect scope
  -> diagnose risks
  -> propose or apply scoped edits
  -> run deterministic checks
  -> write review artifacts
  -> report what changed and what still needs author judgment
```

## Recommended Commands

```bash
python scripts/check_terminology.py <files>
python scripts/scan_repetition.py <files>
python scripts/detect_long_sentences.py <files> --threshold 35
```

## Review Artifacts

When a persistent review is useful, create files under `review/` using:

- `review/templates/changed_files.md`
- `review/templates/verification_result.md`
- `review/templates/open_questions.md`

## Guardrails

- Do not invent data, citations, equations, or unsupported novelty claims.
- Do not silently change numerical values, units, or figure references.
- Do not optimize style by weakening scientific precision.
- Do not assume a fixed manuscript path from a previous project.
