# Test and failure log

Read `verification/run_provenance.json` before interpreting any result. Four team examples and four comparative design walkthroughs are same-assistant, same-conversation controlled reasoning examples, not independent model trials, original student runs, classroom evidence or a business pilot. Local checks test saved artifacts. No successful production performance is claimed.

## Common test design

Primary and contrast use the same Agentic AI definition, chart-review application, historical source packet, management question and proposed four-week horizon. The primary is a hypothetical conservative financial firm with sensitive data and no approved external model environment. The contrast is a hypothetical experiment-oriented media studio with public aggregate data, an approved sandbox and limited engineering capacity. Multiple organization-level fields change together; this demonstrates contextual sensitivity but cannot isolate a single causal factor.

Expected stability: supported technology history and its reliability limits. Expected change: permitted investigative environment and organizational controls. A missing-context case should retain history but withhold organizational judgments. An unsupported-claims case should reject the inference from general chatbot popularity to agentic diffusion, unmeasured costs and deployment authority.

## Saved response review

| Case | Evidence anchor | Observation in saved example | Interpretation limit |
|---|---|---|---|
| Primary | `organization_specific_finding`, `recommendation_management_implication` | Restricts work to public/synthetic offline feasibility, deterministic checks and human review | No actual financial institution or chart model was tested |
| Contrast | Same fields | Uses the existing approved public-data sandbox; keeps a small read-only tool set and editor review | Public data do not establish correctness or readiness |
| Missing context | `organization_specific_finding`, `abstention_or_more_information_needed` | Withholds organization judgment and requests named missing inputs | The deliberately missing case is not proof of robust behavior on all ambiguous inputs |
| Unsupported claims | `contrary_evidence_or_limitations` | Rejects popularity substitution, near-zero cost and automatic deployment approval | This challenges one preserved failure pattern, not every possible unsupported claim |

General history is deliberately identical across the saved responses. This is a controlled content choice, not an observed independent repeatability result. The assistant reviewed its own output; team verification remains pending.

## Preserved weaknesses and revisions

| ID | Preserved weakness or failure | Response in proposed team version | Residual limitation |
|---|---|---|---|
| F01 | Yufei's archived weak v0.1 response was structurally valid but analytically weaker | Require dated source-to-claim notes, mechanisms and bounded recommendations | Schema validity still cannot establish source truth |
| F02 | Minghan primary output uses broad chatbot scale in the Agentic AI evolution argument and makes an unmeasured marginal-cost claim | Explicit category and cost rules; unsupported-claims test | Current diffusion is withheld rather than newly measured |
| F03 | Jianbo analyzes generative language models, not the same full agentic definition | Retain reasoning discipline but add tool-action research evidence | Selective lineage, not an exhaustive account of AI agents |
| F04 | Minghan instructions/metadata/primary output show different version labels | One metadata version is checked against every new team response | Original snapshots retain their inconsistencies for provenance |
| F05 | Original comparisons vary technologies, applications or horizons | Team common pair and four design walkthroughs hold definition, application and horizon fixed | Same assistant, shared fields and no blind or independent reruns |
| F06 | Team rc1 acknowledged general historical gaps but omitted a separate five-category examination | Chutong's audit is added to instructions and all four v1.0 team examples | No new financing, demand, institutional or competitive evidence; coverage is not completeness |

`comparison_prompts/` contains primary and contrast packets for Yufei and Chutong, the two selected competing designs. `comparison_responses/` contains four current-assistant walkthroughs. Definition, case and source packet are shared; history and organizational findings are design-specific; evidence arrays and some common fields reuse a shared scaffold. Both designs keep history stable and change organizational constraints. Chutong's example exposes five separate enabling-condition categories, whereas Yufei's concise example acknowledges nontechnical gaps generally. The selection combines the explicit category audit with agent-specific mechanisms rather than claiming a measured winner. This is a qualitative, unblinded comparison; human challenge remains necessary.

The earlier unexecuted Jianbo comparison packets were replaced by the selected Yufei/Chutong pair; Jianbo's original evidence remains intact. This removes unused setup files rather than hiding a failed run. The actual rc1 primary and instructions are retained under `evidence/team_revision/`.

## Verification scope

`verification/verify_package.py` runs the unchanged course validator and frozen-core check, a separate strict schema check, metadata checks, source-reference checks, matched-case checks and integrity checks. It also verifies that intentionally malformed copies are rejected and demonstrates the basic validator's extra-key blind spot without altering frozen code. See `verification/validation_results.json` for actual execution results. Automated content assertions are regression checks on these examples, not a semantic evaluator.
