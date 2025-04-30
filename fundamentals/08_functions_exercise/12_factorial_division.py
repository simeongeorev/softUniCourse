import math

def factorial_division(num1: int, num2: int):
    fact_num1 = math.factorial(num1)
    fact_num2 = math.factorial(num2)
    return fact_num1 / fact_num2

print(f"{factorial_division(int(input()), int(input())):.2f}")