year_old = int(input())
washing_machine_price = float(input())
toy_price = int(input())

even_bdays_sum = 0
odd_present_count = 0

for i in range(1, year_old + 1):
    if i % 2 != 0:  # odd
        odd_present_count += 1
    elif i % 2 == 0:  # even
        even_bdays_sum += (10 * (i / 2)) - 1

total_sum = odd_present_count * toy_price + even_bdays_sum
money_left = total_sum - washing_machine_price

if money_left >= 0:
    print(f"Yes! {money_left:.2f}")
else:
    print(f"No! {abs(money_left):.2f}")