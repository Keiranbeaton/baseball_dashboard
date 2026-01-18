"""Split stats class module"""


class Split:
    """Split class that stores the stats a team has for a given split"""

    def __init__(self, stats_object):
        self.wrc = stats_object["wrc"]
        self.kbb = stats_object["k"] - stats_object["bb"]
        self.babip = stats_object["babip"]
