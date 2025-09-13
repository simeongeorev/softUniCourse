from collections import deque

children = input().split()
n = int(input())

queue = deque()

for child in children:
    queue.append(child)

while len(queue) > 1:
    for i in range(1, n+1):
        if i == n:
            print(f"Removed {queue.popleft()}")
        else:
            child = queue.popleft()
            queue.append(child)

print(f"Last is {queue.popleft()}")