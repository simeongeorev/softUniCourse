rolls_paper = int(input())
rolls_cloth = int(input())
glue_litres = float(input())
discount_percent = int(input())

price_without_discount = ((rolls_paper * 5.8) + (rolls_cloth * 7.2) + (glue_litres * 1.2))

percents = discount_percent / 100

print(f"{price_without_discount - (price_without_discount * percents):.3f}")