def plant_garden(available_space: float, *plant_types, **planting_requests):
    sorted_planting_requests = sorted(planting_requests.items(), key=lambda x: x[0])

    plant_types_dict = {}
    for tup in plant_types:
        plant_types_dict[tup[0]] = tup[1]

    planted_plants = {}
    message = ""

    for plant, quantity_to_plant in sorted_planting_requests:
        if plant in plant_types_dict.keys():
            space_per_plant = plant_types_dict[plant]
            if available_space >= space_per_plant:
                # plant
                how_many_can_be_planted = available_space // space_per_plant

                # planting all requested
                if how_many_can_be_planted >= quantity_to_plant:
                    available_space -= quantity_to_plant * space_per_plant
                    planted_plants[plant] = quantity_to_plant

                # planting only part of them
                else:
                    available_space -= how_many_can_be_planted * space_per_plant
                    planted_plants[plant] = how_many_can_be_planted
                    message = "Not enough space to plant all requested plants!"
                    continue
            else:
                message = "Not enough space to plant all requested plants!"
                continue
        else:
            continue

    if not message:
        message = (f"All plants were planted!"
                   f" Available garden space: {available_space:.1f} sq meters.")

    planted_plants_message = "Planted plants:\n"

    for plant, pieces in planted_plants.items():
        planted_plants_message += f"{plant}: {int(pieces)}\n"

    return f"{message}\n{planted_plants_message}"


print(plant_garden(50.0, ("rose", 2.5), ("tulip", 1.2), ("sunflower", 3.0), rose=10, tulip=20))
print()
print(plant_garden(20.0, ("rose", 2.0), ("tulip", 1.2), ("sunflower", 3.0), rose=10, tulip=20, sunflower=5))
print()
print(plant_garden(2.0, ("rose", 2.5), ("tulip", 1.2), ("daisy", 0.2), rose=4, tulip=15, sunflower=3, daisy=4))
print()
print(plant_garden(50.0, ("tulip", 1.2), ("sunflower", 3.0), rose=10, tulip=20, daisy=1))
