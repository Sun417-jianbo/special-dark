# Innovation and Disruption Agent

Assignment 3 candidate v0.2 for Jianbo Sun. This is a prompt-based specialist using the instructor's ChatGPT workflow; it is not an autonomous API service. All original scaffold files remain unchanged.

From the scaffold root:
```bash
python tools/check_frozen_core.py
python tools/build_prompt.py --agent agents/innovation_disruption_agent --case agents/innovation_disruption_agent/cases/primary.json
python tools/validate_response.py agents/innovation_disruption_agent/responses/primary_response.json
python agents/innovation_disruption_agent/records/recheck_contracts.py
```
Run built prompt packets in ChatGPT and save new responses under a new filename before comparing them. Do not overwrite the preserved baseline. No API key is required.

- specialist_instructions.md: classification and disruption rules.
- cases/: three hypothetical contexts with the same verified evidence packet.
- prompts/: archived assembled inputs.
- responses/: model-authored outputs, including v0.1 weakness.
- evidence/: source register with claim limits.
- revisions/: exact instruction versions and diagnosis.
- records/: review, validation, provenance, Agent Record and reflection draft.

No team approval or Brightspace submission is claimed. Sources were checked by Codex; personal reflection and independent judgment need student review.
