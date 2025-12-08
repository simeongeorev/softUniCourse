import re
from abc import ABC, abstractmethod

from project.astronauts.base_astronaut import BaseAstronaut


class BaseStation(ABC):

    def __init__(self, name: str, capacity: int):
        self.name = name
        self.capacity = capacity
        self.astronauts: list[BaseAstronaut] = []

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value: str):
        ptrn = r"^[a-zA-Z0-9-]*$"
        if not re.fullmatch(ptrn, value):
            raise ValueError("Station names can contain only letters, numbers, and hyphens!")
        self.__name = value

    @property
    def capacity(self):
        return self.__capacity

    @capacity.setter
    def capacity(self, value: int):
        if value < 0:
            raise ValueError("A station cannot have a negative capacity!")
        self.__capacity = value

    def calculate_total_salaries(self):
        summed_salaries = sum([a.salary for a in self.astronauts])
        return f"{summed_salaries:.2f}"

    def status(self):
        ids = " #".join(sorted([a.id_number for a in self.astronauts])) if self.astronauts else "N/A"
        result = f"Station name: {self.name}; Astronauts: {ids}; Total salaries: {self.calculate_total_salaries()}"
        return result

    @abstractmethod
    def update_salaries(self, min_value: float):
        pass




