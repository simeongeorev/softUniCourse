import math
from collections import deque

bee_groups = deque([int(x) for x in input().split()])
eater_groups = [int(x) for x in input().split()]

while bee_groups and eater_groups:
    cur_bee_group = bee_groups.popleft()
    cur_eater_group = eater_groups.pop()

    how_many_bees_can_kill = cur_eater_group * 7

    if cur_bee_group == how_many_bees_can_kill:
        continue

    elif cur_bee_group > how_many_bees_can_kill:
        cur_bee_group -= how_many_bees_can_kill
        bee_groups.append(cur_bee_group)

    elif how_many_bees_can_kill > cur_bee_group:
        how_many_bees_can_kill -= cur_bee_group
        cur_eater_group = math.ceil(how_many_bees_can_kill / 7)
        eater_groups.append(cur_eater_group)

print("The final battle is over!")
if not bee_groups and not eater_groups:
    print("But no one made it out alive!")
elif bee_groups:
    print(f"Bee groups left: {', '.join([str(x) for x in bee_groups])}")
elif eater_groups:
    print(f"Bee-eater groups left: {', '.join([str(x) for x in eater_groups])}")