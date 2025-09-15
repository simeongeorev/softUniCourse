number_of_guests = int(input())
vip_quests = set()
regular_quests = set()
for _ in range(number_of_guests):
    guest_input = input()
    if guest_input[0] in (range(0, 10)):
        vip_quests.add(guest_input)
    else:
        regular_quests.add(guest_input)

while (command := input()) != "END":
    if command[0] in (range(0, 10)):
        vip_quests.remove(command)
    else:
        regular_quests.remove(command)

vip_quests = sorted(vip_quests)
regular_quests = sorted(regular_quests)

print(len(vip_quests) + len(regular_quests))
if vip_quests:
    print("\n".join(vip_quests))
if regular_quests:
    print("\n".join(regular_quests))
