"""Module for opening webpages with selenium and returning data from therein"""
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from datetime import datetime, timedelta

from url_builders import fg_splits_page

driver = webdriver.Chrome()
driver.implicitly_wait(20)

def get_full_season(split):
    """Function that gets full season stats and returns a Stats tuple for each team listed."""

    url = fg_splits_page("2025-03-01", "2025-11-01", f"{split}")
    driver.get(url)
    return_array = []
    try:
        rows = driver.find_element(By.CLASS_NAME, "fg-data-grid").find_element(By.TAG_NAME, "tbody").find_elements(By.TAG_NAME, "tr")
        for r in rows:
            stats = r.find_elements(By.TAG_NAME, "td")
            #Team name is stats[2], BB% is 4, K% is 5, OPS is 10, BABIP is 12, WRC+ is 16
            return_array.append({"name": stats[2].text, "walk_rate": float(stats[4].text.replace("%","")),"k_rate": float(stats[5].text.replace("%","")), "ops": float(stats[10].text), "babip": float(stats[12].text),"wrc": int(stats[16].text)})
    except Exception as e:
        print("Hit an exception", e)
    driver.close()
    print(return_array)
    return return_array


def get_last_three(split) :
    """Function that gets splits for the last three weeks"""
    today = datetime.today().strftime("%Y-%m-%d")
    three_weeks_ago = (datetime.today - timedelta(weeks=3)).strftime("%Y-%m-%d")
    
    

get_last_three("")