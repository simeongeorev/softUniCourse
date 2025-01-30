# Входът се чете от конзолата и се състои от точно 4 реда:
#     • 1ви ред: X кв.м е лозето – цяло число в интервала [10 … 5000]
#     • 2ри ред: Y грозде за един кв.м – реално число в интервала [0.00 … 10.00]
#     • 3ти ред: Z нужни литри вино – цяло число в интервала [10 … 600]
#     • 4ти ред: брой работници – цяло число в интервала [1 … 20]
import math

x_square_meters = int(input())
y_grapes_per_meter = float(input())
z_needed_litres_wine = int(input())
number_of_workers = int(input())

meters_for_wine = x_square_meters * 0.4

kilos_of_grapes = meters_for_wine * y_grapes_per_meter

produced_litres_of_wine = kilos_of_grapes / 2.5

difference = abs(produced_litres_of_wine - z_needed_litres_wine)

if produced_litres_of_wine < z_needed_litres_wine:
    print(f"It will be a tough winter! More {math.floor(difference)} liters wine needed.")
elif produced_litres_of_wine >= z_needed_litres_wine:
    print(f"Good harvest this year! Total wine: {math.floor(produced_litres_of_wine)} liters.")
    print(f"{math.ceil(difference)} liters left -> {math.ceil(difference / number_of_workers)} liters per person.")

