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

        def add_matchup(self, matchup):
            """function for pushing matchup to schedule list"""
            self.schedule.append(matchup)

        def set_park_factor(self, park):
            """Function to set the park factor for a team."""
            self.park_factor = park

        def set_full(self, timeframe):
            """Function to set the full season timeframe for a team."""
            self.full = timeframe

        def set_recent(self, timeframe):
            """Function to set the recent timeframe for a team."""
            self.recent = timeframe
