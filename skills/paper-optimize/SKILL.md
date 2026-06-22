---
name: paper-optimize
description: Orchestrate any paper-optimization request under the repository's full manuscript-editing constitution. Use when the user asks to optimize, revise, polish, diagnose, de-template, compress, or align any manuscript passage in LaTeX or Markdown and the task may require choosing or sequencing multiple paper-editing phases.
---

# Paper Optimize

## Overview

This skill is the default entry point for manuscript optimization in this repository. It does not replace the narrower skills. Instead, it enforces the shared execution contract that every paper-editing task must follow before any local rewrite, diagnosis, or polishing step begins.

## Mandatory Execution Contract

Before doing any paper-editing task, always:

1. Load the governing rules.
   Read `../../AGENTS.md`, `../../style/paper_optimization_rules.md`, `../../style/terminology.yml`, and `../../style/banned_phrases.txt`.
2. Confirm the local scope.
   Default to one section, subsection, paragraph, reviewer-comment bundle, or figure-caption bundle at a time unless the user explicitly asks to combine scopes. However, allow whole-manuscript comparison or scanning when the local decision depends on global consistency, such as first-use acronym checks, prior definitions, repeated explanations, terminology drift, or cross-section redundancy.
3. Choose the phase before editing.
   Explicitly decide whether the request is diagnosis, section rebuild, sentence-level de-templating, redundancy reduction, rule check, or acceptance output.
4. Apply cumulative rules.
   Combine non-conflicting global, section-specific, terminology, notation, and advisor-preference rules rather than following only one local heuristic.
5. Preserve scientific meaning first.
   Do not trade away meaning, numerical fidelity, notation integrity, or claim scope for smoother phrasing.
6. Flag author-confirmation items.
   Numbers, units, equation meanings, figure and table references, novelty claims, causal claims, prior-work comparisons, and assumption-dependent claims must be preserved carefully and flagged when uncertain.
7. Return results in the repository's required order.
   Diagnosis tasks must follow the diagnosis output contract. Rewrite tasks must follow the substantial-edit output contract.

## Phase Selection Rules

- Use `structure-diagnose` when the user asks what is wrong, what changed, or what should be fixed before rewriting.
- Use `intro-rebuild` when the introduction has the right raw content but weak paragraph logic or contribution placement.
- Use `abstract-optimize` when the scope is the abstract.
- Use `anti-template-rewrite` when the structure is already acceptable and the main problem is mechanical or generic academic phrasing.
- Use `redundancy-reduce` when the core issue is self-overlap within or across adjacent sections.
- Use `terminology-guard` before or after local rewrites when terminology, acronyms, notation, or bond-taxonomy consistency is at risk.
- Use `writing-coach` concurrently with any diagnosis or rewrite skill to embed educational explanations that teach the user the linguistic, grammatical, and rhetorical reasoning behind each edit.

When a request spans multiple phases, sequence them rather than collapsing them by default:

1. Diagnose
2. Rebuild structure if needed
3. De-template sentences
4. Reduce redundancy
5. Check rules
6. Return acceptance-style output

## Advisor-Preference Rules
- Give the highest stylistic priority to the shortest wording that states the technical meaning clearly and correctly.
- Do not add explanatory or bridge sentences for standard or obvious post-processing steps unless they are necessary to prevent ambiguity.
- When splitting a compressed sentence, expand only to the minimum number of sentences needed to make the logic explicit.
- If a sentence is already concise and unambiguous, leave it unchanged rather than rewriting it for polish.

- Prefer concise journal-style compression over lecture-note exposition when the scientific meaning is unchanged.
- Prefer subsection titles that directly state the local function or operation, rather than broader labels that merge multiple tasks.
- When choosing between a more explicit title and a shorter functional title, prefer the shorter functional title if it still identifies the local task unambiguously.
- Subsection-title brevity has the highest priority in advisor-style revision. If a short title is already clear, do not expand it into a longer function-heavy title.
- Preserve established local section titles such as `Single-CNT Architecture` when they are already clear and consistent with surrounding sections.
- When describing waviness in this manuscript, use the bending offset parameter `q` rather than recasting it as curvature radius unless an explicit geometric conversion is required.
- In subsection titles, prefer fully spelled technical nouns when abbreviation is not necessary for clarity.
- Subsection and subsubsection titles should default to the shortest functional form that remains clear; avoid expanding titles into effect summaries when a concise label such as `Effect of Orientation` is sufficient.
- When the manuscript has already established `Single-CNT Architecture` as the parent subsection title, preserve that concise title rather than expanding it into longer alternatives.
- In the current manuscript, use `q` consistently as the bending-offset parameter for CNT waviness; do not relabel it as waviness severity or replace it with a curvature-radius description unless the author explicitly changes the parameter system.
- In methods sections, open by stating what object, model, or algorithm is constructed or adopted for the present analysis, rather than relying on meta-discourse such as `This subsection defines`.
- For standard numerical algorithms, prefer a compact introduction of the form `was solved using ...` or `is integrated with ...`, followed immediately by the governing update equations.
- When a subsection defines simulation objects, check whether the basic setup is complete: object classes, controlling parameters, domain size, boundary geometry, and generation range should be stated when relevant.
- When multiple object classes are introduced together, state explicitly what analytical role each class serves in the paper.
- Keep the parameter system aligned with later results sections. If a methods parameter and a results parameter are not obviously identical, either state the mapping explicitly or flag the mismatch instead of smoothing over it.
- Treat notation-system consistency as a global rule, especially for time-step or iteration-step indices; the position and style of time-like indices should remain uniform throughout the manuscript.
- Prefer standard process-style method prose such as `is defined as`, `was monitored`, `is updated as`, and `was solved using`.
- When a formula introduces a global quantity or control parameter, ensure definitional closure by checking four things: citation/source, summation or index scope, algorithmic role, and parameter value or limit if used later.
- If a parameter is assigned a specific numerical value in the text, give its functional role in a separate sentence rather than burying it inside a longer parameter list.
- Avoid packing parameter definitions, algorithm rules, and figure transitions into one sentence; one sentence should usually serve one primary rhetorical job.
- In method sections, prioritize methodological closure over stylistic elegance. If a sentence must choose between sounding smoother and making the setup reproducible, prefer the more reproducible version.
- In advisor-style revision mode, prefer implementation-driven prose over commentary-driven prose. Describe what was generated, imposed, solved, monitored, or updated before explaining why.
- Do not default to explanatory expansion. For standard methods, give the method name, citation, governing formula, and required parameter definitions, but avoid extra algorithm praise or tutorial-style exposition unless the local passage truly needs it.
- Prefer short, declarative method sentences over polished summary sentences. Replace broad framing such as `This subsection defines...` with direct procedural statements when possible.
- Distinguish fixed specifications from varying descriptors explicitly. Fixed geometric or numerical settings should not be presented as independent design parameters.
- When a local passage is mainly about generation or implementation, prefer `object or method -> descriptors or controls -> generation or update rule -> safeguard or exclusion rule` as the default ordering.
- When a passage introduces a commonly used numerical method, cite a recent domain-relevant paper if available rather than defaulting to the oldest canonical source, unless historical priority is itself important.
- When imitating advisor revisions, reduce interpretive commentary around standard formulas. The default is `equation first, short role sentence second`.
- In method paragraphs, minimize evaluative wording such as `superior`, `beneficial`, `robust`, or `efficient` unless the sentence is explicitly making a comparison supported in the text.
- If the advisor's edits reveal unresolved technical uncertainty, preserve the uncertainty as an explicit question or flagged item rather than silently harmonizing the text.
- In definition-heavy method passages, prefer `modeling purpose -> label or symbol role -> value mapping or taxonomy -> downstream use`.
- Prefer one short sentence per symbol or label when each symbol carries a distinct definitional job.
- If an equation introduces an index range or value mapping needed for interpretation, restate that mapping briefly in the prose instead of leaving it only in the displayed equation.
- Preserve the minimum necessary explanatory sentence when a newly introduced quantity would otherwise appear without a clear role, purpose, or physical function.
- When an indicator variable is introduced mainly through its action on another quantity, prefer defining the indicator together with that action in one sentence.
- Prefer direct definitional verbs such as `distinguishes`, `identifies`, `denotes`, and `represents`.
- Prefer direct enumeration for bond-family definitions rather than padded frames such as `label X is used to denote`.
- State negligible or excluded interaction types in a short standalone sentence after the main taxonomy has been defined.
- In exception sentences, prefer the order `case -> decision -> reason` and avoid heavy relative-clause expansions when a shorter direct statement is sufficient.
- If a local symbol such as `n` already carries another common meaning, choose a less collision-prone symbol such as `m`.
- Order local definitions by dependency whenever possible; avoid explaining or emphasizing a symbol before the reader has been given the minimum context needed to interpret it.
- Make the interface to the next method step explicit when a definition feeds the constitutive law, force state, failure criterion, solver, or later subsection.
- When introducing that next-step interface, prefer lighter forward-linking phrasing such as `can later be used to` unless process chronology itself is important.
- When a sentence introduces an implementation choice, briefly state why that implementation detail appears at that point in the derivation.
- When a sentence relies on a standard theory, calibration, constitutive relation, weight function, or parameter linkage taken from prior work, check whether a citation should be attached locally rather than assumed globally.
- When a material property directly motivates a failure mode or constitutive choice, prefer explicit cause-to-model wording such as `due to ... , failure is governed by ...`.
- When a quantity is derived from fracture energy, yield data, or another higher-level input, prefer direct `derived from` phrasing over longer explanatory detours.
- When several quantities differ only by scale or role, prefer a single closing sentence that keeps them distinct rather than scattering that distinction across multiple sentences.
- In overview or summary sentences, prefer the concrete object names already established locally rather than switching to a new abstract label for the same object.
- State global specifications once in the subsection overview, then reserve local subsection lists or prose for descriptors, generation rules, or other differentiating features.
- When multiple object classes are introduced together, state explicitly what analytical role each class serves.
- Do not force numerals into boldface for global consistency; numeral styling should follow the local notation system and standard mathematical typography.

## Advisor-Derived Results-Section Rules
- Prefer short, object-focused subsection titles when the object is unambiguous, e.g. `Single-CNT` can be preferred over `Single-CNT Architecture` when the local context already establishes the architecture frame.
- Results subsections should open with the studied object, adjusted parameters, and the physical dimension probed by each parameter; avoid front-loading long mechanism explanations.
- Do not add or preserve cross-subsection bridge sentences unless they carry essential logic. Prioritize internal continuity within the current subsection; the next subsection can establish its own transition.
- For figures that contain both curves and field/distribution plots, discuss the curves first, then the damage/stress/plastic-dissipation fields, and close with a compact mechanism or control-mode summary.
- Before optimizing prose that interprets a figure, inspect the corresponding figure assets whenever available. Do not infer curve trends, panel ordering, field-variable names, units, or spatial localization from prose alone.
- Keep paragraph-level summary sentences when they help close a result unit, but compress them to the controlling relation rather than restating every observed feature.
- Delete low-information figure narration, especially color keys, row/column descriptions, or visual details that are obvious from the figure or already stated in the caption.
- Use case-based grouping to reduce repetition: `parallel`, `off-axis`, and `transverse` for orientation; `straight` and `curved` or larger-`q` cases for bending; `full-spanning` and finite-length/non-through-going cases for continuity.
- Preserve core mechanism terms when supported by the results, such as alignment, axial bridging, deformation redistribution, geometric continuity, damage field, and bond failure.
- When field plots omit or mask CNT-interior values for visualization, state this once before interpreting the fields, and describe it as a plotting/visualization choice rather than a physical absence of response.
- In this manuscript, use `bending offset parameter q` for the parameter definition. Use `curvature` or `curved CNT geometry` only as morphology description, not as a replacement for the parameter name.
- Use `damage field` for damage-variable contours or cloud maps, `damage evolution` for process over loading, `damage bands` for localized bands, `bond failure` for PD bond-level failure, and `fracture process` only for broader macroscopic process descriptions.
- Use `3D` directly when needed. At sentence start, spell figure references as `Figure`; use LaTeX spacing such as `Figure~\ref{...}(a)`.

## Global Guardrails

- Do not optimize unrelated sections "for consistency" unless the user asks.
- Do not invent experiments, data, citations, equations, mechanisms, or stronger claims.
- Do not silently rename symbols, labels, or figure references unless notation cleanup is explicitly in scope.
- Do not combine diagnosis and rewriting unless the user asks or the task clearly requires both.
- Do not imitate advisor wording mechanically when that would violate terminology, notation, or evidential scope.

## Output Contract

For diagnosis tasks:

1. Structural problems
2. Logic gaps
3. Repetition hotspots
4. AI-style hotspots
5. Must-keep scientific content

For rewrite tasks:

1. Revised text
2. Change notes
3. Open questions
4. High-risk lines not auto-changed













