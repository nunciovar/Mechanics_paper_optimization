# Section: Methods

Open by stating what object, model, or algorithm is constructed or adopted for the analysis.

## Advisor-Derived Method Rules

- Prefer concise journal-style compression over lecture-note exposition when the scientific meaning is unchanged.
- For standard numerical algorithms, use compact phrasing such as `was solved using ...` or `is integrated with ...`, followed by governing update equations.
- When a subsection defines simulation objects, check whether object classes, controlling parameters, domain size, boundary geometry, and generation range are stated when relevant.
- When multiple object classes are introduced together, state explicitly what analytical role each class serves.
- Keep the parameter system aligned with later results sections; if a methods parameter and a results parameter are not obviously identical, state the mapping or flag it.
- Treat notation-system consistency as a global rule, especially time-step or iteration-step indices.
- Prefer process-style method prose such as `is defined as`, `was monitored`, `is updated as`, and `was solved using`.
- When a formula introduces a global quantity or control parameter, check citation/source, summation or index scope, algorithmic role, and later parameter value or limit.
- If a parameter is assigned a numerical value, give its functional role separately rather than burying it in a long list.
- Avoid packing parameter definitions, algorithm rules, and figure transitions into one sentence.
- Prioritize methodological closure over stylistic elegance.
- Prefer implementation-driven prose over commentary-driven prose.
- For standard methods, give the method name, citation, governing formula, and required parameter definitions without extra tutorial exposition.
- Distinguish fixed specifications from varying descriptors.
- When a passage is about generation or implementation, prefer `object or method -> descriptors or controls -> generation or update rule -> safeguard or exclusion rule`.
- When a standard theory, calibration, weight function, or constitutive parameter linkage is invoked, check whether a local citation anchor is needed.
- Order local definitions by dependency.
- Make the interface to the next constitutive, force-state, failure, solver, or post-processing step explicit when scientifically important.
