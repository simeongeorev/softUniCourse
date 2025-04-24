def calculator(operator: str, num1: int, num2: int) -> int:
    if operator == "multiply":
        return num1 * num2
    elif operator == "divide":
        return int(num1 / num2)
    elif operator == "add":
        return num1 + num2
    elif operator == "subtract":
        return num1 - num2
    else:
        return 0

operator = input()
num1 = int(input())
num2 = int(input())

print(calculator(operator, num1, num2))