from abc import ABC, abstractmethod


class BaseBattleship(ABC):
    MIN_HEALTH = 0

    def __init__(self, name: str, health: int, hit_strength: int, ammunition: int):
        self.name = name
        self.health = health
        self.hit_strength = hit_strength
        self.ammunition = ammunition
        self.is_attacking: bool = False
        self.is_available: bool = True

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value:str):
        if not value.isalpha():
            raise ValueError("Ship name must contain only letters!")
        self.__name = value

    @property
    def health(self):
        return self.__health

    @health.setter
    def health(self, value: int):
        if value < self.MIN_HEALTH:
            self.__health = self.MIN_HEALTH
        else:
            self.__health = value

    def take_damage(self, enemy_battleship: 'BaseBattleship'):
        self.health -= enemy_battleship.hit_strength

    @abstractmethod
    def attack(self):
        pass