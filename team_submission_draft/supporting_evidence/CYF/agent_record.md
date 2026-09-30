# Chart Improvement Specialist Agent Record

- Repository / branch / commit: Local ChatGPT Work-style preparation package; no GitHub repository required for this practice exercise.
- Agent name and version: Business Chart Improvement Agent, version 0.2-student.
- Exact business question: Determine what the Titanic passenger data show about sex and survival for a New York Times editor, reporting survivor counts, survival rates, the percentage-point difference, and relative survival rate while distinguishing association from causal proof of an evacuation policy.
- Baseline chart filename: `assets/baseline_chart.png`.
- Improved chart filename: `responses/improved_chart.png` (final copy of `responses/improved_chart_v2.png`).
- Most important baseline weakness: The generic title and rate-only labels did not present the complete fact-checking answer and supplied no visible causal boundary.
- Visualization principle used: Story, Purpose, Perception, Method, and Charts from the governing Principles paper, especially conclusion-oriented titling, audience fit, zero-baseline comparison, sparse color, direct labels, and removal of chart junk.
- How the case study was used for calibration rather than copied: It informed the need for systematic review, accessibility, and human verification. No case-specific White House title, palette, annotation, or chart redesign was copied.
- Most consequential change made: The final chart combines direct rate-and-count labels with the 53.6-point gap, 3.81x relative rate, and a visible association-not-causation statement.
- Data-fidelity checks performed: Recalculated all sex totals and survivors from `source_data.xlsx`; confirmed 339/466 female survivors and 161/843 male survivors; confirmed rates of 72.7468% and 19.0985%, a 53.6483-point difference, and a 3.8090 relative rate; included all 1,309 records in the sex comparison.
- First test result: The first improved chart used a clearer horizontal comparison, direct rate labels, a takeaway title, and a causal qualification.
- Weakness or failure preserved from the first test: `responses/improved_chart_v1.png` omitted survivor counts, the exact percentage-point difference, and the exact relative survival rate from the PNG even though the JSON reported them.
- Revision made to the specialist instructions: Added an explicit self-contained-metrics rule requiring rate-and-count labels and any comparison metrics expressly requested by the business question, when legible.
- Retest result: `responses/improved_chart_v2.png` presents both groups' rates and counts, the 53.6-point difference, the 3.81x relative rate, source scope, and the causal limitation on one legible chart.
- Remaining limitation: The data show association only and cannot establish policy, mechanism, evacuation sequence, or a children-first result. Other variables such as age and passenger class are not evaluated in this bounded chart.
- Independent judgment: Yes. The specialist materially improved communication because the final artifact answers all requested numerical components, improves perceptual comparison, and reduces the risk of causal overstatement without changing the underlying evidence.
- AI / verification note: Codex assisted with local scaffold preparation, chart generation, structured responses, and revision documentation. All consequential numerical claims were independently recalculated from `source_data.xlsx`; both response files were validated with the frozen validator; FROZEN CORE was checked before and after editing.
