# AI Vendor Due Diligence Questionnaire (DDQ)

> Use this questionnaire when evaluating a vendor that provides AI-powered products or services, or that will process your data using AI systems.
> **Vendor:** ______________ | **Date:** ______________ | **Evaluator:** ______________

---

## Section 1 — AI System Overview

1.1 Describe the AI system(s) included in your product or service.

> *[Vendor response]*

1.2 What type(s) of AI / machine learning does your product use? (check all that apply)
- [ ] Large language model (LLM) / generative AI
- [ ] Predictive / classification models
- [ ] Computer vision
- [ ] Recommendation engine
- [ ] NLP (non-generative)
- [ ] Other: _______________

1.3 Is the AI model developed in-house, a fine-tuned foundation model, or a third-party model accessed via API?

> *[Vendor response]*

1.4 If using a third-party foundation model (e.g., OpenAI, Anthropic, Google), which model(s) and provider(s)?

> *[Vendor response]*

1.5 Is your product/service covered by the EU AI Act? If so, what risk tier do you classify it under?

> *[Vendor response]*

---

## Section 2 — Data Handling

2.1 What customer data does your AI system use as input?

> *[Vendor response]*

2.2 Is customer data used to train or fine-tune AI models?
- [ ] Yes — describe training use below
- [ ] No — inference only; customer data never used for training
- [ ] Depends on contract tier — describe below

> *[Vendor response if Yes or Depends]*

2.3 Do you use anonymized, aggregated, or synthetic data for AI training? Describe your de-identification methodology.

> *[Vendor response]*

2.4 Where is customer data stored and processed (geography, cloud provider)?

> *[Vendor response]*

2.5 What is your data retention policy for customer inputs and AI outputs?

> *[Vendor response]*

2.6 Can customers request deletion of their data, including any data used in AI training? Describe the process.

> *[Vendor response]*

---

## Section 3 — Security

3.1 Do you hold a current SOC 2 Type II report? If yes, provide the report date and auditor.

> *[Vendor response]*

3.2 Have you conducted AI-specific security testing, including:
- [ ] Prompt injection testing
- [ ] Model inversion / extraction testing
- [ ] Adversarial input testing
- [ ] Red team / adversarial ML assessment

> *[Vendor response — describe scope, recency, and findings remediation]*

3.3 How do you prevent prompt injection or jailbreaking attacks on your AI system?

> *[Vendor response]*

3.4 Describe your AI incident detection and response capabilities. What is your SLA for notifying customers of an AI-related security incident?

> *[Vendor response]*

3.5 Do you maintain an AI-specific bug bounty or responsible disclosure program?

> *[Vendor response]*

---

## Section 4 — Model Governance

4.1 Describe your model development and validation process, including how models are tested before production deployment.

> *[Vendor response]*

4.2 How do you monitor for model drift or performance degradation in production? What alerts are generated and who responds?

> *[Vendor response]*

4.3 What is your model update cadence? How are customers notified of significant model changes that may affect output behavior?

> *[Vendor response]*

4.4 Do you conduct bias and fairness testing for your AI models? Describe the methodology and frequency.

> *[Vendor response]*

4.5 Can you provide model performance metrics (accuracy, precision/recall, fairness metrics) for the AI system relevant to our use case?

> *[Vendor response]*

4.6 Do you maintain version control for AI models, enabling rollback to a prior version if needed?

> *[Vendor response]*

---

## Section 5 — Transparency and Explainability

5.1 Can your AI system explain or provide reasoning for its outputs? If so, describe the explainability mechanism.

> *[Vendor response]*

5.2 Do you provide a model card or system card documenting the AI model's intended use, limitations, and known failure modes?

> *[Vendor response]*

5.3 Are there known limitations or edge cases where your AI model performs poorly? Describe.

> *[Vendor response]*

5.4 How do you disclose to end users that they are interacting with an AI system?

> *[Vendor response]*

---

## Section 6 — Human Oversight

6.1 Does your system support human-in-the-loop review before AI outputs trigger automated actions?

> *[Vendor response]*

6.2 Can your system be configured to require human approval for high-stakes outputs?

> *[Vendor response]*

6.3 Is there a mechanism for end users or administrators to override or correct AI decisions?

> *[Vendor response]*

---

## Section 7 — Regulatory and Compliance

7.1 Describe your AI governance program, including any dedicated AI risk or AI ethics function.

> *[Vendor response]*

7.2 Have you conducted an EU AI Act readiness assessment? What is your compliance status?

> *[Vendor response]*

7.3 Do you maintain an AI use case register or inventory of AI systems in your product?

> *[Vendor response]*

7.4 Have you experienced any AI-related regulatory inquiries, enforcement actions, or litigation in the past 24 months?

> *[Vendor response]*

7.5 Do you have a published AI ethics policy or responsible AI principles? Provide a link or attach.

> *[Vendor response]*

---

## Section 8 — Subprocessors and Supply Chain

8.1 Do you use AI subprocessors (third-party AI APIs or models) in delivering your service? List them.

> *[Vendor response]*

8.2 How do you evaluate and monitor the AI governance practices of your AI subprocessors?

> *[Vendor response]*

---

## Evaluator Scoring

| Category | Max Score | Vendor Score | Notes |
|----------|-----------|-------------|-------|
| Data handling | 25 | | |
| Security | 25 | | |
| Model governance | 20 | | |
| Transparency | 10 | | |
| Human oversight | 10 | | |
| Regulatory / compliance | 10 | | |
| **Total** | **100** | | |

**Scoring guide:** 85–100 = Strong; 70–84 = Acceptable with conditions; 55–69 = Requires remediation plan; <55 = High risk — escalate before proceeding

**Recommendation:**
- [ ] Approve for procurement
- [ ] Approve with conditions (document below)
- [ ] Require remediation before approval
- [ ] Do not approve

**Conditions / required remediation:**
> [Evaluator notes]

---

*Template from [ai-governance-toolkit](https://github.com/YOUR_USERNAME/ai-governance-toolkit) | Apache 2.0*
