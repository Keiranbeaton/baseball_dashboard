"""Module for putting together a list of teams and their home parks"""

from teams import Team


def build_list():
    """Function that returns a list of all mlb teams as a Team class object."""
    team_list = []
    team_list.append(Team("Angels", "LAA"))
    team_list.append(Team("Astros", "HOU"))
    team_list.append(Team("Athletics", "OAK"))
    team_list.append(Team("Blue Jays", "TOR"))
    team_list.append(Team("Braves", "ATL"))
    team_list.append(Team("Brewers", "MIL"))
    team_list.append(Team("Cardinals", "STL"))
    team_list.append(Team("Cubs", "CHC"))
    team_list.append(Team("D-Backs", "ARI"))
    team_list.append(Team("Dodgers", "LAD"))
    team_list.append(Team("Giants", "SFG"))
    team_list.append(Team("Guardians", "CLE"))
    team_list.append(Team("Mariners", "SEA"))
    team_list.append(Team("Marlins", "MIA"))
    team_list.append(Team("Mets", "NYM"))
    team_list.append(Team("Nationals", "WSH"))
    team_list.append(Team("Orioles", "BAL"))
    team_list.append(Team("Padres", "SDP"))
    team_list.append(Team("Phillies", "PHI"))
    team_list.append(Team("Pirates", "PIT"))
    team_list.append(Team("Rangers", "TEX"))
    team_list.append(Team("Rays", "TBR"))
    team_list.append(Team("Red Sox", "BOS"))
    team_list.append(Team("Reds", "CIN"))
    team_list.append(Team("Rockies", "COL"))
    team_list.append(Team("Royals", "KCR"))
    team_list.append(Team("Tigers", "DET"))
    team_list.append(Team("Twins", "MIN"))
    team_list.append(Team("White Sox", "CWS"))
    team_list.append(Team("Yankees", "NYY"))
    return team_list


def get_team_by_abbrev(abbrev):
    """Function that takes in a team abbreviation and returns the Team object."""
    teams = build_list()
    for team in teams:
        if team.abbrev == abbrev:
            return team
    return None
