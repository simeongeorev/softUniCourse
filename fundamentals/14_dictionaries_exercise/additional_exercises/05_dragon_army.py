# Using list for [dmg, hp, armor] inside a dict {name:[dmg, hp, armor]} inside a dict {type:name}

# type_and_name_dict = {}
# name_and_info_dict = {}
# n = int(input())
# for _ in range(n):
#     dragons_info = input().split()
#     drag_type = dragons_info[0]
#     drag_name = dragons_info[1]
#     drag_dmg = int(dragons_info[2]) if dragons_info[2] != "null" else 45
#     drag_hp = int(dragons_info[3]) if dragons_info[3] != "null" else 250
#     drag_armor = int(dragons_info[4]) if dragons_info[4] != "null" else 10
#
#     if drag_type not in type_and_name_dict.keys():
#         type_and_name_dict[drag_type] = {}
#
#     type_and_name_dict[drag_type][drag_name] = [drag_dmg, drag_hp, drag_armor]
#
# for dragon_type, dragon_names in type_and_name_dict.items():
#     total_dmg = 0
#     total_hp = 0
#     total_armor = 0
#     for dragon_stats in dragon_names.values():
#         total_dmg += dragon_stats[0]
#         total_hp += dragon_stats[1]
#         total_armor += dragon_stats[2]
#     dragons_count = len(dragon_names.keys())
#     print(f"{dragon_type}::({total_dmg/dragons_count:.2f}/{total_hp/dragons_count:.2f}/{total_armor/dragons_count:.2f})")
#
#     dragon_names_sorted = dict(sorted(dragon_names.items()))
#     for name, stats in dragon_names_sorted.items():
#         print(f"-{name} -> damage: {stats[0]}, health: {stats[1]}, armor: {stats[2]}")


"""Using a Dragon class - by ChatGPT:

class Dragon:
    def __init__(self, name, damage, health, armor):
        self.name = name
        self.damage = damage if damage is not None else 45
        self.health = health if health is not None else 250
        self.armor = armor if armor is not None else 10

    def __str__(self):
        return f"-{self.name} -> damage: {self.damage}, health: {self.health}, armor: {self.armor}"

# Store dragons grouped by type
dragons_by_type = {}

n = int(input())
for _ in range(n):
    parts = input().split()
    d_type = parts[0]
    d_name = parts[1]
    d_dmg = int(parts[2]) if parts[2] != "null" else None
    d_hp = int(parts[3]) if parts[3] != "null" else None
    d_armor = int(parts[4]) if parts[4] != "null" else None

    dragon = Dragon(d_name, d_dmg, d_hp, d_armor)

    if d_type not in dragons_by_type:
        dragons_by_type[d_type] = {}

    # Overwrite if dragon of same name exists
    dragons_by_type[d_type][d_name] = dragon

# Output results
for d_type, dragons in dragons_by_type.items():
    count = len(dragons)
    avg_dmg = sum(d.damage for d in dragons.values()) / count
    avg_hp = sum(d.health for d in dragons.values()) / count
    avg_armor = sum(d.armor for d in dragons.values()) / count
    print(f"{d_type}::({avg_dmg:.2f}/{avg_hp:.2f}/{avg_armor:.2f})")

    for dragon_name in sorted(dragons):
        print(dragons[dragon_name])

"""
# Using a Dragon class - written by me

class Dragon:
    def __init__(self, dmg: int, hp: int, armor: int):
        self.dmg = dmg
        self.hp = hp
        self.armor = armor

type_and_name_dict = {}

n = int(input())
for _ in range(n):
    dragons_info = input().split()
    d_type = dragons_info[0]
    d_name = dragons_info[1]
    d_dmg = int(dragons_info[2]) if dragons_info[2] != "null" else 45
    d_hp = int(dragons_info[3]) if dragons_info[3] != "null" else 250
    d_armor = int(dragons_info[4]) if dragons_info[4] != "null" else 10

    dragon = Dragon(d_dmg, d_hp, d_armor)

    if d_type not in type_and_name_dict.keys():
        type_and_name_dict[d_type] = {}

    type_and_name_dict[d_type][d_name] = dragon

for dragon_type, dragon_names_dict in type_and_name_dict.items():
    total_dmg = 0
    total_hp = 0
    total_armor = 0
    for dragon_object in dragon_names_dict.values():
        total_dmg += dragon_object.dmg
        total_hp += dragon_object.hp
        total_armor += dragon_object.armor
    dragons_count = len(dragon_names_dict.keys())
    print(f"{dragon_type}::({total_dmg/dragons_count:.2f}/{total_hp/dragons_count:.2f}/{total_armor/dragons_count:.2f})")

    dragon_names_sorted = dict(sorted(dragon_names_dict.items()))
    for name, dragon_object in dragon_names_sorted.items():
        print(f"-{name} -> damage: {dragon_object.dmg}, health: {dragon_object.hp}, armor: {dragon_object.armor}")