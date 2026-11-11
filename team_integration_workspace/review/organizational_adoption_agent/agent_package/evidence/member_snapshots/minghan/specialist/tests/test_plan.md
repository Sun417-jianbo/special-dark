# Test plan

Four inputs are run under v1.0 (cycle 1) and v1.1 (cycle 2). The inputs do not change between cycles. Cycle 1 outputs are archived before the critique and never edited. The case designs below, the v1.0 instructions and the source register were committed before any response was generated.

**Design choice.** The adoption posture is held constant (moderate / fast follower) across the primary and both contrasts. Technology, application, industry, need, risk and horizon are also identical. Only the organization, its stakeholders and its capabilities/constraints change. Any change in the readiness conclusion can therefore be attributed to readiness, not to appetite for risk (which was Assignment 6's contrast).

| Case | Change vs primary | Expected if the agent works |
|---|---|---|
| primary | NYU SPS; several facts verified, several are course-case assumptions, and approval capacity is not supplied | Proof of concept: ready with conditions. Live experiment: not yet ready. A specific information request for the missing capacity facts, not an invented answer |
| contrast_1 | Synthetic high-readiness enrollment office: funded, measured volume, protected review hours, named content owner, governance templates; but a CRM migration overlaps the experiment | Experiment ready with conditions; the gap is the timing collision, not a generic checklist; no "adopt" (the technology class does not change with readiness) |
| contrast_2 | Synthetic low-readiness small college: no budget, hiring freeze, three staff, no AI data rule, outsourced IT, stated staff fear of cuts | Not yet ready. The reason is organizational, not "the technology is too immature". Actions proportionate to a three-person office |
| decision_probe | Same organization as contrast_1; the application becomes a rule-based completeness check with reminder emails | Weak technology decision, not a readiness problem. High readiness must not produce a "ready to implement" sign-off |

**Review criteria:**
1. Exact frozen contract.
2. Technology/application fit and organizational readiness reported as separate findings; neither one rewrites the other.
3. All eight readiness dimensions rated, each with evidence.
4. Strengths and gaps specific to each organization.
5. Every action traced to an observed gap; owners taken from the case.
6. One most-consequential gap, with a reason.
7. An explicit information request where a blocking fact is missing; no invented facts.
8. The readiness conclusion changes when capabilities change (primary vs contrasts).
9. Readiness does not mask a weak decision (probe).
10. No legal conclusions.

**Execution.** The frozen `build_prompt.py` builds the packets. They are run with Claude in place of ChatGPT; generation and review occur in the same session. The frozen `validate_response.py` and `tests/verify_package.py` check the outputs. The runs are not blinded or independent.
