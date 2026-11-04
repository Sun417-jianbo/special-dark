# Recommendation categories and decision logic (v1.1)

**Sources:** Module 8 classification and adoption rules (C1); Module 6 early-adopter rule (C2); upstream rules from A4 and A5 (C3). Rows marked *student extension* were added after the cycle 1 failures.

## Permitted recommendations

| Recommendation | Meaning | Real users? | When allowed |
|---|---|---|---|
| Adopt / implement | Production use as the standard process, with an operational owner | Yes | Class is leading edge or commodity (Rule 3); relative advantage shown; no defer gate open |
| Bounded experiment | Capped live use (share, programs, weeks); reversible in days; human approval of consequential outputs; measures against the real baseline set in advance; stop rule; abandonment acceptable | Limited | Bleeding edge (Rule 2) for an early adopter willing to abandon (C2), or after proof-of-concept gates pass for a fast follower |
| Proof of concept | Sandbox feasibility and comparison with synthetic or approved inputs | No | Bleeding edge, relative advantage unproven, testable without users |
| Continue monitoring | No build; triggers and a review date; low-cost preparation | No | Bleeding edge for a conservative or low-capability organization |
| Defer | Decision postponed pending named decision-critical evidence, with owner and date | No | **Defer gate** (*student extension*): a missing fact could allow hard-to-reverse harm |
| Reject for the present | Dominated by an alternative, unacceptable irreversible risk, or not a real product; always with a review date | No | **Reject gate** (*student extension*): A/B evidence only; never a permanent ban |

## Order of decision

1. **Defer gate.** Is a decision-critical fact missing (vendor data terms, permission scope, privacy/legal review), and could acting cause hard-to-reverse harm? If yes, Defer that action.
2. **Reject gate.** Is there A/B evidence of a dominant alternative, unacceptable irreversible risk, or a product that is not real? If yes, Reject for the present, with a review date.
3. **Classify the technology for this application** (C1): bleeding, leading, commodity or trailing edge. The application can change the class; the organization's posture cannot (*student extension*, from C1 slide 61).
4. **Permitted set by class:**
   - bleeding edge: proof of concept, bounded experiment or monitor (Rules 1 and 2);
   - leading edge: adopt (Rule 3);
   - commodity: adopt on cost;
   - trailing edge: replace (Rule 4).
5. **Posture chooses within the set:**
   - early adopter: bounded experiment;
   - fast follower: proof of concept, then an experiment if the gates pass;
   - conservative: monitor.
6. **Upstream checks.**
   - Incremental-counterfactual test (A4): the step must be justified even if the technology were merely incremental.
   - Denominator rule (A5): general generative-AI use is not crossing evidence for this application.
7. **Bias check** (*student extension*): sunk cost, scarcity or FOMO, novelty or first-mover, excessive conservatism.
8. **Output:**
   - tags: [General], [Application-decisive], [Organization-decisive];
   - gates, each with an owner, measure, comparison, threshold and stop rule;
   - triggers for all six memo types;
   - the issue handed to Organizational Adoption.

## Results (evidence date 2026-11-01)

| Case | Class | Recommendation | Decisive factor |
|---|---|---|---|
| NYU SPS (fast follower) | Bleeding edge | **Proof of concept now**, gated to a bounded experiment this cycle | Unproven advantage over Violet |
| Online provider (aggressive, synthetic) | Bleeding edge | **Bounded experiment** for one quarter with an abandonment criterion | Early-adopter posture, willingness to abandon, capability |
| Small college (conservative, synthetic) | Bleeding edge | **Continue monitoring**; proposed ban not supported | Conservative posture and minimal capability |
| Qualification probe (CRM writes, missing data terms) | Bleeding edge | **Defer**, with a four-item evidence request | Decision-critical facts missing |
