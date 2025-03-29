"""Team class file"""

from dataclasses import dataclass


@dataclass
class Team:
    """A class representing a team and storing split stats."""

    name: str
    abbrev: str
    full_season: dict
    last_three: dict

    def add_stats(self, end_date, split, stat_dict):
        """function that takes in a given duration and split value and
        the sets the correct dictionary field equal to the stats passed in"""

        if end_date == "2025-11-01":
            if split == "":
                self.full_season["total"] = stat_dict
            elif split == "1":
                self.full_season["rhp"]["total"] = stat_dict
            elif split == "2":
                self.full_season["lhp"]["total"] = stat_dict
            elif split == "1,7":
                self.full_season["rhp"]["home"] = stat_dict
            elif split == "1,8":
                self.full_season["rhp"]["away"] = stat_dict
            elif split == "2,7":
                self.full_season["lhp"]["home"] = stat_dict
            elif split == "2,8":
                self.full_season["lhp"]["away"] = stat_dict
            else:
                print(f"Did not Match split for {self.name} and split: {split}")
