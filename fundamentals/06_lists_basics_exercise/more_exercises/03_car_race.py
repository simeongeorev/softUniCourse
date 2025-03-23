import math

numbers_list = input().split()

for number in range(len(numbers_list)):
    numbers_list[number] = int(numbers_list[number])

steps_per_racer = math.floor(len(numbers_list) / 2)

first_racer_results = list(numbers_list[:steps_per_racer])
second_racer_results = list(numbers_list[steps_per_racer + 1:])

first_racer_total_time, second_racer_total_time = 0, 0

for time in first_racer_results:
    if time == 0:
        first_racer_total_time *= 0.8
    else:
        first_racer_total_time += time

for time in range(len(second_racer_results) - 1, -1, -1):
    if second_racer_results[time] == 0:
        second_racer_total_time *= 0.8
    else:
        second_racer_total_time += second_racer_results[time]

if first_racer_total_time > second_racer_total_time:
    print(f"The winner is right with total time: {second_racer_total_time:.1f}")
elif first_racer_total_time < second_racer_total_time:
    print(f"The winner is left with total time: {first_racer_total_time:.1f}")
