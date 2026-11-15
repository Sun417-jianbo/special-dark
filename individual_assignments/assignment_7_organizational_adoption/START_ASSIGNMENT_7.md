# Assignment 7 Organizational Adoption Agent
Jianbo Sun | 2026-11-09 | Individual candidate v1.0

Start with agents/organizational_adoption_agent/specialist_instructions.md and records/agent_record.md. The working copy retains the instructor scaffold. The original PACKAGE_SHA256.txt describes the original package, not new specialist files.

From this package directory:
```
python tools/check_frozen_core.py
python tools/build_prompt.py --agent agents/organizational_adoption_agent --case agents/organizational_adoption_agent/cases/primary.json --out work/organizational_adoption_primary.txt
```
Submit that packet to ChatGPT. Save its JSON response to a new file without overwriting preserved evidence, then run:
```
python tools/validate_response.py path/to/new_response.json
python verification/recheck.py
```
The final command rechecks saved examples; it does not generate a new model response. No API key is required. Run the same workflow with contrast, missing_capacity and posture_pressure cases. Tests in this package are current-conversation ChatGPT/Codex responses authored and reviewed by the same assistant. No isolated or independent model run is claimed. Shared stable findings were intentionally retained across examples.

The primary case has a real readiness blocker within its hypothetical facts: nobody owns operation and review capacity is not allocated. The contrast supports bounded evaluation preparation, not sustained adoption. All organization profiles are classroom constructions, not actual NYU systems or policies. Read records/test_and_revision.md before interpreting the weak baseline.

GitHub target: Sun417-jianbo/special-dark, assignment-7-org-readiness-jianbo-20261109, individual_assignments/assignment_7_organizational_adoption. This is an individual candidate, not team acceptance. See repository_handoff.json delivered with the submission for the confirmed remote commit. No Brightspace submission is performed by these scripts.
