"""Matchup class module"""

from teams import Team
from pitcher import Pitcher


class Matchup:
    """Class holding matchup data."""

    def __init__(self, date):
        self.date = date
        self.park_factor = 0
        self.pitcher = Pitcher("N/A", "N/A")
        self.opponent = Team("N/A", "N/A")
        self.team = Team("N/A", "N/A")

    def set_park(self, park):
        """Function to set park_factor attribute for a matchup."""
        self.park_factor = park

    def set_pitcher(self, pitcher):
        """Function to set pitcher attribute for a matchup."""
        self.pitcher = pitcher

    def set_opponent(self, opp):
        """Function to set opponent attribute for a matchup."""
        self.opponent = opp

    def set_team(self, team):
        """Function to set team attribute for a matchup."""
        self.team = team
