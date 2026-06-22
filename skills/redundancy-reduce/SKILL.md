---
name: redundancy-reduce
description: Compress repetitive wording and self-overlap within or across paper sections while preserving each section's rhetorical job. Use when a manuscript repeats the same explanation, sentence frame, or claim across abstract, introduction, results, discussion, or conclusion and needs a scoped, author-safe reduction pass.
---

# Redundancy Reduce

## Overview

Reduce self-repetition without flattening the manuscript into one repeated summary. This skill should preserve the division of labor between sections while trimming unnecessary overlap and keeping the scientific thread intact.
This skill inherits the mandatory execution contract in `../../skills/paper-optimize/SKILL.md`.

## Workflow

1. Load governing rules.
   Read `../../skills/paper-optimize/SKILL.md`, `../../AGENTS.md`, `../../style/paper_optimization_rules.md`, `../../style/terminology.yml`, and `../../style/banned_phrases.txt` before rewriting.
2. Define the comparison set.
   Compare within one section or between two adjacent sections such as abstract vs introduction or results vs conclusion.
3. Identify duplicated content.
   Look for repeated claims, repeated definitions, repeated sentence frames, and repeated paragraph openings.
4. Classify each overlap.
   Decide whether the overlap is necessary reinforcement, section-role overlap, or true redundancy.
5. Preserve role-specific overlap.
   Allow brief restatement when two sections have different rhetorical jobs.
6. Compress locally.
   Remove or shorten the redundant passage with minimal change to surrounding logic.
7. Return the revised text plus what was intentionally kept.
8. Compile after edits when feasible.
   After applying redundancy reductions to the manuscript source, compile `../../first Article_latex/els-cas-templates/cas-dc-sample.tex` unless the user explicitly says not to.

## Keep vs Remove

Keep:

- Short reminders needed for continuity
- Result statements that must reappear in a conclusion, but in shorter form
- Definitions required at first use in a new major section
- Brief overlap that helps a section perform its own job

Remove or compress:

- Repeated concept explanations with no added nuance
- Near-duplicate topic sentences
- Stock transitions repeated across consecutive paragraphs
- Summary sentences that restate the immediately preceding sentence
- Long passages that restate the same claim with no new qualifier, evidence, or interpretive value

## Cross-Section Rules

- `abstract` should present the problem, approach, and main outcome briefly, not duplicate the introduction.
- `introduction` should motivate and position the work, not pre-discuss all results.
- `results` should present what was found.
- `discussion` should interpret what the results mean.
- `conclusion` should compress takeaways, not replay the full argument.

## Helpful Checks

Use `../../scripts/scan_repetition.py` before rewriting when the overlap is broad or hard to judge quickly.

## Guardrails

- Do not use redundancy reduction to bypass unresolved logic gaps or weak paragraph structure.
- Do not cut distinctions that separate results from interpretation.
- Do not compress away methodological qualifiers.
- Do not remove repeated content if it is the only location where a citation anchor or scope limit appears.
- Prefer surgical deletions or mergers over global flattening rewrites.

## Output Template

1. Revised text
2. Redundancies removed
3. Intentional overlap retained
4. Section-role notes
5. Open questions
