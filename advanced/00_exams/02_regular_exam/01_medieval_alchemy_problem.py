from collections import deque

potions_dict = {110: "Brew of Immortality",
                100: "Essence of Resilience",
                90: "Draught of Wisdom",
                80: "Potion of Agility",
                70: "Elixir of Strength"}

substances = [int(x) for x in input().split(", ")]  # LIFO
crystal_energies = deque([int(x) for x in input().split(", ")])  # FIFO

crafted_potions = []

while substances and crystal_energies and potions_dict:
    cur_substance = substances.pop()
    cur_crys_energy = crystal_energies.popleft()
    cur_sum = cur_substance + cur_crys_energy

    # potion is CRAFTED!
    if cur_sum in potions_dict.keys():
        crafted_potions.append(potions_dict[cur_sum])
        del potions_dict[cur_sum]

    elif any(cur_sum > x for x in potions_dict.keys()):
        for k, v in potions_dict.items():
            if cur_sum > k:
                crafted_potions.append(v)
                del potions_dict[k]
                break

        if cur_crys_energy - 20 > 0:
            crystal_energies.append(cur_crys_energy - 20)

    else:
        if cur_crys_energy - 5 > 0:
            crystal_energies.append(cur_crys_energy - 5)

if potions_dict:
    print("The alchemist failed to complete his quest.")
else:
    print("Success! The alchemist has forged all potions!")

if crafted_potions:
    print(f"Crafted potions: {', '.join(crafted_potions)}")

if substances:
    print(f"Substances: {', '.join([str(x) for x in substances][::-1])}")

if crystal_energies:
    print(f"Crystals: {', '.join([str(x) for x in crystal_energies])}")