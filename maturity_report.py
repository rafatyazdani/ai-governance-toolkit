#!/usr/bin/env python3
"""
ai-governance-toolkit: maturity_report.py
------------------------------------------
Takes scorecard inputs and produces a formatted AI governance
maturity report with domain breakdown, gap analysis, and
a prioritized 90-day roadmap.

Usage:
    python maturity_report.py --interactive
    python maturity_report.py --json scores.json --org "Acme Corp"
    python maturity_report.py --json scores.json --output report.md

Input JSON format:
{
  "org": "Acme Corp",
  "assessor": "Jane Smith",
  "date": "2025-01-15",
  "scores": {
    "governance": [3, 2, 1, 3, 2],
    "risk_identification": [2, 3, 2, 1, 2],
    "technical_controls": [2, 2, 1, 2, 1],
    "human_oversight": [3, 2, 3, 1, 2],
    "compliance": [2, 1, 2, 3, 2]
  }
}

Requirements: See requirements.txt
"""

import argparse
import json
import sys
from dataclasses import dataclass, field
from datetime import datetime
from typing import List, Dict


# ---------------------------------------------------------------------------
# Scorecard definition (mirrors maturity-scorecard.md)
# ---------------------------------------------------------------------------

DOMAINS = [
    {
        "key": "governance",
        "label": "Governance Structure",
        "capabilities": [
            "AI risk ownership assigned",
            "AI policy written and enforced",
            "Board visibility into AI risks",
            "AI roles and responsibilities defined",
            "Dedicated AI governance budget",
        ],
    },
    {
        "key": "risk_identification",
        "label": "Risk Identification & Classification",
        "capabilities": [
            "AI use case inventory maintained",
            "Risk tier classification in place",
            "Formal intake and approval process",
            "Impact assessment for high/critical use cases",
            "Third-party AI inventoried and classified",
        ],
    },
    {
        "key": "technical_controls",
        "label": "Technical Controls & Testing",
        "capabilities": [
            "Pre-deployment testing protocol",
            "Bias and fairness testing",
            "AI security testing",
            "Model drift monitoring in production",
            "Explainability for high-stakes outputs",
        ],
    },
    {
        "key": "human_oversight",
        "label": "Human Oversight & Accountability",
        "capabilities": [
            "Human-in-the-loop for high/critical AI",
            "Override and correction mechanisms",
            "Audit trails for AI-influenced decisions",
            "AI incident response procedures",
            "Named accountability for every AI system",
        ],
    },
    {
        "key": "compliance",
        "label": "Compliance & Continuous Improvement",
        "capabilities": [
            "Regulatory mapping complete",
            "AI governance training program",
            "Vendor AI due diligence process",
            "Policy review cycle established",
            "AI governance KPIs tracked",
        ],
    },
]

MATURITY_LABELS = {
    1: "Initial",
    2: "Developing",
    3: "Defined",
    4: "Optimized",
}

MATURITY_DESCRIPTIONS = {
    1: "Ad hoc or absent. No formal process. Outcomes unpredictable.",
    2: "Basic process exists but inconsistently applied. Dependent on individuals.",
    3: "Documented, consistently applied, and understood organization-wide.",
    4: "Measured, continuously improved, and benchmarked against industry.",
}

SCORE_BANDS = [
    (80, 100, "Optimized", "Industry-leading AI governance. Focus on benchmarking and certification."),
    (60, 79,  "Defined",   "Solid foundation. Prioritize consistency and executive reporting."),
    (40, 59,  "Developing","Core elements emerging. Focus on highest-risk areas first."),
    (20, 39,  "Initial",   "Governance largely ad hoc. Immediate investment required."),
    (0,  19,  "Absent",    "No meaningful AI governance program. Critical exposure."),
]

# Prioritized 90-day roadmap items by domain
ROADMAP_ITEMS = {
    "governance": {
        1: "Assign a named AI risk owner (can be existing CISO or CRO) — Week 1",
        2: "Draft and obtain executive approval for AI use policy — Days 1–30",
        3: "Add AI risk to board reporting agenda — Days 30–60",
        4: "Formalize AI governance committee with cross-functional membership — Days 30–90",
    },
    "risk_identification": {
        1: "Conduct AI use case discovery sprint with all business units — Week 1–2",
        2: "Implement risk tier classification for all discovered use cases — Days 14–30",
        3: "Deploy AI intake form and approval workflow — Days 30–45",
        4: "Extend intake to cover third-party AI and SaaS tools — Days 45–90",
    },
    "technical_controls": {
        1: "Define minimum pre-deployment testing requirements per risk tier — Days 1–30",
        2: "Schedule bias testing for highest-risk use cases — Days 30–60",
        3: "Conduct AI security assessment (prompt injection focus) — Days 30–60",
        4: "Implement model monitoring alerting for production AI — Days 45–90",
    },
    "human_oversight": {
        1: "Map all high/critical AI systems and define mandatory human review points — Days 1–30",
        2: "Implement audit logging for AI-influenced decisions — Days 30–60",
        3: "Draft AI incident response runbook and conduct tabletop — Days 45–75",
        4: "Document named accountability for every AI system — Days 1–45",
    },
    "compliance": {
        1: "Complete EU AI Act use case classification for all active systems — Days 1–30",
        2: "Deploy AI governance training for all employees using AI tools — Days 30–60",
        3: "Implement AI vendor DDQ as standard part of vendor onboarding — Days 30–60",
        4: "Define and begin tracking 3–5 AI governance KPIs — Days 45–90",
    },
}


# ---------------------------------------------------------------------------
# Scoring and analysis
# ---------------------------------------------------------------------------

@dataclass
class DomainResult:
    key: str
    label: str
    capabilities: List[str]
    scores: List[int]
    avg_score: float = 0.0
    total_score: float = 0.0   # out of 20
    gaps: List[str] = field(default_factory=list)
    strengths: List[str] = field(default_factory=list)
    roadmap: List[str] = field(default_factory=list)


@dataclass
class MaturityReport:
    org: str
    assessor: str
    date: str
    total_score: int
    maturity_level: str
    maturity_description: str
    domains: List[DomainResult] = field(default_factory=list)
    top_priorities: List[str] = field(default_factory=list)


def analyze(org: str, assessor: str, date: str, scores_by_domain: Dict[str, List[int]]) -> MaturityReport:
    domain_results = []
    grand_total = 0

    for d in DOMAINS:
        raw_scores = scores_by_domain.get(d["key"], [2] * 5)
        # Clamp to 1–4
        clamped = [max(1, min(4, s)) for s in raw_scores]
        avg = sum(clamped) / len(clamped)
        total = sum(clamped)  # max 20

        gaps = [
            f"{cap} (score: {s}/4)"
            for cap, s in zip(d["capabilities"], clamped)
            if s <= 2
        ]
        strengths = [
            cap
            for cap, s in zip(d["capabilities"], clamped)
            if s >= 3
        ]

        # Roadmap: pick items for capabilities scoring 1 or 2
        roadmap = []
        low_caps = [cap for cap, s in zip(d["capabilities"], clamped) if s <= 2]
        rmap = ROADMAP_ITEMS.get(d["key"], {})
        for score_threshold, item in rmap.items():
            if len(roadmap) < 3 and avg <= score_threshold:
                roadmap.append(item)

        dr = DomainResult(
            key=d["key"],
            label=d["label"],
            capabilities=d["capabilities"],
            scores=clamped,
            avg_score=avg,
            total_score=total,
            gaps=gaps,
            strengths=strengths,
            roadmap=roadmap,
        )
        domain_results.append(dr)
        grand_total += total

    # Map to 100-point scale (max 100 = 5 domains × 20 pts)
    score_100 = grand_total

    maturity_level, maturity_description = "Unknown", ""
    for lo, hi, label, desc in SCORE_BANDS:
        if lo <= score_100 <= hi:
            maturity_level, maturity_description = label, desc
            break

    # Top priorities: lowest-scoring capabilities across all domains
    all_gaps = []
    for dr in domain_results:
        for cap, s in zip(dr.capabilities, dr.scores):
            if s == 1:
                all_gaps.append(f"[{dr.label}] {cap}")
    top_priorities = all_gaps[:5]

    return MaturityReport(
        org=org,
        assessor=assessor,
        date=date,
        total_score=score_100,
        maturity_level=maturity_level,
        maturity_description=maturity_description,
        domains=domain_results,
        top_priorities=top_priorities,
    )


# ---------------------------------------------------------------------------
# Report formatting
# ---------------------------------------------------------------------------

def spark(score: float, max_score: float = 20, width: int = 10) -> str:
    filled = int(score / max_score * width)
    return "▓" * filled + "░" * (width - filled)


def generate_markdown(r: MaturityReport) -> str:
    lines = [
        f"# AI Governance Maturity Report — {r.org}",
        f"> Assessor: {r.assessor} | Date: {r.date} | Generated: {datetime.now().strftime('%Y-%m-%d')}",
        "",
        "---",
        "",
        "## Executive Summary",
        "",
        f"**Maturity level: {r.maturity_level}** (Score: {r.total_score} / 100)",
        "",
        f"> {r.maturity_description}",
        "",
        "| Domain | Score | Bar | Level |",
        "|--------|-------|-----|-------|",
    ]

    for dr in r.domains:
        level = MATURITY_LABELS.get(round(dr.avg_score), "—")
        lines.append(f"| {dr.label} | {dr.total_score}/20 | {spark(dr.total_score)} | {level} |")

    lines += [
        f"| **Total** | **{r.total_score}/100** | {spark(r.total_score, 100, 20)} | **{r.maturity_level}** |",
        "",
        "---",
        "",
    ]

    if r.top_priorities:
        lines += ["## Top Immediate Priorities (Score = 1)", ""]
        for p in r.top_priorities:
            lines.append(f"- 🔴 {p}")
        lines += ["", "---", ""]

    lines += ["## Domain Detail", ""]

    for dr in r.domains:
        lines += [
            f"### {dr.label} — {dr.total_score}/20 ({MATURITY_LABELS.get(round(dr.avg_score), '—')})",
            "",
            "| Capability | Score | Level |",
            "|-----------|-------|-------|",
        ]
        for cap, s in zip(dr.capabilities, dr.scores):
            lines.append(f"| {cap} | {s}/4 | {MATURITY_LABELS[s]} |")

        if dr.strengths:
            lines += ["", "**Strengths:**"]
            for s in dr.strengths:
                lines.append(f"- ✅ {s}")

        if dr.gaps:
            lines += ["", "**Gaps requiring attention:**"]
            for g in dr.gaps:
                lines.append(f"- ⚠️  {g}")

        if dr.roadmap:
            lines += ["", "**Recommended 90-day actions:**"]
            for item in dr.roadmap:
                lines.append(f"- {item}")

        lines.append("")

    lines += [
        "---",
        "",
        "## 90-Day Roadmap Summary",
        "",
        "| Priority | Domain | Action | Timeline |",
        "|----------|--------|--------|----------|",
    ]

    priority = 1
    for dr in sorted(r.domains, key=lambda x: x.total_score):
        for item in dr.roadmap[:2]:
            parts = item.rsplit("—", 1)
            action = parts[0].strip()
            timeline = parts[1].strip() if len(parts) > 1 else "Days 1–90"
            lines.append(f"| {priority} | {dr.label} | {action} | {timeline} |")
            priority += 1
            if priority > 10:
                break
        if priority > 10:
            break

    lines += [
        "",
        "---",
        "",
        "## Suggested Next Steps",
        "",
        "1. Share this report with the AI risk owner and executive sponsor",
        "2. Convene a working session to validate gaps and assign owners",
        "3. Schedule re-assessment in 90 days to measure progress",
        "4. Reference [maturity-scorecard.md](../assessments/maturity-scorecard.md) for detailed control criteria",
        "",
        "---",
        "",
        "*Generated by [ai-governance-toolkit](https://github.com/YOUR_USERNAME/ai-governance-toolkit) | Apache 2.0*",
    ]

    return "\n".join(lines)


# ---------------------------------------------------------------------------
# Interactive mode
# ---------------------------------------------------------------------------

def run_interactive():
    print("\n=== AI Governance Maturity Report Generator ===\n")
    org = input("Organization name: ").strip() or "My Organization"
    assessor = input("Assessor name: ").strip() or "Anonymous"
    date = input(f"Assessment date [{datetime.now().strftime('%Y-%m-%d')}]: ").strip() or datetime.now().strftime('%Y-%m-%d')

    scores_by_domain = {}
    print("\nScore each capability from 1 (Initial) to 4 (Optimized).\n")

    for d in DOMAINS:
        print(f"\n--- {d['label']} ---")
        domain_scores = []
        for cap in d["capabilities"]:
            while True:
                val = input(f"  {cap} [1–4]: ").strip()
                if val in ("1", "2", "3", "4"):
                    domain_scores.append(int(val))
                    break
                print("  Enter 1, 2, 3, or 4")
        scores_by_domain[d["key"]] = domain_scores

    return org, assessor, date, scores_by_domain


# ---------------------------------------------------------------------------
# CLI
# ---------------------------------------------------------------------------

def main():
    parser = argparse.ArgumentParser(description="AI Maturity Report Generator — ai-governance-toolkit")
    parser.add_argument("--interactive", action="store_true")
    parser.add_argument("--json", metavar="FILE")
    parser.add_argument("--org", metavar="NAME", default="")
    parser.add_argument("--assessor", metavar="NAME", default="")
    parser.add_argument("--output", metavar="FILE")
    args = parser.parse_args()

    if args.json:
        with open(args.json) as f:
            data = json.load(f)
        org = args.org or data.get("org", "Organization")
        assessor = args.assessor or data.get("assessor", "Anonymous")
        date = data.get("date", datetime.now().strftime("%Y-%m-%d"))
        scores_by_domain = data.get("scores", {})
    elif args.interactive or len(sys.argv) == 1:
        org, assessor, date, scores_by_domain = run_interactive()
    else:
        parser.print_help()
        sys.exit(1)

    result = analyze(org, assessor, date, scores_by_domain)
    report = generate_markdown(result)

    if args.output:
        with open(args.output, "w", encoding="utf-8") as f:
            f.write(report)
        print(f"Report written to {args.output}")
    else:
        print("\n" + report)


if __name__ == "__main__":
    main()
