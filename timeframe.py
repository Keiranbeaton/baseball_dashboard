"""Timeframe Class"""

from split import Split


class Timeframe:
    """Timeframe class that will hold team statistics over a certain period of
    time."""

    def __init__(self):
        self.total = Split(0, 0, 0, 0)
        self.rhp = Split(0, 0, 0, 0)
        self.lhp = Split(0, 0, 0, 0)

    def set_total(self, stat_obj):
        """function that sets total equal to the stat_obj being passed in."""
        self.total = stat_obj

    def set_rhp(self, stat_obj):
        """function that sets rhp equal to the stat_obj being passed in."""
        self.rhp = stat_obj

    def set_lhp(self, stat_obj):
        """Function that sets lhp equal to the stat_obj being passed in."""
        self.lhp = stat_obj
