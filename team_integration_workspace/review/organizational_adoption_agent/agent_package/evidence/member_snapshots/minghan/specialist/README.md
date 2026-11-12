# Organizational Adoption (Readiness) Agent

Assignment 7 (Lab 7 - SubAgent 6 Implementing). Specialist version 1.1. Student: Minghan Liu.

Governing question: *even if adoption is strategically appropriate, can this organization actually absorb, govern, and sustain the proposed application?*

This specialist judges organizational readiness **for a named step**: proof of concept, bounded experiment, or production/sustain. It keeps readiness separate from technology maturity and from technology/application fit, so that a weak decision and an unready organization are never confused.

The method has four parts:
1. A fit screen, which runs first.
2. A readiness framework, R1-R8: leadership and sponsorship, skills, workflow, infrastructure and data, resources and budget, governance and risk, culture and change, operating ownership.
3. Ratings of READY / PARTIAL / GAP / UNKNOWN, with evidence.
4. Rules for traced actions, owners, unknowns and the single most consequential gap.

Version 1.1 follows preserved cycle 1 failures:
- an identical six-item checklist for every organization;
- "too immature for a small college";
- "readiness offsets immaturity, so implement";
- an invented SPS capacity fact;
- a readiness sign-off for a weak decision.

**Current answer (2026-11-08):**

| Case | Proof of concept | Live bounded experiment | Most consequential gap |
|---|---|---|---|
| NYU SPS | Ready with conditions | **Not yet ready** | Operating ownership (R8); plus an information request on approval-queue capacity |
| High-readiness university (synthetic) | Ready | Ready with conditions | CRM migration overlaps the experiment (R4) |
| Low-readiness college (synthetic) | Not yet ready as proposed | Not yet ready | No funded staff time (R5) |
| Completeness-check probe | n/a | n/a | Weak technology decision (fit screen fails); redirect to a deterministic CRM rule |

## Run

From the repository root, use Python 3 (standard library only; no API key):

```bash
python3 tools/check_frozen_core.py
python3 tools/build_prompt.py --agent agents/org_adoption_agent --case agents/org_adoption_agent/cases/primary.json
# paste work/... into ChatGPT, ask for JSON only, save as a NEW file, then:
python3 tools/validate_response.py PATH_TO_NEW_RESPONSE.json
python3 agents/org_adoption_agent/tests/verify_package.py
```

## Package map

| Path | Contents |
|---|---|
| `specialist_instructions.md` | v1.1 procedure, R1-R8 framework, rules, and the graded register |
| `cases/` | primary, contrast_1, contrast_2, decision_probe |
| `responses/` | final v1.1 outputs |
| `tests/cycle_1/`, `tests/cycle_2/` | instructions, outputs, reviews and hash manifests (cycle 1 failures preserved) |
| `tests/prompts/` | exact packets |
| `tests/verify_package.py`, `validation_log.txt` | 31 checks |
| `evidence/source_register.json` | C1-C5, reused E/D sources, and new D26-D32, with grades |
| `records/` | readiness framework, information request, action challenge log, course alignment, team handoff (with intake fields), Agent Record (markdown) |
| `submission/` | Word Agent Record and checklist |

## Limits

- The prompt packets were run with Claude in place of ChatGPT. Generation and review occurred in the same session, and the runs were not blinded.
- Two organizations are synthetic, and several SPS facts are course-case assumptions.
- Readiness frameworks describe good practice; they are not validated predictors for this application.
- Regulatory points are flagged for compliance, not decided.
- The Module 9 deck was not available; task-technology fit is cited from the original paper.
