# #   1. Дължина в см – цяло число в интервала [10 … 500]
#     2. Широчина в см – цяло число в интервала [10 … 300]
#     3. Височина в см – цяло число в интервала [10… 200]
#     4. Процент  – реално число в интервала [0.000 … 100.000]

length = int(input())
width = int(input())
height = int(input())
taken_percentage = float(input())

volume = length * width * height
volume_in_litres = volume / 1000
litres_needed = volume_in_litres * (1 - taken_percentage / 100)

print(litres_needed)
