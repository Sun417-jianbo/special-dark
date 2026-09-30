# Revision Diagnosis

## First-run weakness

The first improved chart communicated the direction and approximate magnitude of the rate difference and added the required causal qualification. It nevertheless failed the complete-response test because the chart itself omitted three numerical elements explicitly requested by the business question: survivor counts, the exact percentage-point difference, and the exact relative survival rate.

The structured JSON contained those values, but an editor viewing the PNG alone would have to consult a second artifact. That weakens the chart's usefulness as a presentation prop and as fact-checking evidence.

## Smallest appropriate instruction change

Revise `specialist_instructions.md` to require all explicitly requested decision metrics to appear in or immediately adjacent to the chart when they can be shown without crowding. For this two-category case, require direct labels containing rates and counts plus a compact summary of the percentage-point gap and relative rate.

## Retest standard

Rerun the same case with the same source data. Accept the revision only if the PNG remains legible, preserves the zero baseline, shows counts and all requested comparison metrics, and retains the association-not-causation boundary.
