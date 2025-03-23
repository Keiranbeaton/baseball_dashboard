from dataclasses import dataclass

from timeframe import Timeframe


@dataclass
class Team:
    """A class representing a team and storing split stats."""

    name: str
    park: str
    full_season: Timeframe
    last_three: Timeframe
