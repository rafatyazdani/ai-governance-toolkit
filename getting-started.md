# Getting Started

> New to this toolkit? Start here. This guide helps you find the right resources for your situation in under five minutes.

---

## What are you trying to do?

### "I need to build an AI governance program from scratch"

1. Choose your framework anchor in [Framework Comparison](comparison.md)
2. Draft your [AI Use Policy](ai-policy-template.md)
3. Run the [Maturity Scorecard](maturity-scorecard.md) to establish your baseline
4. Build your [AI Risk Register](ai-risk-register.md)
5. Use `maturity_report.py` to generate a 90-day roadmap

**Time to first output:** ~2 hours for a baseline report you can share with leadership.

---

### "I need to assess a specific AI use case for risk"

1. Complete the [AI Use Case Intake Form](use-case-intake.md)
2. Run `python risk_scorer.py --interactive` for automated risk tier and ALE estimate
3. Apply controls from the scorecard matching your risk tier
4. Add to [AI Risk Register](ai-risk-register.md)

**Time to first output:** ~20 minutes.

---

### "I'm evaluating an AI vendor"

1. Use the [Vendor AI DDQ](vendor-ddq.md) for qualitative assessment
2. Run `python vendor_screen.py --interactive` for automated scoring
3. Document result in vendor risk register with re-assessment schedule

**Time to first output:** ~45 minutes (depends on vendor responsiveness).

---

### "I need to present AI risk to the board or audit committee"

1. Read [CRQ-F Framework](crq-framework.md) for financial framing methodology
2. Run `risk_scorer.py` on your top 5 risks to generate ALE estimates
3. Build the "five numbers" slide (see CRQ-F Phase 5)
4. Use [AI Risk Register](ai-risk-register.md) Escalation Log as backup detail

**Time to first output:** ~3 hours for a complete board package.

---

### "I need to comply with the EU AI Act"

1. Read [Framework Comparison](comparison.md) — EU AI Act section covers risk tiers and timelines
2. Classify all AI use cases against EU AI Act risk tiers using the intake form
3. Identify any Annex III (high-risk) use cases — these have the most urgent deadlines
4. Map high-risk use cases to required controls
5. Document classification rationale for regulatory defensibility

**Time to first output:** ~4 hours for a complete classification inventory.

---

### "I want to get ISO 42001 certified"

1. Read [ISO 42001 guide](ISO-42001.md)
2. Run the [Maturity Scorecard](maturity-scorecard.md) — ISO 42001 maps directly to its five domains
3. Identify gaps vs. ISO 42001 Annex A controls
4. Build remediation roadmap using `maturity_report.py`
5. Engage an accredited certification body for pre-assessment

**Realistic timeline:** 6–18 months depending on current maturity.

---

## Toolkit Map

```
ai-governance-toolkit/
│
├── Framework guides
│   ├── NIST-AI-RMF.md          ← Start here for US voluntary framework
│   ├── ISO-42001.md             ← Start here for certification path
│   └── comparison.md            ← Not sure which framework? Start here
│
├── Templates                    ← Copy-paste ready governance documents
│   ├── ai-risk-register.md
│   ├── use-case-intake.md
│   ├── ai-policy-template.md
│   └── vendor-ddq.md
│
├── Tools                        ← Python scripts (no dependencies required)
│   ├── risk_scorer.py           ← Score any AI use case for risk
│   ├── vendor_screen.py         ← Screen AI vendors
│   └── maturity_report.py       ← Generate 90-day governance roadmap
│
├── Assessments
│   └── maturity-scorecard.md   ← Self-assessment scorecard
│
├── examples/                    ← Sample JSON inputs for the Python tools
│   ├── risk_scorer_example.json
│   ├── vendor_screen_example.json
│   └── maturity_report_example.json
│
└── crq-framework.md             ← Financial risk quantification methodology
```

---

## Running the Python Tools

All tools require Python 3.9+. No third-party packages needed.

```bash
# Clone the repo
git clone https://github.com/rafatyazdani/ai-governance-toolkit.git
cd ai-governance-toolkit

# Risk scorer — interactive mode
python risk_scorer.py --interactive

# Risk scorer — from JSON
python risk_scorer.py --json examples/risk_scorer_example.json --output report.md

# Vendor screener — interactive mode
python vendor_screen.py --interactive

# Vendor screener — from JSON
python vendor_screen.py --json examples/vendor_screen_example.json --vendor "Acme AI" --output vendor_report.md

# Maturity report — interactive mode
python maturity_report.py --interactive

# Maturity report — from JSON scores file
python maturity_report.py --json examples/maturity_report_example.json --org "My Org" --output maturity.md
```

Sample JSON inputs are in the `examples/` folder.

---

*[ai-governance-toolkit](https://github.com/rafatyazdani/ai-governance-toolkit) | Apache 2.0*
