"""Module for putting together a list of teams and their home parks"""

from teams import Team


def team_factory(name, abbrev):
    """Function that accepts a name string and an abbreviation string
    and returns a Team class object with those properties"""
    return Team(name, abbrev, {}, {})


def build_list():
    """Function that returns a list of all mlb teams as a Team class object."""
    team_list = []
    team_list.append(team_factory("Angels", "LAA"))
    team_list.append(team_factory("Astros", "HOU"))
    team_list.append(team_factory("Athletics", "OAK"))
    team_list.append(team_factory("Blue Jays", "TOR"))
    team_list.append(team_factory("Braves", "ATL"))
    team_list.append(team_factory("Brewers", "MIL"))
    team_list.append(team_factory("Cardinals", "STL"))
    team_list.append(team_factory("Cubs", "CHC"))
    team_list.append(team_factory("D-Backs", "ARI"))
    team_list.append(team_factory("Dodgers", "LAD"))
    team_list.append(team_factory("Giants", "SFG"))
    team_list.append(team_factory("Guardians", "CLE"))
    team_list.append(team_factory("Mariners", "SEA"))
    team_list.append(team_factory("Marlins", "MIA"))
    team_list.append(team_factory("Mets", "NYM"))
    team_list.append(team_factory("Nationals", "WSH"))
    team_list.append(team_factory("Orioles", "BAL"))
    team_list.append(team_factory("Padres", "SDP"))
    team_list.append(team_factory("Phillies", "PHI"))
    team_list.append(team_factory("Pirates", "PIT"))
    team_list.append(team_factory("Rangers", "TEX"))
    team_list.append(team_factory("Rays", "TBR"))
    team_list.append(team_factory("Red Sox", "BOS"))
    team_list.append(team_factory("Reds", "CIN"))
    team_list.append(team_factory("Rockies", "COL"))
    team_list.append(team_factory("Royals", "KCR"))
    team_list.append(team_factory("Tigers", "DET"))
    team_list.append(team_factory("Twins", "MIN"))
    team_list.append(team_factory("White Sox", "CWS"))
    team_list.append(team_factory("Yankees", "NYY"))
    return team_list
