# Paper Optimization Rules

This file consolidates the active manuscript-revision rules used in this repository.
Use it as the quickest reference before diagnosing, rewriting, or polishing any paper section.

## Quick Reference

1. Keep scientific correctness above fluency.
2. Preserve author intent before stylistic improvement.
3. Standardize terminology and acronyms according to `style/terminology.yml`.
4. Work in phases: diagnose first, then rebuild or polish.
4a. Apply non-conflicting manuscript rules cumulatively rather than selectively.
5. Treat equations as the center; keep prose minimal and functional around them.
6. Prefer concise journal-style sentences and standard technical phrases such as `is defined as`, `can be expressed as`, and `is denoted as`.
7. Reduce scaffolding phrases such as `Accordingly`, `For clarity`, and `In the notation adopted here` unless they are necessary.
8. Do not invent data, citations, equations, mechanisms, or stronger claims.
9. Flag high-risk items for author review: numbers, symbols, cross-references, causal/novelty claims, and prior-work comparisons.
10. Keep section roles distinct: abstract orients, introduction motivates, methods define, results report, discussion interprets, conclusion compresses.

## 1. Core Priorities

Apply these priorities in order:

1. Scientific correctness
2. Fidelity to the author's intent
3. Terminology consistency
4. Section logic and rhetorical flow
5. Concision and style polish

If smoother wording would weaken, broaden, or alter the scientific claim, keep the scientific version and flag the risk.

## 2. Workflow Stages

Handle paper work in stages unless the user explicitly asks to combine them:

1. Diagnosis: identify problems only; do not rewrite
2. Section rebuild: rewrite one section for structure only
3. Sentence-level de-templating: reduce template phrasing while preserving meaning
4. Redundancy reduction: remove self-overlap without flattening section roles
5. Rule check: run deterministic checks
6. Acceptance output: present revised text, rationale, open questions, and high-risk items

Default to one section or one task at a time, not the full manuscript.
You may still scan the full manuscript when the local edit depends on global consistency, such as acronym first use, prior definitions, repeated explanation, terminology drift, or cross-section redundancy.

## 3. Allowed And Disallowed Edits

### Allowed

- Reorder sentences or paragraphs within the requested scope
- Tighten wording, remove empty transitions, and compress repetition
- Standardize terminology according to `style/terminology.yml`
- Adjust claim strength with more appropriate hedging when the evidence appears narrower than the phrasing
- Mark places that need citation, data confirmation, or author review

### Disallowed

- Do not invent data, experiments, citations, equations, or numerical results
- Do not change scientific meaning to improve fluency
- Do not silently add novelty claims, broad impact claims, or unsupported certainty
- Do not rewrite unrelated sections "for consistency" unless asked
- Do not perform paraphrasing meant to evade academic integrity checks
- Do not auto-resolve ambiguous terminology when two technical meanings are plausible; flag it

## 4. High-Risk Items

Treat these as author-confirmation items unless direct edits are explicitly requested:

- Numerical values, units, and thresholds
- Equation definitions and symbol meanings
- Figure/table numbering and cross-references
- Causal claims, novelty claims, and limitation statements
- Comparisons against prior work
- Any sentence whose meaning depends on unstated experimental assumptions

## 5. Output Contract

### For substantial paper edits

1. Revised text
2. Change notes
3. Open questions
4. High-risk lines not auto-changed

### For diagnosis tasks

1. Structural problems
2. Logic gaps
3. Repetition hotspots
4. AI-style hotspots
5. Must-keep scientific content

## 6. Global Style Policy

- Prefer field-appropriate academic prose over generic "polished" prose
- Reduce template phrases, but do not force conversational wording
- Prefer concrete academic judgments over vague praise
- Use restraint in transitions such as `notably`, `it should be noted`, and `in conclusion`
- Keep abstract, introduction, results, discussion, and conclusion functionally distinct

## 7. Journal-Style Compression Rules
- Give the highest stylistic priority to the shortest wording that states the technical meaning clearly and correctly
- Do not add explanatory or bridge sentences for standard or obvious post-processing steps unless they are necessary to prevent ambiguity
- When splitting a compressed sentence, expand only to the minimum number of sentences needed to make the logic explicit
- If a sentence is already concise and unambiguous, leave it unchanged rather than rewriting it for polish

These rules were added to capture the preferred "advisor revision" style and now apply across paper optimization work:

- Prefer shorter, denser sentences when the technical meaning is unchanged
- Prefer subsection titles that directly state the local function or operation, rather than broader labels that merge multiple tasks
- When choosing between a more explicit title and a shorter functional title, prefer the shorter functional title if it still identifies the local task unambiguously
- Subsection-title brevity has the highest priority in advisor-style revision. If a short title is already clear, do not expand it into a longer function-heavy title
- Preserve established local section titles such as `Single-CNT Architecture` when they are already clear and consistent with surrounding sections
- When describing waviness in this manuscript, use the bending offset parameter `q` rather than recasting it as curvature radius unless an explicit geometric conversion is required
- In subsection titles, prefer fully spelled technical nouns when abbreviation is not necessary for clarity
- Subsection and subsubsection titles should default to the shortest functional form that remains clear; avoid expanding titles into effect summaries when a concise label such as `Effect of Orientation` is sufficient
- When the manuscript has already established `Single-CNT Architecture` as the parent subsection title, preserve that concise title rather than expanding it into longer alternatives
- In the current manuscript, use `q` consistently as the bending-offset parameter for CNT waviness; do not relabel it as waviness severity or replace it with a curvature-radius description unless the author explicitly changes the parameter system
- In methods sections, open by stating what object, model, or algorithm is constructed or adopted for the present analysis, rather than relying on meta-discourse such as `This subsection defines`
- For standard numerical algorithms, prefer a compact introduction of the form `was solved using ...` or `is integrated with ...`, followed immediately by the governing update equations
- When a subsection defines simulation objects, check whether the basic setup is complete: object classes, controlling parameters, domain size, boundary geometry, and generation range should be stated when relevant
- When multiple object classes are introduced together, state explicitly what analytical role each class serves in the paper
- Keep the parameter system aligned with later results sections. If a methods parameter and a results parameter are not obviously identical, either state the mapping explicitly or flag the mismatch instead of smoothing over it
- Treat notation-system consistency as a global rule, especially for time-step or iteration-step indices; the position and style of time-like indices should remain uniform throughout the manuscript
- Prefer standard process-style method prose such as `is defined as`, `was monitored`, `is updated as`, and `was solved using`
- When a formula introduces a global quantity or control parameter, ensure definitional closure by checking four things: citation/source, summation or index scope, algorithmic role, and parameter value or limit if used later
- If a parameter is assigned a specific numerical value in the text, give its functional role in a separate sentence rather than burying it inside a longer parameter list
- Avoid packing parameter definitions, algorithm rules, and figure transitions into one sentence; one sentence should usually serve one primary rhetorical job
- In method sections, prioritize methodological closure over stylistic elegance. If a sentence must choose between sounding smoother and making the setup reproducible, prefer the more reproducible version
- In advisor-style revision mode, prefer implementation-driven prose over commentary-driven prose. Describe what was generated, imposed, solved, monitored, or updated before explaining why
- Do not default to explanatory expansion. For standard methods, give the method name, citation, governing formula, and required parameter definitions, but avoid extra algorithm praise or tutorial-style exposition unless the local passage truly needs it
- Prefer short, declarative method sentences over polished summary sentences. Replace broad framing such as `This subsection defines...` with direct procedural statements when possible
- Distinguish fixed specifications from varying descriptors explicitly. Fixed geometric or numerical settings should not be presented as independent design parameters
- When a local passage is mainly about generation or implementation, prefer `object or method -> descriptors or controls -> generation or update rule -> safeguard or exclusion rule` as the default ordering
- When a passage introduces a commonly used numerical method, cite a recent domain-relevant paper if available rather than defaulting to the oldest canonical source, unless historical priority is itself important
- When imitating advisor revisions, reduce interpretive commentary around standard formulas. The default is `equation first, short role sentence second`
- In method paragraphs, minimize evaluative wording such as `superior`, `beneficial`, `robust`, or `efficient` unless the sentence is explicitly making a comparison supported in the text
- If the advisor's edits reveal unresolved technical uncertainty, preserve the uncertainty as an explicit question or flagged item rather than silently harmonizing the text
- Treat formulas as the center of gravity; use prose only to define, connect, or constrain them
- Keep the minimum necessary physical definition sentence before or after a formula when it clarifies the object being defined or the physical meaning of the quantity
- Prefer standard equation-leading phrases such as `is defined as`, `can be expressed as`, and `is denoted as`
- Reduce scaffolding phrases such as `Accordingly`, `For clarity`, and `In the notation adopted here` unless they are genuinely needed
- Prefer journal-style compression over lecture-note exposition
- Compress explanatory padding before compressing technical definitions
- Do not remove limiting conditions inside technical definitions, especially phrases such as `within the horizon`, `in the deformed configuration`, or `under quasi-static loading`
- Let argument structure carry transitions whenever paragraph logic is already clear
- Keep the tone closer to journal prose than to lecture notes
- In definition-heavy method passages, prefer the order `modeling purpose -> label or symbol role -> value mapping or taxonomy -> downstream use`
- Prefer one short sentence per symbol or label when each symbol carries a distinct definitional role
- In PD-specific contexts, prefer field-standard formulations such as `domain of the configuration`, `neighborhood`, and `interactions within the horizon`, while retaining more precise continuum-mechanics wording such as `in the deformed configuration` where appropriate
- When adopting advisor-style revisions, preserve the current unified symbol system unless the advisor explicitly changes notation
- Terminology and acronym rules take precedence over stylistic imitation of advisor wording unless the advisor explicitly requests a terminology change
- For label definitions, prefer direct enumeration sentences over layered explanatory clauses
- Define labels first, then describe their later use in the model in a separate short sentence
- Prefer direct definitional verbs such as `distinguishes`, `identifies`, `denotes`, and `represents`; reduce padded frames such as `can thus be identified accordingly` or `label X is used to denote`
- Treat secondary interaction types such as negligible bond families in a short standalone sentence rather than embedding them in the main definition line
- If an equation introduces an index range or value mapping needed for immediate interpretation, restate that mapping briefly in the prose
- Preserve the minimum necessary explanatory sentence when a newly introduced quantity would otherwise appear without a clear role, purpose, or physical function
- When an indicator variable is introduced mainly through its action on another quantity, define the indicator and that action together in one compact sentence whenever possible
- In exception sentences, prefer `case -> decision -> reason` over long relative-clause expansions
- Order local definitions by dependency whenever possible; avoid emphasizing a symbol, correction, or derived quantity before the reader has been given the minimum context needed to interpret it
- Make the closing sentence explain how the definition, notation, or taxonomy feeds the next constitutive, force-state, failure, or solver subsection when that interface is scientifically important
- Prefer lighter forward-linking phrases such as `can later be used to` when introducing that next-step interface, unless strict chronology is itself important
- When an implementation-specific statement appears inside a derivation, briefly state why that implementation detail is needed at that point
- When standard theory, calibration, weight-function choice, or constitutive parameter linkage is invoked locally, check whether a citation anchor should appear in the same local context
- When a physical property directly motivates a constitutive or failure rule, prefer explicit cause-to-model wording such as `due to ... , failure is governed by ...`
- When a quantity is derived from fracture energy, yield data, or another higher-level input, prefer direct `derived from` phrasing
- When several quantities differ only by scale or role, prefer a single closing sentence that keeps them distinct
- In overview or summary sentences, prefer the concrete object names already established locally rather than switching to a new abstract label for the same object
- State global specifications once in the subsection overview, then reserve local subsection lists or prose for descriptors, generation rules, or other differentiating features
- When multiple object classes are introduced together, state explicitly what analytical role each class serves
- Do not force numerals into boldface for global consistency; numeral styling should follow the local notation system and standard mathematical typography
- After each local rewrite, recheck whether any information has been repeated mechanically in the next sentence without adding new meaning

## 8. De-Templating Rules

### Reduce

- Repeated transitions such as `it is worth noting that` or `it should be noted that`
- Hard pivots such as `however` when restructuring would read more naturally
- Rigid list cadence such as `first, second, finally`
- Generic impact statements without evidence
- Promotional words such as `novel`, `important`, or `significant` when the evidence is narrower
- Paragraphs where every sentence has the same length and function
- Sentences that summarize but add no new information
- Overuse of metadiscourse such as `this paper aims to`
- Introductory wrappers such as `Here` or `The label` when direct symbol-definition sentences would be clearer
- Heavy relative clauses such as `which corresponds to` when the same relation can be stated more directly

### Prefer

- Evidence-first phrasing
- Explicit scope limits
- Concrete comparisons
- Transition by logic rather than stock connectors
- Sentence-length variation that still reads as academic prose
- Specific judgments instead of generic praise
- Brief prose-to-formula alignment when a local mapping would otherwise stay implicit
- Direct case-decision-reason sentences for neglected or excluded interaction types
- Cause-condition-result framing when that logic genuinely exists

## 9. Claim Calibration And Hedging

- Strong claim plus narrow evidence requires scope language
- If the statement is interpretive rather than directly observed, make that distinction visible
- Replace broad evaluative praise with a specific methodological or empirical judgment
- Keep discipline-appropriate hedging; do not erase uncertainty to improve fluency

## 10. Introduction-Specific Rules

- Build around background, prior work, gap, objective, method overview, and contribution placement
- State the contribution after the gap is clear, not before
- Phrase the contribution as a scoped advance, not a universal breakthrough
- Do not turn the introduction into a literature-review dump
- Mention results only at a high level when needed
- Summarize prior work by problem and limitation, not by name-dropping alone

## 11. Abstract-Specific Rules

- Treat abstract editing as controlled scientific compression, not general polishing
- Preserve meaning, evidence scope, and abstract function before improving flow
- Default abstract structure: broad problem -> focused gap -> objective -> method or main finding -> key results -> scoped significance
- Keep the abstract focused on one rhetorical job: high-density orientation plus the paper's core findings
- Avoid stock openers such as `In this paper`, `It is worth noting that`, and `In conclusion`
- Avoid acronyms in the abstract unless they are defined on first use within the abstract itself
- Keep method description at the framework level; do not enumerate implementation details unless central to the contribution
- Distinguish observed response, modeled interpretation, and broader implication
- Do not introduce new terminology unless the manuscript already supports it
- Do not oversell novelty, superiority, or generality

## 12. Redundancy-Reduction Rules

- Reduce self-repetition without flattening the manuscript into one repeated summary
- Compare within one section or between adjacent sections such as abstract vs introduction or results vs conclusion
- Preserve role-specific overlap when two sections have different rhetorical jobs
- Keep short reminders needed for continuity, necessary repeated results in shortened form, and definitions required at first use in a new major section
- Remove or compress repeated concept explanations, near-duplicate topic sentences, repeated stock transitions, and summary sentences that add no new information
- Prefer surgical deletions or mergers over global flattening rewrites

## 13. Structure-Diagnosis Rules

- Diagnose before rewriting; do not rewrite during diagnosis
- Work on one section, subsection, or reviewer comment bundle at a time
- Build a quick argument map: section role, paragraph roles, central claims, and supporting evidence
- Audit section-role fit, claim-evidence alignment, logic continuity, information economy, and academic-tone quality
- Use severity labels when helpful: `critical`, `major`, `moderate`, `minor`
- Prefer fewer high-signal findings over long laundry lists
- Flag uncertainty explicitly when a gap may actually be a missing citation or figure reference

## 14. Terminology Rules

The source of truth is `style/terminology.yml`.

Current acronym-first-use control includes:

- `CNT`
- `CNTRPs`
- `PD`
- `OSB-PD`
- `BB-PD`
- `NOSB-PD`
- `RVE`
- `MM`
- `CC`
- `MC`
- `CMC`
- `MCM`

Current preferred technical terminology includes:

- `ordinary state-based peridynamics` / `OSB-PD`
- `representative volume element` / `RVE`
- `interfacial debonding`
- `quasi-static loading`
- `Heterogeneous-bond scheme`
- `intra-matrix bonds`
- `intra-CNT bonds`
- `interfacial bonds`
- `trans-phase bonds`

Additional terminology-control rules:

- Scan terminology before editing when possible
- After first introduction, prefer the acronym alone instead of repeatedly writing `full term (ACRONYM)`
- Check for mixed variants, acronym-before-long-form errors, capitalization drift, hyphenation drift, and naming drift across text/figures/tables
- Do not rename equation symbols, variable names, or figure labels unless notation cleanup is explicitly requested
- If a term variant may reflect a real scientific distinction, flag it instead of normalizing automatically
- When notation cleanup is requested, use one consistent symbol system across the local scope
- In bond-typing passages, keep the taxonomy naming aligned across prose, figure captions, and later constitutive discussion

## 15. Notation Conventions

- Scalar variables: italic
- Explanatory labels or textual qualifiers: roman
- Vectors: bold
- PD state quantities: underline where state notation is intended
- In the current manuscript convention, the underline is reserved for vector state quantities such as `\underline{\boldsymbol{T}}`; the scalar force state `t[\boldsymbol{x},t]\langle\boldsymbol{\xi}\rangle` and the deformed-bond direction vector `\boldsymbol{M}` remain non-underlined unless a full state-notation system is explicitly adopted
- Material-point pair indices: use parenthesized subscripts such as `(k)(j)` to distinguish them from conventional tensor indices
- Conventional tensor indices for continuum-mechanics notation may remain unparenthesized as `i,j,k,l`
- When introducing counters or index ranges, avoid reusing symbols that already carry a common local meaning such as time-step count, node count, or sample count; prefer a fresh symbol such as `m` when it reduces collision risk

## 16. Banned Stock Phrases

The current warning list in `style/banned_phrases.txt` is:

- `it is worth noting that`
- `it should be noted that`
- `deserves special attention`
- `has important significance`
- `provides a new idea`
- `however`
- `firstly`
- `secondly`
- `lastly`
- `in a nutshell`
- `all in all`

These are warning signals, not blind search-and-replace targets.

## 17. Tooling Rules

- Use `skills/` for contextual editing workflows
- Use `scripts/` for deterministic checks
- Read `style/` before terminology or tone edits
- Write diagnostics and acceptance artifacts into `review/` when creating persistent outputs
- Prefer narrow checks such as `check_terminology.py`, `scan_repetition.py`, and `detect_long_sentences.py` when the problem can be measured

## 18. Practical Editing Principle

When revising technical paper prose:

- preserve symbols, evidence, and meaning first
- simplify only where the scientific content stays intact
- shorten prose around formulas before shortening the formulas' explanatory necessities
- prefer a cleaner sentence over a more decorative one
- keep the rhetorical job of each section visible after every edit






































