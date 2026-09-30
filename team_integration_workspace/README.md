# Team Integration Workspace

Shared working area for the MASY1-GC 1800 Emerging Technologies team-approved specialist agents (Team Labs 2–9) and the final mixture-of-experts integration (Team Labs 10–11).

## Rules
1. The canonical frozen Brightspace ZIP is **never modified**. Every team working copy is extracted fresh from it.
2. Individual candidate packages live in `candidates/<member>/` (read-only comparison area) — they are **never merged** into a team working copy.
3. Each team-approved specialist lives in `approved/<specialty_slug>/`, built from a fresh scaffold copy via `tools/new_agent.py`, with only `agents/<slug>/` files edited.
4. `check_frozen_core.py` must print `FROZEN CORE INTACT` before every team acceptance; save the output in `evidence/`.
5. Every approval/supersede decision is logged in `decision_log.md` with reasons; never overwrite an approved version — supersede it.
6. `team_agent_inventory.csv` (copy at workspace root) is the single source of truth for slots, versions, evidence paths, and contribution lineage.

## Layout
- `approved/` — team-approved specialist folders (one per specialty)
- `candidates/` — individual member packages for comparison
- `evidence/` — frozen-core checks, validator runs, test artifacts
- `decision_log.md` — accept/supersede decisions with reasons
