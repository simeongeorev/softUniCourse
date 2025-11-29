from abc import ABC, abstractmethod

from project.artifacts.base_artifact import BaseArtifact
import re


class BaseCollector(ABC):

    def __init__(self, name: str, available_money: float, available_space: int):
        self.name = name
        self.available_money = available_money
        self.available_space = available_space
        self.purchased_artifacts: list[BaseArtifact] = []

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value: str):
        pattern = r"^[a-zA-Z0-9][a-zA-Z0-9 ]*[a-zA-Z0-9]$"
        rgx = re.match(pattern, value)
        if rgx is None:
            raise ValueError("Collector name must contain letters, numbers, "
                             "and optional white spaces between them!")

        self.__name = value

    @property
    def available_money(self):
        return self.__available_money

    @available_money.setter
    def available_money(self, value: float):
        if value < 0.0:
            raise ValueError("A collector cannot have a negative amount of money!")

        self.__available_money = value

    @property
    def available_space(self):
        return self.__available_space

    @available_space.setter
    def available_space(self, value: int):
        if value < 0:
            raise ValueError("A collector cannot have a negative space available for exhibitions!")

        self.__available_space = value

    @abstractmethod
    def increase_money(self):
        pass

    def can_purchase(self, artifact_price: float, artifact_space_required: int):
        enough_money = True if self.available_money >= artifact_price else False
        enough_space = True if self.available_space >= artifact_space_required else False
        return True if enough_money and enough_space else False

    def __str__(self):
        if not self.purchased_artifacts:
            result = "none"
        else:
            result = ", ".join(sorted([a.name for a in self.purchased_artifacts], reverse=True))

        return (f"Collector name: {self.name}; Money available: {self.available_money:.2f};"
                f" Space available: {self.available_space};"
                f" Artifacts: {result}")