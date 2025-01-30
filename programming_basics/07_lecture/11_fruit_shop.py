fruit = str(input())
day = str(input())
amount = float(input())

if (day == "Monday"
        or day == "Tuesday"
        or day == "Wednesday"
        or day == "Thursday"
        or day == "Friday"):
    if fruit == "banana":
        rate = 2.50
    elif fruit == "apple":
        rate = 1.20
    elif fruit == "orange":
        rate = 0.85
    elif fruit == "grapefruit":
        rate = 1.45
    elif fruit == "kiwi":
        rate = 2.70
    elif fruit == "pineapple":
        rate = 5.50
    elif fruit == "grapes":
        rate = 3.85
    else:
        print("error")
        exit()
elif day == "Saturday" or day == "Sunday":
    if fruit == "banana":
        rate = 2.70
    elif fruit == "apple":
        rate = 1.25
    elif fruit == "orange":
        rate = 0.90
    elif fruit == "grapefruit":
        rate = 1.60
    elif fruit == "kiwi":
        rate = 3.00
    elif fruit == "pineapple":
        rate = 5.60
    elif fruit == "grapes":
        rate = 4.20
    else:
        print("error")
        exit()
else:
    print("error")
    exit()

print(f"{rate * amount:.2f}")
