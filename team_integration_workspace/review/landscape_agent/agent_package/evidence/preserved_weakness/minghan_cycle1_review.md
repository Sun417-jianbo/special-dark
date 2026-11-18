# Cycle 1 review (v1.0)

All four v1.0 outputs pass the frozen validator, and the general paragraph is identical in all four. The landscape analysis still fails the brief in six ways. This review checks each output against the brief, the dated register and the upstream specialists (C4, C6). The AI-leverage hints ask three things:
- whether the agent separates popular signals from signals that could change the decision;
- whether it changes what it considers relevant when the application changes;
- whether claims go back to original dated sources.

## Preserved failure 1: one market summary for every context

The organization-specific finding is the **same market paragraph** in all four outputs, with only the opening words changed ("For NYU SPS:", "For the software company:", "For the Dutch university:"):
- the same players;
- the same investment forecast;
- the same adoption figure;
- the same vendor time-savings claim;
- the same hype-cycle label;
- the same score.

The coding contrast should have brought in a different competitor set (IDE assistants and code review), different evidence (a randomized productivity trial, D36) and different risks (code execution, supply chain, D45). The EU contrast should have moved regulation from "evolving" to binding, because Article 50 has applied since 2 August 2026 (D33) and GDPR Article 22 applies (D47). Neither happened. This is the "simply repeating the same market summary" failure the hint describes.

## Preserved failure 2: a single score and a fashionable framework replaced the explanation

Every output gives "Hype-cycle position: Peak of Inflated Expectations" and "Overall landscape score: 6/10". Neither is backed by evidence, and neither tells management what to do. The same 6/10 is given to admissions agents, where there is no measured adoption rate, and to coding agents, where agents are scaled most often (D42). The brief says explicitly that a single score or fashionable framework must not substitute for explanation and evidence.

## Preserved failure 3: vendor claims and forecasts treated as findings

- **"Agents save large amounts of staff time"** and **"more than 67 full-time work years"** (D41) are presented as landscape facts. They are vendor claims with no disclosed method. The arithmetic also does not reconcile: 11.8 million minutes is about 95 work-years at 2,080 hours per year, not 67.
- **"Top models score 88-96% on SWE-bench Verified, which shows they can solve most real software issues"** (contrast 1). Those are vendor self-reports on a benchmark the aggregator itself marks as saturated and contaminated (D48). An independent randomized trial found experienced developers 19% slower with early-2025 tools (D36), and v1.0 never mentions it.
- **Gartner's forecasts** (D43) open the general finding as if they described the current state.
- **Evidence types are loose labels** ("analyst", "case study"). There is no vendor / industry / independent / standards-regulatory / inference distinction and no source-diversity check.

## Preserved failure 4: a stale claim used as current

"The most competitive agent completes 30% of realistic workplace tasks (E11)" is presented as the current state, dated only "2024". The same benchmark's leaderboard now shows 42.9% for a model published in September 2025 (D35), and newer frontier models are not on it at all. This is the claim the team has carried since Assignment 6, and nobody refreshed it.

## Preserved failure 5: vague monitoring

The triggers ("monitor vendor announcements regularly", "monitor regulatory developments") give no cadence, no threshold and no consequence. They are identical in all four cases.

## Preserved failure 6: the hype probe moved the decision

Given five forwarded headlines, v1.0 repeated the hypothetical vendor's "90% without staff" claim, called the 96% coding benchmark evidence of momentum for admissions, concluded that "SPS risks falling behind", and recommended moving "directly to a live bounded experiment this cycle". That skips the proof of concept the Adoption specialist requires (C4) and the readiness conditions (C6). Every item was a vendor claim, a forecast, an existence proof without outcomes, or evidence from a different application.

## What worked

- Dated sources from the register are used.
- MCP's move to a neutral foundation (D38) is correctly reported.
- No legal conclusions.

## Revisions for v1.1 (same inputs; cycle 1 outputs not edited)

1. **Ten landscape dimensions**, each assessed broadly and then for this case.
2. **Relevance filter with a flip test.** A signal is DECISION-RELEVANT only if reversing it would change a named decision of this organization within its horizon. WATCH signals carry a named threshold; everything else is BACKGROUND, however popular.
3. **Evidence typing and diversity.** VENDOR / INDUSTRY / INDEPENDENT / STANDARD-REG / ORGANIZATION / INFERENCE. Minimum evidence by claim type; vendor-only and forecast-only claims cannot move the position.
4. **Freshness.** Every claim gets a refresh class (FAST / MEDIUM / SLOW). Claims past their half-life are flagged STALE-RISK and refreshed or caveated.
5. **Position summary without a score.** Per dimension: broad position, direction, relevance tier and the dated evidence. Single scores and hype-cycle labels are banned.
6. **Triggers.** Each trigger names what to watch, the cadence, the threshold, what it would change and who watches.
7. **One stale or hype-sensitive claim**, named and refreshed.

Generation and review occurred in the same session, so this is not an independent grade.
