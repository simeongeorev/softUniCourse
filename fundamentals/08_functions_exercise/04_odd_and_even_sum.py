def sum_of_odd_digits(numbers: list) -> int:
    sum = 0
    for num in numbers:
        if num % 2 != 0:
            sum += num
    return sum


def sum_of_even_digits(numbers: list) -> int:
    sum = 0
    for num in numbers:
        if num % 2 == 0:
            sum += num
    return sum

def get_odd_and_even_sum(numbers: list) -> str:
    return f"Odd sum = {sum_of_odd_digits(numbers)}, Even sum = {sum_of_even_digits(numbers)}"

input_list = list(input())
numbers_list = [int(item) for item in input_list]

print(get_odd_and_even_sum(numbers_list))
