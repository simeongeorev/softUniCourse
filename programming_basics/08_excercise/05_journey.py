budget = float(input())
season = str(input())

destination = ""
summer = "summer"
winter = "winter"
part_of_budget_spent = 0
accommodation_type = ""

if budget <= 100:
    destination = "Bulgaria"
    if season == summer:
        part_of_budget_spent = 0.3
    elif season == winter:
        part_of_budget_spent = 0.7

elif 100 <budget <= 1000:
    destination = "Balkans"
    if season == summer:
        part_of_budget_spent = 0.4
    elif season == winter:
        part_of_budget_spent = 0.8

elif budget > 1000:
    destination = "Europe"
    part_of_budget_spent = 0.9

if season == summer and not(destination == "Europe"):
    accommodation_type = "Camp"
elif season == winter or destination == "Europe":
    accommodation_type = "Hotel"

price = budget * part_of_budget_spent

print(f"Somewhere in {destination}")
print(f"{accommodation_type} - {price:.2f}")


