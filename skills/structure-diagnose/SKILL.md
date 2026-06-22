---
name: structure-diagnose
description: Diagnose a manuscript section before rewriting. Use when Codex needs to audit section structure, logic continuity, repetition hotspots, terminology drift, or template-like phrasing in LaTeX or Markdown paper drafts, and the correct action is analysis rather than direct rewriting.
---

# Structure Diagnose

## Overview

Produce a section-level diagnosis without rewriting the manuscript. Treat this as a manuscript-review pass, not a style pass. The goal is to surface the highest-value problems before any rewrite changes the evidence structure.
This skill inherits the mandatory execution contract in `../../skills/paper-optimize/SKILL.md`.

## Workflow

1. Confirm the scope.
   Work on one section, subsection, or reviewer comment bundle at a time.
2. Read the governing rules.
   Read `../../skills/paper-optimize/SKILL.md`, `../../AGENTS.md`, and `../../style/paper_optimization_rules.md` before making judgments. Load `../../style/terminology.yml` if terminology drift is part of the task.
3. Build a quick argument map.
   Identify the section's rhetorical job, each paragraph's role, the central claim of each paragraph, and the evidence or citation supporting it.
4. Audit the section without rewriting it.
   Look for structure breaks, logic jumps, evidence gaps, repetition hotspots, and AI-style hotspots.
5. Use deterministic checks when helpful.
   Call `../../scripts/check_terminology.py`, `../../scripts/scan_repetition.py`, or `../../scripts/detect_long_sentences.py` when the problem can be measured instead of guessed.
6. Return a diagnosis only.
   Do not provide rewritten paragraphs unless the user explicitly asks for the next phase.

## Review Lenses

- Section-role fit
  Check whether the section actually performs its intended job. Example failures: introduction reads like a literature dump, results drift into discussion, methods contain justification instead of procedure.
- Claim-evidence alignment
  For each important claim, ask what evidence, citation, figure, table, equation, or assumption supports it. Flag over-claiming, unsupported comparison language, or hidden inference jumps.
- Logic continuity
  Check paragraph sequencing, bridge sentences, causal transitions, and whether the reader can follow why each paragraph appears where it does.
- Definition dependency order
  Check whether local quantities are introduced in an order the reader can follow, and flag places where symbols, implementation choices, or derived quantities appear before their role has been explained.
- Definition-action coupling
  Check whether indicators, switches, or scaling factors are defined together with the quantity they modify when that coupling is the main point the reader needs.
- Information economy
  Identify repeated framing, duplicated definitions, circular summaries, and paragraphs with multiple rhetorical jobs.
- Academic tone quality
  Flag template phrases, empty significance language, overly uniform cadence, and missing hedging where the evidence is narrower than the wording.

## What To Report

- Structural problems: misplaced background, weak paragraph roles, missing bridge sentences, merged section functions, or conclusions appearing too early.
- Logic gaps: unsupported transitions, missing assumptions, unstated comparison criteria, claim jumps, or missing explanation of why a method or result matters.
- Dependency-order gaps: symbols, correction factors, weight functions, or implementation details that appear before the reader has been given the minimum context needed to interpret them.
- Coupling gaps: indicator variables, scaling factors, or switches whose practical action on another quantity is separated too far from their definition.
- Claim-evidence risks: claims with weak support, claims whose support exists but is too far away, and sentences that should cite a figure, table, or reference but currently do not.
- Citation-anchor risks: standard theories, calibrations, influence functions, or parameter linkages invoked without a clear local citation anchor.
- Repetition hotspots: repeated paragraph openings, repeated n-grams, repeated concept explanations, or duplicated section roles.
- AI-style hotspots: empty transitions, generic significance language, overconfident claims without scope limits, or sentences that sound polished but say little.
- Must-keep scientific content: equations, result qualifiers, dataset constraints, parameter settings, boundary conditions, or comparison boundaries that must survive any rewrite.
- Author-confirmation items: any diagnosis that depends on domain intent rather than textual evidence alone.

## Severity Labels

Use these severity labels inside the diagnosis:

- `critical`: distorts the argument or scientific meaning
- `major`: materially weakens review readiness or reader comprehension
- `moderate`: reduces clarity, trust, or section efficiency
- `minor`: style-level issue that can wait until later

## Guardrails

- Do not rewrite during diagnosis.
- Do not collapse diagnosis into line-editing suggestions unless the user explicitly asks for the next phase.
- Do not label a passage `AI-like` just because it is formal; explain the concrete language pattern.
- Treat scientific precision as higher priority than elegance.
- Flag uncertainty explicitly when a logic gap might actually be a missing citation or figure reference.
- Prefer fewer high-signal findings over long laundry lists.

## Output Template

Use this order:

1. Section role summary
2. Structural problems
3. Logic gaps
4. Claim-evidence risks
5. Repetition hotspots
6. AI-style hotspots
7. Must-keep scientific content
8. Author-confirmation items
