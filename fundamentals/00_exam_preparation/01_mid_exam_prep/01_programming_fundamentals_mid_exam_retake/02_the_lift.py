people_waiting = int(input())
lift_seats = list(map(int, input().split()))

max_ppl_per_seat = 4

for i in range(len(lift_seats)):

    current_people_sitting_on_lift = max_ppl_per_seat - lift_seats[i]

    if people_waiting - current_people_sitting_on_lift == 0:
        lift_seats[i] = max_ppl_per_seat
        people_waiting -= current_people_sitting_on_lift
        break

    elif people_waiting - current_people_sitting_on_lift < 0:
        print("The lift has empty spots!")
        lift_seats[i] += people_waiting
        break

    lift_seats[i] = max_ppl_per_seat
    people_waiting -= current_people_sitting_on_lift
else:
    print(f"There isn't enough space! {people_waiting} people in a queue!")
for seat in lift_seats:
    print(seat, end=" ")

#TODO check why only 9/10 pass


