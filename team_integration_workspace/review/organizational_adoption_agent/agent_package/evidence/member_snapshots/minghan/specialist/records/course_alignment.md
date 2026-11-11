# Course alignment

| Assignment 7 requirement | Where it is met |
|---|---|
| 1. Structured readiness framework covering leadership/sponsorship, skills, workflow/process, infrastructure/data, resources/budget, governance/risk, culture/change, operating ownership | `specialist_instructions.md` §Readiness framework; `records/readiness_framework.md`. R1-R8 with "ready means", failure prevented, ratings, blocking sets |
| 2. Current strengths and the gaps that could cause failure even if the technology works | Every assessed output: "Strengths:" (STR-Rn) and "Gaps that could cause failure even if the technology works:" |
| 3. Separate findings for technology/application fit and organizational readiness | Separation rule. `general_et_finding` holds maturity (identical in all four cases); `application_finding` holds the fit screen; `organization_specific_finding` holds readiness. Verifier checks 19-20 |
| 4. Prioritized readiness actions with owners | ACT-n with P1/P2/P3, the gap closed, an owner from case roles and a done-when test. Gap-trace and owner rules; verifier checks 24-26 |
| 5. Primary and context-contrast tests, same technology and application in materially different organizations; the conclusion changes | Primary SPS; contrast 1 high readiness; contrast 2 low readiness. Posture is held constant, so the change is due to readiness. `tests/cycle_2/review.md` |
| 6. Revise the agent; one factor where the agent asks instead of inventing | Cycle 1 to cycle 2; `records/information_request.md` (approval-queue capacity) |
| AI-leverage hint 1: contrasting profiles to test sensitivity vs a generic checklist | Contrasts 1 and 2; action overlap 1.00 (v1.0) vs at most 0.28 (v1.1) |
| AI-leverage hint 2: challenge each action against an observed gap | `records/action_challenge.md` |
| AI-leverage hint 3: verify material claims about regulation, infrastructure, skills and practices | Register D26-D32, opened 2026-11-08; legal points flagged, not decided |
| Common context rule: the organization does not rewrite general evidence | The technology finding is byte-identical in all outputs; "readiness never changes the class" |
| Team handoff, including the intake fields | `records/team_handoff.md` |

## Course concepts used

- **Module 8 (C1):**
  - Rule #1 (no adoption before the crossing) and Rule #2 (pilot) bound the steps this agent may assess.
  - Rule #7 (know the adoption style your job requires): readiness is judged for the step the organization's role permits, not for "adoption" in general.
  - Slide 54 previews Module 9 (Implementing Emerging Technologies: Proof of Concept, Task Technology Fit). These two topics drive the step logic and the fit screen.
- **Module 6 (C2):**
  - Staff are the internal adopters. Compatibility and trialability drive R7.
  - The proof of concept doubles as a trial for staff.
  - Change agents are named only where observed; "stabilize adoption and prevent discontinuance" is what R8 ownership protects.
- **Prep Lab 2 reading (D27):** "When should you build an agent?" supplies the fit-screen criteria and the deterministic-solution test used in the probe.
- **Upstream chain:**
  - A3: compare baselines.
  - A4: significance carries Low weight on present decisions.
  - A5: denominator rule.
  - A6: bleeding edge, PoC gated to an experiment, gate G4 (capacity).

  A7 adds: can this organization execute the permitted step?

**Not available:** the Module 9 deck itself. Task-technology fit is cited from the original paper (C5). If the deck uses different terms, align the vocabulary in the next revision.
