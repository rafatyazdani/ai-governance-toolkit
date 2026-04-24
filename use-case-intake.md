# AI Use Case Intake Form

> Complete this form before deploying any new AI system or significantly modifying an existing one. Submit to the AI Risk Owner for review and approval.

---

## Section 1 — Use Case Identification

**Use case name:**
> [Short descriptive name — e.g., "Customer support chatbot," "Employee expense fraud detection"]

**Business unit / team:**
> [Department and team submitting the request]

**Business owner:**
> [Name, title, email]

**Technical owner:**
> [Name, title, email — person responsible for the system]

**Submission date:**
> [Date]

**Target go-live date:**
> [Date]

---

## Section 2 — System Description

**What does this AI system do?**
> [2–4 sentence plain-language description. Describe the input, the AI action, and the output. Avoid jargon.]

**What problem does it solve?**
> [Business justification. What happens if this isn't deployed?]

**What type of AI is this?**
- [ ] Generative AI (LLM, text/image/code generation)
- [ ] Predictive / classification model
- [ ] Recommendation engine
- [ ] Computer vision / image recognition
- [ ] Natural language processing (non-generative)
- [ ] Robotic process automation with AI components
- [ ] Other: _______________

**Is this a third-party AI system or internally built?**
- [ ] Third-party SaaS / API (vendor: _______________)
- [ ] Fine-tuned or customized third-party foundation model
- [ ] Internally developed
- [ ] Hybrid

**If third-party, which model / vendor?**
> [e.g., OpenAI GPT-4o via API, Salesforce Einstein, custom vendor name]

---

## Section 3 — Data

**What data does this system use as input?**
> [List all data types and sources]

**Does input data include any of the following? (check all that apply)**
- [ ] Personal data (names, emails, IDs)
- [ ] Sensitive personal data (health, financial, biometric, race/ethnicity, sexual orientation)
- [ ] Employee data
- [ ] Customer data
- [ ] Third-party / partner data
- [ ] Proprietary business data / trade secrets
- [ ] No personal or sensitive data

**Where is data stored and processed?**
> [On-premises / cloud provider / vendor environment / hybrid — include geography if relevant for data residency]

**Is data used to train or fine-tune the AI model?**
- [ ] Yes — data is used for training / fine-tuning
- [ ] No — inference only (data is not used to update the model)
- [ ] Unclear / to be confirmed with vendor

**Data retention period:**
> [How long is input/output data retained? By us? By the vendor?]

---

## Section 4 — Decisions and Impact

**What decisions or actions does this system influence?**
> [Describe what a human or automated process does based on the AI output]

**Who is affected by these decisions?**
- [ ] Customers / end users
- [ ] Employees
- [ ] Job applicants
- [ ] Third parties / general public
- [ ] Internal business processes only (no direct human impact)

**Estimated number of people affected per month:**
> [Order of magnitude: <100 / 100–10K / 10K–1M / >1M]

**What is the worst plausible outcome if this system fails or produces incorrect output?**
> [Be specific. What does harm look like? Who is harmed?]

**Estimated financial impact of a significant failure:**
> [Best estimate in $. Use ranges if uncertain. This feeds ALE calculation.]

---

## Section 5 — Human Oversight

**Is there a human in the loop before AI output affects a real decision?**
- [ ] Yes — human always reviews and approves before action
- [ ] Partial — human reviews only flagged or high-stakes cases
- [ ] No — AI output is acted on automatically

**If partial or no: what is the justification for reduced human oversight?**
> [Required field if "Partial" or "No" selected above]

**Can a person affected by an AI decision request human review?**
- [ ] Yes
- [ ] No
- [ ] Not applicable (no direct individual decisions)

---

## Section 6 — Risk Tier Classification

*Complete this section with the AI Risk Owner or Governance team.*

**Proposed risk tier:**
- [ ] Critical — Consequential individual decisions in a regulated domain
- [ ] High — Significant business/reputational impact; limited human oversight
- [ ] Medium — Internal use; human review present
- [ ] Low — No personal data; fully human-reviewed outputs

**EU AI Act classification (if applicable):**
- [ ] Unacceptable (prohibited — do not proceed)
- [ ] High-risk (Annex III)
- [ ] Limited risk (transparency obligations)
- [ ] Minimal risk
- [ ] N/A — not placing on EU market / no EU persons affected

**NIST AI RMF alignment:**
> [Which MAP/MEASURE controls will apply based on this tier?]

---

## Section 7 — Approvals

| Role | Name | Decision | Date | Notes |
|------|------|----------|------|-------|
| Business owner | | ☐ Approve ☐ Reject ☐ More info needed | | |
| AI Risk Owner / CISO | | ☐ Approve ☐ Reject ☐ More info needed | | |
| Privacy / Legal (if personal data) | | ☐ Approve ☐ Reject ☐ More info needed | | |
| CPTO / CTO (if Critical tier) | | ☐ Approve ☐ Reject ☐ More info needed | | |

**Conditions / required controls before go-live:**
> [List any required controls, testing, or documentation before deployment approval is valid]

---

## Section 8 — Post-Deployment Requirements

Based on risk tier, the following monitoring requirements apply:

| Tier | Monitoring cadence | Review trigger |
|------|--------------------|---------------|
| Critical | Monthly performance review | Any incident; model update; data drift alert |
| High | Quarterly review | Significant model update; user complaint spike |
| Medium | Semi-annual review | Significant model update |
| Low | Annual review | Material change in use |

**Assigned monitoring owner:**
> [Name]

**Monitoring start date:**
> [Date]

---

*Template from [ai-governance-toolkit](https://github.com/YOUR_USERNAME/ai-governance-toolkit) | Apache 2.0*
