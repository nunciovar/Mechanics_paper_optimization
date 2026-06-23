# Core Workflow

Use this loop for manuscript-editing tasks:

1. Inspect the user request and local scope.
2. Read `AGENTS.md` and `PROJECT_CONFIG.yml` when present.
3. Select the task phase, section type, domain context, and language mode.
4. Load only the shared core files and relevant router fragments.
5. Diagnose scientific and structural risks before rewriting.
6. Apply scoped edits or provide a diagnosis.
7. Run deterministic checks when useful.
8. Return revised text, change notes, open questions, and high-risk items.

## Scope Rule

Default to one section, subsection, paragraph group, reviewer-comment bundle, or figure-caption bundle. Whole-manuscript scanning is allowed when local decisions depend on global consistency, such as acronym first use, terminology drift, repeated definitions, or cross-section redundancy.

## Phase Rule

Do not collapse diagnosis, rewriting, redundancy reduction, and acceptance review into one step unless the user explicitly asks for a combined pass.
