class CityInfo:
    def __init__(self, population: int, gold: int):
        self.population = population
        self.gold = gold


cities_dict = {}

while (city_info := input()) != "Sail":
    city_info_list = city_info.split("||")
    city_name, city_population, city_gold = city_info_list[0], int(city_info_list[1]), int(city_info_list[2])
    if city_name in cities_dict:
        cities_dict[city_name].population += city_population
        cities_dict[city_name].gold += city_gold
    else:
        cities_dict[city_name] = CityInfo(city_population, city_gold)

while (command := input()) != "End":
    command_list = command.split("=>")
    command = command_list[0]
    town_name = command_list[1]

    if command == "Plunder":
        people_to_kill = int(command_list[2])
        gold_to_take = int(command_list[3])
        cities_dict[town_name].population -= people_to_kill
        cities_dict[town_name].gold -= gold_to_take
        print(f"{town_name} plundered! {gold_to_take} gold stolen, {people_to_kill} citizens killed.")
        if cities_dict[town_name].population <= 0 or cities_dict[town_name].gold <= 0:
            del cities_dict[town_name]
            print(f"{town_name} has been wiped off the map!")

    elif command == "Prosper":
        gold_to_give = int(command_list[2])
        if gold_to_give < 0:
            print("Gold added cannot be a negative number!")
        else:
            cities_dict[town_name].gold += gold_to_give
            print(f"{gold_to_give} gold added to the city treasury."
                  f" {town_name} now has {cities_dict[town_name].gold} gold.")

if cities_dict:
    print(f"Ahoy, Captain! There are {len(cities_dict.keys())} wealthy settlements to go to:")
    for city in cities_dict.keys():
        print(f"{city} -> Population: {cities_dict[city].population} citizens, Gold: {cities_dict[city].gold} kg")
else:
    print("Ahoy, Captain! All targets have been plundered and destroyed!")
