"""Split stats class module"""


class Split:
    """Split class that stores the stats a team has for a given split"""

    def __init__(self, wrc, bb, k, babip):
        self.wrc = wrc
        self.kbb = k - bb
        self.babip = babip
