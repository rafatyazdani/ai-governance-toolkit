# AI Risk Register

> Version: 1.0 | Owner: [Risk Owner Name] | Last reviewed: [Date] | Next review: [Date + 90 days]

This register catalogs AI-related risks across the organization. Each entry links to the AI use case that generates the risk, documents the risk in financial terms where possible, and tracks mitigation status.

---

## How to Use This Register

1. Add a row for each identified AI risk (one risk per row — not one use case per row)
2. Score likelihood (1–5) and impact (1–5); multiply for inherent risk score
3. Document mitigating controls and re-score for residual risk
4. Review quarterly; escalate residual scores ≥ 12 to leadership

**Risk scoring scale:**

| Score | Likelihood | Impact |
|-------|-----------|--------|
| 1 | Rare (<5% probability in 12 months) | Negligible (<$10K) |
| 2 | Unlikely (5–25%) | Minor ($10K–$100K) |
3 | Possible (25–50%) | Moderate ($100K–$1M) |
| 4 | Likely (50–75%) | Significant ($1M–$10M) |
| 5 | Almost certain (>75%) | Severe (>$10M) |

---

## Risk Register

| ID | Risk Name | Use Case | Risk Category | Description | Likelihood | Impact | Inherent Score | Mitigating Controls | Residual Score | Owner | Status | Last Updated |
|----|-----------|----------|--------------|-------------|-----------|--------|---------------|--------------------|--------------|----|--------|------|
| AIR-001 | Biased hiring recommendations | AI resume screening | Bias / Fairness | AI model trained on historical data may systematically disadvantage protected classes, creating EEOC exposure | 3 | 4 | 12 | Human review required for all shortlists; quarterly bias audit; diverse training data validation | 6 | CHRO | Open | [Date] |
| AIR-002 | AI vendor data breach | Customer support chatbot | Third-party / Supply chain | AI SaaS vendor breached; customer PII exposed via chatbot training data | 2 | 5 | 10 | Vendor SOC 2 Type II required; DPA in contract; quarterly vendor review | 4 | CISO | Open | [Date] |
| AIR-003 | Model hallucination in customer-facing output | Product recommendation engine | Reliability / Accuracy | Model generates false product claims, creating consumer protection and reputational risk | 4 | 3 | 12 | Output filtering; human review for edge cases; customer feedback loop; rate limiting | 6 | VP Product | Open | [Date] |
| AIR-004 | Prompt injection attack | Internal AI assistant | Security / Adversarial | Malicious user crafts input to exfiltrate sensitive internal data via AI assistant | 3 | 4 | 12 | Input sanitization; output filtering; access controls on data sources; logging | 4 | CISO | In progress | [Date] |
| AIR-005 | Model drift — fraud detection | Payment fraud AI | Reliability / Drift | Fraud patterns shift; model performance degrades without detection, increasing false negatives | 3 | 5 | 15 | Monthly performance monitoring; alerting on KPI thresholds; quarterly retraining cadence | 8 | Head of Risk | Open | [Date] |
| AIR-006 | EU AI Act non-compliance | [High-risk use case] | Regulatory | Failure to implement required controls for high-risk AI before Aug 2026 deadline | 2 | 5 | 10 | Compliance program underway; legal counsel engaged; gap assessment Q1 | 4 | Chief Compliance | In progress | [Date] |
| AIR-007 | Over-reliance on AI decision | Credit underwriting AI | Human oversight | Loan officers bypass human review, delegating consequential decisions to AI alone | 3 | 4 | 12 | Policy requires human sign-off >$X; audit trail; training program | 6 | Chief Risk Officer | Open | [Date] |

---

## Escalation Log

Risks with residual score ≥ 12 require formal escalation to leadership and documented risk acceptance or mitigation plan.

| ID | Escalated To | Date | Decision | Next Review |
|----|-------------|------|----------|------------|
| AIR-005 | CRO + Board Risk Committee | [Date] | Accepted with enhanced monitoring commitment | [Date + 90 days] |

---

## Risk Summary Dashboard

| Category | Open Risks | Avg Residual Score | Highest Risk |
|----------|-----------|-------------------|-------------|
| Bias / Fairness | 1 | 6 | AIR-001 |
| Third-party / Supply chain | 1 | 4 | AIR-002 |
| Reliability / Accuracy | 2 | 7 | AIR-005 |
| Security / Adversarial | 1 | 4 | AIR-004 |
| Regulatory | 1 | 4 | AIR-006 |
| Human oversight | 1 | 6 | AIR-007 |

---

## Change Log

| Version | Date | Author | Change |
|---------|------|--------|--------|
| 1.0 | [Date] | [Name] | Initial register |

---

*Template from [ai-governance-toolkit](https://github.com/YOUR_USERNAME/ai-governance-toolkit) | Apache 2.0*
