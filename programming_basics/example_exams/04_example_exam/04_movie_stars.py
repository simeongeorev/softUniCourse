budget = float(input())

while True:

    command = input()

    if command == "ACTION":
        print(f"We are left with {budget:.2f} leva.")
        break

    if len(command) > 15:
        salary = budget * 0.2
    else:
        salary = float(input())

    budget -= salary

    if budget < 0:
        print(f"We need {abs(budget):.2f} leva for our actors.")
        break