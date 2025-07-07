materials = {"shards": 0,
             "fragments": 0,
             "motes": 0}
legendary_obtained = False

while True:
    command_list = input().split()

    for i in range(0, len(command_list), 2):
        material = command_list[i + 1].lower()
        quantity = int(command_list[i])

        if material not in materials.keys():
            materials[material] = 0
        materials[material] += quantity

        if material == "shards" and materials[material] >= 250:
            materials[material] -= 250
            print("Shadowmourne obtained!")
            legendary_obtained = True
            break

        if material == "fragments" and materials[material] >= 250:
            materials[material] -= 250
            print("Valanyr obtained!")
            legendary_obtained = True
            break

        if material == "motes" and materials[material] >= 250:
            materials[material] -= 250
            print(f"Dragonwrath obtained!")
            legendary_obtained = True
            break

    if legendary_obtained:
        break

for mat, quant in materials.items():
    print(f"{mat}: {quant}")