# Creation Agent Evidence Sources

Date accessed for every source: October 2, 2026.

## Scope and verification method

Seven selected sources separate general generative-AI history and risk guidance from audit-application evidence. Each listed URL was opened through web research and returned the intended source page or document. Paper abstracts, author/date records, and linked full-text PDFs were inspected; NIST and PCAOB documents were inspected directly. Search snippets and secondary commentary were not used as evidence. Claims below are short paraphrases, not quotations.

Classification: **Verified fact** means verified publication metadata, reported research method/result, or the actual content of a requirement; it does not mean independent replication. **Source interpretation** means an author's assessment or staff-reported observation. **Inference** means an explicitly bounded implication we may draw, not a source's proven result. No case response or pilot decision is made here.

## A. Generative AI generally

### S1 — Transformer predecessor architecture

- Exact title: Attention Is All You Need
- Authors: Ashish Vaswani, Noam Shazeer, Niki Parmar, Jakob Uszkoreit, Llion Jones, Aidan N. Gomez, Lukasz Kaiser, Illia Polosukhin.
- Publication date: June 12, 2017 (initial arXiv submission; the current record lists later revisions).
- Direct URL: https://arxiv.org/abs/1706.03762
- Full text inspected: https://arxiv.org/pdf/1706.03762
- Evidence type: Original research paper and author-submitted bibliographic record.
- Claim supported: The authors introduced an attention-based Transformer without recurrence or convolution and reported greater parallelization in translation experiments.
- Classification: Verified fact about the architecture and reported experiments.
- Locator: Abstract; introduction and architecture discussion.
- Date accessed: October 2, 2026.
- Limitation/caution: Translation results do not establish audit-review reliability. This is a major predecessor capability, not proof of a complete or single-cause origin story for all generative AI.
- URL verification: Both URLs resolved to the intended paper.

### S2 — Large-scale language-model development

- Exact title: Language Models are Few-Shot Learners
- Authors/issuing organization: Tom B. Brown and 30 coauthors, OpenAI; complete author list is on the linked record and paper.
- Publication date: May 28, 2020 (initial arXiv submission; current record revised July 22, 2020).
- Direct URL: https://arxiv.org/abs/2005.14165
- Full text inspected: https://arxiv.org/pdf/2005.14165
- Evidence type: Original research paper.
- Claim supported: GPT-3 used 175 billion parameters; evaluated tasks used text instructions/examples without task-specific gradient updates. Authors reported improved few-shot performance with model scale, alongside task and methodological limitations.
- Classification: Verified fact for model size/method; source interpretation for reported scaling benefits.
- Locator: Abstract; Section 2 and Table 2.1.
- Date accessed: October 2, 2026.
- Limitation/caution: Neither scaling nor benchmark performance proves audit accuracy or monotonically improving performance on every task.
- URL verification: Both URLs resolved to the intended paper.

### S3 — Instruction following and human feedback

- Exact title: Training language models to follow instructions with human feedback
- Authors/issuing organization: Long Ouyang and 19 coauthors, OpenAI; complete author list is on the linked record and paper.
- Publication date: March 4, 2022 (arXiv submission).
- Direct URL: https://arxiv.org/abs/2203.02155
- Full text inspected: https://arxiv.org/pdf/2203.02155
- Evidence type: Original research paper.
- Claim supported: InstructGPT combined supervised fine-tuning on demonstrations with reinforcement learning from ranked human feedback. Authors reported preferred outputs on their evaluated prompt distribution while acknowledging remaining mistakes.
- Classification: Verified fact for training method; source interpretation for reported preference improvements.
- Locator: Abstract; training-method description.
- Date accessed: October 2, 2026.
- Limitation/caution: Human preference is not equivalent to factual correctness, auditor judgment, or guaranteed alignment in a new domain.
- URL verification: Both URLs resolved to the intended paper.

### S4 — Transition to a public conversational system

- Exact title: Introducing ChatGPT
- Author/issuing organization: OpenAI.
- Publication date: November 30, 2022.
- Direct URL: https://openai.com/index/chatgpt/
- Evidence type: Contemporaneous first-party product-release and methods announcement; not independent commentary.
- Claim supported: OpenAI introduced a conversational research preview, described GPT-3.5 fine-tuning with human dialogue data and RLHF, and disclosed plausible but incorrect answers.
- Classification: Verified fact for the dated announcement; source-reported method and limitations.
- Locator: Opening announcement; Methods; Limitations.
- Date accessed: October 2, 2026.
- Limitation/caution: Use solely as primary evidence of this release and disclosed design, not marketing proof of broad adoption or business value. It describes the 2022 system, not present-day performance.
- URL verification: URL resolved to the intended official announcement.

### S5 — Authoritative cross-sector generative-AI risk guidance

- Exact title: Artificial Intelligence Risk Management Framework: Generative Artificial Intelligence Profile
- Authors: Chloe Autio, Reva Schwartz, Jesse Dunietz, Shomik Jain, Martin Stanley, Elham Tabassi, Patrick Hall, Kamie Roberts.
- Issuing organization: National Institute of Standards and Technology (NIST).
- Publication date: July 26, 2024; NIST AI 600-1. The landing-page update is not a new publication date.
- Direct URL: https://www.nist.gov/publications/artificial-intelligence-risk-management-framework-generative-artificial-intelligence
- Full text inspected: https://nvlpubs.nist.gov/nistpubs/ai/NIST.AI.600-1.pdf
- Evidence type: Official voluntary risk-management guidance.
- Claim supported: The profile identifies confabulation, privacy, security, and human-AI interaction risks; it suggests empirical capability evaluation and verification of generated sources/citations.
- Classification: Verified fact about guidance content, not quantified case risk.
- Locator: Sections 2.2 and 2.4; actions MS-2.3-002 and MS-2.5-003.
- Date accessed: October 2, 2026.
- Limitation/caution: Cross-sector voluntary guidance, not an audit standard or certification that a pilot is safe.
- URL verification: Both URLs resolved to the intended NIST publication.

## B. Evidence relevant to the U.S. audit application

### S6 — PCAOB audit evidence requirements

- Exact title: AS 1105: Audit Evidence
- Issuing organization: Public Company Accounting Oversight Board (PCAOB).
- Publication/adoption date: August 5, 2010, adopting Release No. 2010-004; current AS 1105 is a subsequently amended standard. The live consolidated page has no single publication date for every amendment.
- Direct URL: https://pcaobus.org/oversight/standards/auditing-standards/details/AS1105
- Adoption-date verification document inspected: https://assets.pcaobus.org/pcaob-dev/docs/default-source/rulemaking/docket_026/release_2010-004_risk_assessment.pdf?sfvrsn=6326eac2_0
- Evidence type: Official auditing standard; adopting release supplies historical date.
- Claim supported: Auditors must obtain sufficient appropriate evidence; quality includes relevance and reliability. Inconsistent evidence or reliability doubts require procedures to resolve the matter.
- Classification: Verified fact about requirements, not an AI-specific rule.
- Locator: AS 1105 paragraphs .04–.08 and .29.
- Date accessed: October 2, 2026.
- Limitation/caution: Apply to engagements governed by PCAOB standards; do not automatically apply to every private-company audit. No blanket GenAI authorization or prohibition follows from these paragraphs. Verify engagement-specific applicability and amendment effective dates.
- URL verification: Both URLs resolved to the intended standard and its linked adopting release.

### S7 — PCAOB observations on GenAI in audits

- Exact title: Staff Update on Outreach Activities Related to the Integration of Generative Artificial Intelligence in Audits and Financial Reporting
- Issuing organization: PCAOB staff.
- Publication date: July 2024 on the document; July 22, 2024 release confirmed by the official announcement.
- Direct URL: https://pcaobus.org/documents/generative-ai-spotlight.pdf
- Release-date verification page inspected: https://pcaobus.org/news-events/news-releases/news-release-detail/pcaob-staff-shares-observations-from-outreach-on-use-of-generative-artificial-intelligence-in-audits-and-financial-reporting
- Evidence type: Official staff outreach report, not a Board rule or policy.
- Claim supported: Firms discussed possible documentation-completeness uses, confidentiality safeguards, human review and responsibility, and unreliable or hallucinated output.
- Classification: Source interpretation and reported firm practices, not effectiveness findings.
- Locator: Printed pages 4–5; status disclaimer on page 1.
- Date accessed: October 2, 2026.
- Limitation/caution: Limited outreach mainly to larger firms; not representative of the hypothetical mid-sized firm or evidence of 2026 adoption. Potential uses are not proven performance.
- URL verification: Both URLs resolved to the intended report and official announcement.

## C. Evidence boundaries for later analysis

- S1–S4 support selected historical capabilities and release milestones, not an exhaustive history or a claim that novelty creates value.
- S5 identifies general risks and suggested evaluation practices. S6 establishes audit-evidence requirements. S7 records contextual observations about audit use. These evidence categories must remain distinct.
- No selected source establishes that the hypothetical firm's proposed workpaper review reduces errors, saves a particular amount of time, or is ready for deployment. Those would require application-specific evidence and the appropriate specialists' analysis.
- Private-company engagement requirements, complete professional confidentiality obligations, and all supervision standards are not exhaustively covered by this seven-source set. Do not present this record as a comprehensive compliance review.
- Source-based facts and observations above may be used later. No case-specific management recommendation or unsupported causal inference is adopted in this verification step.

## D. URL verification summary

All seven selected sources and their listed supporting pages/documents were opened successfully and matched the intended title and issuing organization or authors. Paper dates were checked against submission histories; NIST's publication date against its official record; PCAOB dates against the report, release announcement, and linked adopting release. Successful resolution confirms source identity and access, not independent replication of research or approval of the proposed pilot.
