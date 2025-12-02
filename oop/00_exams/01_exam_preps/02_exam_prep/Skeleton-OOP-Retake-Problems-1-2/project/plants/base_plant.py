from abc import ABC, abstractmethod


class BasePlant(ABC):
    def __init__(self, name: str, price: float, water_needed: int):
        self.name = name
        self.price = price
        self.water_needed = water_needed

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value: str):
        if value.strip() == "":
            raise ValueError("Plant name cannot be null or empty!")

        self.__name = value

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, value: float):
        if value <= 0:
            raise ValueError("Price must be greater than zero!")

        self.__price = value

    @property
    def water_needed(self):
        return self.__water_needed

    @water_needed.setter
    def water_needed(self, value):
        if 1 <= value <= 2_000:
            self.__water_needed = value
        else:
            raise ValueError("Water needed must be between 1 and 2000 ml!")

    @abstractmethod
    def plant_details(self):
        return f"{self.name}, Price: {self.price:.2f}, Watering: {self.water_needed}ml"
