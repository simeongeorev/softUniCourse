n1 = int(input())
n2 = int(input())
operator = str(input())

result = 0
number_type = "odd"

if operator == "+":
    result = n1 + n2
    if result % 2 == 0:
        number_type = "even"
    print(f"{n1} {operator} {n2} = {result} - {number_type}")

elif operator == "-":
    result = n1 - n2
    if result % 2 == 0:
        number_type = "even"
    print(f"{n1} {operator} {n2} = {result} - {number_type}")

elif operator == "*":
    result = n1 * n2
    if result % 2 == 0:
        number_type = "even"
    print(f"{n1} {operator} {n2} = {result} - {number_type}")

elif operator == "/":
    if n2 == 0:
        print(f"Cannot divide {n1} by zero")
        exit()
    result = n1 / n2
    print(f"{n1} / {n2} = {result:.2f}")

elif operator == "%":
    if n2 == 0:
        print(f"Cannot divide {n1} by zero")
        exit()
    result = n1 % n2
    print(f"{n1} % {n2} = {result}")







