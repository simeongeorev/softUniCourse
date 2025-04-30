
sum_numbers = lambda num1, num2: num1 + num2
subtract = lambda num1, num2: num1 - num2

def add_and_subtrack(num1:int, num2:int, num3:int) -> int:
    return subtract(sum_numbers(num1, num2), num3)

print(add_and_subtrack(int(input()), int(input()), int(input())))