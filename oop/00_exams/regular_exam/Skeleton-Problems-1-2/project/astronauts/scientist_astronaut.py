from project.astronauts.base_astronaut import BaseAstronaut


class ScientistAstronaut(BaseAstronaut):
    STAMINA_INCREASE_UNITS = 3

    def __init__(self, id_number: str, salary: float):
        super().__init__(id_number, salary, specialization="ScientistAstronaut", stamina=70)

    @property
    def stamina_increase(self):
        return self.STAMINA_INCREASE_UNITS