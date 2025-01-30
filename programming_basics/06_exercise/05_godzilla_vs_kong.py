# 05_godzilla_vs_kong
# Ред 1. Бюджет за филма – реално число в интервала [1.00 … 1000000.00]
# Ред 2. Брой на статистите – цяло число в интервала [1 … 500]
# Ред 3. Цена за облекло на един статист – реално число в интервала [1.00 … 1000.00]

film_budget = float(input())

statists_count = int(input())
price_for_dressing_a_statist = float(input())

decor = film_budget * 0.10
if statists_count > 150:
    price_for_dressing_a_statist *= 0.9
    
total_price = decor + price_for_dressing_a_statist * statists_count

if total_price > film_budget:
    print("Not enough money!")
    print(f"Wingard needs {((film_budget - total_price) * -1):.2f} leva more.")
else:
    print("Action!")
    print(f"Wingard starts filming with {film_budget - total_price:.2f} leva left.")