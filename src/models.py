from dataclasses import dataclass
from typing import List


@dataclass
class RiskResult:
    score: int
    level: str
    blast_radius: int
    tested_calls: int
    untested_calls: int
    summary: str