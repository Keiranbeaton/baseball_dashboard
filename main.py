"""Main module to run the baseball dashboard application."""

from teams_list import build_list
from url_calls import get_full_season, get_park_factors, get_three_weeks, get_matchups


def main():
    """Main function to start the application."""

    teams = build_list()

    for team in teams:
        for park in get_park_factors():
            if team.name == park["name"]:
                team.set_park_factor(float(park["factor"]))

        for data in get_three_weeks(2):
            if team.abbrev == data["name"]:
                team.recent.set_lhp(data["stats"])

        for data in get_three_weeks(1):
            if team.abbrev == data["name"]:
                team.recent.set_rhp(data["stats"])

        for data in get_full_season(2):
            if team.abbrev == data["name"]:
                team.full.set_lhp(data["stats"])

        for data in get_full_season(1):
            if team.abbrev == data["name"]:
                team.full.set_rhp(data["stats"])
        
        for matchup in get_matchups():
            if team.abbrev == matchup["abbrev"]:
                for m in matchup["matchups"]:
                    

main()