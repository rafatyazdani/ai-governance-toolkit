# NIST AI Risk Management Framework (AI RMF 1.0)

> Published January 2023. Voluntary framework for managing risks to individuals, organizations, and society from AI systems throughout their lifecycle.

---

## Overview

The NIST AI RMF organizes AI risk management into four core functions — **GOVERN, MAP, MEASURE, MANAGE** — applied iteratively across the AI lifecycle. Unlike compliance mandates, it is outcome-oriented: you define what "trustworthy AI" means for your context, then build controls to get there.

**Key insight for practitioners:** NIST AI RMF maps cleanly onto existing cybersecurity GRC programs. If your organization already runs NIST CSF, the conceptual vocabulary is intentionally parallel — making the AI RMF the lowest-lift governance entry point for security-mature organizations.

---

## The Four Core Functions

### 1. GOVERN

*Establishes the policies, processes, procedures, and practices that shape how AI risk is approached organization-wide.*

**What it covers:**
- AI risk culture and accountability structures
- Organizational roles (who owns AI risk?)
- Policies for AI development, procurement, and deployment
- Mechanisms for surfacing and escalating AI risk

**Practitioner checklist:**
- [ ] AI use policy exists and is enforced
- [ ] AI risk ownership assigned (CISO? CDO? Board committee?)
- [ ] AI-specific role definitions documented
- [ ] Vendor/third-party AI governance requirements defined
- [ ] AI risk appetite statement approved by leadership

**Board-ready framing:** GOVERN answers the question the audit committee will ask: *"Who is accountable when an AI system causes harm?"*

---

### 2. MAP

*Identifies and categorizes AI risks in context — technical, societal, operational.*

**What it covers:**
- AI use case inventory
- Risk identification (who is harmed? how? what are the failure modes?)
- Categorization by risk tier (low / medium / high / critical)
- Stakeholder impact analysis

**Practitioner checklist:**
- [ ] AI use case register maintained and current
- [ ] Each use case mapped to a risk tier
- [ ] Affected populations and impact pathways documented
- [ ] AI supply chain risks identified (third-party models, APIs, training data)
- [ ] Legal/regulatory exposure assessed per use case

**Risk tier guidance (practitioner-adapted):**

| Tier | Criteria | Example |
|------|----------|---------|
| Critical | Consequential decisions about individuals; regulated domain | Credit scoring AI, medical diagnosis AI |
| High | Significant business or reputational impact; limited human oversight | Customer-facing chatbot, fraud detection |
| Medium | Internal use; human review present | Document summarization, code generation |
| Low | No personal data; fully human-reviewed outputs | Internal search, knowledge base Q&A |

---

### 3. MEASURE

*Analyzes and assesses identified AI risks using qualitative and quantitative methods.*

**What it covers:**
- AI risk measurement methodologies
- Testing and evaluation (red-teaming, bias testing, robustness testing)
- Performance monitoring in production
- Metrics for trustworthiness dimensions

**NIST trustworthiness dimensions:**
1. Accuracy and reliability
2. Explainability and interpretability
3. Privacy
4. Safety
5. Security and resilience
6. Fairness and bias mitigation
7. Accountability and transparency

**Practitioner checklist:**
- [ ] Pre-deployment testing protocol defined per risk tier
- [ ] Bias and fairness testing conducted for high/critical use cases
- [ ] Model drift monitoring in production
- [ ] Incident detection and response metrics defined
- [ ] Red-team / adversarial testing for critical systems

**Financial framing (CRQ-F alignment):**
Use MEASURE outputs to feed quantitative risk calculations:
- *Annualized Loss Expectancy (ALE)* = probability of AI failure × financial impact
- Track MTTR (Mean Time to Remediate) for AI incidents as a board metric

---

### 4. MANAGE

*Prioritizes and addresses AI risks based on measurement outputs.*

**What it covers:**
- Risk response planning (mitigate, accept, transfer, avoid)
- Incident response for AI-specific failures
- Decommissioning and model retirement
- Continuous improvement processes

**Practitioner checklist:**
- [ ] Risk response documented per use case
- [ ] AI incident response runbook exists
- [ ] Model retirement criteria defined
- [ ] Lessons learned loop from incidents to governance

---

## Mapping NIST AI RMF to Existing Controls

| AI RMF Function | CSF Parallel | ISO 27001 Domain | SOC 2 Category |
|----------------|--------------|-----------------|----------------|
| GOVERN | Identify (ID.GV) | A.5 Org controls | CC1, CC2 |
| MAP | Identify (ID.RA) | A.8 Asset mgmt | CC3 |
| MEASURE | Detect (DE) | A.8.8, A.12.7 | CC7 |
| MANAGE | Respond/Recover | A.5.26, A.5.29 | CC5, CC9 |

---

## Implementation Roadmap

**Phase 1 — Foundation (0–30 days)**
- Assign AI risk owner
- Draft AI use policy
- Complete AI use case inventory

**Phase 2 — Assessment (30–60 days)**
- Risk-tier all active AI use cases
- Run MEASURE activities on high/critical tier
- Identify top 3–5 control gaps

**Phase 3 — Operationalization (60–90 days)**
- Implement MANAGE actions for top gaps
- Establish monitoring cadence
- Report to leadership

---

## Resources

- [NIST AI RMF 1.0 (official)](https://airc.nist.gov/RMF)
- [NIST AI RMF Playbook](https://airc.nist.gov/Docs/1)
- [AI RMF Crosswalk Tool](https://airc.nist.gov/Docs/2)

---

*See also: [EU AI Act](EU-AI-Act.md) | [ISO 42001](ISO-42001.md) | [Framework Comparison](comparison.md)*
