# 🧭 AI Governance Toolkit

> A practitioner-built, open-source toolkit for designing, assessing, and operationalizing AI governance programs — grounded in real-world GRC practice.

[![License](https://img.shields.io/badge/License-Apache_2.0-blue.svg)](LICENSE)
[![Framework Coverage](https://img.shields.io/badge/Frameworks-NIST%20AI%20RMF%20%7C%20EU%20AI%20Act%20%7C%20ISO%2042001-green)](frameworks/)
[![Maintained](https://img.shields.io/badge/Maintained-Yes-brightgreen)](CONTRIBUTING.md)

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
├── frameworks/          # Annotated breakdowns of major AI governance frameworks
├── tools/               # Python scripts for scoring, screening, and reporting
├── templates/           # Ready-to-use governance documents
├── assessments/         # Scorecards and assessment guides
├── docs/                # Explainers, guides, and the CRQ-F methodology
├── README.md
├── CONTRIBUTING.md
└── LICENSE
```

---

## Quick start

### Use the templates (no setup required)
Browse `templates/` and `assessments/` — every document is Markdown, copy-paste ready.

### Run the Python tools
```bash
git clone https://github.com/YOUR_USERNAME/ai-governance-toolkit.git
cd ai-governance-toolkit/tools
pip install -r requirements.txt

# Score an AI use case for governance risk
python risk_scorer.py --input ../templates/use-case-intake.md

# Screen a vendor for AI governance maturity
python vendor_screen.py --vendor "Acme AI" --tier high

# Generate a maturity report
python maturity_report.py --org "Your Org" --output report.md
```

---

## Framework coverage

| Framework | Region | Focus | Guide |
|-----------|--------|-------|-------|
| NIST AI RMF 1.0 | US | Risk management lifecycle | [→](frameworks/NIST-AI-RMF.md) |
| EU AI Act | EU | Regulatory compliance, risk tiers | [→](frameworks/EU-AI-Act.md) |
| ISO/IEC 42001:2023 | Global | AI management systems | [→](frameworks/ISO-42001.md) |
| Framework comparison | — | Side-by-side analysis | [→](frameworks/comparison.md) |

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

See [`docs/crq-framework.md`](docs/crq-framework.md) for the full methodology.

---

## Contributing

Contributions welcome. See [CONTRIBUTING.md](CONTRIBUTING.md).

---

## License

Apache 2.0 — free to use, adapt, and deploy in commercial contexts with attribution.

---

*Built by a CISSP + CPA with 10+ years in GRC and cybersecurity strategy. If this helped you, star the repo or connect on [LinkedIn](https://linkedin.com/in/YOUR_HANDLE).*
