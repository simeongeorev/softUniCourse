age = float(input())
sex = str(input())

if sex == "m":
    if age >= 16:
        print("Mr.")
    elif age < 16:
        print("Master")
elif sex == "f":
    if age >= 16:
        print("Ms.")
    elif age < 16:
        print("Miss")

