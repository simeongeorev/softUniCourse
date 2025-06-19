food_kg = float(input())
hay_kg = float(input())
cover_kg = float(input())

weight = float(input())

food_grams = food_kg * 1000

for day in range(1, 31):
    food_grams -= 300

    if day % 2 == 0:
        hay_kg -= 0.05 * (food_grams / 1000)

    if day % 3 == 0:
        cover_kg -= 1/3 * weight

    if food_grams <= 0 or hay_kg <= 0 or cover_kg <= 0:
        print("Merry must go to the pet store!")
        break
else:
    print(f"Everything is fine! Puppy is happy! Food: {food_grams / 1000:.2f}, Hay: {hay_kg:.2f}, Cover: {cover_kg:.2f}.")