degrees = int(input())
time_of_day = str(input())

shirt = "Shirt"
moccasins = "Moccasins"
t_shirt = "T-Shirt"
sandals = "Sandals"

if 10 <= degrees <= 18:
    if time_of_day == "Morning":
        outfit = "Sweatshirt"
        shoes = "Sneakers"
    elif time_of_day == "Afternoon" or time_of_day == "Evening":
        outfit = shirt
        shoes = moccasins

elif 18 < degrees <= 24:
    if time_of_day == "Morning" or time_of_day == "Evening":
        outfit = shirt
        shoes = moccasins
    elif time_of_day == "Afternoon":
        outfit = t_shirt
        shoes = sandals

elif degrees >= 25:
    if time_of_day == "Morning":
        outfit = t_shirt
        shoes = sandals
    elif time_of_day == "Afternoon":
        outfit = "Swim Suit"
        shoes = "Barefoot"
    elif time_of_day == "Evening":
        outfit = shirt
        shoes = moccasins
print(f"It's {degrees} degrees, get your {outfit} and {shoes}.")
