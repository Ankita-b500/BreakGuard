import sys
import os

sys.path.append(
    os.path.abspath(
        os.path.join(os.path.dirname(__file__), "..", "src")
    )
)

from risk_scorer import calculate_risk


def test_low_risk():

    result = calculate_risk(
        changed_functions=["foo"],
        affected_files=["a.py"],
        untested_files=[],
        breaking_changes=[],
    )

    assert result.level == "LOW"


def test_medium_risk():

    result = calculate_risk(
        changed_functions=["a", "b"],
        affected_files=["a.py", "b.py", "c.py"],
        untested_files=["b.py"],
        breaking_changes=[],
    )

    assert result.level == "MEDIUM"


def test_high_risk():

    result = calculate_risk(
        changed_functions=["a", "b", "c"],
        affected_files=[
            "1.py",
            "2.py",
            "3.py",
            "4.py",
            "5.py",
        ],
        untested_files=[
            "1.py",
            "2.py",
            "3.py",
        ],
        breaking_changes=[
            "signature",
            "removed method",
        ],
    )

    assert result.level == "HIGH"