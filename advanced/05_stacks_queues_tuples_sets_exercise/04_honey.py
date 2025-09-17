from collections import deque

working_bees = deque(map(int, input().split())) # first
nectar =  list(map(int, input().split())) # last
symbols = deque(input().split()) # first

break_flag = False
total_honey = 0

operators = {
    "+": lambda a, b: a + b,
    "-": lambda a, b: a - b,
    "*": lambda a, b: a * b,
    "/": lambda a, b: a / b
}

while working_bees and nectar:
    honey_made = 0
    current_bee = working_bees[0]
    current_nectar = nectar[-1]

    while current_nectar < current_bee:
        nectar.pop()
        if nectar:
            current_nectar = nectar[-1]
        else:
            break_flag = True
            break

    if break_flag:
        break

    current_symbol = symbols[0]

    if current_symbol != "/" and current_nectar != 0:
        honey_made = abs(operators[current_symbol](current_bee, current_nectar))
        total_honey += honey_made

    working_bees.popleft()
    nectar.pop()
    symbols.popleft()

print(f"Total honey made: {total_honey}")
if working_bees:
    print(f"Bees left: {', '.join(str(el) for el in working_bees)}")
if nectar:
    print(f"Nectar left: {', '.join(str(el) for el in nectar)}")
