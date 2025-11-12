from abc import ABC, abstractmethod


class Vehicle(ABC):

    @abstractmethod
    def drive(self, distance):
        pass

    @abstractmethod
    def refuel(self, fuel):
        pass

class Car(Vehicle):

    AC_FUEL_CONSUMPTION = 0.9

    def __init__(self, fuel_quantity, fuel_consumption):
        self.fuel_quantity = fuel_quantity
        self.fuel_consumption = fuel_consumption

    def drive(self, distance):
        fuel_for_drive = distance * (self.fuel_consumption + self.AC_FUEL_CONSUMPTION)
        if fuel_for_drive <= self.fuel_quantity:
            self.fuel_quantity -= fuel_for_drive

    def refuel(self, fuel):
        self.fuel_quantity += fuel

class Truck(Vehicle):

    AC_FUEL_CONSUMPTION = 1.6
    FUEL_QUANTITY_MULTIPLIER = 0.95

    def __init__(self, fuel_quantity, fuel_consumption):
        self.fuel_quantity = fuel_quantity
        self.fuel_consumption = fuel_consumption

    def drive(self, distance):
        fuel_for_drive = distance * (self.fuel_consumption + self.AC_FUEL_CONSUMPTION)
        if fuel_for_drive <= self.fuel_quantity:
            self.fuel_quantity -= fuel_for_drive

    def refuel(self, fuel):
        self.fuel_quantity += fuel * self.FUEL_QUANTITY_MULTIPLIER

car = Car(20, 5)
car.drive(3)
print(car.fuel_quantity)
car.refuel(10)
print(car.fuel_quantity)
truck = Truck(100, 15)
truck.drive(5)
print(truck.fuel_quantity)
truck.refuel(50)
print(truck.fuel_quantity)
