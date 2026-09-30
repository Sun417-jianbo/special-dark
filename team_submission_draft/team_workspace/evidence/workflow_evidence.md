# Workflow Evidence

## Exercised workflow CYF Chart Improvement Agent

**Question.** How did passenger survival rates differ by sex in the supplied Titanic data, and how should the result be presented for a business reader?

**Baseline.** The preserved baseline chart displayed survival rates by sex. Source-data checks found 339 survivors among 466 female passengers and 161 survivors among 843 male passengers, corresponding to 72.7468 percent and 19.0985 percent.

**First run.** Version 1 preserved the correct data and returned the required response structure. Review found that the output did not make the magnitude of the gap sufficiently explicit and needed stronger decision framing, direct labels, and clearer uncertainty language.

**Revision.** Version 2 required the output to state the 53.6483 percentage-point gap, retain counts and denominators, avoid causal claims, and explain why the redesigned chart was more usable for the decision context.

**Retest.** The revised response passed the structured-output validator. The final chart matches the v2 chart, the final JSON matches the v2 response, and the frozen-core hash check passed.

**Limit.** The observed difference is descriptive within this dataset. It does not establish that sex caused the survival difference, and it should not be generalized beyond the supplied passenger records without additional evidence.

**Evidence paths.** See `supporting_evidence/CYF/` for the baseline chart, v1 and v2 charts, v1 and v2 structured responses, revision diagnosis, validation logs, frozen-core check, and Agent Record.

## Team comparison pending

The same procedure must be applied to the remaining candidate agents. If the team cannot exercise an agent during the workshop, record the blocker, owner, and next test date rather than marking it accepted without evidence.
