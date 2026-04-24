#!/usr/bin/env python3
"""
ai-governance-toolkit: vendor_screen.py
----------------------------------------
Automates AI vendor screening based on the vendor DDQ.
Scores responses across six domains and produces a
pass/conditional/fail recommendation with gap analysis.

Usage:
    python vendor_screen.py --interactive
    python vendor_screen.py --json vendor_responses.json
    python vendor_screen.py --output vendor_report.md

Requirements: See requirements.txt
"""

import argparse
import json
import sys
from dataclasses import dataclass, field
from datetime import datetime
from typing import List


# ---------------------------------------------------------------------------
# Scoring model
# ---------------------------------------------------------------------------

DOMAINS = {
    "data_handling": {
        "label": "Data handling",
        "weight": 25,
        "questions": [
            ("Customer data not used for training by default", 8),
            ("Data residency controls meet requirements", 5),
            ("Data retention policy documented and enforced", 5),
            ("Customer data deletion on request supported", 7),
        ],
    },
    "security": {
        "label": "Security",
        "weight": 25,
        "questions": [
            ("SOC 2 Type II report current (within 12 months)", 10),
            ("AI-specific security testing conducted (prompt injection, adversarial)", 8),
            ("AI incident notification SLA ≤ 72 hours", 4),
            ("Responsible disclosure / bug bounty program exists", 3),
        ],
    },
    "model_governance": {
        "label": "Model governance",
        "weight": 20,
        "questions": [
            ("Model validation process documented", 5),
            ("Model drift monitoring in production", 5),
            ("Customer notification on significant model changes", 4),
            ("Bias and fairness testing conducted", 6),
        ],
    },
    "transparency": {
        "label": "Transparency",
        "weight": 10,
        "questions": [
            ("Model card or system card available", 5),
            ("Known limitations and failure modes documented", 5),
        ],
    },
    "human_oversight": {
        "label": "Human oversight",
        "weight": 10,
        "questions": [
            ("Human-in-the-loop configurable for high-stakes outputs", 5),
            ("Override / correction mechanism available", 5),
        ],
    },
    "regulatory": {
        "label": "Regulatory & compliance",
        "weight": 10,
        "questions": [
            ("EU AI Act readiness assessment completed", 4),
            ("AI governance program or function exists", 3),
            ("Published AI ethics policy available", 3),
        ],
    },
}

PASS_THRESHOLD = 75
CONDITIONAL_THRESHOLD = 55


@dataclass
class DomainResult:
    domain_key: str
    label: str
    weight: int
    raw_score: float = 0.0     # 0–100 within domain
    weighted_score: float = 0.0
    gaps: List[str] = field(default_factory=list)
    responses: dict = field(default_factory=dict)


@dataclass
class VendorScreenResult:
    vendor_name: str
    tier: str
    total_score: float
    recommendation: str
    domains: List[DomainResult] = field(default_factory=list)
    blockers: List[str] = field(default_factory=list)
    conditions: List[str] = field(default_factory=list)


# ---------------------------------------------------------------------------
# Screening engine
# ---------------------------------------------------------------------------

def screen_vendor(vendor_name: str, tier: str, responses: dict) -> VendorScreenResult:
    """
    responses: dict keyed by domain_key, then question index (0-based) → True/False/None
    tier: "high" | "medium" | "low" — high-tier vendors require stricter scoring
    """
    domain_results = []
    total_weighted = 0.0
    blockers = []
    conditions = []

    for domain_key, config in DOMAINS.items():
        domain_resp = responses.get(domain_key, {})
        domain_max = sum(pts for _, pts in config["questions"])
        domain_earned = 0
        gaps = []

        for i, (q_label, pts) in enumerate(config["questions"]):
            answer = domain_resp.get(str(i), None)
            if answer is True:
                domain_earned += pts
            elif answer is False:
                gaps.append(q_label)
            # None = unknown / not answered → partial credit (50%) for low-tier, 0 for high
            elif answer is None:
                if tier == "low":
                    domain_earned += pts * 0.5
                gaps.append(f"{q_label} (not confirmed)")

        raw_pct = (domain_earned / domain_max * 100) if domain_max else 0
        weighted = raw_pct * config["weight"] / 100

        dr = DomainResult(
            domain_key=domain_key,
            label=config["label"],
            weight=config["weight"],
            raw_score=raw_pct,
            weighted_score=weighted,
            gaps=gaps,
            responses=domain_resp,
        )
        domain_results.append(dr)
        total_weighted += weighted

    # Determine recommendation
    if total_weighted >= PASS_THRESHOLD:
        recommendation = "APPROVE"
    elif total_weighted >= CONDITIONAL_THRESHOLD:
        recommendation = "APPROVE WITH CONDITIONS"
    else:
        recommendation = "DO NOT APPROVE"

    # Hard blockers regardless of score
    sec_domain = next(d for d in domain_results if d.domain_key == "security")
    soc2_answered = responses.get("security", {}).get("0", None)
    if soc2_answered is False:
        blockers.append("No current SOC 2 Type II — procurement should not proceed without compensating assurance")
        if recommendation == "APPROVE":
            recommendation = "APPROVE WITH CONDITIONS"

    data_domain = next(d for d in domain_results if d.domain_key == "data_handling")
    training_data = responses.get("data_handling", {}).get("0", None)
    if training_data is False and tier == "high":
        blockers.append("Customer data used for training by default — contractual prohibition required before approval")
        recommendation = "APPROVE WITH CONDITIONS"

    # Auto-generate conditions for gaps
    for dr in domain_results:
        if dr.raw_score < 60:
            conditions.append(f"Vendor must remediate {dr.label} gaps before go-live: {'; '.join(dr.gaps[:3])}")

    return VendorScreenResult(
        vendor_name=vendor_name,
        tier=tier,
        total_score=round(total_weighted, 1),
        recommendation=recommendation,
        domains=domain_results,
        blockers=blockers,
        conditions=conditions,
    )


# ---------------------------------------------------------------------------
# Report generation
# ---------------------------------------------------------------------------

def bar(score: float, width: int = 20) -> str:
    filled = int(score / 100 * width)
    return "█" * filled + "░" * (width - filled)


def generate_markdown_report(result: VendorScreenResult) -> str:
    now = datetime.now().strftime("%Y-%m-%d %H:%M")
    rec_emoji = {"APPROVE": "✅", "APPROVE WITH CONDITIONS": "⚠️", "DO NOT APPROVE": "🚫"}
    emoji = rec_emoji.get(result.recommendation, "")

    lines = [
        f"# AI Vendor Screening Report — {result.vendor_name}",
        f"> Generated: {now} | Tier: {result.tier.upper()} | Tool: ai-governance-toolkit/vendor_screen.py",
        "",
        "---",
        "",
        "## Recommendation",
        "",
        f"### {emoji} {result.recommendation}",
        "",
        f"**Total score: {result.total_score} / 100**",
        "",
        "| Score | Meaning |",
        "|-------|---------|",
        "| 75–100 | Approve |",
        "| 55–74 | Approve with conditions |",
        "| <55 | Do not approve |",
        "",
        "---",
        "",
        "## Domain Scores",
        "",
        "| Domain | Score | Weight | Weighted | Bar |",
        "|--------|-------|--------|---------|-----|",
    ]

    for dr in result.domains:
        lines.append(
            f"| {dr.label} | {dr.raw_score:.0f}% | {dr.weight}% | {dr.weighted_score:.1f} | {bar(dr.raw_score, 15)} |"
        )

    lines += ["", "---", ""]

    if result.blockers:
        lines += ["## 🚫 Blockers (must resolve before approval)", ""]
        for b in result.blockers:
            lines.append(f"- {b}")
        lines += ["", "---", ""]

    if result.conditions:
        lines += ["## ⚠️  Conditions (required before go-live)", ""]
        for c in result.conditions:
            lines.append(f"- {c}")
        lines += ["", "---", ""]

    lines += ["## Gap Detail by Domain", ""]
    for dr in result.domains:
        if dr.gaps:
            lines.append(f"### {dr.label} ({dr.raw_score:.0f}%)")
            lines.append("")
            for g in dr.gaps:
                lines.append(f"- [ ] {g}")
            lines.append("")

    lines += [
        "---",
        "",
        "## Next Steps",
        "",
        "1. Share this report with the vendor and request remediation plan",
        "2. Re-screen after vendor provides evidence for flagged gaps",
        "3. Execute [Vendor AI DDQ](../templates/vendor-ddq.md) for full qualitative assessment",
        "4. Add to vendor risk register with review cadence",
        "",
        "---",
        "",
        "*Generated by [ai-governance-toolkit](https://github.com/YOUR_USERNAME/ai-governance-toolkit) | Apache 2.0*",
    ]

    return "\n".join(lines)


# ---------------------------------------------------------------------------
# Interactive mode
# ---------------------------------------------------------------------------

def ask_yn(prompt: str) -> bool | None:
    val = input(f"  {prompt} (y/n/skip): ").strip().lower()
    if val in ("y", "yes"):
        return True
    if val in ("n", "no"):
        return False
    return None  # skip / unknown


def run_interactive() -> tuple[str, str, dict]:
    print("\n=== AI Vendor Screening Tool ===\n")
    vendor_name = input("Vendor name: ").strip() or "Unknown Vendor"
    tier = input("Engagement tier (high/medium/low) [high]: ").strip().lower() or "high"
    if tier not in ("high", "medium", "low"):
        tier = "high"

    responses = {}
    print("\nAnswer each question based on vendor evidence. 'skip' = not yet confirmed.\n")

    for domain_key, config in DOMAINS.items():
        print(f"\n--- {config['label']} ---")
        domain_resp = {}
        for i, (q_label, pts) in enumerate(config["questions"]):
            answer = ask_yn(f"[{pts} pts] {q_label}")
            domain_resp[str(i)] = answer
        responses[domain_key] = domain_resp

    return vendor_name, tier, responses


# ---------------------------------------------------------------------------
# CLI
# ---------------------------------------------------------------------------

def main():
    parser = argparse.ArgumentParser(description="AI Vendor Screener — ai-governance-toolkit")
    parser.add_argument("--interactive", action="store_true", help="Run interactive questionnaire")
    parser.add_argument("--vendor", metavar="NAME", help="Vendor name (used with --json)")
    parser.add_argument("--tier", choices=["high", "medium", "low"], default="high")
    parser.add_argument("--json", metavar="FILE", help="Load responses from JSON")
    parser.add_argument("--output", metavar="FILE", help="Write report to file")
    args = parser.parse_args()

    if args.json:
        with open(args.json) as f:
            data = json.load(f)
        vendor_name = args.vendor or data.get("vendor_name", "Unknown Vendor")
        tier = args.tier or data.get("tier", "high")
        responses = data.get("responses", {})
    elif args.interactive or len(sys.argv) == 1:
        vendor_name, tier, responses = run_interactive()
    else:
        parser.print_help()
        sys.exit(1)

    result = screen_vendor(vendor_name, tier, responses)
    report = generate_markdown_report(result)

    if args.output:
        with open(args.output, "w") as f:
            f.write(report)
        print(f"Report written to {args.output}")
    else:
        print("\n" + report)


if __name__ == "__main__":
    main()
