# Minghan Liu — Creation Agent Candidate (Team Lab 3 handoff)

## What this package contains
- `specialist_instructions.md` (v1.1) — the candidate agent's creation-lens instructions
- `agent_metadata.json` — agent identity/version
- `cases/` — primary case (NYU SPS prospective-student engagement), contrast_1 (regional hospital intake), contrast_2 (abstention test, org context withheld)
- `responses/` — the agent's validated JSON outputs for all three cases
- `records/agent_record.md` — full Agent Record: design choices, evidence, tests, weakness + revision, independent judgment, GitHub version

## Technology analyzed
Agentic AI built on large language models.

## Decisive design choice
Three-level finding discipline (general ET → ET for the application → ET for the application in THIS organization) + a dated-evidence rule: any claim beyond "innovation" requires at least one dated usage/deployment metric.

## Best evidence
S1–S4 primary-source lineage, each opened and verified: Bengio et al. 2003 (JMLR), Vaswani et al. 2017 (arXiv:1706.03762), Brown et al. 2020 (arXiv:2005.14165), Ouyang et al. 2022 (arXiv:2203.02155).

## Preserved weakness
v1.0 claimed commercialization/application placement without a dated scale-of-use metric → revised to v1.1 with the dated-evidence rule. Also: abstention test — when org context was withheld, the agent correctly refused the org-level finding instead of inventing one.

## Version
https://github.com/lmh04250425/MASY1800-agents — branch `assignment-2-creation-agent`, commit `9073384541654b1f5d12fc1e1bd7b73a8ce3dfb5`
