---
name: intro-rebuild
description: Rebuild an introduction around background, gap, objective, method overview, and contribution placement. Use when a paper introduction in LaTeX or Markdown has the right raw content but weak flow, blurred section roles, or unclear motivation, and Codex should rewrite only the introduction rather than the full manuscript.
---

# Intro Rebuild

## Overview

Rebuild the introduction as a staged argument, not as a general-purpose style pass. This skill is strongest when the raw content is already present but the reader cannot clearly see the progression from field context to research gap to contribution.
This skill inherits the mandatory execution contract in `../../skills/paper-optimize/SKILL.md`.

## Workflow

1. Load governing rules.
   Read `../../skills/paper-optimize/SKILL.md`, `../../AGENTS.md`, `../../style/paper_optimization_rules.md`, `../../style/terminology.yml`, and `../../style/banned_phrases.txt` before rewriting.
2. Diagnose before rewriting.
   Identify which paragraph currently tries to do background, related work, gap, objective, method overview, and contribution placement.
3. Build a target logic map.
   Decide what each paragraph should do before writing any new prose.
4. Preserve the scientific anchors.
   Keep citations, terminology, core method names, and result qualifiers that the introduction needs to foreshadow.
5. Reorder before embellishing.
   Fix paragraph roles and transitions first. Tighten sentence-level style only after the paragraph logic is stable.
6. Calibrate the literature positioning.
   Present prior work fairly, show the real limitation or unresolved issue, and avoid straw-man framing.
7. Keep boundaries clear.
   Do not rewrite references, figure captions, results discussion, or terminology globally as part of this skill.
8. Run narrow checks when helpful.
   Use `../../scripts/check_terminology.py`, `../../scripts/scan_repetition.py`, or `../../scripts/detect_long_sentences.py` when the local introduction problem can be measured.
9. Return a controlled rewrite.
   Provide the revised introduction plus a short note explaining how each paragraph role changed.

## Introduction Logic

- Paragraph 1: establish the field problem and why it matters within the discipline.
- Paragraph 2: summarize what prior work already solved.
- Paragraph 3: expose the remaining gap or methodological limitation.
- Paragraph 4: state the study objective and the paper's approach.
- Paragraph 5: place the contribution without overselling it.

If the introduction is shorter, merge adjacent jobs carefully. Do not drop the gap or objective.

## Contribution Placement Rules

- State the contribution after the gap is clear, not before.
- Phrase the contribution as a scoped advance, not as a universal breakthrough.
- If the paper has multiple contributions, rank them and make one primary contribution explicit.
- Mention results only at a high level when they help clarify what the study delivers.

## Related-Work Guardrails

- Summarize prior work by problem and limitation, not by name-dropping alone.
- Do not overstate deficiencies in prior literature to create an artificial gap.
- Keep citations attached to the claims they support.
- Prefer paragraph restructuring over blunt transition words such as `however` when moving from prior work to the paper's gap.

## Heading Rules

- Keep subsection and subsubsection titles short, parallel, and structurally symmetric across the same level.
- Prefer journal-style headings over lecture-note headings when the scientific scope is unchanged.
- When revising a section, check whether adjacent headings at the same level should be optimized together for symmetry and consistency.
- Apply non-conflicting style, terminology, and structure rules cumulatively; do not optimize body text while ignoring heading quality.

## Guardrails

- Do not skip the paragraph-role diagnosis step unless the user explicitly asks for rewrite-only execution.
- Do not inflate novelty claims.
- Do not turn the introduction into a mini literature review dump.
- Do not import detailed results into the introduction unless they are needed to state the contribution at a high level.
- Use author-provided terminology from `../../style/terminology.yml` where relevant.
- If the introduction depends on unresolved scientific claims, leave them marked for author review instead of smoothing them over.

## Journal-Style Compression Rules

- Prefer shorter, more direct sentences when the scientific scope is unchanged.
- Let the argument structure carry the transition; avoid extra metadiscourse when paragraph logic is already clear.
- Prefer standard research-paper formulations such as `is defined as`, `can be expressed as`, and `is denoted as` when introducing technical objects.
- Reduce scaffolding phrases such as `Accordingly`, `For clarity`, and `In the notation adopted here` unless they prevent ambiguity.
- Keep the tone closer to journal prose than to lecture notes; remove explanatory padding before removing scientific qualifiers.

## Output Template

1. Revised introduction
2. Before/after paragraph-role map
3. Open questions
4. High-risk lines left unchanged
