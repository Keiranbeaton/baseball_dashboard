"""Team class file"""

from timeframe import Timeframe


class Team:
    """A class representing a team and storing split stats."""

    def __init__(self, name, abbrev):
        self.name = name
        self.abbrev = abbrev
        self.park_factor = 0
        self.schedule = []
        self.full = Timeframe()
        self.recent = Timeframe()
