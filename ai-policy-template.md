# Artificial Intelligence Use Policy

> **Document owner:** [CISO / Chief Risk Officer / Chief AI Officer]
> **Version:** 1.0 | **Effective date:** [Date] | **Review cycle:** Annual
> **Approved by:** [CEO / Board] on [Date]

---

## 1. Purpose

This policy establishes the organization's requirements for the responsible development, procurement, deployment, and use of artificial intelligence (AI) systems. It is designed to:

- Enable the organization to capture business value from AI while managing associated risks
- Protect individuals — employees, customers, and the public — from potential AI-related harm
- Maintain compliance with applicable laws and regulations
- Build trust with customers, partners, and regulators through transparent AI governance

This policy applies to **all AI systems** — whether developed internally, procured from vendors, or accessed via API — and to **all employees, contractors, and third parties** acting on behalf of the organization.

---

## 2. Scope

This policy applies to:

- AI systems developed or fine-tuned by the organization
- AI systems procured from third-party vendors or accessed via API
- General-purpose AI tools used by employees (e.g., AI writing assistants, coding assistants, image generators)
- AI systems embedded in existing software products

This policy does **not** apply to traditional rule-based automation that contains no machine learning component.

---

## 3. Definitions

**Artificial intelligence (AI) system:** A machine-based system that infers from inputs how to generate outputs — such as predictions, recommendations, decisions, or content — that can influence real or virtual environments.

**Generative AI:** AI systems that generate text, images, code, audio, or other content in response to prompts.

**High-risk AI system:** An AI system whose failure or malfunction could cause significant harm to individuals, create material financial loss, or generate significant legal/regulatory exposure. Defined further in the AI Use Case Classification Standard.

**AI risk owner:** The designated individual accountable for AI governance at the organizational level. [Assign: CISO, Chief Risk Officer, or Chief AI Officer]

---

## 4. Core Principles

All AI use within the organization must adhere to the following principles:

**4.1 Human accountability**
Every AI system must have a designated human owner accountable for its behavior and outputs. AI systems do not bear accountability — people do.

**4.2 Proportional oversight**
The level of human oversight applied to an AI system must be proportional to its risk. High-risk AI systems require meaningful human review of outputs before consequential decisions are made.

**4.3 Transparency**
Individuals affected by AI-informed decisions have the right to know that AI was involved. The organization will not use AI in ways that are intentionally deceptive.

**4.4 Fairness and non-discrimination**
AI systems must not produce outputs that discriminate against individuals on the basis of protected characteristics. Regular bias testing is required for systems that influence decisions about people.

**4.5 Data minimization**
AI systems will use only the minimum data necessary to achieve their purpose. Sensitive personal data will not be used for AI training without explicit authorization.

**4.6 Security and resilience**
AI systems must meet the organization's security standards. AI-specific threat vectors — including prompt injection, model inversion, and data poisoning — must be assessed and mitigated.

---

## 5. Requirements

### 5.1 Use case intake and approval

Before deploying any new AI system — or materially changing an existing one — the team must:

1. Complete the [AI Use Case Intake Form](../templates/use-case-intake.md)
2. Obtain approval from the AI risk owner
3. Obtain privacy/legal review if personal data is involved
4. Document the approved use case in the AI use case register

**No AI system may be deployed in a production environment without completed intake and documented approval.**

### 5.2 Risk classification

All approved AI use cases must be classified by risk tier (Critical / High / Medium / Low) using the AI Risk Classification Standard. Risk tier determines the required control set and monitoring cadence.

### 5.3 Prohibited AI uses

The following uses of AI are prohibited without exception:

- Using AI to make final, unreviewed consequential decisions about individuals in contexts where human review is feasible (e.g., employment termination, credit denial, benefits eligibility)
- Using AI to create deceptive synthetic media (deepfakes) representing real individuals without their consent
- Using AI in a manner that violates anti-discrimination laws or produces outputs that discriminate based on protected characteristics
- Inputting personal data of customers, employees, or third parties into unauthorized external AI tools
- Using AI systems classified as "unacceptable risk" under the EU AI Act

### 5.4 Approved AI tools

Employees may only use AI tools that have been reviewed and approved through the intake process or that appear on the organization's approved tool list. Use of unapproved AI tools for work purposes is prohibited.

*[Approved tools list maintained by: IT / CISO team. Location: [link to internal list]]*

### 5.5 Data handling

Employees must not input any of the following into external AI tools (including consumer AI products) unless the tool has been specifically approved for that data type:

- Customer personal data
- Employee personal data
- Confidential business information, financial projections, M&A information
- Proprietary source code
- Attorney-client privileged communications

### 5.6 Vendor and third-party AI

Third-party AI systems must be evaluated through the vendor risk management process before procurement. Minimum requirements:

- SOC 2 Type II report (or equivalent) reviewed and accepted
- Data Processing Agreement (DPA) executed
- AI-specific security questionnaire completed
- Contractual prohibitions on training on customer data without explicit consent

### 5.7 Monitoring and incident reporting

Approved AI systems must be monitored according to their risk tier monitoring schedule. Any AI-related incident — including model failures, unexpected outputs, data exposure, or bias incidents — must be reported to the AI risk owner within [24/48/72] hours of discovery.

---

## 6. Roles and Responsibilities

| Role | Responsibility |
|------|---------------|
| AI Risk Owner | Policy ownership; intake approvals; risk register maintenance; board reporting |
| Business unit leaders | Ensuring their teams comply; sponsoring intake requests; incident escalation |
| IT / Engineering | Technical controls implementation; vendor assessment; monitoring infrastructure |
| Legal / Privacy | Regulatory compliance review; DPA management; incident response |
| All employees | Comply with this policy; report incidents; complete required training |

---

## 7. Training

All employees who use AI systems in the course of their work must complete AI literacy and responsible AI use training within [30/60/90] days of this policy's effective date, and annually thereafter. High-risk AI system operators require role-specific training before system access is granted.

---

## 8. Enforcement

Violations of this policy may result in disciplinary action, up to and including termination of employment. Intentional misuse of AI that results in harm to individuals, legal violations, or significant financial loss may be referred to law enforcement or regulatory authorities.

---

## 9. Exceptions

Exceptions to this policy require written approval from the AI Risk Owner and, for Critical-tier exceptions, from the [CEO / Board]. All approved exceptions must be documented, time-limited, and reviewed at the next scheduled policy review.

---

## 10. Policy Review

This policy will be reviewed annually and updated to reflect changes in the regulatory environment, organizational AI usage, or lessons learned from incidents. Material changes require re-approval by [CEO / Board].

---

## Appendix A — Regulatory Context

This policy is designed to support compliance with:
- EU AI Act (Regulation EU 2024/1689)
- NIST AI Risk Management Framework 1.0
- ISO/IEC 42001:2023
- [State/local AI regulations as applicable]
- Applicable privacy regulations (GDPR, CCPA, etc.)

---

*Template from [ai-governance-toolkit](https://github.com/YOUR_USERNAME/ai-governance-toolkit) | Apache 2.0*
