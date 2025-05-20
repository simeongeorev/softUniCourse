items_list = input().split("|")

starting_money = int(input())
money_left = starting_money

clothes_max_price = 50.00
shoes_max_price = 35.00
accessories_max_price = 20.50

original_prices = 0
list_of_sold_items = []

for item in items_list:
    item_as_list = item.split("->")
    type_of_item = item_as_list[0]
    price_of_item = float(item_as_list[1])

    if ((type_of_item == "Clothes" and price_of_item <= clothes_max_price)
            or (type_of_item == "Shoes" and price_of_item <= shoes_max_price)
            or (type_of_item == "Accessories" and price_of_item <= accessories_max_price)):

        if money_left >= price_of_item:
            money_left -= price_of_item
            original_prices += price_of_item
            list_of_sold_items.append(price_of_item * 1.4)

profit = sum(list_of_sold_items) - original_prices
money_left += sum(list_of_sold_items)

for item in list_of_sold_items:
    print(f"{item:.2f}", end=" ")
print()
print(f"Profit: {profit:.2f}")
print("Hello, France!") if money_left >= 150 else print("Not enough money.")
