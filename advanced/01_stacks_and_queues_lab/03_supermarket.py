from collections import deque

shop_queue = deque()

while True:
    command = input()

    if command == "End":
        print(f"{len(shop_queue)} people remaining.")
        break
    elif command == "Paid":
        while shop_queue:
            print(shop_queue.popleft())
    else:
        shop_queue.append(command)
