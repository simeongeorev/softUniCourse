# Ако литрите гориво са повече или равни на 25, на конзолата да се отпечата
# "You have enough {вида на горивото}.", ако са по-малко от 25, да се отпечата
# "Fill your tank with {вида на горивото}!". В случай, че бъде въведено гориво,
# различно от посоченото, да се отпечата "Invalid fuel!".

fuel_type = str(input())
litres_in_reservoir = float(input())

if not(fuel_type == "Diesel" or fuel_type == "Gasoline" or fuel_type == "Gas"):
    print("Invalid fuel!")
elif litres_in_reservoir >= 25:
    print(f"You have enough {fuel_type.lower()}.")
elif litres_in_reservoir < 25:
    print(f"Fill your tank with {fuel_type.lower()}!")
