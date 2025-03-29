from dataclasses import dataclass


@dataclass
class Matchup:
    """Class holding matchup data."""

    home_team: str
    pitcher_handedness: str
    pitcher_era: float
