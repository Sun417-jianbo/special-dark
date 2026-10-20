# Special Dark TW5 Promethean Classification

One Team Agent Record and the complete working specialist package are prepared in this folder. The ZIP contains that same Word, evidence, tests, source register and repository handoff. Original course and member materials remain untouched. QA renders, temporary scripts and duplicate authored report drafts are excluded. The scaffold's docs, templates and toy example are instructor reference files, not extra student drafts.

Status: team-accepted version 1.0, confirmed through Yufei Cai on 2026-10-20. The final specialist combines contributions from all four individual Lab 4 submissions. The adopted decision and attributed contributions are recorded under agent_package/team_records.

Current specialist: agent_package/agents/promethean_classification_agent. Candidate originals are compact attributed bundles under evidence/candidates; their original self-reports are not new verification. Read team_records/candidate_comparison.md, synthesis_decision.md and test_and_failure_log.md. The source register bounds every accepted external claim. Run python3 verification/recheck.py from agent_package for structural and integrity checks, not an accuracy benchmark.

Repository: https://github.com/Sun417-jianbo/special-dark
Branch: tw5-promethean-classification-20261020
Directory: team_integration_workspace/review/promethean_classification
No automatic merge or Brightspace submission is performed. Follow the actual upload fields and deadline. The local material does not establish a Word-only submission requirement.

## Working with the specialist

From agent_package, build a packet with:
`python3 tools/build_prompt.py --agent agents/promethean_classification_agent --case agents/promethean_classification_agent/cases/primary.json --out work/promethean_primary_prompt.txt`

Use that packet in ChatGPT/Codex and save the structured response. Validate a saved example with:
`python3 tools/validate_response.py agents/promethean_classification_agent/responses/primary_response.json`

Run `python3 verification/recheck.py` for the packaged contract/integrity fixtures. The preserved failed artifacts are required test history, not alternative final reports.


Release status 2026-10-20: version 1.0 records the team's accepted analytical scheme and its handoff for academic integration. Operational adoption remains subject to the separate Adoption and Organizational Readiness decisions.
