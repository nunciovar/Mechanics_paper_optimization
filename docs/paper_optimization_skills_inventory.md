# Paper Optimization Skills Inventory

This document lists the reusable skills and support files that make up the
mechanics-oriented paper-optimization harness.

Status labels:

- `Stable`: safe as a regular entry point.
- `Beta`: usable but still expected to evolve with real paper edits.
- `Draft`: newly introduced or not yet validated across multiple projects.

## Core Files

| File | Status | Use case | Inputs | Outputs |
| --- | --- | --- | --- | --- |
| `AGENTS.md` | Stable | Repository-level editing constitution | User request, project scope | Operating rules and guardrails |
| `PROJECT_CONFIG.example.yml` | Beta | Template for per-paper paths and checks | Project-specific paths | `PROJECT_CONFIG.yml` copy |
| `style/terminology.yml` | Beta | Canonical terms and acronym checks | Project terminology | Terminology rules |
| `style/banned_phrases.txt` | Beta | Warning list for template-like prose | Phrase list | Script-readable warnings |
| `review/templates/terminology_ledger.md` | Draft | Lock terminology before major rewriting | Project terms and symbols | Canonical terminology ledger |

## Skills

| Skill | Status | Use case | Trigger words | Inputs | Outputs |
| --- | --- | --- | --- | --- | --- |
| `paper-optimize` | Beta | Router for scientific manuscript optimization | optimize, revise, polish, diagnose, compress, de-template | User request, `manifest.yaml`, shared core, selected fragments | Routed editing plan or scoped edit |
| `structure-diagnose` | Beta | Diagnose section logic before rewriting | diagnose, what is wrong, logic, structure | Manuscript section, rules | Structural problems and risks |
| `intro-rebuild` | Beta | Rebuild introduction flow | introduction, gap, contribution, background | Introduction draft | Rebuilt introduction and notes |
| `abstract-optimize` | Beta | Compress and calibrate abstracts | abstract, concise, summarize | Abstract draft | Revised abstract and high-risk notes |
| `anti-template-rewrite` | Beta | Reduce template-like academic phrasing | AI-like, template, polish, de-template | Stable passage | Revised passage and change notes |
| `redundancy-reduce` | Beta | Remove self-overlap while preserving section roles | repeated, redundant, overlap, compress | One or more sections | Redundancy reductions and retained overlap |
| `terminology-guard` | Beta | Guard terminology, acronym, and notation consistency | terminology, acronym, notation, consistent | Text plus terminology rules | Issues, narrow fixes, ambiguities |
| `writing-coach` | Draft | Explain writing principles behind edits | explain, teach, why edit | Revision or diagnosis task | Writing lessons and reusable rules |
| `mechanics-reviewer` | Draft | Pre-submission reviewer-style assessment | reviewer, pre-submission, technical risks, validation | Manuscript excerpt, visible evidence | Three-reviewer assessment and synthesis |

## Shared Core Layer

| File | Status | Use case | Inputs | Outputs |
| --- | --- | --- | --- | --- |
| `skills/_shared/core/stance.md` | Draft | Shared editorial stance | Any skill task | Non-invention and fidelity rules |
| `skills/_shared/core/workflow.md` | Draft | Shared loop workflow | User request and scope | Inspect-diagnose-edit-verify loop |
| `skills/_shared/core/output-format.md` | Draft | Shared output contracts | Task phase | Required response structure |
| `skills/_shared/core/qa-checklist.md` | Draft | Final safety check | Proposed edit or assessment | Non-invention checklist |
| `skills/_shared/core/terminology-ledger.md` | Draft | Terminology locking workflow | Project terms | Ledger-use rules |

## Router Fragments

The `paper-optimize` router uses `skills/paper-optimize/manifest.yaml` to load
only relevant fragments:

- phase fragments: diagnose, rebuild, polish, redundancy, terminology, acceptance
- section fragments: abstract, introduction, methods, results, discussion, conclusion
- domain fragments: mechanics, peridynamics, CNT/epoxy, advisor style, generic
- language fragments: Chinese academic, Chinese-to-English, English polish

## Deterministic Scripts

| Script | Status | Use case | Trigger words | Inputs | Outputs |
| --- | --- | --- | --- | --- | --- |
| `scripts/check_terminology.py` | Beta | Check mixed variants, banned phrases, acronym first use | terminology, banned phrases, acronym | Text files, terminology file | Console findings |
| `scripts/scan_repetition.py` | Beta | Report repeated openers and n-grams | repetition, redundancy | Text files | Repetition hotspots |
| `scripts/detect_long_sentences.py` | Beta | Report sentences above word threshold | long sentence, readability | Text files | Long sentence list |

## Recommended Minimal Upload

For a new project, keep at least:

- `AGENTS.md`
- `PROJECT_CONFIG.example.yml`
- `style/`
- `skills/_shared/core/`
- `skills/paper-optimize/`
- `skills/structure-diagnose/`
- `skills/anti-template-rewrite/`
- `skills/terminology-guard/`
- `scripts/`
- `docs/codex_workflow.md`
- `review/templates/`
