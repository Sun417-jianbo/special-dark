# Context-Contrast Case Design (Team Lab 2)

## Purpose
Decide whether a specialist is **actually contextual** rather than **merely fluent**. Fluency passes the validator; only a contrast case reveals context sensitivity.

## Design
Run the **same specialist** (same `specialist_instructions.md`, same version) on **two contrasting contexts** with the same data, e.g.:

- **Context A:** executive audience, decision = "should we fund expansion?" → emphasis on the decision-relevant comparison, assertive headline title, minimal supporting detail.
- **Context B:** analyst audience, decision = "which segment drives the pattern?" → emphasis on segment-level structure, precise labels, fuller annotation of uncertainty.

## What must change between A and B (contextual behavior)
Title framing, visual emphasis, annotation depth, and level of detail — all traceable to the audience and decision context named in the case JSON.

## What must NOT change (frozen discipline)
Data fidelity (same values, units, scales, ordering), the business question as given, the common output schema, and the governing-vs-illustrative source hierarchy.

## Pass/fail rule for team acceptance
- **Pass:** the two outputs differ in decision-relevant emphasis while both preserve data fidelity and schema; the Agent Record explains *why* each choice serves its context.
- **Fail:** the two outputs differ only in styling (colors, fonts, layout) or are near-identical — the specialist is fluent but generic and is rejected or sent back for revision.
