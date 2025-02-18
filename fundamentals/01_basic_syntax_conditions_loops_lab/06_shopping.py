budget = int(input())

while budget >= 0:
    command = input()

    if command == "End":
        print(f"You bought everything needed.")
        break

    price = int(command)

    budget -= price
else:
    print(f"You went in overdraft!")