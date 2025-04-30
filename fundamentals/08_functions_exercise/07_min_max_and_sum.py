min_number = lambda numbers: min(numbers)
max_number = lambda numbers: max(numbers)
sum_numbers = lambda numbers: sum(numbers)

def print_all_nums(input_str: str):
    int_list = list(map(int, input_str.split()))

    print(f"The minimum number is {min_number(int_list)}")
    print(f"The maximum number is {max_number(int_list)}")
    print(f"The sum number is: {sum_numbers(int_list)}")

print_all_nums(input())