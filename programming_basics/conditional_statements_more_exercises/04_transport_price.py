# От конзолата се четат два реда:
#     • Първият ред съдържа числото n – брой километри – цяло число в интервала [1…5000]
#     • Вторият ред съдържа дума “day” или “night” – пътуване през деня или през нощта

distance = int(input())
time_of_travel = str(input())

taxi_starting_price = 0.7

if time_of_travel == "day":
    taxi_tariff = 0.79
elif time_of_travel == "night":
    taxi_tariff = 0.9

if distance < 20:
    travel_price = distance * taxi_tariff + taxi_starting_price
elif distance < 100:
    bus_tariff = 0.09
    travel_price = distance * bus_tariff
elif distance >= 100:
    train_tariff = 0.06
    travel_price = distance * train_tariff

print(f"{travel_price:.2f}")


