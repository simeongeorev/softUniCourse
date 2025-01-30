import sys

order = input()
smallest_num = sys.maxsize

while order != "Stop":
    order_int = int(order)
    if order_int < smallest_num:
        smallest_num = order_int
    order = input()

print(smallest_num)