class Vehicle:

    DEFAULT_FUEL_CONSUMPTION: float = 1.25
    # fuel: float
    # horse_power: int

    def __init__(self, fuel: float, horse_power: int):
        self.fuel = fuel
        self.horse_power = horse_power
        self.fuel_consumption = self.DEFAULT_FUEL_CONSUMPTION

    def drive(self, kilometers):
        fuel_to_drive = kilometers * self.fuel_consumption
        if self.fuel >= fuel_to_drive:
            self.fuel -= fuel_to_drive

