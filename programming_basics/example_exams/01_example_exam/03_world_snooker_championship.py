stage = input()
ticket_type = input()
num_of_tickets = int(input())
picture_with_the_trophy_str = input()

price_for_ticket = 0

if stage == "Quarter final":
    if ticket_type == "Standard":
        price_for_ticket = 55.50
    elif ticket_type == "Premium":
        price_for_ticket = 105.20
    elif ticket_type == "VIP":
        price_for_ticket = 118.90

elif stage == "Semi final":
    if ticket_type == "Standard":
        price_for_ticket = 75.88
    elif ticket_type == "Premium":
        price_for_ticket = 125.22
    elif ticket_type == "VIP":
        price_for_ticket = 300.40

elif stage == "Final":
    if ticket_type == "Standard":
        price_for_ticket = 110.10
    elif ticket_type == "Premium":
        price_for_ticket = 160.66
    elif ticket_type == "VIP":
        price_for_ticket = 400.00

price_for_all_tickets = num_of_tickets * price_for_ticket

discounted_price = price_for_all_tickets

if price_for_all_tickets > 4_000:
    discounted_price *= 0.75
elif price_for_all_tickets > 2_500:
    discounted_price *= 0.9

if picture_with_the_trophy_str == "Y" and price_for_all_tickets <= 4_000:
    discounted_price += num_of_tickets * 40

print(f"{discounted_price:.2f}")