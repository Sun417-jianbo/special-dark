# Readiness framework (v1.1)

The agent answers one question: **"Can this organization execute this step now?"** It keeps that question apart from **"Is this a good technology decision?"**

## 1. Order of work

1. **Step.** Proof of concept (sandbox, no real users), bounded experiment (live users, human approval) or production/sustain. Permitted steps come from the Adoption specialist (C4). Production adoption of a bleeding-edge application is never assessed.
2. **Fit screen** (technology/application fit). Does the task need judgment, exceptions, hard-to-maintain rules, unstructured language or multi-step tool use (D27, C5)? If not, a deterministic solution may suffice (D27, E15). A failed fit screen ends the assessment: the result is a weak technology decision.
3. **Rate R1-R8** for the step, with evidence.
4. **Verdict and decision diagnosis.**
5. **Actions** (gap-trace and owner rules).
6. **Information request and triggers.**

## 2. Dimensions

| ID | Dimension | Ready for a live, human-approved experiment means | Failure it prevents even if the technology works | Main source |
|---|---|---|---|---|
| R1 | Leadership & sponsorship | Named sponsor; decision rights; budget for the step; stop authority | Orphaned pilot | D26 GOVERN 2.3 |
| R2 | Skills & training | Reviewers know the error types and the correction process; outputs evaluated systematically | Rubber-stamping or blanket rejection | D26 GOVERN 2.2 |
| R3 | Workflow & process | Review step defined; workflow redesigned, not bolted on; capacity covers **peak** load | Queue backs up; applicants wait longer | D28 |
| R4 | Infrastructure & data | Approved-content source of truth; least-privilege integration; logging; sandbox | Stale content; uncontrolled actions | C4, D27 |
| R5 | Resources & budget | Step and next step funded, **including staff review time and content upkeep** | Abandoned after the proof of concept | D22, D29, D7 |
| R6 | Governance & risk | Data classified; vendor terms reviewed; compliance review; incident procedure; deactivation responsibility | Error or data exposure with no response path | D32, D26 GOVERN 6.1, MANAGE 2.4/4.1/4.3, D21 |
| R7 | Culture & change | Staff (internal adopters) find it compatible and can try it; trust in how saved time is used | Resistance, workarounds, discontinuance | C2 |
| R8 | Operating ownership | One owner for content, queue, monitoring, incidents, change and retirement | Agent drifts; nobody fixes or stops it | D26 GOVERN 2.1, 3.2 |

**Coverage check.** EDUCAUSE's readiness assessment uses Strategy, Governance, Technology, Workforce, and Teaching and Learning (D30).
- R1 maps to Strategy, R6 to Governance, R4 to Technology, and R2 and R7 to Workforce.
- Teaching and Learning is out of scope for admissions.
- R3, R5 and R8 are added because the documented failure points sit there: workflow redesign (D28); cost and value after the proof of concept (D29, D7); and owned risk controls (D26).

## 3. Ratings and blocking

| Rating | Meaning |
|---|---|
| READY | Case evidence shows the dimension is adequate for the step |
| PARTIAL | Some evidence; a named element is missing |
| GAP | Case evidence shows it is inadequate |
| UNKNOWN | No evidence in the case. It is never silently converted into a rating; see triage below |

**Default blocking sets:**
- **Proof of concept:** R1, R2, R4, R5, R6 (test data only).
- **Bounded experiment:** all eight.
- **Production/sustain:** all eight, plus recurring budget and full ownership.

**UNKNOWN triage:**
- (a) **Ask now**: blocking, factual, not settled by a decision or by the proof of concept.
- (b) **Observe in the proof of concept**: the PoC will produce the evidence.
- (c) **Close by decision**: a manager can settle it by deciding, so it becomes an action.

## 4. Verdicts and decision diagnosis

**Verdicts:** READY / READY WITH CONDITIONS / NOT YET READY / CANNOT DETERMINE. A verdict is given per step.

| | Organization ready | Organization not yet ready |
|---|---|---|
| **Sound technology decision** | Proceed with the step | Build readiness; keep the decision; do not downgrade the technology |
| **Weak technology decision** | Redirect; readiness does not rescue it | Stop; do not invest in readiness for it |

## 5. Action rules

- **Gap-trace:** every action closes a named GAP-, PARTIAL- or UNKNOWN-Rn, or verifies a named assumption (VERIFY-Rn). An action that closes no observed gap is dropped.
- **Owner:** only roles named in the case, or "owner to be named by" a named role.
- **Priority:**
  - P1: blocks the next step.
  - P2: needed before scaling.
  - P3: needed to sustain operation.
  - At most six actions; mark the no-regret ones.
- **Most consequential gap:** exactly one, with the reason it outranks the others: it is blocking, most likely to fail even if the technology works, and slowest to fix.
- **Proportionality:** the size of the remedy matches the size of the organization.
