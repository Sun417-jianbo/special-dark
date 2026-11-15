# Landscape Agent 1.0

Individual candidate prepared for Jianbo Sun, Lab 8 / SubAgent 7. Assessment: 2026-11-15. Team approval, student endorsement, remote GitHub publication and LMS submission are pending.

## Use this agent for a new question
From the scaffold root, copy and edit cases/primary.json, including a fresh dated source packet in additional_context. Do not use this frozen evidence packet indefinitely.

```bash
python tools/build_prompt.py --agent agents/landscape_agent --case agents/landscape_agent/cases/primary.json --out work/landscape_prompt.txt
```

Send the COMPLETE work/landscape_prompt.txt to ChatGPT. Save the actual JSON answer to a new file, then run:

```bash
python tools/validate_response.py path/to/new_response.json
python tools/check_frozen_core.py
```

This is the supported prompt-agent workflow, not an always-on application or an autonomous API service. The supplied saved outputs are current-assistant-authored examples, not independently generated or independently evaluated runs. Do not present the serialization scripts as inference engines.

For stronger checking of the supplied artifacts, install the optional `jsonschema` dependency in your environment and run:

```bash
python agents/landscape_agent/tests/verify.py
```

The source register is embedded in each case; build_prompt.py does not automatically read separate evidence files. Refresh the register AND case source packets before rebuilding future prompts. Use original publisher evidence for consequential claims. Date the evidence observation, publication/update and retrieval separately.

## Inventory and handoff
Specialist: SubAgent 7 Landscape; status: individual candidate for team consideration. Version 0.1 and its weak monitoring output are preserved. Version 1.0 adds actionable triggers and explicit freshness/claim-scope rules. General finding stays stable across the primary/retail contrast; conventional alternatives and monitoring signals change. The hype probe retains Assess despite an unsupported 40% savings/free-access claim.

Most consequential signal: verified grounding in the actual tenant plus local task evidence. Strongest conventional alternative: authoritative checklist for the university case; approved FAQ/macros for retail. Proposed reassessment: access/terms verified and local quality/time gates met. These gates have NOT been tested on real documents.

Integration consumes the frozen common case schema and returns the frozen common JSON schema. Pass timestamped evidence, contrary evidence, intake gaps and monitoring owners to the MoE coordinator. Route adoption approval to Adoption, rollout to Implementing, origin to Creation, diffusion to Diffusion, disruption/cycles to its specialist, classification to Promethean. Landscape does not replace those judgments.

## Limits and remaining human work
Four original-source pages support a deliberately bounded comparison. No independent current market share, investment dataset, head-to-head product benchmark, tenant quote or local pilot exists. Local gates and owners are proposed. The same assistant authored and reviewed the saved responses. Student must review the judgment and personalize the clearly labeled reflection draft before submission. Repository publication remains a separate pending step.
