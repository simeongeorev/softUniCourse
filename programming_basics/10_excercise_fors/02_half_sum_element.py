n = int(input())

sum = 0
biggest_num = 0

for i in range(0, n):
    number = int(input())
    sum += number
    if number > biggest_num:
        biggest_num = number

sum -= biggest_num
if sum == biggest_num:
    print("Yes")
    print(f"Sum = {biggest_num}")
else:
    print("No")
    print(f"Diff = {abs(sum - biggest_num)}")