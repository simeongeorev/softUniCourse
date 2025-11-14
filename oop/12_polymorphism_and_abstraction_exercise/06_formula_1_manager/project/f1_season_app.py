from project.formula_teams.mercedes_team import MercedesTeam
from project.formula_teams.red_bull_team import RedBullTeam


class F1SeasonApp:
    teams = ["Red Bull", "Mercedes"]

    def __init__(self):
        self.red_bull_team: RedBullTeam = None
        self.mercedes_team: MercedesTeam = None

    def register_team_for_season(self, team_name: str, budget: int):
        if team_name not in self.teams:
            raise ValueError("Invalid team name!")

        if team_name == self.teams[0]:
            self.red_bull_team = RedBullTeam(budget)
        else:
            self.mercedes_team = MercedesTeam(budget)

        return f"{team_name} has joined the new F1 season."

    def new_race_results(self, race_name: str, red_bull_pos: int, mercedes_pos: int):
        if not self.red_bull_team or not self.mercedes_team:
            raise Exception("Not all teams have registered for the season.")

        # red bull wins
        winner = self.teams[0] if red_bull_pos < mercedes_pos else self.teams[1]

        return (f"Red Bull: {self.red_bull_team.calculate_revenue_after_race(red_bull_pos)}."
                f" Mercedes: {self.mercedes_team.calculate_revenue_after_race(mercedes_pos)}."
                f" {winner} is ahead at the {race_name} race.")

    