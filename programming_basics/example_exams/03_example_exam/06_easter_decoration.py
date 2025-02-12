n_clients = int(input())

total_money_spent = 0

for _ in range(n_clients):

    n_items_purchased_for_client = 0
    money_spent_for_client = 0

    while True:

        command = input()

        if command == "Finish":
            break

        n_items_purchased_for_client += 1

        if command == "basket":
            money_spent_for_client += 1.5
        elif command == "wreath":
            money_spent_for_client += 3.8
        elif command == "chocolate bunny":
            money_spent_for_client += 7.0

    if n_items_purchased_for_client % 2 == 0:
        money_spent_for_client *= 0.8

    total_money_spent += money_spent_for_client

    print(f"You purchased {n_items_purchased_for_client} items for {money_spent_for_client:.2f} leva.")

print(f"Average bill per client is: {total_money_spent / n_clients:.2f} leva.")