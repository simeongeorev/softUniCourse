#     • Брой пакети химикали - цяло число в интервала [0...100]
#     • Брой пакети маркери - цяло число в интервала [0...100]
#     • Литри препарат за почистване на дъска - цяло число в интервала [0…50]
#     • Процент намаление - цяло число в интервала [0...100]

pen_packages = int(input())
markers_packages = int(input())
board_cleaner_litres = int(input())
discount_percent = int(input())

total_sum = (pen_packages * 5.80
             + markers_packages * 7.20
             + board_cleaner_litres * 1.20) \
            * (1 - discount_percent / 100)

print(total_sum)