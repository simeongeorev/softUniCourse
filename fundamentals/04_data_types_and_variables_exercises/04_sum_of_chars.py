N = int(input())

total = 0

for _ in range(N):
    letter = input()
    number_of_letter = ord(letter)
    total += number_of_letter

print(f"The sum equals: {total}")

