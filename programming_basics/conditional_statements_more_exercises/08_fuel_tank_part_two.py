fuel_type = str(input())
litres_to_fill = float(input())
has_club_card = str(input())

# gas_discount = 0.08 * litres_to_fill
# gasoline_discount = 0.18 * litres_to_fill
# diesel_discount = 0.12 * litres_to_fill

if fuel_type == "Gas":
    fuel_price = litres_to_fill * 0.93
elif fuel_type == "Gasoline":
    fuel_price = litres_to_fill * 2.22
elif fuel_type == "Diesel":
    fuel_price = litres_to_fill * 2.33

if has_club_card == "Yes" and fuel_type == "Gas":
    fuel_price -= 0.08 * litres_to_fill
elif has_club_card == "Yes" and fuel_type == "Gasoline":
    fuel_price -= 0.18 * litres_to_fill
elif has_club_card == "Yes" and fuel_type == "Diesel":
    fuel_price -= 0.12 * litres_to_fill

if 20 <= litres_to_fill <= 25:
    fuel_price *= 0.92
elif litres_to_fill > 25:
    fuel_price *= 0.90

print(f"{fuel_price:.2f} lv.")


# HOW TO DO IT BETTER:

fuel_type = input()
litres_to_fill = float(input())
has_club_card = input()

# Define fuel prices per liter
if fuel_type == "Gas":
    base_price_per_liter = 0.93
    club_card_discount = 0.08
elif fuel_type == "Gasoline":
    base_price_per_liter = 2.22
    club_card_discount = 0.18
elif fuel_type == "Diesel":
    base_price_per_liter = 2.33
    club_card_discount = 0.12

# Calculate initial fuel price
fuel_price = litres_to_fill * base_price_per_liter

# Apply club card discount if applicable
if has_club_card == "Yes":
    fuel_price -= litres_to_fill * club_card_discount

# Apply volume discount
if 20 <= litres_to_fill <= 25:
    fuel_price *= 0.92
elif litres_to_fill > 25:
    fuel_price *= 0.90

print(f"{fuel_price:.2f} lv.")

