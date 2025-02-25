water_tank_capacity = 255
n = int(input())

for i in range(n):
    litres_to_fill = int(input())
    if litres_to_fill > water_tank_capacity:
        print("Insufficient capacity!")
        continue
    water_tank_capacity -= litres_to_fill

print(255 - water_tank_capacity)

