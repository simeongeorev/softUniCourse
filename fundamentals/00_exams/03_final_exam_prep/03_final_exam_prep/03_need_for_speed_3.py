class Car:
    def __init__(self, name, mileage, fuel):
        self.name = name
        self.mileage = mileage
        self.fuel = fuel
        self.should_be_sold = False

    def drive(self, distance, fuel_needed):
        if self.fuel < fuel_needed:
            print("Not enough fuel to make that ride")
        else:
            self.mileage += distance
            self.fuel -= fuel_needed
            print(f"{self.name} driven for {distance} kilometers. {fuel_needed} liters of fuel consumed.")

        if self.mileage >= 100000:
            print(f"Time to sell the {self.name}!")
            self.should_be_sold = True

    def refuel(self, fuel_to_refill):
        if self.fuel + fuel_to_refill > 75:
            print(f"{self.name} refueled with {75 - self.fuel} liters")
            self.fuel = 75
        else:
            self.fuel += fuel_to_refill
            print(f"{self.name} refueled with {fuel_to_refill} liters")

    def revert(self, kilometers):
        if (self.mileage - kilometers) < 10000:
            self.mileage = 10000
        else:
            self.mileage -= kilometers
            print(f"{self.name} mileage decreased by {kilometers} kilometers")


n_cars = int(input())
my_cars = []

for i in range(n_cars):
    car_info = input().split("|")
    my_cars.append(Car(car_info[0], int(car_info[1]), int(car_info[2])))

while True:
    command = input()

    if command == "Stop":
        break

    command_list = command.split(" : ")
    car_name = command_list[1]

    for car in my_cars:
        if car.name == car_name:
            if command.startswith("Drive"):
                car.drive(int(command_list[2]), int(command_list[3]))
                if car.should_be_sold:
                    my_cars.remove(car)

            elif command.startswith("Refuel"):
                car.refuel(int(command_list[2]))

            elif command.startswith("Revert"):
                car.revert(int(command_list[2]))

            break

for car in my_cars:
    print(f"{car.name} -> Mileage: {car.mileage} kms, Fuel in the tank: {car.fuel} lt.")
