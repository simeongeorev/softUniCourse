from collections import deque

str_expression = deque(input().split())
numbers = deque()

operators = {
    "+": lambda a, b: a + b,
    "-": lambda a, b: a - b,
    "*": lambda a, b: a * b,
    "/": lambda a, b: int(a / b),
}

while str_expression:
    current_el = str_expression.popleft()

    if current_el not in "+-*/":
        numbers.append(int(current_el))
    else:
        while len(numbers) > 1:
            numbers[1] = operators[current_el](numbers[0], numbers[1])
            numbers.popleft()

print(numbers[0])