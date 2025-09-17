from collections import deque

chocolates = list(map(int, input().split(", ")))  # last to first
cups_of_milk = deque(map(int, input().split(", ")))  # first to last

milkshakes = 0
break_flag = False

while chocolates and cups_of_milk and (milkshakes < 5):
    current_chocolate = chocolates[-1]
    current_cup_of_milk = cups_of_milk[0]

    while current_chocolate <= 0:
        chocolates.pop()
        if chocolates:
            current_chocolate = chocolates[-1]
        else:
            break_flag = True
            break

    while current_cup_of_milk <= 0:
        cups_of_milk.popleft()
        if cups_of_milk:
            current_cup_of_milk = cups_of_milk[0]
        else:
            break_flag = True
            break

    if break_flag:
        break

    if current_chocolate == current_cup_of_milk:
        milkshakes += 1
        chocolates.pop()
        cups_of_milk.popleft()
    else:
        cups_of_milk.rotate(-1)
        chocolates[-1] -= 5

if milkshakes == 5:
    print("Great! You made all the chocolate milkshakes needed!")
else:
    print("Not enough milkshakes.")

print(f"Chocolate: {', '.join(str(el) for el in chocolates) if chocolates else 'empty'}")
print(f"Milk: {', '.join(str(el) for el in cups_of_milk) if cups_of_milk else 'empty'}")
