from collections import deque

pumps_num = int(input())
petrol_stations = deque()

for i in range(pumps_num):
    petrol_amount, distance_to_next_station = list(map(int, input().split()))
    petrol_stations.append((petrol_amount, distance_to_next_station)) # (1 5), (10 3)

starting_position = 0
stops = 0

while stops < pumps_num:
    litres_in_tank = 0
    for petrol_amount, distance_to_next_station in petrol_stations:
        litres_in_tank += petrol_amount
        if litres_in_tank < distance_to_next_station:
            stops = 0
            starting_position += 1
            petrol_stations.rotate(-1)
            break
        else:
            litres_in_tank -= distance_to_next_station
            stops += 1

print(starting_position)

