from project.astronauts.base_astronaut import BaseAstronaut


class EngineerAstronaut(BaseAstronaut):
    STAMINA_INCREASE_UNITS = 5

    def __init__(self, id_number: str, salary: float):
        super().__init__(id_number, salary, specialization="EngineerAstronaut", stamina=80)

    @property
    def stamina_increase(self):
        return self.STAMINA_INCREASE_UNITS
