#     • Първи ред - дни за престой - цяло число в интервала [0...365]
#     • Втори ред - вид помещение - "room for one person", "apartment" или "president apartment"
#     • Трети ред - оценка - "positive"  или "negative"
days_of_stay = int(input())
kind_of_room = str(input())
score = str(input())

nights = days_of_stay - 1
room_price_per_night = 0
discount = 1

if kind_of_room == "room for one person":
    room_price_per_night = 18

elif kind_of_room == "apartment":
    room_price_per_night = 25
    if days_of_stay < 10:
        discount -= 0.30
    elif 10 <= days_of_stay <= 15:
        discount -= 0.35
    elif days_of_stay > 15:
        discount -= 0.50

elif kind_of_room == "president apartment":
    room_price_per_night = 35
    if days_of_stay < 10:
        discount -= 0.10
    elif 10 <= days_of_stay <= 15:
        discount -= 0.15
    elif days_of_stay > 15:
        discount -= 0.20

total_price = nights * room_price_per_night * discount

if score == "positive":
    total_price *= 1.25
elif score == "negative":
    total_price *= 0.90

print(f"{total_price:.2f}")


