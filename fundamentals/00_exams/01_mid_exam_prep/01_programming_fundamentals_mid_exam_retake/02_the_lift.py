people_waiting = int(input())

lift_wagons = list(map(int, input().split()))

people_already_on_the_lift = sum(lift_wagons)

capacity_for_new_people = len(lift_wagons) * 4 - people_already_on_the_lift

if people_waiting == capacity_for_new_people:
    lift_wagons = [4 for wagon in lift_wagons]

if people_waiting > capacity_for_new_people:
    print(f"There isn't enough space! {people_waiting - capacity_for_new_people} people in a queue!")
    lift_wagons = [4 for wagon in lift_wagons]

if people_waiting < capacity_for_new_people:
    print("The lift has empty spots!")
    for i in range(len(lift_wagons)):
        while lift_wagons[i] < 4 and people_waiting > 0:
            people_waiting -= 1
            lift_wagons[i] += 1

for wagon in lift_wagons:
    print(wagon, end=" ")
