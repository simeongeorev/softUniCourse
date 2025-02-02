n_bottles = int(input())

detergent_ml = 750 * n_bottles
detergent_for_plate = 5
detergent_for_crockpot = 15
counter_of_washes = 0
detergent_used = 0
n_plates = 0
n_crockpots = 0

command = input()

while command != "End":
    number_of_dishes = int(command)
    counter_of_washes += 1

    if counter_of_washes % 3 == 0: # every 3 washes - crockpots
        detergent_used += number_of_dishes * detergent_for_crockpot
        n_crockpots += number_of_dishes

    else: # plates
        detergent_used += number_of_dishes * detergent_for_plate
        n_plates += number_of_dishes

    if detergent_used > detergent_ml:
        print(f"Not enough detergent, {detergent_used - detergent_ml}"
              f" ml. more necessary!")
        break

    command = input()
else:
    print("Detergent was enough!")
    print(f"{n_plates} dishes and"
          f" {n_crockpots} pots were washed.")
    print(f"Leftover detergent {detergent_ml - detergent_used} ml.")

