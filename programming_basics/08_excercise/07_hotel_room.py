month = str(input())
nights = int(input())

apartment_price = 0
studio_price = 0
studio_price_correction = 1
apartment_price_correction = 1

if month == "May" or month == "October":
    studio_price = 50
    apartment_price = 65
    if 7 < nights <= 14:
        studio_price_correction -= 0.05
    elif nights > 14:
        studio_price_correction -= 0.30
        apartment_price_correction -= 0.10

elif month == "June" or month == "September":
    studio_price = 75.20
    apartment_price = 68.70
    if nights > 14:
        studio_price_correction -= 0.20
        apartment_price_correction -= 0.10

elif month == "July" or month == "August":
    studio_price = 76
    apartment_price = 77
    if nights > 14:
        apartment_price_correction -= 0.10

print(f"Apartment: {(nights * (apartment_price * apartment_price_correction)):.2f} lv.")
print(f"Studio: {(nights * (studio_price * studio_price_correction)):.2f} lv.")