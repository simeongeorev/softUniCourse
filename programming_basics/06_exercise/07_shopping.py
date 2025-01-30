# Петър иска да купи N видеокарти, M процесора и P на брой рам памет.
# Ако броя на видеокартите е по-голям от този на процесорите получава 15% отстъпка от крайната сметка. Важат следните цени:
# · Видеокарта – 250 лв./бр.
# · Процесор – 35% от цената на закупените видеокарти/бр.
# · Рам памет – 10% от цената на закупените видеокарти/бр.
# Да се изчисли нужната сума за закупуване на материалите и да се пресметне дали бюджета ще му стигне.

# Входът се състои от четири реда:
# 1. Бюджетът на Петър - реално число в интервала [1.0…100000.0]
# 2. Броят видеокарти - цяло число в интервала [1…100]
# 3. Броят процесори - цяло число в интервала [1…100]
# 4. Броят рам памет - цяло число в интервала [1…100]

budget = float(input())

videocards = int(input())
processors = int(input())
rams = int(input())

videocards_price = videocards * 250
processors_price = processors * (0.35 * videocards_price) # the price of the all videocards or per 1?
rams_price = rams * (0.1 * videocards_price) # the price of the all videocards or per 1?

price_total = videocards_price + processors_price + rams_price

if videocards > processors:
    price_total *= 0.85

if budget >= price_total:
    print(f"You have {budget - price_total:.2f} leva left!")
else:
    print(f"Not enough money! You need {price_total - budget:.2f} leva more!")
