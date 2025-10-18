from collections import deque


def boarding_passengers(ship_capacity: int, *args):
    args = deque(args)
    boarded_guests = {}
    guests_not_boarded = 0

    while ship_capacity > 0 and args:
        current_group = args.popleft()

        # cannot be boarded
        if current_group[0] > ship_capacity:
            guests_not_boarded += current_group[0]
            continue

        # can be boarded
        if current_group[0] <= ship_capacity:
            if current_group[1] not in boarded_guests.keys():
                boarded_guests[current_group[1]] = 0
            boarded_guests[current_group[1]] += current_group[0]
            ship_capacity -= current_group[0]

    # sorting
    sorted_boarded_guests = sorted(boarded_guests.items(),
                                   key=lambda x: (-x[1], x[0]))

    #printing
    output_str = "Boarding details by benefit plan:\n"

    for k, v in sorted_boarded_guests:
        output_str += f"## {k}: {v} guests\n"

    if not args and guests_not_boarded == 0:
        output_str += "All passengers are successfully boarded!"
    elif ship_capacity <= 0:
        output_str += "Boarding unsuccessful. Cruise ship at full capacity."
    elif ship_capacity > 0:
        output_str += (f"Partial boarding completed."
                       f" Available capacity: {ship_capacity}.")

    return output_str

# print(boarding_passengers(150, (35, 'Diamond'),
#                           (55, 'Platinum'), (35, 'Gold'), (25, 'First Cruiser')))
print()
print(boarding_passengers(100, (20, 'Diamond'),
                          (15, 'Platinum'), (25, 'Gold'),
                          (25, 'First Cruiser'), (15, 'Diamond'),
                          (10, 'Gold')))
print()
print(boarding_passengers(120, (30, 'Gold'),
                          (20, 'Platinum'), (30, 'Diamond'),
                          (10, 'First Cruiser'), (31, 'Platinum'),
                          (20, 'Diamond')))
