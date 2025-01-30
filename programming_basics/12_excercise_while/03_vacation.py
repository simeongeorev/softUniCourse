money_needed = float(input())
starting_money = float(input())

days_gone = 0
days_spending_in_a_row = 0

while True:
    action = input()
    money_spend_or_saved = float(input())

    days_gone += 1

    if action == "save":
        starting_money += money_spend_or_saved
        days_spending_in_a_row = 0

        if starting_money >= money_needed:
            print(f"You saved the money for {days_gone} days.")
            break

    if action == "spend":
        starting_money -= money_spend_or_saved

        if starting_money < 0:
            starting_money = 0

        days_spending_in_a_row += 1

        if days_spending_in_a_row == 5:
            print("You can't save the money.")
            print(f"{days_gone}")
            break


