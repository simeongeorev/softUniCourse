from abc import ABC, abstractmethod


class FormulaTeam(ABC):
    MIN_BUDGET = 1_000_000

    def __init__(self, budget: int):
        self.budget = budget

    @property
    def budget(self):
        return self._budget

    @budget.setter
    def budget(self, value):
        if value < self.MIN_BUDGET:
            raise ValueError("F1 is an expensive sport, find more sponsors!")
        self._budget = value

    @property
    @abstractmethod
    def sponsors(self) -> dict[str, dict[int, int]]:
        pass

    @property
    @abstractmethod
    def expenses(self) -> int:
        pass

    def calculate_revenue_after_race(self, race_pos: int):
        earned_money = 0
        for sponsor, graph in self.sponsors.items():

            if race_pos in graph.keys():
                earned_money += graph[race_pos]
                continue

            for pos in graph.keys():
                if race_pos < pos:
                    earned_money += graph[pos]
                    break

        revenue = earned_money - self.expenses
        self.budget += revenue
        return f"The revenue after the race is {revenue}$. Current budget {self.budget}$"


