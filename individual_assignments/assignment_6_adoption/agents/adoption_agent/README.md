# Emerging Technology Adoption Agent
Candidate v0.2, Assignment 6 / Lab 6 SubAgent 5. Standard supplied ChatGPT prompt workflow; no API key.

From the scaffold root:
1. `python tools/build_prompt.py --agent agents/adoption_agent --case agents/adoption_agent/cases/primary.json --out work/adoption_primary.txt`
2. Submit the complete packet to ChatGPT; save returned JSON as a new response file.
3. `python tools/validate_response.py agents/adoption_agent/responses/primary_v0.2.json`
4. `python tools/check_frozen_core.py`
5. `python agents/adoption_agent/records/recheck_contracts.py`

Review semantic reasoning separately using records/test_comparison.md. The structure checker is not a truth evaluator. Read decision_logic.md and experiment_protocol.md for the action categories and proposed study conditions. Baseline instructions, packet and output are preserved for comparison.

Current examples are model-authored in one conversation, not independent API runs. Python serialized the saved output content. No company pilot or measured local gains are claimed. The supplied original core, tools and templates remain unchanged. Student judgment/reflection review and GitHub publication remain outstanding; see submission-root VERSION_RECORD.json.
