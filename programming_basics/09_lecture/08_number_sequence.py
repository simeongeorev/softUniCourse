n = int(input())

max_number = 0
min_number = 0

for i in range(0, n):
    number = int(input())
    if i == 0:
        max_number = number
        min_number = number
    if number > max_number:
        max_number = number
    if number < min_number:
        min_number = number

print(f"Max number: {max_number}")

print(f"Min number: {min_number}")
