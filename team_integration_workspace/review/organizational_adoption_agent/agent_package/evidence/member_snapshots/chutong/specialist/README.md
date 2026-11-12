# Organizational Adoption Agent

Assignment 7, Chutong Wang, Special Dark. This specialist assesses whether the organization can absorb, govern and sustain the specified application. It does not recertify technical maturity, decide procurement, grant permission or implement an enterprise chart tool. Frozen common contracts remain unchanged.

Start with records/agent_record.md, readiness_framework.md, prioritized_actions.md, poc_and_use_case.md and intake_handoff.md. Review the actual outputs, original hashes, revision diagnosis and remaining limitations.

From the scaffold root:

```bash
python3 tools/check_frozen_core.py
python3 tools/build_prompt.py --agent agents/organizational_adoption_agent --case agents/organizational_adoption_agent/cases/primary.json --out work/organizational_primary_prompt.txt
```

Submit the packet in ordinary ChatGPT, save its actual JSON, and run tools/validate_response.py on that response. No API key, separate API account or pip installation is needed. Local verification checks structure and provenance; future responses may vary and saved cases do not establish independent reliability or company readiness.
