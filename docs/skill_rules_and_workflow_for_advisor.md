# Current Paper-Optimization Skills: Rules And Workflow

This document summarizes the current manuscript-optimization skill system in this repository for advisor review. It consolidates the governing rules, skill responsibilities, decision logic, deterministic checks, and the full execution workflow currently used for paper editing support.

## 1. Scope And Purpose

These skills are designed to support disciplined manuscript revision rather than autonomous paper writing.

The system is built around the following principle:

1. Preserve scientific meaning first.
2. Preserve the author's intent second.
3. Standardize terminology and notation carefully.
4. Improve section logic and rhetorical flow.
5. Polish style only after the scientific and structural layers are stable.

The skills are intended for local, controlled revision of LaTeX manuscript content, with emphasis on CNT/epoxy composite and peridynamics-related technical prose.

## 2. Source Files That Govern The System

### Core repository rules

- `AGENTS.md`
- `style/paper_optimization_rules.md`
- `style/terminology.yml`
- `style/banned_phrases.txt`

### Skill entry points

- `skills/paper-optimize/SKILL.md`
- `skills/structure-diagnose/SKILL.md`
- `skills/intro-rebuild/SKILL.md`
- `skills/abstract-optimize/SKILL.md`
- `skills/anti-template-rewrite/SKILL.md`
- `skills/redundancy-reduce/SKILL.md`
- `skills/terminology-guard/SKILL.md`

### Deterministic support scripts

- `scripts/check_terminology.py`
- `scripts/scan_repetition.py`
- `scripts/detect_long_sentences.py`

### Main manuscript source

The manuscript source should be read from `PROJECT_CONFIG.yml` when present.
This repository should not assume one fixed paper path.

## 3. Governing Philosophy

The skill system is explicitly editorial rather than generative. It is meant to revise and diagnose existing scientific prose under constraints.

### Global priority order

1. Scientific correctness
2. Fidelity to the author's intent
3. Terminology consistency
4. Section logic and rhetorical flow
5. Concision and style polish

### Global editing stance

- Do not trade away scientific meaning for smoother phrasing.
- Do not invent data, citations, equations, mechanisms, or stronger claims.
- Do not silently add novelty claims, broad impact claims, or unsupported certainty.
- Do not rewrite unrelated sections for consistency unless explicitly requested.
- Do not auto-resolve ambiguous terminology if two technical meanings are both plausible.
- Flag uncertainty instead of smoothing it over when the underlying scientific intent is unclear.

## 4. Shared Execution Contract

Before any paper-editing task is performed, the system is supposed to do the following:

1. Load the governing files:
   - `AGENTS.md`
   - `style/paper_optimization_rules.md`
   - `style/terminology.yml`
   - `style/banned_phrases.txt`
2. Confirm the local scope.
3. Choose the phase before editing.
4. Apply cumulative rules rather than following only one local heuristic.
5. Preserve scientific meaning first.
6. Flag author-confirmation items.
7. Return outputs in the repository's required order.

### Default scope rule

The default scope is one section, subsection, paragraph, reviewer-comment bundle, or figure-caption bundle at a time.

Whole-manuscript scanning is allowed only when a local decision depends on global consistency, such as:

- acronym first use
- terminology drift
- repeated explanations
- prior definitions
- cross-section redundancy

## 5. High-Risk Items Requiring Author Confirmation

Unless the task explicitly asks for direct edits, the following items are treated as author-confirmation items:

- numerical values, units, and thresholds
- equation definitions and symbol meanings
- figure or table numbering and cross-references
- causal claims
- novelty claims
- limitation statements
- comparisons against prior work
- statements that depend on unstated experimental assumptions

## 6. Workflow Phases

The system is organized as a staged editorial pipeline. By default, these phases should not be collapsed.

1. Diagnosis
   Identify problems only; do not rewrite.
2. Section rebuild
   Rewrite one section for structure only.
3. Sentence-level de-templating
   Reduce mechanical or generic academic phrasing.
4. Redundancy reduction
   Remove self-overlap without flattening section roles.
5. Rule check
   Run deterministic checks where applicable.
6. Acceptance output
   Present revised text, rationale, open questions, and high-risk items.

## 7. Overall Skill Architecture

### 7.1 `paper-optimize`: the orchestrator

This is the top-level manuscript-optimization skill.

It does not replace the narrower skills. Instead, it:

- enforces the shared execution contract
- determines the phase
- selects the appropriate specialist skill
- sequences multi-phase work when needed

### 7.2 Specialized skills

- `structure-diagnose`: diagnosis before rewriting
- `intro-rebuild`: rebuild introduction logic
- `abstract-optimize`: optimize abstract structure and compression
- `anti-template-rewrite`: reduce template-like academic phrasing
- `redundancy-reduce`: remove repetitive self-overlap
- `terminology-guard`: enforce terminology and acronym consistency

## 8. Skill Selection Logic

The current intended selection logic is:

- Use `structure-diagnose` when the user asks what is wrong, what should be fixed, or what changed before revision.
- Use `intro-rebuild` when the introduction has the correct raw content but weak paragraph logic or contribution placement.
- Use `abstract-optimize` when the scope is the abstract.
- Use `anti-template-rewrite` when the structure is already acceptable and the main problem is mechanical or generic academic phrasing.
- Use `redundancy-reduce` when the primary issue is self-overlap within or across nearby sections.
- Use `terminology-guard` before or after local rewrites when terminology, acronyms, notation, or bond-taxonomy consistency may drift.

### Default sequence for multi-phase tasks

1. Diagnose
2. Rebuild structure if needed
3. De-template sentences
4. Reduce redundancy
5. Check rules
6. Return acceptance-style output

## 9. Advisor-Style Revision Preferences Already Embedded In The System

The current system already includes advisor-style compression and revision preferences as global rules rather than as a separate standalone skill.

These advisor-preference rules include:

- Prefer concise journal-style compression over lecture-note exposition when meaning is unchanged.
- Treat formulas as the center of gravity; use prose only to define, connect, or constrain them.
- Prefer standard technical lead-ins such as `is defined as`, `can be expressed as`, and `is denoted as`.
- Reduce scaffolding phrases such as `Accordingly`, `For clarity`, and `In the notation adopted here` unless they are necessary.
- In definition-heavy method passages, prefer the order:
  `modeling purpose -> label or symbol role -> value mapping or taxonomy -> downstream use`
- Prefer one short sentence per symbol or label when each symbol has a distinct role.
- Restate index ranges or value mappings in prose when they are needed for immediate interpretation.
- Define indicator variables together with the quantity they modify when that coupling is the main point.
- Prefer direct definitional verbs such as `distinguishes`, `identifies`, `denotes`, and `represents`.
- Prefer direct enumeration for bond-family definitions rather than padded explanatory frames.
- State negligible or excluded interaction types in short standalone sentences after the main taxonomy.
- Prefer `case -> decision -> reason` order in exception sentences.
- Order local definitions by dependency.
- Make the interface to the next constitutive, force-state, failure, or solver step explicit when scientifically important.
- Prefer lighter forward-linking phrases such as `can later be used to`.
- Use short cause-to-model wording when a physical property motivates a constitutive or failure rule.
- Prefer `derived from` phrasing when a quantity comes from fracture energy, yield data, or other higher-level inputs.

## 10. Global Style And Tone Rules

- Prefer field-appropriate academic prose over generic polished prose.
- Reduce template phrases, but do not force conversational wording.
- Prefer concrete academic judgments over vague praise.
- Use restraint with transitions such as `notably`, `it should be noted`, and `in conclusion`.
- Keep abstract, introduction, methods, results, discussion, and conclusion functionally distinct.
- Keep discipline-appropriate hedging where evidence is narrower than the wording.
- Do not weaken precision merely to sound less uniform.

## 11. De-Templating Rules

### Patterns to reduce

- `it is worth noting that`
- `it should be noted that`
- rigid pivoting with `however` where restructuring would work better
- rigid enumerations such as `firstly`, `secondly`, `lastly`
- generic significance language without evidence
- repetitive sentence cadence
- low-information summary sentences
- overuse of metadiscourse such as `this paper aims to`
- padded symbol-definition wrappers
- heavy relative-clause expansions

### Patterns to prefer

- evidence-first phrasing
- explicit scope limits
- concrete comparisons
- transition by logic rather than stock connectors
- variation in sentence function and cadence while remaining academic
- direct definitional verbs
- short standalone exception sentences
- compact case-decision-reason framing
- cause-condition-result framing when genuinely justified

## 12. Claim Calibration And Hedging Rules

- Strong claims with narrow evidence require scope language.
- If a statement is interpretive rather than directly observed, that distinction should be visible.
- Broad evaluative praise should be replaced with specific methodological or empirical judgment.
- Uncertainty should not be erased for fluency.
- Simulation trends should not be rewritten as universal physical laws.

## 13. Terminology, Acronym, And Notation Rules

### Preferred terminology source

The source of truth is `style/terminology.yml`.

### Current preferred term families

- `CNT`
- `CNTRPs`
- `carbon nanotube (CNT)-reinforced polymer composite`
- `epoxy matrix`
- `reinforcement architecture`
- `ordinary state-based peridynamics` / `OSB-PD`
- `bond-based peridynamics` / `BB-PD`
- `non-ordinary state-based peridynamics` / `NOSB-PD`
- `representative volume element` / `RVE`
- `interfacial debonding`
- `quasi-static loading`
- `Heterogeneous-bond scheme`
- `intra-matrix bonds`
- `intra-CNT bonds`
- `interfacial bonds`
- `trans-phase bonds`

### Acronym first-use control

The current first-use control list includes:

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

### Terminology-control rules

- Scan terminology before editing when possible.
- After first introduction, prefer the acronym alone rather than repeatedly writing `full term (ACRONYM)`.
- Check mixed variants, acronym-before-long-form problems, capitalization drift, hyphenation drift, and naming drift.
- Do not rename equation symbols, variable names, or figure labels unless notation cleanup is explicitly requested.
- If a term variant may reflect a real scientific distinction, flag it rather than normalizing it automatically.
- Keep bond-family taxonomy consistent across prose, captions, and constitutive discussion.

### Notation conventions

- scalar variables: italic
- explanatory labels: roman
- vectors: bold
- PD state quantities: underline where state notation is intended
- in the current manuscript convention, underline is reserved for vector state quantities such as `\underline{\boldsymbol{T}}`
- the scalar force state `t[\boldsymbol{x},t]\langle\boldsymbol{\xi}\rangle` and the deformed-bond direction vector `\boldsymbol{M}` remain non-underlined unless the notation system is globally changed
- material-point pair indices may use parenthesized subscripts such as `(k)(j)` when needed to avoid collision with tensor indices
- avoid reusing local symbols such as `n` if they already carry another common meaning; use a fresh symbol such as `m` when that reduces confusion

## 14. Banned-Phrase Warning List

The current warning list is:

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

## 15. Output Contract

### For diagnosis tasks

The expected order is:

1. Structural problems
2. Logic gaps
3. Repetition hotspots
4. AI-style hotspots
5. Must-keep scientific content

`structure-diagnose` expands this with a more explicit template:

1. Section role summary
2. Structural problems
3. Logic gaps
4. Claim-evidence risks
5. Repetition hotspots
6. AI-style hotspots
7. Must-keep scientific content
8. Author-confirmation items

### For rewrite tasks

The general expected order is:

1. Revised text
2. Change notes
3. Open questions
4. High-risk lines not auto-changed

Specialized skills may refine this slightly for local needs.

## 16. Detailed Rules By Skill

### 16.1 `structure-diagnose`

Main role:

- section-level diagnosis before rewriting

Main review lenses:

- section-role fit
- claim-evidence alignment
- logic continuity
- definition dependency order
- definition-action coupling
- information economy
- academic tone quality

Severity labels available:

- `critical`
- `major`
- `moderate`
- `minor`

Guardrails:

- do not rewrite during diagnosis
- do not collapse diagnosis into line edits unless the user explicitly asks
- do not label text as AI-like without pointing to a concrete language pattern
- prefer fewer high-signal findings over long laundry lists

### 16.2 `intro-rebuild`

Main role:

- rebuild introduction logic rather than merely polish sentences

Target introduction logic:

1. field problem and relevance
2. prior work and what is already solved
3. remaining gap or limitation
4. study objective and approach
5. contribution placement without overselling

Guardrails:

- diagnose paragraph roles before rewriting
- do not inflate novelty claims
- do not turn the introduction into a literature dump
- do not import detailed results unless needed at a high level
- keep unresolved scientific claims marked for author review

### 16.3 `abstract-optimize`

Main role:

- controlled scientific compression of the abstract

Target abstract structure:

1. broad field problem and immediate context
2. focused unresolved limitation or modeling gap
3. study objective
4. main method, result, or take-home finding
5. most important results
6. scoped significance

Additional abstract-specific rules:

- avoid stock openers such as `In this paper`
- avoid undefined acronyms in the abstract
- keep method description at framework level unless implementation details are central
- distinguish observed response, modeled interpretation, and broader implication
- do not oversell generality, superiority, or novelty

### 16.4 `anti-template-rewrite`

Main role:

- remove template-like academic phrasing while preserving technical meaning

Typical problem targets:

- empty transitions
- vague significance claims
- repeated sentence frames
- exaggerated certainty
- low-information sentences

Guardrails:

- do not use this as a substitute for structure diagnosis
- do not randomize synonyms
- do not make the prose colloquial
- do not weaken necessary precision
- keep strong statements strong when the evidence is genuinely strong

### 16.5 `redundancy-reduce`

Main role:

- reduce repetitive overlap within one section or across adjacent sections

Keep:

- short reminders needed for continuity
- results that must reappear in a shorter conclusion form
- definitions needed at first use in a new section
- brief overlap required for section-specific rhetorical function

Remove or compress:

- repeated concept explanations with no new nuance
- near-duplicate topic sentences
- repeated stock transitions
- summary sentences that add no new content

Guardrails:

- do not use redundancy reduction to bypass unresolved logic gaps
- do not cut distinctions between reporting and interpretation
- do not remove the only local citation anchor or scope limit
- prefer surgical deletion over flattening rewrites

### 16.6 `terminology-guard`

Main role:

- narrow, high-precision terminology and acronym control

Main checks:

- mixed term variants
- acronym first use
- symbol-style consistency when notation cleanup is in scope
- capitalization and hyphenation consistency
- formula-to-prose mapping mismatches
- local citation-anchor gaps around standard theory or constitutive linkage

Guardrails:

- do not merge genuinely different concepts
- do not standardize away venue-mandated capitalization
- do not rename symbols or labels unless the task includes notation cleanup
- if notation cleanup is in scope, apply it consistently across the full local scope

## 17. Deterministic Script Usage

The repository currently includes three scripts for measurable checks:

- `check_terminology.py`
  Used for mixed variants, banned phrases, and acronym-first-use issues.
- `scan_repetition.py`
  Used for repeated n-grams and broad overlap detection.
- `detect_long_sentences.py`
  Used for long-sentence detection when readability is part of the issue.

These scripts are intended to support judgment, not replace it.

## 18. End-To-End Practical Workflow

The current intended workflow for a normal manuscript optimization task is:

1. Receive the editing request.
2. Identify the local scope.
3. Load `AGENTS.md`, `style/paper_optimization_rules.md`, `style/terminology.yml`, and `style/banned_phrases.txt`.
4. Decide whether the task is diagnosis, structure rebuild, de-templating, redundancy reduction, terminology control, or a multi-phase sequence.
5. Select the appropriate skill under `paper-optimize`.
6. If needed, run narrow deterministic checks:
   - terminology
   - repetition
   - long sentences
7. Perform the local edit or diagnosis while preserving scientific meaning and high-risk items.
8. If terminology or redundancy edits were applied to manuscript source, compile the main LaTeX file when feasible.
9. Return the result using the required output contract.
10. If scientific uncertainty remains, flag author-confirmation items explicitly rather than smoothing them away.

## 19. Example Decision Flow

### Case A: "What is wrong with this subsection?"

- select `structure-diagnose`
- do not rewrite
- report structural and logic problems first

### Case B: "Please improve this introduction."

- enter through `paper-optimize`
- likely sequence:
  - paragraph-role diagnosis
  - `intro-rebuild`
  - possibly `anti-template-rewrite`
  - optionally `terminology-guard`

### Case C: "This abstract sounds AI-written."

- enter through `paper-optimize`
- use `abstract-optimize`
- if structure is already acceptable, apply `anti-template-rewrite` logic locally

### Case D: "These two sections repeat each other."

- use `redundancy-reduce`
- compare rhetorical jobs before removing overlap

### Case E: "Please make terminology consistent."

- use `terminology-guard`
- run `check_terminology.py` when helpful

## 20. Current Strength Of The System

The current skill system is strong in the following ways:

- It enforces scientific preservation ahead of stylistic polish.
- It separates diagnosis from rewriting.
- It already embeds advisor-style journal compression rules.
- It is suitable for equation-heavy technical writing.
- It explicitly protects terminology, notation, and evidential scope.
- It includes deterministic checks to support repeatable review.

## 21. Current System Boundary

The system is not intended to:

- invent scientific content
- act as an autonomous paper author
- rewrite the full manuscript by default
- evade academic-integrity checks through paraphrasing
- overwrite unresolved scientific ambiguity with smooth prose

## 22. Short Summary

In its current form, the repository uses one orchestration skill plus six specialist skills to run manuscript revision as a staged editorial workflow. The system is built to mimic disciplined advisor-style revision in process and sentence compression, while still prioritizing scientific fidelity, terminology control, and explicit handling of high-risk lines.
