def abs_nums(numbers):
    for i in range(len(numbers)):
        numbers[i] = abs(float(numbers[i]))
    return numbers

numbers_list = input().split()
print(abs_nums(numbers_list))