#    • Брой пилешки менюта – цяло число в интервала [0 … 99]
#     • Брой менюта с риба – цяло число в интервала [0 … 99]
#     • Брой вегетариански менюта – цяло число в интервала [0 … 99]

chicken = int(input())
fish = int(input())
vegetarian = int(input())

chicken *= 10.35
fish *= 12.40
vegetarian *= 8.15

all_foods_sum = chicken + fish + vegetarian
desert = all_foods_sum * 0.2
delivery = 2.50

whole_order_price = all_foods_sum + desert + delivery

print(whole_order_price)

