---
name: abstract-optimize
description: Optimize a paper abstract for high-level academic journals while preserving scientific meaning, numerical fidelity, terminology consistency, and scope control. Use when Codex needs to diagnose, rewrite, or quality-check an abstract in LaTeX or Markdown for clearer structure, tighter logic, higher information density, and less template-like phrasing without adding unsupported claims.
---

# Abstract Optimize

## Overview

Treat abstract editing as controlled scientific compression, not as general polishing. Preserve meaning, evidence scope, and section function before improving flow.
This skill inherits the mandatory execution contract in `../../skills/paper-optimize/SKILL.md`.

## Workflow

1. Confirm the scope.
   Work on the abstract only unless the user explicitly extends the task.
2. Load governing rules.
   Read `../../skills/paper-optimize/SKILL.md`, `../../AGENTS.md`, `../../style/paper_optimization_rules.md`, `../../style/terminology.yml`, and `../../style/banned_phrases.txt` before rewriting.
3. Diagnose before rewriting.
   Identify structure problems, logic gaps, repetition hotspots, AI-style hotspots, and must-keep scientific content.
4. Build the target abstract map.
   Reorganize the abstract into background, focused gap, study objective, method or main finding, key results, and scoped significance.
5. Rewrite with semantic lock.
   Improve structure, sentence rhythm, and information density without changing scientific claims, numbers, limitations, or evidential scope.
6. Run narrow checks when helpful.
   Prefer `../../scripts/check_terminology.py` and `../../scripts/detect_long_sentences.py` for local validation.
7. Return the rewrite with risk notes.
   Always separate the revised abstract from the rationale and the author-confirmation items.

## Required Priorities

Apply these priorities in order:

1. Scientific correctness
2. Fidelity to author intent
3. Terminology consistency
4. Internal abstract logic
5. Concision and style polish

If smoother wording would weaken, strengthen, or broaden the scientific claim, keep the original meaning and flag the risk.

## Target Abstract Structure

Default to this order unless the venue clearly requires another pattern:

1. Use 1 to 2 sentences to establish the broad field problem and immediate context.
2. Use 2 to 3 sentences to narrow the background and expose the unresolved limitation, missing mechanism, or modeling gap.
3. Use 1 sentence to state the study objective or core problem being solved.
4. Use 1 sentence to summarize the main method, result, or take-home finding.
5. Use 2 to 3 sentences to present the most important results and explain what they clarify relative to prior understanding.
6. Use 1 to 2 sentences to state broader significance, methodological value, or engineering relevance without promotional overreach.

Keep the abstract focused on one rhetorical job: high-density orientation plus the paper's core findings.

## Language Rules

- Prefer academic, restrained, discipline-appropriate prose.
- Avoid stock openers such as `In this paper`, `It is worth noting that`, and `In conclusion`.
- Prefer concrete statements over vague praise or generic significance language.
- Transition by logic, not by filler connectors.
- Compress repeated framing before cutting technical detail.
- Vary sentence function and cadence enough to avoid template-like symmetry.
- Preserve author terminology from `../../style/terminology.yml`.
- Prefer `architecture` or `configuration` over `topology` when describing fiber arrangement if that matches the author's preferred framing.
- Avoid acronyms in the abstract unless they are defined on first use within the abstract itself; when in doubt, spell the term out.
- If the author prefers, keep key material-system terms fully spelled out throughout the abstract rather than introducing acronyms that are used only locally.
- Name the framework explicitly in the abstract when that named framework is a central contribution, but keep the description at the framework level rather than enumerating implementation details.
- Keep method description at the level needed to orient the reader; do not enumerate implementation-level bond families, solver steps, or submodules in the abstract unless that detail is central to the paper's main contribution.

## Scientific Guardrails

- Do not invent data, experiments, equations, citations, mechanisms, or novelty claims.
- Do not write model assumptions as if they were experimentally verified facts.
- Do not convert simulated trends into universal physical laws.
- Do not blur numerical conditions, parameter ranges, or applicability limits.
- Do not overstate causal claims, superiority claims, or generality.
- Do not introduce new terminology unless the manuscript already supports it.

## Domain-Specific Caution For Mechanics And Materials Abstracts

When the paper concerns materials, mechanics, simulation, multi-scale modeling, CNT/epoxy systems, peridynamics, or related engineering topics:

- Distinguish observed response, modeled interpretation, and broader implication.
- Keep architecture/configuration, interface effects, damage evolution, and toughening mechanisms within the evidence actually shown.
- Use hedging when a mechanism is inferred rather than directly measured.
- Preserve the exact scope of comparisons against prior work and against other architectures/configurations, load cases, or parameter settings.

## Output Order

Use this order for substantive abstract work:

1. Original abstract diagnosis
2. Optimized abstract, main recommended version
3. Optimized abstract, shorter version if useful
4. Modification notes
5. High-risk points requiring author confirmation

For the diagnosis section, explicitly cover:

- Structure problems
- Logic problems
- Repetition or redundancy
- AI-style or template-style hotspots
- Must-keep scientific content

## Guardrails

- Do not skip the diagnosis step unless the user explicitly asks for a rewrite-only pass.
- Do not rewrite unrelated sections for consistency.
- Do not remove key qualifiers merely to shorten the abstract.
- Do not use synonym swapping as the main editing strategy.
- Do not oversell the venue fit by imitating marketing-heavy prose.
- If the abstract is already scientifically careful, prefer structural refinement over stylistic reinvention.
