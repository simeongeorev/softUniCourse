from collections import deque

rows, cols = [int(x) for x in input().split()]
snake_str = input()

snake_deque = deque(snake_str)
matrix = []

for i in range(rows):
    matrix.append(cols*[" "])

for i in range(rows):
    if i % 2 == 0:
        for j in range(cols):
            matrix[i][j] = snake_deque.popleft()
            if not snake_deque:
                snake_deque = deque(snake_str)
    else:
        for j in range(cols-1, -1, -1):
            matrix[i][j] = snake_deque.popleft()
            if not snake_deque:
                snake_deque = deque(snake_str)
    print("".join(matrix[i]))
