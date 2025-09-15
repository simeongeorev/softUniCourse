from collections import deque

total_food = int(input())
orders = deque(map(int, input().split()))

print(max(orders))

while orders:
    order = orders[0]
    if order <= total_food:
        total_food -= order
        orders.popleft()
    else:
        break

if orders:
    print("Orders left:", *orders)
else:
    print("Orders complete")