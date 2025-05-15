quantity_of_decor, days_until_christmas = int(input()), int(input())

money_spent = 0
spirit_points = 0

ornament_set_price = 2
tree_skirt_price = 5
tree_garland_price = 3
tree_lights_price = 15

# check if it will work with 0 or 1 as starting point
for day in range(1, days_until_christmas + 1):

    # check for 11th day
    if day % 11 == 0:
        quantity_of_decor += 2

    # every 2nd day
    if day % 2 == 0:
        money_spent += (ornament_set_price * quantity_of_decor)
        spirit_points += 5

    # every 3rd day
    if day % 3 == 0:
        money_spent += (tree_skirt_price * quantity_of_decor) + (tree_garland_price * quantity_of_decor)
        spirit_points += 13

    # every 5th day
    if day % 5 == 0:
        money_spent += (tree_lights_price * quantity_of_decor)
        spirit_points += 17
        if day % 3 == 0:
            spirit_points += 30

    # cat logic - every 10th day
    if day % 10 == 0:
        spirit_points -= 20
        money_spent += (tree_skirt_price + tree_garland_price + tree_lights_price)

# check if it ends on a 10th day
if days_until_christmas % 10 == 0:
    spirit_points -= 30

print(f"Total cost: {money_spent}")
print(f"Total spirit: {spirit_points}")



