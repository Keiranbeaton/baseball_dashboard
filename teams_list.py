"""Module for putting together a list of teams and their home parks"""
from teams import Team

def team_factory(name, abbrev, park):
    return Team(name, abbrev, park, {}, {})

def build_list():
    team_list = []
    team_list.append(team_factory("Angels", "LAA", "Angel Stadium"))
    team_list.append(team_factory("Astros", "HOU", "Minute Maid Park"))
    team_list.append(team_factory("Athletics", "OAK", ""))
    team_list.append(team_factory("Blue Jays", "TOR", "Rogers Centre"))
    team_list.append(team_factory("Braves", "ATL", "Truist Park"))
    team_list.append(team_factory("Brewers", "MIL", "American Family Field"))
    team_list.append(team_factory("Cardinals", "STL", "Busch Stadium"))
    team_list.append(team_factory("Cubs", "CHC", "Wrigley Field"))
    team_list.append(team_factory("D-Backs", "ARI", "Chase Field"))
    team_list.append(team_factory("Dodgers", "LAD","Dodger Stadium"))
    team_list.append(team_factory("Giants", "SFG", "Oracle Park"))
    team_list.append(team_factory("Guardians", "CLE", "Progressive Field"))
    team_list.append(team_factory("Mariners", "SEA", "T-Mobile Park"))
    team_list.append(team_factory("Marlins", "MIA", "LoanDepot Park"))
    team_list.append(team_factory("Mets", "NYM", "Citi Field"))
    team_list.append(team_factory("Nationals", "WSH", "Nationals Park"))
    team_list.append(team_factory("Orioles", "BAL", "Oriole Park at Camden Yards"))
    team_list.append(team_factory("Padres", "SDP", "Petco Park"))
    team_list.append(team_factory("Phillies", "PHI", "Citizens Bank Park"))
    team_list.append(team_factory("Pirates", "PIT", "PNC Park"))
    team_list.append(team_factory("Rangers","TEX", "Globe Life Field"))
    team_list.append(team_factory("Rays", "TBR", "Tropicana Field"))
    team_list.append(team_factory("Red Sox", "BOS", "Fenway Park"))
    team_list.append(team_factory("Reds", "CIN", "Great American Ball Park"))
    team_list.append(team_factory("Rockies", "COL", "Coors Field"))
    team_list.append(team_factory("Royals", "KCR", "Kauffman Stadium"))
    team_list.append(team_factory("Tigers", "DET", "Comerica Park"))
    team_list.append(team_factory("Twins", "MIN", "Target Field"))
    team_list.append(team_factory("White Sox", "CWS", "Guaranteed Rate Field"))
    team_list.append(team_factory("Yankees", "NYY", "Yankee Stadium"))
    return team_list