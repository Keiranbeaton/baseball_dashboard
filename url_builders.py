# Pass in desired season for year
# Num: Full season is 0, vs Left is 13, vs Righty is 14
def fg_main_page(year, num):
    return f"https://www.fangraphs.com/leaders/major-league?pos=all&stats=bat&lg=all&qual=0&season={year}&season1={year}&ind=0&team=0%2Cts&rost=&filter=&players=0&type=8&month={num}"


# Pass in 1 for vs rhp, 2 for vs lhp, 7 for home, 8 for away
def fg_splits_page(year, start_month, start_day, end_month, end_day, split):
    return f"https://www.fangraphs.com/leaders/splits-leaderboards?splitArr={split},8&splitArrPitch=&autoPt=false&splitTeams=false&statType=team&statgroup=1&startDate={year}-{start_month}-{start_day}&endDate={year}-{end_month}-{end_day}&players=&filter=&groupBy=season&wxTemperature=&wxPressure=&wxAirDensity=&wxElevation=&wxWindSpeed=&position=B&sort=22,1"
