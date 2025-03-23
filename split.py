from dataclasses import dataclass

from stats import Stats


@dataclass
class Split:
    """A class holding stats for home, away and both when facing a pitcher of
    certain handedness."""

    total: Stats
    home: Stats
    away: Stats
