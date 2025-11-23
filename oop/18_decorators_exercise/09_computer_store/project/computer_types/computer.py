import math
from abc import ABC, abstractmethod


class Computer(ABC):

    def __init__(self, manufacturer: str,
                 model: str):
        self.manufacturer = manufacturer
        self.model = model
        self.processor = None
        self.ram = None
        self.price = 0

    @property
    def manufacturer(self):
        return self._manufacturer

    @manufacturer.setter
    def manufacturer(self, value):
        if not value or all(x == " " for x in value):
            raise ValueError("Manufacturer name cannot be empty.")
        self._manufacturer = value

    @property
    def model(self):
        return self._model

    @model.setter
    def model(self, value):
        if not value or all(x == " " for x in value):
            raise ValueError("Model name cannot be empty.")
        self._model = value

    @staticmethod
    def is_valid_ram_size(ram_size, ram_size_cap):
        return 2 <= ram_size <= ram_size_cap and (ram_size & (ram_size - 1)) == 0


    @property
    @abstractmethod
    def valid_processors(self) -> dict:
        pass

    @property
    @abstractmethod
    def valid_ram_ceil(self) -> int:
        pass

    def configure_computer(self, processor: str, ram: int):
        if processor not in self.valid_processors.keys():
            raise ValueError(f"{self.processor} is not compatible with "
                             f"desktop computer {self.manufacturer} {self.model}!")
        if not self.is_valid_ram_size(ram, self.valid_ram_ceil):
            raise ValueError(f"{ram}GB RAM is not compatible with "
                             f"desktop computer {self.manufacturer} {self.model}!")

        self.processor = processor
        self.ram = ram
        self.price += self.valid_processors[processor] + (int(math.log2(ram)) * 100)
        return f"Created {self.__repr__()} for {self.price}$."

    def __repr__(self):
        return (f"{self.manufacturer} {self.model} with "
                f"{self.processor} and {self.ram}GB RAM")
