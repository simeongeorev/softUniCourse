#     • Магнолии – 3.25 лева
#     • Зюмбюли – 4 лева
#     • Рози – 3.50 лева
#     • Кактуси – 8 лева
# От общата сума, Мария трябва да плати 5% данъци.
import math

magnolias = int(input())
zumbuls = int(input())
roses = int(input())
cactuses = int(input())
present_price = float(input())

magnolias_price = magnolias * 3.25
zumbuls_price = zumbuls * 4
roses_price = roses * 3.5
cactuses_price = cactuses * 8

total_sum = (magnolias_price + zumbuls_price + roses_price + cactuses_price) * 0.95

money_left = total_sum - present_price

if money_left >= 0:
    print(f"She is left with {math.floor(money_left)} leva.")
elif money_left < 0:
    print(f"She will have to borrow {math.ceil(abs(money_left))} leva.")

