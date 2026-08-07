"""
Stage 3
Risk Scorer
"""

from models import RiskResult


def calculate_risk(
    changed_functions,
    affected_files,
    untested_files,
    breaking_changes,
):
    """
    Calculates project risk based on:

    - changed functions
    - affected files
    - missing tests
    - breaking API changes
    """

    score = 0

    score += len(changed_functions) * 5
    score += len(affected_files) * 10
    score += len(untested_files) * 20
    score += len(breaking_changes) * 25

    if score >= 80:
        level = "HIGH"
    elif score >= 40:
        level = "MEDIUM"
    else:
        level = "LOW"

    return RiskResult(
        score=score,
        level=level,
        blast_radius=len(affected_files),
        tested_calls=max(
            len(affected_files) - len(untested_files),
            0
        ),
        untested_calls=len(untested_files),
        summary=f"{level} risk with blast radius of {len(affected_files)} files.",
    )