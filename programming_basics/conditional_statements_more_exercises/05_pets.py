#     • Първи ред – брой дни – цяло число в интервал [1…5000]
#     • Втори ред – оставена храна в килограми – цяло число в интервал [0…100000]
#     • Трети ред – храна на ден за кучето в килограми – реално число в интервал [0.00…100.00]
#     • Четвърти ред – храна на ден за котката в килограми– реално число в интервал [0.00…100.00]
#     • Пети ред – храна на ден за костенурката в грамове – реално число в интервал [0.00…10000.00]
import math

days = int(input())
kilos_of_food_available = int(input())
kilos_dog_food_per_day = float(input())
kilos_cat_food_per_day = float(input())
grams_turtle_food_per_day = float(input())

kilos_turtle_food_per_day = grams_turtle_food_per_day / 1000

food_eaten_per_day = kilos_dog_food_per_day + kilos_cat_food_per_day + kilos_turtle_food_per_day
food_eaten_total = food_eaten_per_day * days

difference = food_eaten_total - kilos_of_food_available

if difference <= 0:
    print(f"{math.floor(abs(difference))} kilos of food left.")
elif difference > 0:
    print(f"{math.ceil(difference)} more kilos of food are needed.")
