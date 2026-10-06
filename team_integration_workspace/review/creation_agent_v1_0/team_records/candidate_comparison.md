# Candidate comparison and synthesis rationale

Updated on 2026-10-06 after all four individual candidates became available. At Yufei Cai's explicit request, the assistant selected version 1.0 by combining the strongest mechanisms below. This is a delegated implementation decision, not a retrospective team vote. Candidate artifacts are preserved under `evidence/candidate_snapshots/`; hashes are in `evidence/candidate_snapshot_manifest.json`.

## Intake and comparability

| Candidate | Available evidence | Important comparability limit |
|---|---|---|
| Yufei Cai | Local working agent, instructions, primary and two contrasts, weak v0.1 output, Agent Record; personal repository `caiyf17/masy1800-assignment2-creation-agent`, local HEAD `bdbab604c1743a75e21011be0e0a581e4f783bbf` | Agentic AI and chart review; different organizations and horizons in original contrasts |
| Jianbo Sun | Supplied PDF and public agent files retrieved at commit `56c08e63d7525fcf0b26862a01d0f8dedf66f7db` in `Sun417-jianbo/special-dark`; revision and run provenance preserved | Transformer-based generative language models, not the same defined technology as Agentic AI |
| Minghan Liu | Supplied ZIP and identical extracted `pkg`; instructions, metadata, three cases/responses, Agent Record and handoff | Agentic AI for admissions/hospital contexts; metadata is v1.1, primary response is v1.0, and instruction heading says v1.0 |
| Chutong Wang | Newly supplied complete ZIP; Agent Record identifies the author, repository, reported commit and v0.2; initial/revised responses and contrast preserved | LLM-based generative AI for audit review versus marketing; application and horizon change. `contrast_2.json` is an unfilled template, not a third test |

Minghan's ZIP and `pkg` are one candidate, not two. Original tests differ in technology and context, so they cannot establish a comparative accuracy ranking. For the decisive design comparison, Yufei and Chutong were selected: Yufei has the closest agentic/tool-use scope, while Chutong has the strongest explicit enabling-condition audit. Four same-assistant controlled walkthroughs use the shared primary/contrast cases in `comparison_responses/`; their prompt packets are in `comparison_prompts/`. These are new assistant-authored examples, not original student runs or independent model trials.

## Comparison under common criteria

| Criterion | Yufei | Jianbo | Minghan | Proposed synthesis |
|---|---|---|---|---|
| Need and opportunity | Connects multi-step knowledge work to the chart-review need | Explicitly separates original research need from the present business need | Need-pull is visible but causal weight relies partly on interpretation | Adopt Jianbo's distinction and label business demand as inference |
| Predecessor mechanisms | Distinguishes model, tool and integration layers | Explains neural features, attention, pretraining and instruction refinement | Includes tool/planning layer but historical references alone do not establish every component claim | Use Jianbo's mechanism structure plus Yufei's agent-specific research lineage |
| Enabling conditions | Models, data, tools and standards; MCP treated as a later enabler | Documents enabling mechanisms and refuses invented market causality | Adds GPU/data/economic forces, including unsupported near-zero serving-cost premise | Keep supported technical enablers; reject unmeasured cost and necessary-cause claims |
| Evidence and evolution | Dated sources and claim limits; selected lineage remains incomplete | Strong explicit boundary between historical evidence and current diffusion | ChatGPT user counts are used in support of arc placement for Agentic AI | Distinguish language-model use, agentic-workflow use, release availability and diffusion |
| Context and abstention | Organizational implications change, but original tests do not test missing organization | Bank contrast and missing-context abstention; provenance discloses deliberate shared history | Hospital contrast and unknown-context abstention | Match technology, application and horizon; vary organization; add abstention and unsupported-premise stress cases |
| Authority and test honesty | Human review and deterministic checks | Clear distinction between proposed evaluation and actual business results | Handoff routes some conclusions onward, but “pilot now” can overstate creation authority | Recommend bounded investigation only; route final adoption and readiness decisions onward |

## Exact evidence anchors

- Yufei: `specialist_instructions.md`; `responses/primary_response.json` fields `general_et_finding`, `risk_governance_implication`; `responses/primary_response_v0_1_weak.json` preserves the weaker first attempt. Its existence is historical evidence, not a newly generated failed run.
- Jianbo: `specialist_instructions.md` sections on need, enabling conditions and missing context; `responses/primary_response.json` distinguishes evidence and inference; `responses/contrast_2_response.json.organization_specific_finding` withholds judgment; `records/run_provenance.json` discloses same-session generation.
- Minghan: `responses/primary_response.json.general_et_finding` contains the unmeasured serving-cost premise and diffusion inference; `evidence[6]` cites aggregate ChatGPT users. `responses/contrast_2_response.json` demonstrates useful abstention. `records/team_handoff.md` repeats the popularity-to-agentic-diffusion connection.
- Chutong: `specialist_instructions.md`, analytical framework step 4, explicitly requires five enabling categories and claim-level evidence status; `records/test_and_revision_log.md` sections 2–5 document the weakness and revision. `responses/primary_response_v1.json` acknowledges nontechnical gaps generally; the revised primary actually examines each category. `records/agent_record.md` supersedes older missing-identity notes in the test log. No audit-specific legal claims are imported into the chart-review specialist.

## Fourth candidate assessment

Chutong's need/predecessor/recombination reasoning is compatible with Jianbo's discipline. Her distinctive improvement is explicit coverage of scientific/technical, economic/resource, social/user-demand, institutional/regulatory and market/competitive conditions, each supported, inferred or identified as a gap. This exposes an omission in our own 1.0-rc1 account: it acknowledged incomplete history but did not separately examine all five categories. The actual rc1 primary and instructions are preserved in `evidence/team_revision/`. Version 1.0 adds the category audit without pretending that missing financing, demand or institutional evidence has been collected. Her original generative-AI genealogy and audit standards are not mechanically relabeled as Agentic AI evidence.

## Common comparison observations

| Criterion | Yufei design walkthrough | Chutong design walkthrough | Selection implication |
|---|---|---|---|
| Technology distinction | Explicit model-selected tool loop and deterministic calculations | Adapts its general creation framework to the same tool-action definition | Retain Yufei's operational definition and action/tool research |
| Enabling-condition coverage | Explains technical enablers and acknowledges nontechnical unknowns globally | Separately identifies all five categories and material gaps | Adopt Chutong's explicit audit to reduce silent omissions |
| Primary/contrast behavior | Same history; offline public/synthetic feasibility becomes an approved public-data sandbox | Same history; distinguishes supplied reviewer requirements from demonstrated control effectiveness | Combine contextual controls with Chutong's requirement-versus-capability guard |
| Authority and evidence | Does not approve production or claim measured chart performance | Does not equate planning horizon, available reviewer or low stakes with readiness | Keep both boundaries; use Jianbo's original-need and proposed-versus-actual language |

There is no measured accuracy winner. This is a traceable design selection supported by limited controlled examples. Shared evidence arrays and parts of the response contract are reused deliberately. General history is deliberately fixed. The assistant generated and reviewed these examples and knew both candidates; further human challenge can reverse the choice.

## Selected design and alternatives

1. Adopt a mechanism-first structure. Jianbo supplies the original-need/current-need separation, Yufei supplies agent-specific tool-use evidence, and Chutong supplies the five-category evidence-status audit.
2. Retain Agentic AI and chart review as the common scope, selected under Yufei's delegated request. This creates continuity with the prior chart project but does not reuse its performance results or claim an all-member vote.
3. Preserve Minghan's missing-context challenge; reject the use of broad chatbot popularity as proof of agentic diffusion. Even an accurate chatbot count would not measure the same construct.
4. Retain a supported research-to-integration arc while withholding a precise current maturity stage. An alternative is to classify releases as commercialization evidence. That narrower release claim can be supported; it still does not establish measured diffusion or organizational readiness.
5. Keep the frozen interface unchanged. Add verification outside `core/` and `tools/` because the supplied basic validator does not enforce every schema rule or factual correctness.

The tradeoff is a longer, less decisive-sounding historical account in exchange for explicit evidence gaps. No named member is recorded as holding a dissenting view. The unresolved analytical concern is the incomplete LLM/tool-use lineage and missing nontechnical causal evidence. User delegation settles the implementation choice; it does not establish the required in-class group process or verification by all four members.
