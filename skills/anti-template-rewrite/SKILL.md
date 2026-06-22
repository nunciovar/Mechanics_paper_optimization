---
name: anti-template-rewrite
description: Rewrite a passage to reduce template-like academic phrasing, empty transitions, and generic significance language while preserving technical meaning and discipline-appropriate tone. Use when a paper section sounds mechanically polished, overly symmetric, or overconfident, but the scientific content itself should remain intact.
---

# Anti Template Rewrite

## Overview

Reduce template flavor by improving argument texture, sentence rhythm, and claim discipline. This skill is for academic de-templating, not for disguising authorship or forcing conversational prose.
This skill inherits the mandatory execution contract in `../../skills/paper-optimize/SKILL.md`.

## Workflow

1. Isolate the passage.
   Work on a paragraph or small section, not the whole paper.
2. Load governing rules.
   Read `../../skills/paper-optimize/SKILL.md`, `../../AGENTS.md`, `../../style/paper_optimization_rules.md`, `../../style/terminology.yml`, and `../../style/banned_phrases.txt` before rewriting.
3. Identify the concrete problem.
   Look for empty transitions, vague significance claims, repeated sentence frames, exaggerated certainty, and low-information sentences.
4. Rewrite with semantic lock.
   Preserve technical meaning, limitations, and quantitative qualifiers while changing only the rhetorical packaging.
5. Check tone against discipline norms.
   Prefer field-appropriate restraint over chatty style.
6. Recheck claim calibration.
   If the revised sentence sounds stronger than the original evidence warrants, reintroduce hedging or scope limits.
7. Rebuild definition-heavy paragraphs by role when needed.
   Prefer the order `purpose -> label or symbol role -> taxonomy -> exceptions -> downstream use` instead of one long explanation-first sentence.
8. Run a narrow terminology or notation check when needed.
   Use `../../scripts/check_terminology.py` if the rewrite touches acronyms, bond families, labels, or notation-sensitive definitions.
9. Return the rewrite with rationale.
   Briefly note which template patterns were removed.

## Patterns To Reduce

- Repeated transitions such as "it is worth noting that" or "it should be noted that"
- Hard pivot words such as "however" when a softer transition or sentence restructuring would read more naturally
- Rigid list-like cadence such as "first, second, finally"
- Generic impact statements without evidence
- Overuse of promotional words such as "novel", "important", or "significant" when the evidence is narrower
- Paragraphs where every sentence has the same length and function
- Sentences that summarize but add no new information
- Overuse of metadiscourse such as "this paper aims to" when the surrounding context already shows the purpose
- Padded definitional frames such as "can thus be identified accordingly", "label X is used to denote", or "for the other case of"
- Long taxonomy sentences that define primary types and negligible exceptions in the same breath
- Introductory wrappers such as "Here" or "The label" when a symbol can be defined directly
- Heavy relative-clause expansions such as "which corresponds to ..." when the same content can be stated more directly

## Patterns To Prefer

- Evidence-first phrasing
- Explicit scope limits
- Concrete comparisons
- Transition by logic rather than by stock connectors
- Sentence length variation that still reads as academic prose
- Direct definitional verbs such as "distinguishes", "identifies", "denotes", and "represents"
- One short sentence per symbol or label when each definition does a different job
- Brief prose restatement of equation mappings such as index ranges when they matter for immediate interpretation
- Short standalone exception sentences after the main taxonomy has been defined
- Direct case-decision-reason sentences for neglected or excluded interaction types
- Definition-plus-action sentences when an indicator variable is primarily used by multiplying, scaling, or switching another quantity
- Cause-condition-result framing when that logic genuinely exists

## Journal-Style Compression Rules

- Prefer shorter, denser sentences when the technical meaning is unchanged.
- For results subsections, use the advisor-style order `object and parameters -> response curves -> field/distribution evidence -> compact summary`.
- For figure-based result paragraphs, inspect the relevant figure assets before rewriting. Match the text to the actual panel order, curve type, field variable, unit, and visible localization pattern.
- When a figure includes both response curves and field maps, describe the curves before damage, stress, or plastic-dissipation fields so that the field evidence supports an already stated macroscopic trend.
- Retain a short paragraph closing sentence when it states the controlling relation, but compress or remove template summaries that only repeat the preceding observations.
- Remove low-information figure narration such as obvious color keys or row/column descriptions when the figure or caption already supplies them.
- Avoid cross-subsection bridge sentences such as `This framework is then used...` unless the sentence carries necessary technical logic; keep the current subsection internally coherent instead.
- Prefer case-based wording over mechanical parameter listing when the cases have clear physical roles, e.g. `parallel`, `off-axis`, and `transverse` orientations.
- Keep the core mechanism chain but trim side details that do not support the result: parameter change, curve trend, field redistribution, and the local control mechanism.
- If CNT-interior values are hidden in the plotted fields to improve visibility, explain this once as a visualization convention, e.g. the CNT field values are omitted from the plots to highlight the surrounding matrix response.
- Treat formulas as the center of gravity; use prose only to define, connect, or constrain them.
- Keep the minimum necessary physical definition sentence before or after a formula when it clarifies the object being defined or the physical meaning of the quantity.
- End every displayed equation with a comma or period according to the sentence structure.
- Prefer standard equation-leading phrases such as `is defined as`, `can be expressed as`, and `is denoted as`.
- Reduce pre-formula scaffolding such as `Accordingly`, `For clarity`, and `In the notation adopted here` unless they are genuinely needed for interpretation.
- Prefer journal-style compression over lecture-note exposition; keep only the minimum prose needed for equation readability.
- When revising technical-method sections, compress explanatory padding before compressing technical definitions.
- Do not remove limiting conditions inside technical definitions when they carry mathematical scope or physical constraints.
- In PD-specific contexts, prefer field-standard formulations such as `domain of the configuration`, `neighborhood`, and `interactions within the horizon`, while retaining more precise continuum-mechanics wording such as `in the deformed configuration` where appropriate.
- When adopting advisor-style revisions, preserve the current unified symbol system unless the advisor explicitly changes notation.
- Terminology and acronym rules take precedence over stylistic imitation of advisor wording unless the advisor explicitly requests a terminology change.
- In CNT results, do not replace the parameter definition `bending offset parameter q` with `curvature`; use `curvature` only for morphology descriptions such as `curved CNT geometry`.
- Use `damage field` for damage cloud maps, `damage bands` for localized damage bands, `bond failure` for PD bond-level failure, and `fracture process` only for broad process-level descriptions.
- Use `3D` directly. At sentence start, use `Figure` rather than `Fig.`, preferably as `Figure~\ref{...}(a)`.
- For label definitions, prefer direct enumeration sentences over layered explanatory clauses.
- In definition-heavy technical paragraphs, open with the modeling purpose, then define labels or symbols, then enumerate the taxonomy, and only then state any negligible or excluded cases.
- When a displayed equation already gives the formal definition, keep the following prose focused on role and mapping rather than re-explaining the same mathematics at lecture-note length.
- Preserve the minimum necessary explanatory sentence when a newly introduced quantity would otherwise appear without a clear role or purpose.
- Define labels first, then describe their later use in the model in a separate short sentence.
- Treat secondary interaction types such as negligible bond families in a short standalone sentence rather than embedding them in the main definition line.
- Order local definitions by dependency whenever possible; avoid explaining a symbol after it has already been used in a way the reader cannot yet parse.
- When a physical property directly motivates a constitutive or failure rule, prefer short causal phrasing such as `due to the large stiffness ..., failure is governed by ...`.
- Prefer compact closing sentences that keep bond-level, point-level, and neighborhood-level quantities distinct in one place.
- Prefer lighter forward-linking phrases such as `can later be used to` over heavier process narration such as `is then used to` when bridging to the next subsection.
- When an implementation-specific sentence appears inside a derivation, briefly state why that implementation detail is needed at that point.
- When standard theory, calibration, or constitutive linkage is invoked locally, check whether a citation anchor should be kept or added in the same local context.
- After each local rewrite, recheck whether the next sentence merely repeats information that has already been stated without adding new value.

## Claim And Hedging Rules

- Strong claim plus narrow evidence requires scope language.
- If the statement is interpretive rather than directly observed, make that distinction visible.
- Replace broad evaluative praise with a specific methodological or empirical judgment.
- Keep discipline-appropriate hedging; do not erase uncertainty to improve fluency.

## Guardrails

- Do not use this skill as a substitute for structure diagnosis when the real problem is paragraph logic or section-role confusion.
- Do not randomize synonyms.
- Do not make the prose colloquial.
- Do not weaken necessary technical precision just to sound less uniform.
- If a sentence is strong because the evidence is strong, keep it strong.
- Use `../../style/banned_phrases.txt` as a warning list, not a blind search-and-replace list.

## Output Template

1. Revised passage
2. Removed template patterns
3. Claim-calibration notes
4. Open questions or risk notes
