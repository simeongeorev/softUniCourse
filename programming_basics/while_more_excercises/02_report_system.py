target_sum = int(input())
pay_counter = 1
sum_collected = 0
paid_cash = 0
paid_card = 0
money_from_cash = 0
money_from_card = 0

command = input()

while command != "End":
    transaction_sum = int(command)

    if pay_counter % 2 != 0: # odd - cash
        if transaction_sum > 100:
            print("Error in transaction!")
        else:
            sum_collected += transaction_sum
            paid_cash += 1
            money_from_cash += transaction_sum
            print("Product sold!")

    else: # even - card
        if transaction_sum < 10:
            print("Error in transaction!")
        else:
            sum_collected += transaction_sum
            paid_card += 1
            money_from_card += transaction_sum
            print("Product sold!")

    if sum_collected >= target_sum:
        print(f"Average CS: {money_from_cash / paid_cash:.2f}")
        print(f"Average CC: {money_from_card / paid_card:.2f}")
        break

    pay_counter += 1
    command = input()

else:
    print("Failed to collect required money for charity.")