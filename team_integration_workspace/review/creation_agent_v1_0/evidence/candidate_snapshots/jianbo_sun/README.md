# Emerging Technology Creation Agent

Assignment 2, Creative Force. Student: Jianbo Sun. Version: 0.2-student, October 4, 2026.

This specialist explains a technology's origins and translates that history into bounded implications for an application and organization. The demonstration uses Transformer-based generative AI for internal retail reporting, external bank reporting and a missing-context case. Organizations are hypothetical.

## Run from the scaffold root

```bash
python tools/check_frozen_core.py
python tools/build_prompt.py --agent agents/creation_agent --case agents/creation_agent/cases/primary.json
```

Paste the generated packet from work/ into ChatGPT. Save its JSON response, then run:

```bash
python tools/validate_response.py agents/creation_agent/responses/primary_response.json
```

Repeat for contrast_1.json and contrast_2.json. Preserve new runs under new filenames so the submitted evidence remains intact. No API key is required. The agent is a prompt-based specialist, not an autonomous API service.

## Evidence and integration

- specialist_instructions.md: creation framework, evidence policy and authority boundary.
- agent_metadata.json: name, specialty and version.
- cases/: unchanged common input fields plus source notes in additional_context.
- prompts/: exact saved prompt packets for this submission, including v0.1.
- responses/: initial weakness and revised primary/contrast outputs.
- evidence/source_register.json: original sources, checked dates and claim limitations.
- records/: agent record, qualitative review, execution provenance and validator log.
- revisions/: initial/revised instructions and weakness diagnosis.

All 32 original scaffold files remain byte-for-byte unchanged. Only this specialist folder was added. The common schemas retain 11 required input fields and 13 required top-level output fields. They are located in core/input_schema.json and core/output_schema.json.

The orchestrator should keep general_et_finding, application_finding and organization_specific_finding separate; retain dated evidence, confidence and abstention fields. Route market diffusion, organizational readiness and demonstrated value to the relevant experts. A positive creation finding is not an adoption decision. This is an individual candidate, not a team-approved agent.
