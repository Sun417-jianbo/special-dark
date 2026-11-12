# Request-for-more-information condition (assignment step 6)

**Factor:** approval-queue capacity for the SPS bounded experiment (dimension R3, workflow and process).

**Why this factor:** the Adoption specialist's design (C4) requires a counselor to approve every outbound message during the experiment. Whether SPS can run that design depends on facts the case does not supply:
- weekly and peak-season inquiry volume;
- counselor hours that can be protected for review.

v1.0 invented the answer: counselors "can absorb approval of agent drafts within their current workload". v1.1 asks for it.

## Why it is asked now, and the other unknowns are not

| Unknown | Triage | Reason |
|---|---|---|
| Approval-queue capacity (R3) | **Ask now** | It blocks the experiment, it is a fact, and neither a decision nor the PoC can supply peak volume or protectable hours |
| Staff views of the change (R7) | Observe in the PoC | Counselors reviewing sandbox drafts is itself the trial |
| Minutes per review | Observe in the PoC | Measured during the PoC, and an input to the rule below |
| Operating owner (R8) | Close by decision | Leadership can name one; it becomes ACT-2 |
| Review-time budget (R5) | Close by decision | It becomes ACT-4 |

## The request (as the agent states it)

| Item | Needed | Who has it |
|---|---|---|
| 1 | Weekly web-inquiry volume, and the peak-season weekly volume | Admissions counselors' manager |
| 2 | Counselor hours per week that can be protected for reviewing drafts, and who covers peaks | Admissions counselors' manager; SPS enrollment management leadership |
| 3 | Target response time | SPS enrollment management leadership |
| 4 | Current Violet hand-off volume, if tracked | Admissions / marketing-enrollment staff |

**Decision rule when it arrives:**

experiment share = protected hours × 60 ÷ (peak weekly inquiries × minutes per review measured in the PoC), capped at 10% (C4).

If the share would be too small to learn from (proposed floor: about 2%), fund review time before starting. Until the data arrive, R3 stays UNKNOWN and the experiment verdict cannot be READY.

**Worked illustration (synthetic contrast 1, not SPS):**
- 2,500 inquiries at peak × 3 minutes per draft at 10% = 12.5 hours, within 20 protected hours.
- Break-even: 20 × 60 ÷ 250 = 4.8 minutes per draft.

SPS's own numbers are unknown, so no SPS figure is given.
