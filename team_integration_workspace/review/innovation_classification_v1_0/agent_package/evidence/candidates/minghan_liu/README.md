# Innovation and Disruption Agent

Assignment 3 working specialist, version 1.1. Student: Minghan Liu.

This is a reproducible analytical specialist built from the frozen course scaffold. It evaluates a proposed technology/application; it does not contact applicants or operate NYU systems.

## Run
From the repository root, use Python 3 (standard library only):

```bash
python3 tools/check_frozen_core.py
python3 tools/build_prompt.py --agent agents/innovation_disruption_agent --case agents/innovation_disruption_agent/cases/primary.json
```

Paste the generated packet into ChatGPT and request JSON only. Save a NEW response file so archived tests remain intact, then run:

```bash
python3 tools/validate_response.py PATH_TO_NEW_RESPONSE.json
python3 agents/innovation_disruption_agent/tests/verify_package.py
```

Repeat with contrast_1.json and contrast_2.json. Check factual claims and the qualitative criteria manually. The extra checker covers only schema keywords present in the frozen contracts; it is not a general JSON Schema implementation. No API key is needed.

## Package map
- specialist_instructions.md: final specialist logic and embedded source summaries.
- cases/: unchanged primary, synthetic contrast and ambiguous FAQ inputs.
- responses/: final v1.1 outputs.
- tests/cycle_1 and tests/cycle_2: preserved instructions, outputs, reviews and hash manifests.
- tests/prompts/: exact generated prompt packets for both rounds.
- evidence/source_register.json: public sources, dates, support and limits.
- records/: criteria, business-model analysis, course alignment, Agent Record and team handoff.

## Before submission
Complete every [STUDENT INPUT REQUIRED] section in the English Word record. The student's independent judgment and personal reflection are deliberately not invented. Two testing rounds document revision; the title Sub Agent 2 Cycles names specialist number 2 and is not evidence of an exact two-cycle requirement. The updated assignment memo and Brightspace rubric govern this package.

## Evaluation limits
Outputs were generated and reviewed in one Codex conversation. They are not blinded or statistically independent tests. No applicant-service outcome or ROI was measured. See tests/cycle_2/review.md. Original teacher slides have not been republished.
