from abc import ABC, abstractmethod

from project.products.base_product import BaseProduct


class BaseStore(ABC):

    def __init__(self, name: str, location: str, capacity: int):
        self.name = name
        self.location = location
        self.capacity = capacity
        self.products: list[BaseProduct] = []

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value:str):
        stripped_value = value.strip()
        if stripped_value == "":
            raise ValueError("Store name cannot be empty!")
        self.__name = value

    @property
    def location(self):
        return self.__location

    @location.setter
    def location(self, value:str):
        if len(value) != 3 or any(x.isspace() for x in value):
            raise ValueError("Store location must be 3 chars long!")
        self.__location = value

    @property
    def capacity(self):
        return self.__capacity

    @capacity.setter
    def capacity(self, value):
        if value < 0:
            raise ValueError("Store capacity must be a positive number or 0!")
        self.__capacity = value

    def get_estimated_profit(self):
        prices_sum = sum([x.price for x in self.products])
        estimated_profit = prices_sum * 0.1
        return f"Estimated future profit for {len(self.products)} products is {estimated_profit:.2f}"

    @property
    def store_type(self):
        return type(self).__name__ # check if this is okay or we need .__name__

    @abstractmethod
    def store_stats(self):
        pass

