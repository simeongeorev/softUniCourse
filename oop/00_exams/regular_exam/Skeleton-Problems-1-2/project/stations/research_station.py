from project.stations.base_station import BaseStation


class ResearchStation(BaseStation):

    def __init__(self, name: str):
        super().__init__(name, capacity=5)

    def update_salaries(self, min_value: float):
        for a in self.astronauts:
            if a.specialization == "ScientistAstronaut" and a.salary <= min_value:
                a.salary += 5000.0


