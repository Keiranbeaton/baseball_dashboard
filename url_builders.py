# Num: Full season is 0, vs Left is 13, vs Righty is 14
def fg_main_page(year, num):
    """Set the year and the id of the desired split, return  fangraphs URL of
    the team leaders page that will be passed into the web crawler.
    Arguments: 0 for full season, 13 for stats vs LHP, 14 for stats vs RHP.
    """
    return f"https://www.fangraphs.com/leaders/major-league?pos=all&stats=bat&lg=all&qual=0&season={year}&season1={year}&ind=0&team=0%2Cts&rost=&filter=&players=0&type=8&month={num}"


# Pass in 1 for vs rhp, 2 for vs lhp, 7 for home, 8 for away
def fg_splits_page(year, start_month, start_day, end_month, end_day, split):
    """Set the year, months, days and id of the desired split, return the
    fangraphs URL of the splits page that will be passed into the web crawler.
    Arguments: 1 for stats vs RHP, 2 for stats vs LHP, 7 for stats at home,
    8 for stats on the road."
    """
    return f"https://www.fangraphs.com/leaders/splits-leaderboards?splitArr={split},8&splitArrPitch=&autoPt=false&splitTeams=false&statType=team&statgroup=1&startDate={year}-{start_month}-{start_day}&endDate={year}-{end_month}-{end_day}&players=&filter=&groupBy=season&wxTemperature=&wxPressure=&wxAirDensity=&wxElevation=&wxWindSpeed=&position=B&sort=22,1"
