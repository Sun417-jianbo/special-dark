# Promethean Technology Classification Agent
Candidate v0.2 for Assignment 4 / SubAgent 3. Run from the scaffold root. No API key required.

1. Build a packet: `python tools/build_prompt.py --agent agents/promethean_agent --case agents/promethean_agent/cases/primary.json --out work/promethean_primary.txt`
2. Paste the complete packet into ChatGPT. Save the returned JSON as a new file in `agents/promethean_agent/responses/`; retain existing evidence.
3. Validate: `python tools/validate_response.py agents/promethean_agent/responses/primary_v0.2.json`
4. Check core: `python tools/check_frozen_core.py`
5. Review substantive reasoning using `records/test_comparison.md`; valid structure is not sufficient.

Files: specialist instructions and metadata; four cases; dated source register and bounded packet; five prompts/responses including v0.1; preserved revision/weakness; comparison, validation and provenance records; reflection draft. Source script outputs are illustrative same-session examples, not independent benchmark results. The report and source commit record are in the submission package root.

Before submission, Jianbo should confirm the professional judgment and personalize the explicit reflection. Before team integration, obtain independent tests and agreement; no team approval is claimed.
