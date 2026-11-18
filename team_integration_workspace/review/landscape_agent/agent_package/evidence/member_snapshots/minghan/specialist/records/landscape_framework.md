# Landscape framework (v1.1)

## 1. Three layers

| Layer | Output field | Varies with | Purpose |
|---|---|---|---|
| Broad landscape | general_et_finding | Technology only (dated) | Where agentic AI stands in general |
| Application landscape | application_finding | Application | Competitors, the strongest alternative, the ecosystem, application-specific adoption |
| Organizational relevance | organization_specific_finding | Organization and horizon | Which few signals could change this organization's decision |

## 2. Ten dimensions

| # | Dimension | Typical evidence needed |
|---|---|---|
| 1 | Maturity & capability | Independent benchmarks and evaluations |
| 2 | Performance & cost trends | Independent price/performance data; vendor list prices for list price only |
| 3 | Competing technologies | Inference from the task; vendor product facts |
| 4 | Incumbent / conventional alternative | Organization facts; adoption surveys |
| 5 | Complementary technologies | Upstream readiness findings; organization facts |
| 6 | Vendors & ecosystem | Vendor announcements (existence only); trade press |
| 7 | Standards & interoperability | Standards bodies, foundations, security standards |
| 8 | Regulation | Official legal texts and regulator guidance |
| 9 | Investment & forecasts | Analyst forecasts (background only) |
| 10 | Industry adoption | Surveys with a stated denominator |

## 3. Relevance tiers (flip test)

- **DECISION-RELEVANT:** reversing the signal would change a named decision within the horizon. At most four per case.
- **WATCH:** a named threshold would make it decision-relevant; the threshold becomes a trigger.
- **BACKGROUND:** true or popular, but reversing it would not change the decision.

## 4. Evidence types and minimums

| Type | Examples | Can it move the position? |
|---|---|---|
| VENDOR | Press releases, self-reported scores, vendor outcome claims | No, not alone |
| INDUSTRY | Consulting/analyst/association surveys, trade press | Adoption with a denominator: yes. Forecasts: never |
| INDEPENDENT | Peer-reviewed research, independent benchmarks, randomized studies, government statistics | Yes |
| STANDARD-REG | Legal texts, regulators, standards bodies | Yes, for regulatory and standards claims |
| ORGANIZATION | The organization's own pages | Facts about the organization only |
| INFERENCE | The agent's own reasoning | Only when labelled, and only where the other types cannot exist |

**Diversity rule:**
- A DECISION-RELEVANT signal needs at least one non-vendor source.
- A change of position needs INDEPENDENT or STANDARD-REG evidence.

## 5. Freshness

| Class | Covers | Refresh | Stale after |
|---|---|---|---|
| FAST | Benchmarks, model releases, prices, vendor features | Quarterly | 6 months |
| MEDIUM | Surveys, deployments, adoption | Semiannually | 12 months |
| SLOW | Regulation, standards governance | On any official change, plus an annual check | 12 months |

Leaderboards lag. When newer models are missing from a leaderboard, that is not evidence that capability has stalled.

## 6. Position summary rule

Each of the ten dimensions gets one line: broad position (direction) | tier | dated, typed evidence. There is no single score, no composite index and no hype-cycle placement. The course classification is cited from the Adoption specialist where it exists.

## 7. Trigger format

`TRIGGER n [Dimension]: Watch … | Cadence … | Threshold … | Then … | Watcher <role stated in the case>`. Each case ends with a refresh schedule.
