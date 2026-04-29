# AI Governance Toolkit

> A practitioner-built, open-source toolkit for designing, assessing, and operationalizing AI governance programs — grounded in real-world GRC practice.

[![License](https://img.shields.io/badge/License-Apache_2.0-blue.svg)](LICENSE)
[![Framework Coverage](https://img.shields.io/badge/Frameworks-NIST%20AI%20RMF%20%7C%20EU%20AI%20Act%20%7C%20ISO%2042001-green)]()
[![Maintained](https://img.shields.io/badge/Maintained-Yes-brightgreen)]()

---

## Why this exists

Most AI governance resources are either too academic or too vendor-driven. This toolkit is built by a practitioner — for practitioners — combining:

- **GRC rigor** (NIST, ISO, SOC 2, CISA frameworks)
- **Financial fluency** (risk quantification, board-ready metrics)
- **Operational realism** (templates you can actually use in Monday's meeting)

AI governance isn't a compliance checkbox. Done right, it's a **business enabler** — accelerating AI adoption safely while building trust with customers, investors, and regulators.

---

## What's inside

```
ai-governance-toolkit/
├── Framework guides
│   ├── NIST-AI-RMF.md          # Annotated NIST AI RMF 1.0 breakdown
│   ├── ISO-42001.md             # ISO/IEC 42001:2023 guide
│   ├── comparison.md            # Side-by-side framework analysis
│   └── crq-framework.md         # CRQ-F financial risk methodology
│
├── Templates
│   ├── ai-policy-template.md    # AI use policy (copy-paste ready)
│   ├── ai-risk-register.md      # Risk tracking register
│   ├── use-case-intake.md       # AI deployment approval form
│   └── vendor-ddq.md            # Vendor due diligence questionnaire
│
├── Assessments
│   └── maturity-scorecard.md    # 5-domain governance maturity scorecard
│
├── Tools
│   ├── risk_scorer.py           # AI use case risk tier classifier
│   ├── vendor_screen.py         # Vendor governance screening tool
│   └── maturity_report.py       # Maturity report and 90-day roadmap generator
│
├── examples/
│   ├── risk_scorer_example.json
│   ├── vendor_screen_example.json
│   └── maturity_report_example.json
│
├── getting-started.md
├── requirements.txt
└── README.md
```

---

## Quick start

### Use the templates (no setup required)
Browse the markdown files — every document is copy-paste ready.

### Run the Python tools

```bash
git clone https://github.com/rafatyazdani/ai-governance-toolkit.git
cd ai-governance-toolkit
pip install -r requirements.txt

# Score an AI use case for governance risk
python risk_scorer.py --json examples/risk_scorer_example.json

# Screen a vendor for AI governance maturity
python vendor_screen.py --json examples/vendor_screen_example.json --vendor "Acme AI"

# Generate a maturity report
python maturity_report.py --json examples/maturity_report_example.json --org "Your Org"
```

All tools also support interactive mode:

```bash
python risk_scorer.py --interactive
python vendor_screen.py --interactive
python maturity_report.py --interactive
```

---

## Framework coverage

| Framework | Region | Focus | Guide |
|-----------|--------|-------|-------|
| NIST AI RMF 1.0 | US | Risk management lifecycle | [→](NIST-AI-RMF.md) |
| EU AI Act | EU | Regulatory compliance, risk tiers | [→](comparison.md) |
| ISO/IEC 42001:2023 | Global | AI management systems | [→](ISO-42001.md) |
| Framework comparison | — | Side-by-side analysis | [→](comparison.md) |

---

## Who this is for

- **CISOs and GRC leaders** building or maturing an AI governance program
- **Security managers** advising the business on AI risk
- **Compliance professionals** mapping AI usage to regulatory requirements
- **Founders and operators** at AI-native companies who need governance without the bureaucracy
- **Consultants** who need a credible starting point for client engagements

---

## The CRQ-F Framework

This toolkit includes the **Cyber Risk Quantification — Financial (CRQ-F) Framework**, a five-phase methodology for expressing AI and cyber risk in board-ready financial terms (ALE, ROSI, MTTR).

See [`crq-framework.md`](crq-framework.md) for the full methodology.

---

## License

Apache 2.0 — free to use, adapt, and deploy in commercial contexts with attribution.

---

*Built by a CISSP + CPA with 10+ years in GRC and cybersecurity strategy.*
