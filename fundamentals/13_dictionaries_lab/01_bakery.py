food_and_quantities = input().split()

my_dict = {}

for i in range(0, len(food_and_quantities), 2):
    key = food_and_quantities[i]
    value = food_and_quantities[i+1]
    my_dict[key] = int(value)

print(my_dict)