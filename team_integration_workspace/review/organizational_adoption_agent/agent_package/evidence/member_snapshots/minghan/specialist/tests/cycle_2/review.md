# Cycle 2 review (v1.1)

The same four inputs were rerun with the revised instructions; cycle 1 outputs were not edited. All eight archived outputs pass the frozen validator. The 31 checks in `tests/verify_package.py` also pass. These checks confirm structure and the promised invariances, not that a readiness judgment is right.

| Review question | Cycle 1 (v1.0) | Cycle 2 (v1.1) | Remaining limit |
|---|---|---|---|
| Generic checklist? | Same six actions in all four outputs (overlap 1.00); three of them duplicate things contrast 1 already has | Every action names the gap it closes; no action text repeats; overlap between organizations at most 0.28 | Gap tags are the author's judgment |
| Readiness vs maturity | Small college: "too immature for an institution of this size". University: "readiness offsets the technology's immaturity... full implementation" | Maturity carried from C4 and identical everywhere; fit screen separate; readiness separate; the small college is "not yet ready" for organizational reasons; the university is "ready with conditions" for the experiment, not adoption | Rests on the Adoption specialist's class (C4) |
| Missing facts (SPS) | Invented: counselors "can absorb approval of agent drafts within their current workload" | R3 = UNKNOWN; an information request with the data needed, who holds it and a decision rule (experiment share formula) | The 2% "too small to learn from" floor is a proposal |
| Step | "Proof of concept and bounded experiment this cycle" | Verdicts per step: PoC ready with conditions; live experiment not yet ready | Step definitions come from C4 |
| Most consequential gap | None named | SPS: GAP-R8 operating ownership; university: PARTIAL-R4 CRM-migration collision; college: GAP-R5 no funded staff time | Ranking rule is a design choice |
| Weak decision masked? | Probe: "ready to implement the completeness-check agent this term" | Fit screen FAIL: rule-based task, deterministic CRM rule suffices (D27, E15, C5); readiness not assessed; redirected to the Adoption specialist | Assumes the task is fully rule-based, as the case states |
| Owners | "Senior leadership", "IT", "project lead" | Only roles named in the case, or "owner to be named by" a named role | Real people unknown for SPS |
| Proportionality | Governance committee for a three-person office | Committee dropped; a short written data rule instead | — |

## Contrast result: what stayed the same and what changed

**Stayed the same, correctly:**
- the technology-maturity finding, byte-identical in all four outputs;
- the fit-screen finding (PASS) for the three cases with the same application;
- the adoption posture (held constant by design);
- "no production adoption" for this bleeding-edge class, whatever the readiness.

**Changed, correctly, because capabilities and constraints changed:**

| | NYU SPS (primary) | High-readiness university (contrast 1) | Low-readiness college (contrast 2) |
|---|---|---|---|
| Live experiment | NOT YET READY | READY WITH CONDITIONS | NOT YET READY |
| Proof of concept | READY WITH CONDITIONS | READY | NOT YET READY as proposed |
| Most consequential gap | Operating ownership (R8) | CRM migration overlaps the experiment (R4) | No funded staff time (R5) |
| Information request | Yes: approval-queue capacity | None needed | None needed |
| Number of actions | 6 | 3 | 5 |

**Changed, correctly, because the decision changed:** the probe keeps contrast 1's organization but changes the application. The verdict moves from "ready with conditions" to "weak technology decision; readiness not assessed".

## Two judgment points worth noting

1. **The small college's problem is not review volume.** v1.0 said "insufficient staff to review agent outputs". v1.1 does the arithmetic: 10% of about 150 inquiries is about 15 drafts a week, roughly an hour. The binding constraint is the unfunded setup, testing and ownership work, under a hiring freeze. A checklist answer would have missed this.
2. **SPS's most consequential gap is ownership, not capacity.** Capacity is unknown, so the agent asks for it instead of guessing. Ownership is an observed gap that blocks the other fixes, and it is a no-regret fix because Violet needs the same owner.

## AI challenge of the actions (AI-leverage hint 2)

Every v1.0 and candidate v1.1 action was tested with one question: does it close a gap observed in this case, or does it only sound like good management? The full log is in `records/action_challenge.md`.
- Across the three organizations, the six v1.0 checklist actions (18 case-action pairs) were dropped 9 times, recast 8 times into specific traced actions, and deferred once.
- Three further generic candidates were dropped for SPS: an AI center of excellence, a chief AI officer and a culture campaign.
- Five v1.1 actions have no checklist counterpart, including the SPS operating-owner action, which closes the most consequential gap.

## Limits

- Generation and review occurred in the same session, with Claude in place of ChatGPT; there was no blinded scoring.
- Two organizations are synthetic, and several SPS facts are course-case assumptions.
- The readiness frameworks used (D26, D30) describe practice; they are not validated predictors for this application.
- Legal points are flagged for compliance, not decided.
- Recommended next step: paste `tests/prompts/cycle_2/primary.txt` into ChatGPT and compare its verdicts and information request.
