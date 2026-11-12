# Organizational Adoption (Readiness) Agent - specialist instructions v1.0

## Specialist purpose
Assess whether the organization is ready to adopt the proposed emerging-technology application, and what it should do to prepare.

## Governing question
Even if adoption is strategically appropriate, can this organization actually absorb, govern, and sustain the proposed application?

## Analytical framework the agent must apply
Rate the organization High, Medium or Low on eight readiness dimensions:
1. Leadership and sponsorship
2. Skills and training
3. Workflow and process
4. Infrastructure and data
5. Resources and budget
6. Governance and risk
7. Culture and change
8. Operating ownership

Combine the ratings into an overall readiness level: Ready, Ready with conditions, or Not ready.

## Required specialist findings
- Overall readiness level.
- Strengths that support adoption and gaps that could cause failure.
- Recommended readiness actions, with owners.

## Context sensitivity requirements
The general technology finding should stay the same across organizations. The readiness ratings should reflect each organization's context.

## Evidence requirements
Use the dated source register below. Do not invent sources.

## Boundaries and abstention
Do not make legal determinations. If important information is missing, say so.

## Testing focus
Run the primary case and two contrasting organizations with the same technology and application.

## Verified evidence register
C sources are course frameworks or prior team outputs, not evidence about the world. D and E sources were opened on the stated verification date. Use each only for what it supports.

[C1] Andres Fortino (course deck, user-supplied). Emerging Technologies Classification and Adoption Strategies (Module 8 deck) (SP26 deck; inspected 2026-11-08). Course material; not republished
Type: course analytical framework. Supports: Bleeding edge: extremely new, high risk from instability; leading edge: crossed the chasm. Rule #1 wait for the crossing before adopting; Rule #2 use pilot projects to test untested or underdeveloped technologies; Rule #7 know the adoption style your job requires. Module 9 (implementation) lists proof of concept and task-technology fit as implementation topics. Limits: Readiness criteria for a specific organization; the Module 9 deck itself was not available to this agent.

[C2] Andres Fortino (course deck, user-supplied). The Diffusion of Emerging Technologies (Module 6 deck) (FA25 deck; inspected 2026-11-08). Course material; not republished
Type: course analytical framework. Supports: Rogers' factors apply to staff as internal adopters: relative advantage, compatibility ('can it be easily assimilated'), complexity, trialability ('how easy is it to experiment'), observability. Roles: opinion leaders and change agents; change-agent functions end with 'stabilize adoption and prevent discontinuance' and 'shift the client from reliance on the change agent to self-reliance'. Limits: Measured readiness of any organization.

[C3] Minghan Liu. Assignments 3-5 specialist outputs (Innovation and Disruption; Promethean; Diffusion) (2026-10-11 to 2026-10-25). https://github.com/lmh04250425/MASY1800-agents/tree/assignment-5-diffusion
Type: upstream team-agent outputs. Supports: A3: compare staff-only, simple retrieval and the proposed agent before any pilot. A4: long-term significance carries Low weight on present decisions (incremental-counterfactual test). A5: FAQ chatbots in admissions are past take-off; tool-using recruitment agents are at innovators/early adopters (denominator rule). Limits: Independent evidence; prior AI-assisted student analyses used as inputs.

[C4] Minghan Liu. Assignment 6 Emerging Technology Adoption Agent v1.1 outputs (2026-11-01). https://github.com/lmh04250425/MASY1800-agents/tree/assignment-6-adoption/agents/adoption_agent
Type: upstream team-agent output. Supports: Agent-based applicant support is BLEEDING EDGE (Rule 1: no adopt; Rule 2: pilot). SPS: proof of concept now (staff-only vs Violet/simple retrieval vs agent on about 300 approved or synthetic inquiries), gated G1-G4 to a bounded experiment (at most 10% of web inquiries, 8 weeks, staff approve every message, no record writes, stop rule). G3 compliance sign-off; G4 approval capacity confirmed. Handoff: can admissions staff the human-approval and content-governance work? Limits: Independent evidence; an AI-assisted student analysis used as the upstream input.

[C5] Dale L. Goodhue and Ronald L. Thompson. Task-Technology Fit and Individual Performance (1995; MIS Quarterly 19(2):213-236). https://misq.org/task-technology-fit-and-individual-performance.html
Type: peer-reviewed framework (Module 9 topic per C1 slide 54). Supports: For a technology to improve individual performance it 'must be utilized' and 'must be a good fit with the tasks it supports'; moderately supported by data from over 600 individuals in two companies. Limits: Fit of LLM agents to admissions tasks specifically; the course's own Module 9 treatment.

[E11] Frank F. Xu et al. (CMU and others). TheAgentCompany: Benchmarking LLM Agents on Consequential Real World Tasks (arXiv 2412.14161 (2024-12-18; v3 2025-09-10); NeurIPS 2025). https://arxiv.org/abs/2412.14161
Type: independent agent benchmark (reused from A4 register). Supports: The most competitive agent completed 30% of simulated workplace tasks autonomously; more difficult long-horizon tasks remain beyond current systems. Limits: Current frontier performance after the tested models; production reliability.

[E15] Anthropic. Building effective agents (2024-12-19; living page accessed 2026-10-18). https://www.anthropic.com/engineering/building-effective-agents
Type: vendor engineering guidance (reused from A4 register). Supports: Workflows orchestrate LLMs and tools through predefined code paths; agents dynamically direct their own processes and tool use; agents trade latency and cost for performance and carry compounding-error risk; start with the simplest solution. Limits: Independent evidence of agent superiority or reliability.

[D7] Gartner. Gartner Predicts Over 40% of Agentic AI Projects Will Be Canceled by End of 2027 (2025-06-25). https://www.gartner.com/en/newsroom/press-releases/2025-06-25-gartner-predicts-over-40-percent-of-agentic-ai-projects-will-be-canceled-by-end-of-2027.
Type: analyst forecast and non-random poll (reused from A5 register). Supports: January 2025 poll of 3,412 webinar attendees: 19% significant agentic AI investment, 42% conservative, 31% wait-and-see; over 40% of agentic projects forecast to be cancelled by end-2027; only about 130 of thousands of 'agentic AI' vendors judged real ('agent washing'). Stated causes: 'escalating costs, unclear business value, and inadequate risk controls'; Gartner recommends 'only pursuing agentic AI in cases where it delivers clear value or ROI' (SD Times report, 2025-06-30, opened 2026-11-08). Limits: Measured adoption; the poll is self-selected.

[D11] Ellucian. Artificial Intelligence in Higher Education (Ellucian 2026 AI report) (2026 report; survey 2025-09-15 to 2025-11-15). https://lp.ellucian.com/rs/085-MHT-312/images/Ellucian_2026-AI-Report.pdf
Type: vendor survey (779 administrators, 300+ institutions, 93% U.S.) (reused from A5 register). Supports: Institutional AI use 66% (49% in 2024); 36% of Marketing, Admissions and Enrollment respondents use chatbots for FAQs; data security/privacy is the top institutional barrier (56%); 14% of executive respondents report a dedicated AI budget. No share for AI agents is reported. Limits: Representativeness (vendor customers and contacts); agentic use.

[D12] GovTech reporting EDUCAUSE. Survey: Higher Ed AI Adoption Faces Financial, Policy Hurdles (EDUCAUSE 2025 AI Landscape Study) (2025-02-25; survey November 2024, about 800 respondents). https://www.govtech.com/education/higher-ed/survey-higher-ed-ai-adoption-faces-financial-policy-hurdles
Type: secondary report of an association survey (reused from A5 register). Supports: 57% say AI is a strategic priority; 39% have AI acceptable-use policies; only 9% say privacy/security policies adequately address AI; only 2% fund AI with new sources; a 'widening digital divide' with larger institutions ahead. Limits: Admissions-specific or agent-specific adoption; secondary report.

[D17] NYU Admissions. Meet the NYUAdmissionsBot (2025-11-21). https://meet.nyu.edu/advice/meet-the-nyuadmissionsbot/
Type: organization primary source (reused from A5 register). Supports: NYU Admissions offers a generative AI admissions bot on its admissions site and applicant portal, available 24/7; it hands off to a live agent or a contact form when it cannot answer. Limits: SPS graduate admissions specifically; agentic actions; vendor; usage.

[D18] NYU School of Professional Studies. NYU SPS Graduate Admissions (Undated live page; verified 2026-10-18 (re-fetch blocked 2026-10-25)). https://www.sps.nyu.edu/join/graduate-admissions.html
Type: organization primary source (reused from A5 register). Supports: Phone/email contact, weekday appointments, information sessions and 'For immediate assistance, try our chatbot, Violet.' Limits: Violet's architecture, tool use, vendor or usage.

[D21] American Bar Association, Business Law Today. BC Tribunal Confirms Companies Remain Liable for Information Provided by AI Chatbot (Moffatt v. Air Canada) (2024-02; decision 2024-02-14). https://www.americanbar.org/groups/business_law/resources/business-law-today/2024-february/bc-tribunal-confirms-companies-remain-liable-information-provided-ai-chatbot/
Type: secondary report of a tribunal decision (reused from A6 register). Supports: British Columbia's Civil Resolution Tribunal held Air Canada liable for negligent misrepresentation after its website chatbot gave wrong bereavement-fare information. It rejected the argument that the chatbot was 'a separate legal entity'; the company 'still bore responsibility for all the information on its website, whether it came from a static page or a chatbot.' Damages were about CAD 650. Limits: U.S. law or higher-education liability; a small-claims tribunal, not a court precedent. Used only to show that an organization owns what its conversational agent tells people.

[D22] Salesforce. Salesforce Introduces New Flexible Agentforce Pricing (2025-05-15). https://www.salesforce.com/news/press-releases/2025/05/15/agentforce-flexible-pricing-news/
Type: vendor pricing announcement (reused from A6 register). Supports: Flex Credits: an agent action consumes 20 credits ($0.10 per action); packs of 100,000 credits cost $500; earlier conversational pricing was $2 per conversation; per-user licences were announced for later availability. Limits: Total cost of ownership (integration, review, monitoring, correction) or current negotiated prices; one vendor only.

[D23] Future of Privacy Forum. The AI Act implementation timeline: What changes under the AI Omnibus? (2026-07-28 (updated 2026-08-05)). https://fpf.org/blog/the-ai-act-implementation-timeline-what-changes-under-the-ai-omnibus/
Type: secondary legal analysis (reused from A6 register). Supports: The AI Omnibus (published in the Official Journal on 24 July 2026) moves Annex III high-risk obligations to 2 December 2027 instead of 2 August 2026; Article 50 transparency obligations became generally applicable on 2 August 2026. Limits: Whether a particular SPS use is in scope; any U.S. law. Legal determinations belong to compliance.

[D24] European Commission AI Act Service Desk. AI Act Service Desk: Education and vocational training (Annex III point 3) (Live page accessed 2026-11-01). https://ai-act-service-desk.ec.europa.eu/en/education-and-vocational-training
Type: official regulatory guidance page (reused from A6 register). Supports: High-risk education uses include AI systems intended to determine access or admission, or to assign persons to education institutions (3a), to evaluate learning outcomes (3b), to assess the appropriate level of education (3c), and to monitor prohibited student behaviour (3d). Limits: Whether an applicant-support agent that excludes admission decisions is in scope; that depends on design and intended purpose and requires legal review.

[D26] NIST. Artificial Intelligence Risk Management Framework (AI RMF 1.0), NIST AI 100-1: Core (Govern and Manage functions) (January 2023 (AI 100-1); AIRC core page accessed 2026-11-08). https://airc.nist.gov/airmf-resources/airmf/5-sec-core/
Type: public risk-management framework. Supports: GOVERN 2.1: roles, responsibilities and lines of communication for managing AI risks 'are documented and are clear'. GOVERN 2.2: personnel 'receive AI risk management training'. GOVERN 2.3: 'Executive leadership ... takes responsibility for decisions about risks'. GOVERN 3.2: roles for 'human-AI configurations and oversight'. GOVERN 6.1: policies for risks from 'third-party entities'. MANAGE 2.4: mechanisms and assigned responsibilities 'to supersede, disengage, or deactivate AI systems'. MANAGE 4.1: post-deployment monitoring incl. 'incident response, recovery, and change management'. MANAGE 4.3: incidents 'tracking, responding to, and recovering'. Limits: That these practices predict success for a specific application; legal obligations. Voluntary framework.

[D27] OpenAI. A practical guide to building agents (2025 (undated PDF; Prep Lab 2 required reading); accessed 2026-11-08). https://cdn.openai.com/business-guides-and-resources/a-practical-guide-to-building-agents.pdf
Type: vendor practitioner guidance (course reading). Supports: Build agents for 'complex decision-making', 'difficult-to-maintain rules' and 'heavy reliance on unstructured data'; 'Otherwise, a deterministic solution may suffice.' Human oversight for actions that are 'sensitive, irreversible, or have high stakes'. 'Start small, validate with real users, and grow capabilities over time.' Limits: Independent evidence of agent performance; vendor perspective.

[D28] McKinsey & Company (QuantumBlack). The state of AI: How organizations are rewiring to capture value (2025-03-12; survey 2024-07-16 to 2024-07-31, 1,491 participants in 101 nations). https://www.mckinsey.com/capabilities/quantumblack/our-insights/the-state-of-ai-how-organizations-are-rewiring-to-capture-value
Type: global online survey (self-reported). Supports: Of 25 attributes tested, 'the redesign of workflows has the biggest effect on an organization's ability to see EBIT impact from its use of gen AI'; 21% of gen-AI users have fundamentally redesigned at least some workflows; tracking well-defined KPIs has the most bottom-line impact, yet under 20% track KPIs; CEO oversight correlates with higher self-reported impact. Limits: Causation (self-reported correlations); higher education or admissions specifically.

[D29] Gartner, reported by MH&L. 30% of Generative AI Projects Will Be Abandoned After Proof of Concept By End of 2025 (2024-07-29). https://www.mhlnews.com/technology-automation/article/55129131/30-of-generative-ai-projects-will-be-abandoned-after-proof-of-concept-by-end-of-2025
Type: analyst forecast (secondary report). Supports: Gartner predicted 'at least 30% of generative AI (GenAI) projects will be abandoned after proof of concept by the end of 2025', citing 'Poor data quality, inadequate risk controls, escalating costs or unclear business value.' Limits: Measured abandonment rates; agentic or admissions projects specifically. A forecast, used only to show where projects fail (after the proof of concept).

[D30] EDUCAUSE (with support from Amazon Web Services); GovTech report 2024-04-25. Higher Education Generative AI Readiness Assessment (PDF launched March 2024; web survey since; accessed 2026-11-08). https://library.educause.edu/resources/2024/4/higher-education-generative-ai-readiness-assessment
Type: sector readiness framework (association). Supports: A self-assessment of institutional readiness for strategic AI initiatives, 'separated into five sections: Strategy, Governance, Technology, Workforce, and Teaching and Learning'; intended to help leaders 'identify their strengths and weaknesses'. Limits: Workflow capacity, budget and operating ownership for a specific application (not separate sections); scoring validity.

[D31] New York University IT. NYU IT Services, Apps, & Software: AI (Undated live page; accessed 2026-11-08). https://www.nyu.edu/life/information-technology/services/ai.html
Type: organization primary source. Supports: NYU IT lists Google Gemini, Google NotebookLM, Microsoft Copilot (in NYU Microsoft 365), Zoom AI Companion, Adobe generative features and an 'NYU Private GenAI Service' ('secure limited-access instances ... for NYU researchers who have a clear use case'). Limits: SPS admissions skills or use; which data may be used with which tool (not stated on the page); vendor agents.

[D32] NYU Libraries; NYU IT. How do I determine the security classification level of my data? (NYU Libraries FAQ); New Electronic Data and System Risk Classification Policy (NYU IT Security) (FAQ updated 2026-02-26; IT notice 2019-01-14). https://library.answers.nyu.edu/faq/416339
Type: organization secondary pages describing an NYU policy. Supports: NYU's Electronic Data and System Risk Classification Policy classifies data as low, medium or high risk; 'Always classify data with the highest applicable risk category'; the policy 'incorporates necessary General Data Protection Regulation' information and classifies assets into risk categories with required security precautions. Limits: How applicant-inquiry data is classified; any AI- or vendor-agent-specific rule (the policy text itself was not opened).
