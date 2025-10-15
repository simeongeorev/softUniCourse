from collections import deque


def accommodate(*guest_groups, **rooms):
    guest_groups = deque(guest_groups)
    rooms_dict = {}

    for room_number, capacity in rooms.items():
        room_number = int(room_number.split("_")[1])
        rooms_dict[room_number] = int(capacity)

    sorted_rooms_dict = dict(sorted(rooms_dict.items(), key=lambda x: (x[1], x[0])))

    taken_rooms_dict = {}
    unaccounted_guests = 0

    while guest_groups:
        cur_group = guest_groups.popleft()

        suitable_room_n = next((k for k, v in sorted_rooms_dict.items() if v >= cur_group), None)

        if not suitable_room_n:
            unaccounted_guests += cur_group
            continue

        taken_rooms_dict[suitable_room_n] = cur_group
        del sorted_rooms_dict[suitable_room_n]

    output_str = ""

    if not taken_rooms_dict:
        output_str += "No accommodations were completed!\n"
    else:
        output_str += f"A total of {len(taken_rooms_dict)} accommodations were completed!\n"
        for room, guests in sorted(taken_rooms_dict.items(), key=lambda x: x[0]):
            output_str += f"<Room {room} accommodates {guests} guests>\n"
    if unaccounted_guests:
        output_str += f"Guests with no accommodation: {unaccounted_guests}\n"
    if sorted_rooms_dict:
        output_str += f"Empty rooms: {len(sorted_rooms_dict)}"

    return output_str

print(accommodate(5, 4, 2, room_305=6, room_410=5, room_204=2))
print()
print(accommodate(10, 9, 8, room_307=6, room_802=5))
print()
print(accommodate(1, 2, 4, 8, room_102=3, room_101=1, room_103=2))
