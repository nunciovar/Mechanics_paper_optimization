# Mechanics_paper_optimization

力学论文优化系统。

本文档面向导师审阅，汇总了当前论文编辑框架中的所有规则、技能模块（Skills）和工作流程，并附带实际优化示例。

This repository contains a controlled manuscript-revision workflow for mechanics and peridynamics-related scientific papers.

The system is designed to help diagnose, restructure, polish, de-template, compress, and terminology-check manuscript sections without altering scientific meaning or inventing unsupported claims.

## Core Principles

1. Diagnose before rewriting.
2. Preserve scientific meaning before improving fluency.
3. Preserve author intent and evidential scope.
4. Standardize terminology, acronyms, and notation.
5. Keep section roles distinct.
6. Reduce template-like academic phrasing.
7. Flag high-risk scientific claims for author review.

## Directory Layout

```text
paper-optimization-system/
├─ README.md
├─ AGENTS.md
├─ style/
│  ├─ paper_optimization_rules.md
│  ├─ terminology.yml
│  ├─ banned_phrases.txt
│  └─ preferred_patterns.txt
├─ skills/
│  ├─ paper-optimize/
│  ├─ structure-diagnose/
│  ├─ intro-rebuild/
│  ├─ abstract-optimize/
│  ├─ anti-template-rewrite/
│  ├─ redundancy-reduce/
│  ├─ terminology-guard/
│  └─ writing-coach/
├─ scripts/
│  ├─ check_terminology.py
│  ├─ scan_repetition.py
│  └─ detect_long_sentences.py
└─ docs/
   ├─ paper_optimization_skills_inventory.md
   ├─ paper_optimization_system_overview.md
   ├─ skill_rules_and_workflow_for_advisor.md
   └─ acceptance_checklist.md
```

## Skills

- `paper-optimize`: orchestration entry point for manuscript optimization.
- `structure-diagnose`: diagnose section logic before rewriting.
- `intro-rebuild`: rebuild introduction logic.
- `abstract-optimize`: compress and optimize abstracts.
- `anti-template-rewrite`: reduce template-like academic phrasing.
- `redundancy-reduce`: remove self-overlap while preserving section roles.
- `terminology-guard`: enforce terminology, acronym, and notation consistency.
- `writing-coach`: explain writing principles behind edits.

## Typical Workflow

```text
diagnose
  -> rebuild structure if needed
  -> de-template sentence style
  -> reduce redundancy
  -> check terminology and long sentences
  -> return revised text with risk notes
```

## Deterministic Checks

The scripts in `scripts/` provide lightweight checks for terminology drift, repeated phrases, and long sentences.

```bash
python scripts/check_terminology.py
python scripts/scan_repetition.py
python scripts/detect_long_sentences.py
```

Adapt these scripts to the manuscript path and terminology file of each new paper project.
