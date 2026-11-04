# Special Dark TW7 Adoption Agent

Start with agents/adoption_agent/specialist_instructions.md and the primary case.
Use the canonical builder, then paste the resulting prompt into an interactive LLM. No API key is required:

    python3 tools/build_prompt.py --agent agents/adoption_agent --case agents/adoption_agent/cases/primary.json --out work/tw7_primary.txt

Return JSON only and validate the saved answer with tools/validate_response.py.
To recheck the included evidence and saved examples, run:

    python3 verification/recheck.py

Saved examples were reasoned through by the current assistant, not independently sampled model trials. The scripts reconstruct prompts and validate artifacts; they do not invoke an LLM or implement a chart-review application. Case assertions in K1/H1-H3 are fictional test controls, never real permissions.
