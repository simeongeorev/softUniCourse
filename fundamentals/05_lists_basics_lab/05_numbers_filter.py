N = int(input())

numbers_list = []
filtered_numbers = []

for _ in range(N):
    number = int(input())
    numbers_list.append(number)

command = input()

if command == "even":
    for n in numbers_list:
        if n % 2 == 0:
            filtered_numbers.append(n)
elif command == "odd":
    for n in numbers_list:
        if n % 2 != 0:
            filtered_numbers.append(n)
elif command == "negative":
    for n in numbers_list:
        if n < 0:
            filtered_numbers.append(n)
elif command == "positive":
    for n in numbers_list:
        if n >= 0:
            filtered_numbers.append(n)

print(filtered_numbers)