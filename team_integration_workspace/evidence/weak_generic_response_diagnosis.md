# Weak / Generic Output Diagnosis (Team Lab 2, in-class exercise)

## What we did
Built a deliberately weak, fluent-but-generic specialist response (`weak_response.json`) and ran it through the frozen validator:

```
python tools/validate_response.py evidence/weak_response.json
→ VALIDATION PASSED
```

## Why it fails the course context rule (even though the JSON is valid)
1. **Copies the illustrative source instead of applying the governing framework.** It adopts the case study's teal-and-orange palette and headline-title style without any independent justification from the chart, data, audience, or business question — exactly what the scaffold forbids ("principles govern; do not copy case-specific revisions").
2. **Cosmetic changes only.** Assessment and comparison entries describe the chart as "more colorful" and "modern" — no diagnosis of analytical, perceptual, labeling, scale, or decision-communication weaknesses tied to the business answer.
3. **Vacuous data-fidelity checks.** A single "appears to show the correct general shape" check — no verification of values, units, scales, ordering, categories, or the substantive business answer against the source data.
4. **Ignores the business question.** The stated question is vague ("What does the Titanic data show?") and no improvement choice is traceable to answering it better.
5. **Claims limitation-free success** ("None significant; the chart now looks publication-ready"), violating the required honest accounting of remaining limitations.

## Team implication
`validate_response.py` checks JSON structure only — it cannot detect generic, non-contextual, or source-copying behavior. **Team acceptance therefore requires human review against the context rule plus a passing contrast test; validator output is necessary but never sufficient.** This is recorded as a fixed convention in the Team Agent Design and Integration Standard.
