from dataclasses import dataclass

from split import Split
from stats import Stats


@dataclass
class Timeframe:
    """Dataclass holding stats from a certain timeframe"""

    total: Stats
    vs_lhp: Split
    vs_rhp: Split
