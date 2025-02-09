start_n = int(input())
end_n = int(input())
sum_of_start = 0
sum_of_end = 0

for number in range(start_n, end_n + 1):
    length_of_number = len(str(number))
    for i in range(length_of_number):
        if i % 2 != 0: # odd
            sum_of_start += int(str(number)[i])
        elif i % 2 == 0: # even
            sum_of_end += int(str(number)[i])
    if sum_of_start == sum_of_end:
        print(number, end=" ")
    sum_of_start = 0
    sum_of_end = 0
