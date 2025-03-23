from dataclasses import dataclass


@dataclass
class Matchup:
    """Class holding matchup data."""

    park: str
    pitcher_handedness: str
    pitcher_era: float
