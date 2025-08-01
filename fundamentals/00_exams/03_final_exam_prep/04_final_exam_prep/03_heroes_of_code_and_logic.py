class HeroStats:
    def __init__(self, hp: int, mp: int):
        self.hp = hp
        self.mp = mp


n = int(input())
heroes_dict = {}

for _ in range(n):
    hero_info = input().split()
    heroes_dict[hero_info[0]] = HeroStats(int(hero_info[1]), int(hero_info[2]))

while (command := input()) != "End":
    command_list = command.split(" - ")
    command = command_list[0]
    hero_name = command_list[1]

    if command == "CastSpell":
        mp_needed = int(command_list[2])
        spell_name = command_list[3]

        if heroes_dict[hero_name].mp >= mp_needed:
            heroes_dict[hero_name].mp -= mp_needed
            print(f"{hero_name} has successfully cast {spell_name} and now has {heroes_dict[hero_name].mp} MP!")
        else:
            print(f"{hero_name} does not have enough MP to cast {spell_name}!")

    elif command == "TakeDamage":
        damage = int(command_list[2])
        attacker = command_list[3]

        if heroes_dict[hero_name].hp > damage:
            heroes_dict[hero_name].hp -= damage
            print(f"{hero_name} was hit for {damage} HP by {attacker} and now has {heroes_dict[hero_name].hp} HP left!")
        else:
            print(f"{hero_name} has been killed by {attacker}!")
            del heroes_dict[hero_name]

    elif command == "Recharge":
        amount = int(command_list[2])

        if (heroes_dict[hero_name].mp + amount) > 200:
            amount_recharged = 200 - heroes_dict[hero_name].mp
            heroes_dict[hero_name].mp = 200
        else:
            heroes_dict[hero_name].mp += amount
            amount_recharged = amount
        print(f"{hero_name} recharged for {amount_recharged} MP!")

    elif command == "Heal":
        amount = int(command_list[2])

        if (heroes_dict[hero_name].hp + amount) > 100:
            amount_recharged = 100 - heroes_dict[hero_name].hp
            heroes_dict[hero_name].hp = 100
        else:
            heroes_dict[hero_name].hp += amount
            amount_recharged = amount
        print(f"{hero_name} healed for {amount_recharged} HP!")

for hero in heroes_dict.items():
    print(f"{hero[0]}\n  HP: {hero[1].hp}\n  MP: {hero[1].mp}")
