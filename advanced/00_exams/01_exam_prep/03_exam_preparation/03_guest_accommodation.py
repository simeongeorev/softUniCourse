from collections import deque


def accommodate(*guest_groups, **rooms):
    guest_groups = deque(guest_groups)
    rooms_dict = {}
    for room_number, capacity in rooms:
        room_number = int(room_number.split("_")[1])
        rooms_dict[room_number] = int(capacity)

    sorted_rooms_dict = sorted(rooms_dict.items(), key= lambda x: (x[1], x[0]))

    taken_rooms_dict = {}

    while True:
        cur_group = guest_groups.popleft()





print(accommodate(5, 4, 2, room_305=6, room_410=5, room_204=2))
print()
print(accommodate(10, 9, 8, room_307=6, room_802=5))
print()
print(accommodate(1, 2, 4, 8, room_102=3, room_101=1, room_103=2))