"""Pitcher Class to represent a probable starter"""


class Pitcher:
    """Pitcher Class holding name and throwing hand. May add some statistics
    later."""

    def __init__(self, name, hand):
        self.name = name
        self.hand = hand
