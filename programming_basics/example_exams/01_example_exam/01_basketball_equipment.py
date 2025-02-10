annual_price = int(input())

shoes = annual_price * 0.6
suit = shoes * 0.8
ball = suit * (1/4)
accessories = ball * (1/5)

total_price = annual_price + shoes + suit + ball + accessories

print(f"{total_price:.2f}")