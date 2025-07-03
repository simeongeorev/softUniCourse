products_and_quantities = input().split()

my_dict = {}

for i in range(0, len(products_and_quantities), 2):
    key = products_and_quantities[i]
    value = products_and_quantities[i+1]
    my_dict[key] = int(value)

products_search = input().split()

for product in products_search:
    if product in my_dict.keys():
        print(f"We have {my_dict[product]} of {product} left")
    else:
        print(f"Sorry, we don't have {product}")