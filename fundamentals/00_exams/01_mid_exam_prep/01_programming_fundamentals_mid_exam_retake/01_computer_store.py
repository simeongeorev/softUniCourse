total_price_without_tax = 0
total_price_with_tax = 0
user_is_special = False

while True:

    command = input()

    if command == "special":
        user_is_special = True
        break

    if command == "regular":
        break

    component_price = float(command)

    if component_price <= 0:
        print("Invalid price!")
        continue

    total_price_without_tax += component_price
    total_price_with_tax += component_price * 1.2

if total_price_with_tax > 0:
    print("Congratulations you've just bought a new computer!")
    print(f"Price without taxes: {total_price_without_tax:.2f}$")
    print(f"Taxes: {(total_price_with_tax - total_price_without_tax):.2f}$")
    print("-----------")
    if user_is_special:
        total_price_with_tax = total_price_with_tax * 0.9
    print(f"Total price: {total_price_with_tax:.2f}$")
else:
    print("Invalid order!")