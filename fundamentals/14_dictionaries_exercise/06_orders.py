products_list = []

while True:
    command = input()

    if command == "buy":
        break

    command_list = command.split()
    name, price, quantity = command_list[0], float(command_list[1]), int(command_list[2])
    already_in_list = False

    for product in products_list:
        if product["name"] == name:
            product["price"] = price
            product["quantity"] += quantity
            already_in_list = True

    if not already_in_list:
        products_list.append({"name": str(name),
                              "price": float(price),
                              "quantity": int(quantity)})

for product_dict in products_list:
    product_dict["total_price"] = product_dict["price"] * product_dict["quantity"]
    del product_dict["price"]
    del product_dict["quantity"]
    print(f"{product_dict['name']} -> {product_dict['total_price']:.2f}")