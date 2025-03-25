"""Module for opening webpages with selenium and returning data from therein"""
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import time

from url_builders import fg_splits_page

driver = webdriver.Chrome()
driver.implicitly_wait(60)

def get_full_season():
    """Function that gets full season stats and returns a Stats tuple for each team listed."""

    # url = fg_splits_page("2025-03-01", "2025-11-01", "")
    url = "https://www.fangraphs.com/leaders/splits-leaderboards?splitArr=&splitArrPitch=&autoPt=false&splitTeams=false&statType=team&statgroup=2&startDate=2025-03-01&endDate=2025-11-01&players=&filter=&groupBy=season&wxTemperature=&wxPressure=&wxAirDensity=&wxElevation=&wxWindSpeed=&position=B&sort=22,1"
    driver.get(url)

    try:
        rows = driver.find_element(By.CLASS_NAME, "fg-data-grid").find_element(By.TAG_NAME, "tbody").find_elements(By.TAG_NAME, "tr")
        for r in rows:
            stats = r.find_elements(By.TAG_NAME, "td")
            #Team name is stats[2], BB% is 4, K% is 5, OPS is 10, BABIP is 12, WRC+ is 16
    except Exception as e:
        print("Hit an exception", e)
    
    driver.close()

get_full_season()