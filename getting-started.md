# Getting Started

> New to this toolkit? Start here. This guide helps you find the right resources for your situation in under five minutes.

---

## What are you trying to do?

### "I need to build an AI governance program from scratch"

1. Read [AI Governance 101](ai-governance-101.md) for foundational concepts
2. Choose your framework anchor in [Framework Comparison](../frameworks/comparison.md)
3. Draft your [AI Use Policy](../templates/ai-policy-template.md)
4. Run the [Maturity Scorecard](../assessments/maturity-scorecard.md) to establish your baseline
5. Build your [AI Risk Register](../templates/ai-risk-register.md)
6. Use `maturity_report.py` to generate a 90-day roadmap

**Time to first output:** ~2 hours for a baseline report you can share with leadership.

---

### "I need to assess a specific AI use case for risk"

1. Complete the [AI Use Case Intake Form](../templates/use-case-intake.md)
2. Run `python tools/risk_scorer.py --interactive` for automated risk tier and ALE estimate
3. Apply controls from the scorecard matching your risk tier
4. Add to [AI Risk Register](../templates/ai-risk-register.md)

**Time to first output:** ~20 minutes.

---

### "I'm evaluating an AI vendor"

1. Use the [Vendor AI DDQ](../templates/vendor-ddq.md) for qualitative assessment
2. Run `python tools/vendor_screen.py --interactive` for automated scoring
3. Document result in vendor risk register with re-assessment schedule

**Time to first output:** ~45 minutes (depends on vendor responsiveness).

---

### "I need to present AI risk to the board or audit committee"

1. Read [CRQ-F Framework](crq-framework.md) for financial framing methodology
2. Run `risk_scorer.py` on your top 5 risks to generate ALE estimates
3. Build the "five numbers" slide (see CRQ-F Phase 5)
4. Use [AI Risk Register](../templates/ai-risk-register.md) Escalation Log as backup detail

**Time to first output:** ~3 hours for a complete board package.

---

### "I need to comply with the EU AI Act"

1. Read [EU AI Act guide](../frameworks/EU-AI-Act.md) — focus on risk tier and timeline sections
2. Classify all AI use cases against EU AI Act risk tiers using the intake form
3. Identify any Annex III (high-risk) use cases — these have the most urgent deadlines
4. Map high-risk use cases to required controls
5. Document classification rationale for regulatory defensibility

**Time to first output:** ~4 hours for a complete classification inventory.

---

### "I want to get ISO 42001 certified"

1. Read [ISO 42001 guide](../frameworks/ISO-42001.md)
2. Run the [Maturity Scorecard](../assessments/maturity-scorecard.md) — ISO 42001 maps directly to its five domains
3. Identify gaps vs. ISO 42001 Annex A controls
4. Build remediation roadmap using `maturity_report.py`
5. Engage an accredited certification body for pre-assessment

**Realistic timeline:** 6–18 months depending on current maturity.

---

## Toolkit Map

```
ai-governance-toolkit/
│
├── frameworks/
│   ├── NIST-AI-RMF.md          ← Start here for US voluntary framework
│   ├── EU-AI-Act.md             ← Start here for EU regulatory compliance
│   ├── ISO-42001.md             ← Start here for certification path
│   └── comparison.md            ← Not sure which? Start here
│
├── templates/                   ← Copy-paste ready governance documents
│   ├── ai-risk-register.md
│   ├── use-case-intake.md
│   ├── ai-policy-template.md
│   └── vendor-ddq.md
│
├── tools/                       ← Python scripts (no dependencies required)
│   ├── risk_scorer.py           ← Score any AI use case for risk
│   ├── vendor_screen.py         ← Screen AI vendors
│   └── maturity_report.py       ← Generate 90-day governance roadmap
│
├── assessments/
│   ├── maturity-scorecard.md   ← Self-assessment scorecard
│   ├── model-risk.md            ← Model-level risk assessment
│   ├── bias-fairness.md         ← Bias and fairness assessment guide
│   └── third-party-ai.md        ← Third-party AI risk assessment
│
└── docs/
    ├── getting-started.md       ← You are here
    ├── ai-governance-101.md     ← Foundational concepts
    ├── crq-framework.md         ← Financial risk quantification methodology
    └── changelog.md             ← Version history
```

---

## Running the Python Tools

All tools require Python 3.9+. No third-party packages needed for core functionality.

```bash
# Clone the repo
git clone https://github.com/YOUR_USERNAME/ai-governance-toolkit.git
cd ai-governance-toolkit/tools

# Risk scorer — interactive mode
python risk_scorer.py --interactive

# Risk scorer — from JSON
python risk_scorer.py --json my_use_case.json --output report.md

# Vendor screener — interactive mode
python vendor_screen.py --interactive

# Maturity report — interactive mode
python maturity_report.py --interactive

# Maturity report — from JSON scores file
python maturity_report.py --json scores.json --org "My Org" --output maturity.md
```

**JSON input examples** are provided in `tools/examples/` (see `use_case_example.json`, `vendor_example.json`, `scores_example.json`).

---

## Contributing

See [CONTRIBUTING.md](../CONTRIBUTING.md). Pull requests welcome — especially for new framework mappings, assessment templates, and tool enhancements.

---

*[ai-governance-toolkit](https://github.com/YOUR_USERNAME/ai-governance-toolkit) | Apache 2.0*
