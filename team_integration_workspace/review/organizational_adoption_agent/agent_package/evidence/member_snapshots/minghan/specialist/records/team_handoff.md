# Team handoff (Assignment 7, Organizational Adoption / Readiness specialist)

| Item | Content |
|---|---|
| Agent package | `agents/org_adoption_agent` (v1.1 instructions with R1-R8 framework and graded register, four cases, eight archived outputs, 31-check verifier, records) |
| Readiness conclusion (SPS) | **Proof of concept: ready with conditions. Live bounded experiment: not yet ready.** This is a sound technology decision that SPS is not yet prepared to execute at the live step |
| Most important gap | **GAP-R8 operating ownership.** No one is named to own agent content, the review queue, incidents and the stop decision |
| Most important action | **ACT-2:** SPS enrollment management leadership names one owner, with a deputy, for the applicant-support channel (Violet and the agent), with a content-update rule. It is a no-regret action because Violet needs it too |
| Missing-information condition | **Approval-queue capacity** (R3): weekly and peak inquiry volume, and protectable counselor review hours. Decision rule: experiment share = hours × 60 ÷ (peak inquiries × minutes per review), capped at 10% |
| Upstream consistency | The A6 class (bleeding edge) and its path (PoC, then gated experiment) are unchanged. A7 operationalizes A6 gate G4 (approval capacity) and adds ownership, funding and compliance conditions |

## Organizational fields the final intake form must capture

The common intake has one free-text field, `capabilities_constraints`. For this expert to work well, the final form should split it into these fields. Each one maps to a dimension, and each was needed in at least one test case.

| # | Intake field | Dimension | Why the expert needs it |
|---|---|---|---|
| 1 | Step under consideration (PoC / bounded experiment / production) and its scope | all | Readiness is step-relative |
| 2 | Sponsor role, decision rights, budget for this step and the next, stop authority | R1, R5 | Distinguishes a sponsor from a funded, accountable sponsor |
| 3 | Weekly and peak inquiry (task) volume; staff hours protectable for human review; target response time | R3 | Drives the capacity rule; SPS lacked it |
| 4 | Named operating owner (content, queue, incidents, retirement), or "none" | R8 | The most consequential SPS gap |
| 5 | Staff experience with AI tools; existing correction or QA processes | R2 | Separates general familiarity from review skill |
| 6 | Systems: CRM/scheduling platform, API access, planned migrations, and who builds integrations | R4 | Revealed the contrast-1 collision |
| 7 | Data rules: data classification, vendor terms status, compliance review status, incident and pause procedure | R6 | Blocks any live step |
| 8 | Staff views, recent staffing changes, and concerns about job impact (as stated by the organization) | R7 | Revealed the contrast-2 trust gap |
| 9 | Concurrent changes or initiatives competing for the same people | R4, R5 | Change saturation |
| 10 | Which of the above are verified facts, assumptions, or not known | all | Lets the agent apply the unknown rule instead of guessing |

## For the next specialist and the orchestrator

- **Landscape specialist (A8):** vendor shortlist only after ACT-5's data-terms requirements are known (no-training, retention, deletion, least-privilege connector).
- **Orchestrator rule:** run the fit screen before readiness. If the fit screen fails (weak decision), do not call this specialist's readiness program.
- **Orchestrator rule:** readiness findings may change timing, scope and conditions. They never change the technology class.
