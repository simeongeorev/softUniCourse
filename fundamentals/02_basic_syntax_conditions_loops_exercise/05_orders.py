number_of_orders = int(input())

total_price = 0

for _ in range(number_of_orders):

    should_skip = False

    price_per_capsule = float(input())
    if price_per_capsule < 0.01 or price_per_capsule > 100.00:
        should_skip = True

    days = int(input())
    if days < 1 or days > 31:
        should_skip = True

    capsules_needed_per_day = int(input())
    if capsules_needed_per_day < 1 or capsules_needed_per_day > 2_000:
        should_skip = True

    if should_skip:
        continue

    price = capsules_needed_per_day * price_per_capsule * days

    print(f"The price for the coffee is: ${price:.2f}")

    total_price += price

print(f"Total: ${total_price:.2f}")