worker1, worker2, worker3 = int(input()), int(input()), int(input())

total_customers = int(input())

customers_per_hour = worker1 + worker2 + worker3

hours_needed = 0

while True:

    if total_customers <= 0:
        break

    total_customers -= customers_per_hour

    hours_needed += 1

    if hours_needed % 4 == 0:
        hours_needed += 1

print(f"Time needed: {hours_needed}h.")

