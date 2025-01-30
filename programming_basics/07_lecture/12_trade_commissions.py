city = str(input())
sells = float(input())

if city == "Sofia":
    if 0 <= sells <= 500:
        commission = 0.05
    elif 500 < sells <= 1000:
        commission = 0.07
    elif 1000 < sells <= 10000:
        commission = 0.08
    elif sells > 10000:
        commission = 0.12
    else:
        print("error")
        exit()

elif city == "Varna":
    if 0 <= sells <= 500:
        commission = 0.045
    elif 500 < sells <= 1000:
        commission = 0.075
    elif 1000 < sells <= 10000:
        commission = 0.10
    elif sells > 10000:
        commission = 0.13
    else:
        print("error")
        exit()

elif city == "Plovdiv":
    if 0 <= sells <= 500:
        commission = 0.055
    elif 500 < sells <= 1000:
        commission = 0.08
    elif 1000 < sells <= 10000:
        commission = 0.12
    elif sells > 10000:
        commission = 0.145
    else:
        print("error")
        exit()
else:
    print("error")
    exit()

print(f"{sells * commission:.2f}")
