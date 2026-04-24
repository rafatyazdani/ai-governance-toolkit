#!/usr/bin/env python3
"""
ai-governance-toolkit: risk_scorer.py
-------------------------------------
Scores an AI use case for governance risk based on key attributes.
Produces a risk tier classification, control recommendations,
and an estimated Annualized Loss Expectancy (ALE) range.

Usage:
    python risk_scorer.py --interactive
    python risk_scorer.py --json input.json
    python risk_scorer.py --output report.md

Requirements: See requirements.txt
"""

import argparse
import json
import sys
from dataclasses import dataclass, field, asdict
from typing import Optional
from datetime import datetime


# ---------------------------------------------------------------------------
# Data model
# ---------------------------------------------------------------------------

@dataclass
class UseCaseInput:
    name: str = ""
    uses_personal_data: bool = False
    uses_sensitive_data: bool = False          # health, biometric, financial, race, etc.
    affects_consequential_decisions: bool = False  # employment, credit, benefits, etc.
    regulated_domain: bool = False             # financial services, healthcare, legal, HR
    eu_market_exposure: bool = False
    human_in_loop: str = "full"                # full | partial | none
    third_party_model: bool = False
    estimated_monthly_affected_persons: int = 0
    estimated_financial_impact_usd: int = 0    # worst-case single-incident estimate
    autonomous_action: bool = False            # AI output triggers automated real-world action


@dataclass
class RiskScore:
    raw_score: int = 0
    tier: str = ""
    tier_label: str = ""
    ale_low_usd: int = 0
    ale_high_usd: int = 0
    control_requirements: list = field(default_factory=list)
    regulatory_flags: list = field(default_factory=list)
    notes: list = field(default_factory=list)


# ---------------------------------------------------------------------------
# Scoring engine
# ---------------------------------------------------------------------------

TIER_THRESHOLDS = {
    "critical": 15,
    "high": 9,
    "medium": 4,
    "low": 0,
}

TIER_LABELS = {
    "critical": "CRITICAL — Highest governance burden. Board-level visibility required.",
    "high":     "HIGH — Significant controls and monitoring required.",
    "medium":   "MEDIUM — Moderate controls. Human review present.",
    "low":      "LOW — Minimal governance required.",
}

# Annual probability of a significant incident by tier (for ALE)
TIER_INCIDENT_PROBABILITY = {
    "critical": 0.30,
    "high":     0.15,
    "medium":   0.05,
    "low":      0.01,
}

REQUIRED_CONTROLS = {
    "critical": [
        "Formal AI use case intake and board-level approval",
        "Human-in-the-loop review required for ALL outputs affecting individuals",
        "Bias and fairness testing before deployment and quarterly in production",
        "AI-specific red team / adversarial testing",
        "Explainability mechanism for all consequential outputs",
        "Full audit trail with individual-level logging",
        "EU AI Act high-risk conformity assessment (if EU-exposed)",
        "Post-market monitoring with automated drift alerting",
        "AI incident response runbook with ≤24hr escalation SLA",
        "Annual third-party audit or ISO 42001 certification",
    ],
    "high": [
        "AI use case intake and CISO/risk owner approval",
        "Human review for high-stakes or edge-case outputs",
        "Bias testing before deployment; semi-annual in production",
        "AI security assessment (prompt injection, model attacks)",
        "Audit trail for AI-influenced decisions",
        "Quarterly model performance review",
        "AI incident response procedures",
        "Vendor SOC 2 Type II and AI DDQ (if third-party)",
    ],
    "medium": [
        "AI use case intake and manager approval",
        "Human review present for consequential outputs",
        "Pre-deployment functional testing",
        "Semi-annual model performance review",
        "Basic audit logging",
        "Vendor security review (if third-party)",
    ],
    "low": [
        "Use case registration in AI inventory",
        "Annual review",
        "Basic output validation",
    ],
}


def score_use_case(uc: UseCaseInput) -> RiskScore:
    score = 0
    flags = []
    notes = []

    # Personal / sensitive data
    if uc.uses_sensitive_data:
        score += 4
        flags.append("Sensitive personal data in scope — privacy review required")
    elif uc.uses_personal_data:
        score += 2
        notes.append("Personal data in scope — DPA and data minimization required")

    # Decision impact
    if uc.affects_consequential_decisions:
        score += 4
        flags.append("Consequential individual decisions — human oversight controls mandatory")

    # Regulated domain
    if uc.regulated_domain:
        score += 3
        flags.append("Regulated domain — sector-specific AI requirements may apply")

    # EU exposure
    if uc.eu_market_exposure:
        score += 2
        flags.append("EU market exposure — EU AI Act obligations apply")

    # Human oversight
    if uc.human_in_loop == "none":
        score += 4
        flags.append("No human-in-the-loop — highest automation risk")
    elif uc.human_in_loop == "partial":
        score += 2
        notes.append("Partial human oversight — define clear escalation criteria")

    # Autonomous action
    if uc.autonomous_action:
        score += 3
        flags.append("AI output triggers automated real-world action — failure blast radius is high")

    # Third-party model
    if uc.third_party_model:
        score += 1
        notes.append("Third-party model — vendor AI DDQ required")

    # Scale
    if uc.estimated_monthly_affected_persons > 1_000_000:
        score += 3
        notes.append("Scale >1M persons/month — societal impact assessment recommended")
    elif uc.estimated_monthly_affected_persons > 10_000:
        score += 1

    # Determine tier
    if score >= TIER_THRESHOLDS["critical"]:
        tier = "critical"
    elif score >= TIER_THRESHOLDS["high"]:
        tier = "high"
    elif score >= TIER_THRESHOLDS["medium"]:
        tier = "medium"
    else:
        tier = "low"

    # ALE calculation
    base_impact = uc.estimated_financial_impact_usd if uc.estimated_financial_impact_usd > 0 else _default_impact(tier)
    prob = TIER_INCIDENT_PROBABILITY[tier]
    ale = int(base_impact * prob)
    ale_low = int(ale * 0.5)
    ale_high = int(ale * 2.0)

    return RiskScore(
        raw_score=score,
        tier=tier,
        tier_label=TIER_LABELS[tier],
        ale_low_usd=ale_low,
        ale_high_usd=ale_high,
        control_requirements=REQUIRED_CONTROLS[tier],
        regulatory_flags=flags,
        notes=notes,
    )


def _default_impact(tier: str) -> int:
    defaults = {"critical": 10_000_000, "high": 2_000_000, "medium": 250_000, "low": 25_000}
    return defaults[tier]


# ---------------------------------------------------------------------------
# Report generation
# ---------------------------------------------------------------------------

def format_usd(n: int) -> str:
    if n >= 1_000_000:
        return f"${n/1_000_000:.1f}M"
    if n >= 1_000:
        return f"${n/1_000:.0f}K"
    return f"${n}"


def generate_markdown_report(uc: UseCaseInput, result: RiskScore) -> str:
    now = datetime.now().strftime("%Y-%m-%d %H:%M")
    lines = [
        f"# AI Risk Assessment — {uc.name or 'Unnamed Use Case'}",
        f"> Generated: {now} | Tool: ai-governance-toolkit/risk_scorer.py",
        "",
        "---",
        "",
        "## Risk Tier",
        "",
        f"**{result.tier.upper()}** — Score: {result.raw_score}",
        "",
        f"> {result.tier_label}",
        "",
        "---",
        "",
        "## Financial Exposure (ALE Estimate)",
        "",
        f"| Metric | Value |",
        f"|--------|-------|",
        f"| Annualized Loss Expectancy (low) | {format_usd(result.ale_low_usd)} |",
        f"| Annualized Loss Expectancy (high) | {format_usd(result.ale_high_usd)} |",
        f"| Incident probability (annual) | {TIER_INCIDENT_PROBABILITY[result.tier]*100:.0f}% |",
        f"| Estimated single-incident impact | {format_usd(uc.estimated_financial_impact_usd or _default_impact(result.tier))} |",
        "",
        "*ALE = Annualized Loss Expectancy. Low/high range reflects uncertainty in incident probability and impact.*",
        "",
        "---",
        "",
    ]

    if result.regulatory_flags:
        lines += ["## Regulatory and Risk Flags", ""]
        for flag in result.regulatory_flags:
            lines.append(f"- ⚠️  {flag}")
        lines.append("")
        lines.append("---")
        lines.append("")

    if result.notes:
        lines += ["## Additional Notes", ""]
        for note in result.notes:
            lines.append(f"- {note}")
        lines.append("")
        lines.append("---")
        lines.append("")

    lines += ["## Required Controls", ""]
    for i, ctrl in enumerate(result.control_requirements, 1):
        lines.append(f"{i}. {ctrl}")
    lines += [
        "",
        "---",
        "",
        "## Next Steps",
        "",
        f"1. Submit [AI Use Case Intake Form](../templates/use-case-intake.md) if not already completed",
        f"2. Assign a named AI system owner",
        f"3. Implement required controls above before go-live",
        f"4. Schedule first monitoring review per {result.tier.upper()} tier cadence",
        "",
        "---",
        "",
        "*Generated by [ai-governance-toolkit](https://github.com/YOUR_USERNAME/ai-governance-toolkit) | Apache 2.0*",
    ]
    return "\n".join(lines)


# ---------------------------------------------------------------------------
# Interactive mode
# ---------------------------------------------------------------------------

def ask(prompt: str, default: str = "") -> str:
    suffix = f" [{default}]" if default else ""
    val = input(f"{prompt}{suffix}: ").strip()
    return val if val else default


def ask_bool(prompt: str) -> bool:
    val = ask(f"{prompt} (y/n)", "n").lower()
    return val in ("y", "yes", "1", "true")


def ask_choice(prompt: str, choices: list, default: str) -> str:
    opts = "/".join(choices)
    val = ask(f"{prompt} ({opts})", default).lower()
    return val if val in choices else default


def run_interactive() -> UseCaseInput:
    print("\n=== AI Use Case Risk Scorer ===\n")
    uc = UseCaseInput()
    uc.name = ask("Use case name")
    uc.uses_personal_data = ask_bool("Does it process personal data?")
    if uc.uses_personal_data:
        uc.uses_sensitive_data = ask_bool("Does it process SENSITIVE personal data (health, biometric, financial, race)?")
    uc.affects_consequential_decisions = ask_bool("Does it influence consequential decisions about individuals (employment, credit, benefits)?")
    uc.regulated_domain = ask_bool("Is this in a regulated domain (finance, healthcare, legal, HR)?")
    uc.eu_market_exposure = ask_bool("Is the system used in or affecting persons in the EU?")
    uc.human_in_loop = ask_choice("Human oversight level", ["full", "partial", "none"], "partial")
    uc.autonomous_action = ask_bool("Does the AI output trigger automated real-world actions (no human step)?")
    uc.third_party_model = ask_bool("Does it use a third-party AI model or API?")
    persons_str = ask("Estimated monthly affected persons (0 if internal only)", "0")
    uc.estimated_monthly_affected_persons = int(persons_str) if persons_str.isdigit() else 0
    impact_str = ask("Estimated worst-case single incident financial impact in USD (0 to use default)", "0")
    uc.estimated_financial_impact_usd = int(impact_str) if impact_str.isdigit() else 0
    return uc


# ---------------------------------------------------------------------------
# CLI
# ---------------------------------------------------------------------------

def main():
    parser = argparse.ArgumentParser(description="AI Use Case Risk Scorer — ai-governance-toolkit")
    parser.add_argument("--interactive", action="store_true", help="Run interactive questionnaire")
    parser.add_argument("--json", metavar="FILE", help="Load use case from JSON file")
    parser.add_argument("--output", metavar="FILE", help="Write markdown report to file (default: stdout)")
    args = parser.parse_args()

    if args.json:
        with open(args.json) as f:
            data = json.load(f)
        uc = UseCaseInput(**data)
    elif args.interactive or not any(vars(args).values()):
        uc = run_interactive()
    else:
        parser.print_help()
        sys.exit(1)

    result = score_use_case(uc)
    report = generate_markdown_report(uc, result)

    if args.output:
        with open(args.output, "w") as f:
            f.write(report)
        print(f"Report written to {args.output}")
    else:
        print("\n" + report)


if __name__ == "__main__":
    main()
