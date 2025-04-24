
def calculate_order(product: str, quantity: int) -> float:
    price = 0
    if product == "coffee":
        price = 1.50
    elif product == "water":
        price = 1.00
    elif product == "coke":
        price = 1.40
    elif product == "snacks":
        price = 2.00

    return quantity * price

order = input()
quantity = int(input())

print(f"{calculate_order(order, quantity):.2f}")