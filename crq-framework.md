# CRQ-F Framework — Cyber Risk Quantification (Financial)

> A five-phase methodology for expressing AI and cybersecurity risk in board-ready financial terms. Built for security leaders who need to translate technical risk into language that CFOs, audit committees, and boards already speak.

---

## Why Financial Risk Language Matters

Security leaders lose budget battles not because their risks aren't real — but because they're expressed in the wrong language. When a CISO says "we have a critical vulnerability in our authentication layer," the CFO hears noise. When the same CISO says "unmitigated, this vulnerability creates $4.2M in annualized expected loss — for $180K in controls investment, we reduce that exposure by 73%," the conversation changes.

The CRQ-F Framework gives practitioners a structured, repeatable way to build that second sentence — for AI risk, cyber risk, and the intersection of both.

---

## The Five Phases

```
Phase 1        Phase 2        Phase 3        Phase 4        Phase 5
INVENTORY  →   CLASSIFY  →   QUANTIFY  →   PRIORITIZE  →  REPORT
Use cases      Risk tiers     ALE / ROSI     Control ROI    Board narrative
```

---

## Phase 1 — Inventory

**Goal:** Build a complete, living inventory of AI and cyber risk exposures.

**For AI systems:**
- Deploy the [AI Use Case Intake Form](../templates/use-case-intake.md)
- Capture: system description, data types, affected populations, human oversight level, decision impact

**For cyber risk:**
- Map threat scenarios to business processes (not just assets)
- Use FAIR taxonomy: Loss Event Frequency × Loss Magnitude

**Output:** Structured risk inventory. Every risk has: a name, a scenario description, an asset or system reference, and a business process it threatens.

---

## Phase 2 — Classify

**Goal:** Tier risks by severity to focus quantification effort where it matters.

**Risk tier criteria:**

| Tier | AI criteria | Cyber criteria | Quantification effort |
|------|------------|---------------|----------------------|
| Critical | Consequential decisions; regulated domain; high scale | Crown-jewel asset; ransomware target; external exposure | Full Monte Carlo |
| High | Material business impact; partial oversight | Significant data exposure; internal lateral movement | ALE + scenario analysis |
| Medium | Internal use; human review present | Limited impact; internal only | Simplified ALE |
| Low | No personal data; fully reviewed | Minimal assets; no external exposure | Point estimate only |

**Tool:** Use `risk_scorer.py` to automate tier classification for AI use cases.

---

## Phase 3 — Quantify

### Core formula: Annualized Loss Expectancy (ALE)

```
ALE = ARO × SLE

Where:
  ARO = Annualized Rate of Occurrence (probability of incident per year)
  SLE = Single Loss Expectancy (financial impact of one incident)
```

**Building SLE — loss components to include:**

| Component | Description | How to estimate |
|-----------|-------------|----------------|
| Direct response costs | Incident response, forensics, breach notification | Vendor quotes + historical incidents |
| Regulatory fines | GDPR, EU AI Act, SEC penalties | Regulatory guidance + legal counsel |
| Legal liability | Class action, customer claims, settlements | Industry benchmarks (Advisen, Willis Towers Watson) |
| Business disruption | Revenue loss during outage, SLA penalties | Finance team — revenue per hour/day |
| Reputational damage | Customer churn, brand damage | Marketing / customer success data |
| Third-party claims | Vendor indemnification, supply chain impact | Contract review |

**Building ARO — probability inputs:**

For AI-specific risks:
- Model bias incident: 15–30% annually for untested high-risk AI (practitioner estimate)
- AI vendor breach: correlate with vendor SOC 2 findings and sector breach rates
- Model drift causing failure: 20–40% annually without monitoring (research-based)
- Prompt injection exploit: 10–25% annually for customer-facing LLM without controls

For cyber risk:
- Use insurance actuarial data (Corvus, Coalition, At-Bay publish frequency data)
- FAIR Institute provides calibrated frequency databases
- Sector-specific data: FS-ISAC, H-ISAC, financial sector regulatory guidance

### Monte Carlo simulation

For Critical-tier risks, point estimates understate uncertainty. Monte Carlo simulation replaces single ARO and SLE inputs with distributions, producing a range of outcomes and confidence intervals.

**Minimum inputs for Monte Carlo:**
- ARO: triangular distribution (min, most likely, max)
- SLE: lognormal distribution (mean and standard deviation)
- Iterations: 10,000+ for stable results

**Tool:** Use `tools/risk_scorer.py` for simplified ALE. For full Monte Carlo, see the [OrionMaturity framework](https://github.com/YOUR_USERNAME/OrionMaturity) or use @PALISADE, Crystal Ball, or a Python `numpy`/`scipy` implementation.

---

## Phase 4 — Prioritize (ROSI)

**Goal:** Rank control investments by financial return.

### Return on Security Investment (ROSI)

```
ROSI = (Risk Reduction Value − Control Cost) / Control Cost

Where:
  Risk Reduction Value = ALE_before − ALE_after
  Control Cost = Annualized cost of implementing the control
```

**Example:**

| Input | Value |
|-------|-------|
| ALE before control | $2,400,000 |
| Control effectiveness (risk reduction) | 65% |
| ALE after control | $840,000 |
| Risk reduction value | $1,560,000 |
| Control annualized cost | $180,000 |
| **ROSI** | **767%** |
| **Net value** | **$1,380,000** |

**Interpreting ROSI:**
- ROSI > 100%: Control delivers more value than it costs — invest
- ROSI 0–100%: Control costs more than expected savings — consider alternative controls or risk acceptance
- ROSI < 0%: Control destroys value — avoid unless required for compliance

### Control ROI Scoring Engine

For portfolios of controls, use the Control ROI Scoring Engine (Excel-based tool available in this toolkit) to rank controls by ROSI, factoring in:
- Control effectiveness decay over time (controls become less effective without maintenance)
- Implementation timeline (delayed controls mean deferred risk reduction)
- Interdependencies (some controls only work in combination)

---

## Phase 5 — Report

**Goal:** Deliver board-ready risk narrative with clear ask and financial justification.

### Board reporting structure

**Slide 1 — AI/Cyber risk summary**
- Total risk exposure (aggregate ALE): $X
- Year-over-year change: +/- X%
- Top 3 risks by ALE

**Slide 2 — Control investment proposal**
- Proposed investment: $X
- Expected risk reduction: $X (ROSI: X%)
- Residual exposure after investment: $X

**Slide 3 — Risk acceptance**
- Risks accepted (not mitigated): list with rationale and residual ALE
- Board sign-off requested for risks above appetite threshold

### The five numbers every CISO should know

When walking into any board or audit committee meeting, know these five numbers cold:

1. **Aggregate ALE** — Total annualized expected loss across all material risks
2. **Top risk ALE** — The single largest risk by expected financial impact
3. **Current security budget as % of IT spend** — Benchmarks: 8–15% for most sectors
4. **ROSI on proposed investments** — Your financial justification for the ask
5. **MTTR** — Mean Time to Remediate critical vulnerabilities (operational health metric)

---

## AI-Specific Risk Quantification Notes

**Why AI risk is harder to quantify than traditional cyber risk:**
- Failure modes are often probabilistic, not binary (AI doesn't "go down" — it degrades)
- Harm can be diffuse and delayed (biased AI decisions accumulate harm over months)
- Regulatory penalty exposure is uncertain (EU AI Act enforcement is still maturing)
- Reputational damage from AI failures can be disproportionate to the technical severity

**Practitioner adjustments:**
- Add a "reputational multiplier" (1.5–3×) to SLE for customer-facing AI failures
- Model bias incidents: use class action settlement data as SLE anchor
- Regulatory fines: use EU AI Act maximum penalties as upper bound for sensitivity analysis
- Include opportunity cost of AI being disabled post-incident (revenue impact of taking down the system)

---

## Resources

- [FAIR Institute](https://www.fairinstitute.org) — Open FAIR standard for risk quantification
- [NIST AI RMF](../frameworks/NIST-AI-RMF.md) — Governance framework alignment
- [AI Risk Register template](../templates/ai-risk-register.md) — Capture risks for quantification
- [risk_scorer.py](../tools/risk_scorer.py) — Automate ALE estimation

---

*Part of [ai-governance-toolkit](https://github.com/YOUR_USERNAME/ai-governance-toolkit) | Apache 2.0*
