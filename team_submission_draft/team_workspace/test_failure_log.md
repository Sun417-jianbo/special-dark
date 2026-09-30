# Test and Failure Log

| Agent and version | Test | Expected result | Observed result | Failure or limitation | Revision | Retest result | Evidence |
|---|---|---|---|---|---|---|---|
| chart_improvement_agent v1 | Titanic survival rate by sex | Accurate, decision-ready chart and explanation using the shared schema | Data were accurate and schema-valid, but the chart and explanation did not make the size of the gap sufficiently explicit for a business reader | Weak decision framing; limited direct labeling; insufficient statement of uncertainty and non-causality | v2 required direct percentage labels, the 53.6 percentage-point gap, a non-causal limitation, and a decision-oriented title and note | Passed structural validation; final chart preserved the source counts and rates | `supporting_evidence/CYF/` |
| `[agent version]` | `[test]` | `[expected]` | `[observed]` | `[failure or limitation]` | `[revision]` | `[result]` | `[path]` |

## Logging rule

Record behavior that affects correctness, usability, evidence quality, or integration. Do not erase failed attempts after a successful revision; they establish why the change was necessary.
