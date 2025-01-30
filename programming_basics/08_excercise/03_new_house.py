flowers_type = str(input())
flowers_count = int(input())
budget = int(input())

price_per_flower = 0
price_correction = 1

if flowers_type == "Roses":
    price_per_flower = 5
    if flowers_count > 80:
        price_correction -= 0.1
elif flowers_type == "Dahlias":
    price_per_flower = 3.8
    if flowers_count > 90:
        price_correction -= 0.15
elif flowers_type == "Tulips":
    price_per_flower = 2.8
    if flowers_count > 80:
        price_correction -= 0.15
elif flowers_type == "Narcissus":
    price_per_flower = 3
    if flowers_count < 120:
        price_correction += 0.15
elif flowers_type == "Gladiolus":
    price_per_flower = 2.5
    if flowers_count < 80:
        price_correction += 0.2

flowers_price_total = (flowers_count * price_per_flower) * price_correction

money_left = budget - flowers_price_total

if money_left >= 0:
    print(f"Hey, you have a great garden with {flowers_count} {flowers_type} and {money_left:.2f} leva left.")
elif money_left < 0:
    print(f"Not enough money, you need {abs(money_left):.2f} leva more.")

