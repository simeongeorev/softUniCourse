divisor = int(input())
boundary = int(input())

n = 0

for i in range(boundary, 0, -1):
    if i % divisor == 0:
        n = i
        break

print(n)