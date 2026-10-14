# Innovation and Disruption Agent

Chutong Wang | Assignment 3 | October 12, 2026

This prompt-based specialist evaluates innovation and creative destruction in context. It analyzes a proposed agentic-AI chart-review application; it does not implement a chart-checking system or authorize deployment. The primary case continues the TW3 financial-services scenario. The contrast deliberately changes the firm's economics to a studio selling routine analyst work. All organizations and economic premises are constructed teaching cases.

## Run from the repository root

Python 3 standard-library tools are supplied by the course. No OpenAI API key is needed.

```bash
python tools/check_frozen_core.py
python tools/build_prompt.py --agent agents/innovation_disruption_agent --case agents/innovation_disruption_agent/cases/primary.json
python tools/validate_response.py agents/innovation_disruption_agent/responses/cycle_2/primary_response.json
```

Paste the generated packet into ChatGPT, execute it and save the returned JSON. Repeat for `contrast_1.json` (services studio) and `contrast_2.json` (ambiguous vendor demo). Current instructions and metadata are the final candidate; version 0.1 is retained under `revisions/` and the first prompt packets preserve the original run configuration.

## Evidence map

- `specialist_instructions.md`: bounded criteria and common-field mapping.
- `cases/`: three unchanged contextual inputs.
- `prompts/cycle_1/` and `prompts/cycle_2/`: actual course-script prompt packets.
- `responses/cycle_1/` and `responses/cycle_2/`: preserved model outputs, not chart-tool performance data.
- `records/source_register.json`: original-source claims, limitations and access dates.
- `records/test_and_revision_log.md`: reasoning review, observed weakness and revision.
- `records/run_provenance.json`: execution receipts and input/output hashes.
- `records/agent_record.md` and Word record: findings and version handoff.
- `records/rubric_checklist.md`: four 20-point criteria from the supplied Brightspace screenshots.

Schema checks verify structure; reasoning review is separate. Limited examples, AI-generated context and assistant review do not establish general reliability. Student review of the final judgment and personal reflection remain essential. No observed company outcomes or full team approval are asserted.
