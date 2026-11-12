# Cycle 1 review (v1.0)

All four v1.0 outputs pass the frozen validator, and the general paragraph is identical in all four. The readiness analysis still fails the assignment in five ways. This review checks each output against the brief, the case facts, the upstream Adoption specialist (C4) and the agent's own sources. The AI-leverage hints ask two questions: does the agent respond to readiness differences, or does it repeat a generic change-management checklist? And does each action address an observed gap?

## Preserved failure 1: one generic checklist for every organization

All four outputs end with the **same six actions**, word for word, with the same generic owners ("senior leadership", "IT", "project lead"):
- secure sponsorship;
- form a governance committee;
- train staff;
- write a change plan;
- "ensure data quality";
- define KPIs.

The action lists have a Jaccard similarity of 1.0 across all four cases.

**Challenge of each action against the case facts (AI-leverage hint 2):**

| v1.0 action | SPS (primary) | High-readiness university (contrast 1) | Small college (contrast 2) |
|---|---|---|---|
| Secure executive sponsorship | A sponsor exists; the missing element is funded review time and stop authority | **Already exists** (VP, funded through year 1) | A sponsor exists; the missing element is a budget and a decision on how saved time is used |
| Establish an AI governance committee | The missing element is a review of this agent plus an incident/pause procedure, not a committee | **Already exists** | Disproportionate for a three-person office; the gap is a missing written data rule |
| Invest in staff AI training | Partly relevant (reviewers need error-type training) | **Already exists** (a year of drafting-tool use plus a correction process) | Relevant only after staff time exists |
| Change-management plan | No evidence of a culture problem was supplied | No observed gap | Misses the actual stated concern (fear of cuts), which needs a management decision, not a plan |
| Ensure data quality and integration | Vague | **Misses the real gap**: the CRM team's migration overlaps the experiment | Misses that the CRM tier has no API at all |
| Define KPIs | Generic | Generic | Generic |

In the contrast-1 column, three actions duplicate things the university already has, and the integration action misses its real gap (the CRM migration). Across all three columns, no action names a specific observed gap; only training (for SPS) and integration come close, and only vaguely. This is the generic checklist the hint warns about.

## Preserved failure 2: readiness confused with technology maturity, in both directions

- **Contrast 2 (low readiness):** "Agentic AI is too immature and complex for an institution of this size; revisit when the technology matures." The technology is exactly as mature at a small college as at a large university. The college's obstacles are its own: no budget, a hiring freeze, no data rule, staff fear of cuts. Reporting them as immaturity sends management to wait for the market instead of fixing them.
- **Contrast 1 (high readiness):** "its organizational readiness offsets the technology's immaturity... proceed to full implementation." Readiness cannot change the technology's class. The Adoption specialist (C4) and course Rule 1 do not permit production adoption of a bleeding-edge application, however capable the organization.

The brief requires "separate findings for technology/application fit and organizational readiness so that low readiness is not misreported as low technology maturity." v1.0 fails this requirement.

## Preserved failure 3: an invented answer where the facts were missing (primary)

The SPS case says plainly that inquiry volume, peak load and protected counselor hours are **not supplied**. Even so, v1.0 rated Workflow "High" because "existing admissions counselors can absorb approval of agent drafts within their current workload, since they already answer these inquiries." That is an invented fact. It also contradicts the design: under C4, every outbound message needs staff approval, so the experiment adds review work.

"Culture: High - staff are used to AI because of Violet" is a second unsupported inference; the case does not describe staff views. The abstention field says "None identified." This is the factor the brief says the agent must ask about instead of inventing an answer.

## Preserved failure 4: readiness masked a weak technology decision (probe)

The probe keeps the contrast-1 organization and changes the application to a rule-based completeness check over fixed CRM fields. v1.0 rated everything "High" and said "implement the completeness-check agent this term." It never asked whether an agent fits the task. The course reading's test ("Otherwise, a deterministic solution may suffice", D27) and task-technology fit (C5) both point the other way. A ready organization was used to sign off a poor decision.

## Weakness 5: ratings without evidence or step

- Ratings are High/Medium/Low with almost no citations to case facts.
- They are not tied to a step. A sandbox proof of concept and a live experiment need different things, and v1.0 says SPS can do both "this cycle."
- Contrast 2 rates workflow "Low - insufficient staff to review agent outputs" without doing the arithmetic. At about 150 inquiries a week, a 10% experiment is about 15 drafts a week. That load is small; the real constraint lies elsewhere.
- No output names a single most-consequential gap.

## What worked

- All eight dimensions from the brief are named.
- The general paragraph is identical across cases.
- No legal conclusions.

## Revisions for v1.1 (same inputs; cycle 1 outputs not edited)

1. **Step first.** Readiness is assessed for a named step (proof of concept, bounded experiment, production/sustain), with a default blocking set per step.
2. **Fit screen before readiness.** Check task-technology fit and the deterministic-solution test. If the fit screen fails, report a weak technology decision and stop.
3. **Separation rule.** Technology maturity (carried from C4), technology/application fit, and organizational readiness go in three separate fields. Phrases that turn readiness into maturity are banned, and so is "ready, therefore adopt".
4. **Four ratings with evidence.** READY / PARTIAL / GAP / UNKNOWN, each tied to a case fact or source, and marked blocking or not for the step.
5. **Unknown rule.** Never fill an UNKNOWN with a typical value. Triage it as ask now, observe in the proof of concept, or close by decision. "Ask now" items become a written information request with a decision rule.
6. **Gap-trace and owner rules.** Every action names the gap it closes. Actions that duplicate an existing strength or close no observed gap are dropped. Owners come from roles named in the case.
7. **One most-consequential gap**, with the reason it outranks the others. Plus a four-way decision diagnosis: sound or weak decision × ready or not ready.

Generation and review occurred in the same session, so this is not an independent grade.
