type = str(input())
rows = int(input())
columns = int(input())

if type == "Premiere":
    price = 12
elif type == "Normal":
    price = 7.5
elif type == "Discount":
    price = 5
else:
    exit()
full_price = rows * columns * price

print(f"{full_price:.2f} leva")


