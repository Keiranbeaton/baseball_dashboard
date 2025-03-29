"""Module for functions used to create a URL to feed into the Webcrawler."""


def fg_splits_page(start_date, end_date, split):
    """Set the year, months, days and id of the desired split, return the
    fangraphs URL of the splits page that will be passed into the web crawler.
    Arguments: 1 for stats vs RHP, 2 for stats vs LHP, 7 for stats at home,
    8 for stats on the road. 1,7 for RHP at home, and so forth."
    """
    return f"https://www.fangraphs.com/leaders/splits-leaderboards?splitArr={split}&splitArrPitch=&autoPt=false&splitTeams=false&statType=team&statgroup=2&startDate={start_date}&endDate={end_date}&players=&filter=&groupBy=season&wxTemperature=&wxPressure=&wxAirDensity=&wxElevation=&wxWindSpeed=&position=B&sort=22,1"
