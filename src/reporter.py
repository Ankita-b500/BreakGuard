"""
Stage 4
Reporter

Generates a Markdown report from the calculated risk.
"""

from pathlib import Path
from models import RiskResult


class Reporter:
    """Generates a Markdown risk report."""

    def generate(self, result: RiskResult, output_file="risk_report.md"):
        report = f"""# BreakGuard Risk Report

## Overall Risk

- **Risk Level:** {result.level}
- **Risk Score:** {result.score}
- **Blast Radius:** {result.blast_radius}

## Test Coverage

- Tested Calls: {result.tested_calls}
- Untested Calls: {result.untested_calls}

## Summary

{result.summary}
"""

        Path(output_file).write_text(report, encoding="utf-8")

        return report