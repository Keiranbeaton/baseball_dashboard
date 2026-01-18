"""Module for opening webpages with selenium and returning data from therein"""

from datetime import datetime, timedelta, date

from selenium import webdriver
from selenium.webdriver.common.by import By


from matchup import Matchup
from pitcher import Pitcher
from url_builders import fg_splits_page
from teams_list import get_team_by_abbrev, get_team_by_name


def get_stat_dicts(start_date, end_date, split):
    """Function that gets full season stats and returns a Stats tuple for each
    team listed.
    """
    driver = webdriver.Chrome()
    driver.implicitly_wait(10)
    url = fg_splits_page(start_date, end_date, f"{split}")
    driver.get(url)
    return_array = []
    try:
        rows = (
            driver.find_element(By.CLASS_NAME, "fg-data-grid")
            .find_element(By.TAG_NAME, "tbody")
            .find_elements(By.TAG_NAME, "tr")
        )
        for r in rows:
            stats = r.find_elements(By.TAG_NAME, "td")
            # Team name is stats[2], BB% is 4, K% is 5, OPS is 10, BABIP is 12,
            # WRC+ is 16
            return_array.append(
                {
                    "name": stats[2].text,
                    stats: {
                        "walk_rate": float(stats[4].text.replace("%", "")),
                        "k_rate": float(stats[5].text.replace("%", "")),
                        "babip": float(stats[12].text),
                        "wrc": int(stats[16].text),
                    },
                }
            )
    except Exception as e:
        print("Hit an exception", e)
    driver.close()
    return return_array


def get_park_factors():
    """Function that gets park factors from baseball savant and returns"""
    driver = webdriver.Chrome()
    driver.implicitly_wait(10)
    url = "https://baseballsavant.mlb.com/leaderboard/statcast-park-factors"
    driver.get(url)
    park_factors_array = []
    try:
        rows = (
            driver.find_element(By.ID, "parkFactors")
            .find_element(By.TAG_NAME, "tbody")
            .find_elements(By.TAG_NAME, "tr")
        )
        for r in rows:
            cells = r.find_elements(By.TAG_NAME, "td")
            team = {
                "name": get_team_by_name(
                    cells[1].find_element(By.TAG_NAME, "span").text
                ),
                "factor": cells[5].find_element(By.TAG_NAME, "span").text,
            }
            park_factors_array.append(team)
    except Exception as e:
        print("Hit an exception", e)
    driver.close()
    return park_factors_array


def get_full_season(split):
    """Function that takes a split as an argument and passes it into the stat
    dict with the full season dates and returns the array from stat dict
    getter.
    """
    year = str(datetime.today().year)
    dict_array = get_stat_dicts(f"{year}-03-01", f"{year}-11-01", split)
    return dict_array


def get_three_weeks(split):
    """Function that takes a split as an argument and passes it into the stat
    dict getter with the dates from the last three weeks. Returns the array
    from the stat dict getter.
    """

    start = datetime.today().strftime("%Y-%m-%d")
    end = (datetime.today() - timedelta(weeks=3)).strftime("%Y-%m-%d")
    dict_array = get_stat_dicts(end, start, split)
    return dict_array


def get_pitcher(link):
    """Function that takes in a fangraphs link to a pitcher page and returns
    a Pitcher object with the data filled in.
    """
    driver = webdriver.Chrome()
    driver.implicitly_wait(10)
    driver.get(link)
    try:
        handedness = driver.find_elements(By.CLASS_NAME, "header_item_6AFbi")[2].text[
            -1
        ]
        name = driver.find_element(By.ID, "h1").text
        pitcher = Pitcher(name, handedness)
    except Exception as e:
        print("Exception getting pitcher data: ", e)
        pitcher = Pitcher("N/A", "N/A")
    driver.close()
    return pitcher


def get_matchups():
    """Function that gets the opponent, probable pitcher and park for for a team for the next 10 days"""
    return_array = []
    driver = webdriver.Chrome()
    driver.implicitly_wait(10)
    driver.get("fangraphs.com/roster-resource/probables-grid")

    try:
        rows = (
            driver.find_element(By.CLASS_NAME, "fg-data-grid")
            .find_element(By.TAG_NAME, "tbody")
            .find_elements(By.TAG_NAME, "tr")
        )
        for r in rows:
            team_matchups = r.find_elements(By.TAG_NAME, "td")
            if len(team_matchups) > 0:
                matchups_dict = {"abbrev": team_matchups[0].text, "matchups": []}
                "TODO: finish building matchup objecting once I know the structure of the table element I'm pulling from"
                for i in range(1, 10):

                    single_matchup = Matchup()
                    matchups_dict["matchups"].append()
    except Exception as e:
        print("Exception, ", e)
    driver.close()
    return return_array
