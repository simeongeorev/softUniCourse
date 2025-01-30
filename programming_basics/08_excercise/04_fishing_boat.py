budget = int(input())
season = str(input())
persons = int(input())

discount = 1
special_discount = 1

if season == "Spring":
    boat_price = 3000
elif season == "Summer" or season == "Autumn":
    boat_price = 4200
elif season == "Winter":
    boat_price = 2600

if persons <= 6:
    discount -= 0.1
elif 7 <= persons <= 11:
    discount -= 0.15
elif persons >= 12:
    discount -= 0.25

if persons % 2 == 0 and not (season == "Autumn"):
    special_discount -= 0.05

price_total = (boat_price * discount) * special_discount
money_left = budget - price_total

if money_left >= 0:
    print(f"Yes! You have {money_left:.2f} leva left.")
elif money_left < 0:
    print(f"Not enough money! You need {abs(money_left):.2f} leva.")




