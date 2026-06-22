# Mechanics Paper Optimization

This repository contains a controlled manuscript-revision workflow for mechanics,
peridynamics, and composite-material papers.

It is designed to help Codex or another editing agent diagnose, restructure,
polish, de-template, compress, and terminology-check manuscript sections without
changing scientific meaning or inventing unsupported claims.

## Core Principles

1. Diagnose before rewriting.
2. Preserve scientific meaning before improving fluency.
3. Preserve author intent, evidence scope, numerical values, and citations.
4. Standardize terminology, acronyms, and notation.
5. Keep section roles distinct.
6. Reduce template-like academic phrasing.
7. Flag high-risk scientific claims for author review.

## Repository Layout

```text
.
|-- AGENTS.md
|-- PROJECT_CONFIG.example.yml
|-- README.md
|-- docs/
|   |-- acceptance_checklist.md
|   |-- codex_workflow.md
|   |-- paper_optimization_skills_inventory.md
|   |-- paper_optimization_system_overview.md
|   `-- skill_rules_and_workflow_for_advisor.md
|-- review/
|   `-- templates/
|       |-- changed_files.md
|       |-- open_questions.md
|       `-- verification_result.md
|-- scripts/
|   |-- check_terminology.py
|   |-- detect_long_sentences.py
|   `-- scan_repetition.py
|-- skills/
`-- style/
    |-- banned_phrases.txt
    |-- preferred_patterns.txt
    `-- terminology.yml
```

## Typical Workflow

```text
diagnose
  -> rebuild structure if needed
  -> de-template sentence style
  -> reduce redundancy
  -> check terminology and long sentences
  -> return revised text, verification notes, and open questions
```

For project-specific manuscript paths, copy `PROJECT_CONFIG.example.yml` to
`PROJECT_CONFIG.yml` and edit the paths. Do not hard-code one paper's directory
into reusable workflow files.

## Deterministic Checks

The scripts in `scripts/` provide lightweight, repeatable checks:

```bash
python scripts/check_terminology.py --help
python scripts/scan_repetition.py --help
python scripts/detect_long_sentences.py --help
```

Example:

```bash
python scripts/check_terminology.py README.md AGENTS.md
python scripts/scan_repetition.py README.md AGENTS.md
python scripts/detect_long_sentences.py README.md AGENTS.md --threshold 35
```

These checks are not a substitute for scientific review. They are a harness:
they make repeated editing passes easier to verify.
