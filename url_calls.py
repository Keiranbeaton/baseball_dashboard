"""Module for opening webpages with selenium and returning data from therein"""

from datetime import datetime, timedelta

from selenium import webdriver
from selenium.webdriver.common.by import By


from url_builders import fg_splits_page


def get_stat_dicts(start_date, end_date, split):
    """Function that gets full season stats and returns a Stats tuple for each
    team listed.
    """
    driver = webdriver.Chrome()
    driver.implicitly_wait(20)
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
                        "ops": float(stats[10].text),
                        "babip": float(stats[12].text),
                        "wrc": int(stats[16].text),
                    },
                }
            )
    except Exception as e:
        print("Hit an exception", e)
    driver.close()
    print(return_array)
    return return_array


def get_full_season(split):
    """Function that takes a split as an argument and passes it into the stat
    dict with the full season dates and returns the array from stat dict
    getter.
    """

    dict_array = get_stat_dicts("2025-03-01", "2025-11-01", split)
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
