n = int(input())

sum_left = 0
sum_right = 0

for i in range(0, n):
    number = int(input())
    sum_left += number

for i in range(0, n):
    number = int(input())
    sum_right += number

if sum_left == sum_right:
    print(f"Yes, sum = {sum_left}")
else:
    print(f"No, diff = {abs(sum_left - sum_right)}")
