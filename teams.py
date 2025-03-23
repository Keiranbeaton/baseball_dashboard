from dataclasses import dataclass


@dataclass
class Team:
    name: str
    fullseason: int
    last_three_weeks: int
    facing_lefty: int
    facing_righty: int
    facing_lefty_last_three_weeks: int
    facing_righty_last_three_weeks: int
    home: int
    away: int
    home_last_three_weeks: int
    away_last_three_weeks: int
