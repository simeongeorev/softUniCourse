n = int(input())

odd_sum = 0
even_sum = 0

for i in range(0, n):
    number = int(input())
    if (i + 1) % 2 != 0:
        odd_sum += number
    elif (i + 1) % 2 == 0:
        even_sum += number

if odd_sum == even_sum:
    print("Yes")
    print(f"Sum = {odd_sum}")
else:
    print("No")
    print(f"Diff = {abs(odd_sum - even_sum)}")

