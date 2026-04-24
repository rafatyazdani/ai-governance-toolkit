# AI Governance Framework Comparison

> Side-by-side analysis of NIST AI RMF 1.0, EU AI Act, and ISO/IEC 42001:2023 to help practitioners choose and combine frameworks for their context.

---

## At a Glance

| Dimension | NIST AI RMF 1.0 | EU AI Act | ISO/IEC 42001:2023 |
|-----------|----------------|-----------|-------------------|
| **Type** | Voluntary framework | Binding regulation | Certifiable standard |
| **Origin** | US (NIST) | EU (Parliament/Council) | International (ISO/IEC JTC 1) |
| **Enforcer** | None (voluntary) | National market surveillance authorities | Accredited certification bodies |
| **Primary audience** | AI developers and deployers | All organizations placing AI on EU market | Organizations seeking certified AI management |
| **Structure** | 4 functions (GOVERN, MAP, MEASURE, MANAGE) | Risk tiers + obligations | PDCA management system (10 clauses) |
| **Penalties** | None | Up to €35M / 7% global turnover | None (but certification at risk) |
| **Certification** | No | No (conformity assessment) | Yes |
| **Maturity required** | Any | Any (compliance is binary) | Moderate+ |

---

## Which Framework for Your Context

**Use NIST AI RMF if:**
- You are US-based with no immediate EU market exposure
- You have an existing NIST CSF program and want AI alignment
- You want a governance starting point with no compliance mandate
- Your leadership needs a structured but flexible AI risk vocabulary

**Use EU AI Act compliance as the driver if:**
- You operate in the EU or serve EU customers
- You have high-risk AI systems (see Annex III)
- Your legal/compliance team is driving the initiative
- You face regulatory scrutiny (financial services, healthcare, HR tech)

**Pursue ISO 42001 certification if:**
- You sell enterprise B2B software and AI governance is a buyer requirement
- You want third-party assurance of your AI governance maturity
- You are ISO 27001 certified and want to extend your certification portfolio
- You are building toward EU AI Act conformity assessment readiness

**Combine all three if:**
- You are a global enterprise with EU exposure, an existing security certification program, and board-level AI governance expectations

---

## Functional Mapping

| NIST AI RMF | EU AI Act Obligation | ISO 42001 Clause |
|-------------|---------------------|-----------------|
| GOVERN — Policies and accountability | Art. 9 Risk mgmt system; Art. 17 QMS | Cl. 5 Leadership; Cl. 4 Context |
| MAP — Use case inventory and risk categorization | Art. 6-7 Risk classification | Cl. 6 Planning; A.5 Impact assessment |
| MAP — Stakeholder impact | Art. 9.9 Fundamental rights impact | A.5 Impact assessment |
| MEASURE — Testing and evaluation | Art. 9.5-9.8 Accuracy, robustness | Cl. 8 Operation; A.6 Lifecycle |
| MEASURE — Bias and fairness testing | Art. 10 Data governance | A.7 Data for AI |
| MANAGE — Human oversight | Art. 14 Human oversight | A.6.2.6 Human oversight design |
| MANAGE — Incident response | Art. 73 Serious incident reporting | Cl. 10 Improvement |
| MANAGE — Monitoring | Art. 72 Post-market monitoring | Cl. 9 Performance evaluation |

---

## Compliance Strategy by Organization Profile

### Financial services firm (US-headquartered, EU operations)
**Priority order:**
1. EU AI Act compliance (binding; high-risk classification likely for credit/fraud AI)
2. ISO 42001 certification (enterprise trust signal; auditor familiarity)
3. NIST AI RMF alignment (maps to existing NIST CSF program)

### B2B SaaS startup (US-based, selling to enterprises)
**Priority order:**
1. NIST AI RMF (lightweight governance foundation; SDO-aligned)
2. ISO 42001 (when enterprise customers start requiring it in vendor questionnaires)
3. EU AI Act (when EU expansion is on the roadmap)

### AI-native product company (global)
**Priority order:**
1. EU AI Act (likely GPAI obligations if building foundation models)
2. ISO 42001 (certification differentiator vs. competitors)
3. NIST AI RMF (US market credibility; NIST alignment in US procurement)

### Internal enterprise AI consumer (no AI products sold)
**Priority order:**
1. NIST AI RMF (operational framework for governing internal AI use)
2. EU AI Act deployer obligations if EU-present (transparency, high-risk use controls)
3. ISO 42001 (if seeking third-party assurance for board/audit committee)

---

## Common Questions

**"Can ISO 42001 certification satisfy EU AI Act conformity assessment?"**
Partially. The EU AI Act requires conformity assessment for high-risk AI systems. ISO 42001 addresses governance process maturity, not product conformity. A certified AIMS strengthens your conformity assessment position but does not substitute for it. EU-accredited notified bodies will be the authoritative voice as guidance develops.

**"Is NIST AI RMF becoming mandatory in the US?"**
As of 2025, it remains voluntary. However, US federal agencies are increasingly using it as a procurement requirement, and the SEC's AI disclosure expectations are pushing public companies toward documented AI governance frameworks.

**"If we're ISO 27001 certified, how much additional work is ISO 42001?"**
Practitioners report 30–50% overlap between the two standards. The main incremental work is in AI-specific clauses: Annex A.5 (impact assessment), A.6 (AI system lifecycle controls), and A.7 (data governance for AI). Expect 3–6 months of additional work for an already-mature ISO 27001 program.

---

*See also: [NIST AI RMF](NIST-AI-RMF.md) | [EU AI Act](EU-AI-Act.md) | [ISO 42001](ISO-42001.md)*
