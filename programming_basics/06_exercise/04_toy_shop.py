# 04_toy_shop
# 1. Цена на екскурзията - реално число в интервала [1.00 … 10000.00]
# 2. Брой пъзели - цяло число в интервала [0… 1000]
# 3. Брой говорещи кукли - цяло число в интервала [0 … 1000]
# 4. Брой плюшени мечета - цяло число в интервала [0 … 1000]
# 5. Брой миньони - цяло число в интервала [0 … 1000]
# 6. Брой камиончета - цяло число в интервала [0 … 1000]

trip_price = float(input())

puzzles = int(input())
dolls = int(input())
teddy_bears = int(input())
minions = int(input())
toy_trucks = int(input())

toys_price_sum = puzzles * 2.60 + dolls * 3 + teddy_bears * 4.10 + minions * 8.20 + toy_trucks * 2
toys_total_count = puzzles + dolls + teddy_bears + minions + toy_trucks

if toys_total_count >= 50:
    toys_price_sum *=  0.75
    
toys_price_sum *= 0.90

if toys_price_sum >= trip_price:
    print(f"Yes! {toys_price_sum - trip_price:.2f} lv left.")
else:
    print(f"Not enough money! {(toys_price_sum - trip_price) * -1:.2f} lv needed.")