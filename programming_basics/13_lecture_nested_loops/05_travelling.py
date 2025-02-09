# izbira kyde she hodi i kolko shte i trqbva
end = False

destination = input()

while True:
    if destination == "End" or end is True:
        break

    goal = input()
    if goal == "End" or end is True:
        break
    goal_money = float(goal)
    money_gathered = 0
    # dobavq pari dokato ne izkara dostatychno
    while True:
        deposit_command = input()
        if deposit_command == "End":
            end = True
            break

        deposit_sum = float(deposit_command)
        money_gathered += deposit_sum
        if money_gathered >= goal_money:
            print(f"Going to {destination}!")
            break

    destination = input()