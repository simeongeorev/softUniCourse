import math

price_for_racket = float(input())
n_of_rackets = int(input())
n_of_trainers = int(input())

price_for_rackets = n_of_rackets * price_for_racket
price_for_trainers = n_of_trainers * (price_for_racket * (1/6))
equipment_price = (price_for_rackets + price_for_trainers) * 0.2
total_price = price_for_trainers + price_for_rackets + equipment_price

print(f"Price to be paid by Djokovic {math.floor(total_price * (1/8))}")
print(f"Price to be paid by sponsors {math.ceil(total_price * (7/8))}")

