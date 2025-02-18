largest_number = float('-inf')

for i in range(3):
    n = int(input())
    if n > largest_number:
        largest_number = n
print(largest_number)
